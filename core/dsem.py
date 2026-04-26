"""Dynamic Structural Equation Modeling (DSEM) for intensive longitudinal data.

Implements the two-level DSEM framework (Asparouhov et al., 2018) combining
multilevel modeling, time series analysis, and structural equation modeling.
Supports both frequentist two-step estimation and full Bayesian estimation via PyMC.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import warnings


@dataclass
class DSEMResult:
    within_parameters: pd.DataFrame
    between_parameters: pd.DataFrame
    random_effects: pd.DataFrame
    fit_stats: Dict[str, float]
    residual_autocorrelation: Dict[str, float]
    person_counts: Dict[str, int]
    n_persons: int
    n_observations: int
    model_syntax: str


class DSEM:
    def __init__(
        self,
        variables: List[str],
        time_var: str,
        person_var: str,
        autoregressive: bool = True,
        cross_lagged: bool = True,
        latent_vars: Optional[Dict[str, List[str]]] = None,
    ):
        self.variables = variables
        self.time_var = time_var
        self.person_var = person_var
        self.autoregressive = autoregressive
        self.cross_lagged = cross_lagged
        self.latent_vars = latent_vars or {}

    def prepare_data(self, data: pd.DataFrame) -> pd.DataFrame:
        df = data.copy()
        df = df.sort_values([self.person_var, self.time_var]).reset_index(drop=True)
        for var in self.variables:
            lag_col = f"{var}_lag1"
            df[lag_col] = df.groupby(self.person_var)[var].shift(1)
        df = df.dropna(subset=[f"{v}_lag1" for v in self.variables]).reset_index(drop=True)
        return df

    def fit(self, data: pd.DataFrame, method: str = "two_step", **kwargs) -> DSEMResult:
        prepared = self.prepare_data(data)
        if method == "two_step":
            return self._fit_two_step(prepared, data)
        elif method == "bayesian":
            return self._fit_bayesian(prepared, data, **kwargs)
        else:
            raise ValueError(f"Unknown method: {method}. Use 'two_step' or 'bayesian'.")

    def _fit_two_step(self, prepared: pd.DataFrame, original: pd.DataFrame) -> DSEMResult:
        persons = prepared[self.person_var].unique()
        n_persons = len(persons)

        person_intercepts: Dict[str, Dict[str, float]] = {}
        person_ar_coefs: Dict[str, Dict[str, float]] = {}
        person_cross_coefs: Dict[str, Dict[str, float]] = {}

        all_within_rows: List[Dict[str, Any]] = []

        for person_id in persons:
            person_data = prepared[prepared[self.person_var] == person_id].copy()
            n_obs = len(person_data)
            if n_obs < 3:
                continue

            intercepts: Dict[str, float] = {}
            ar_coefs: Dict[str, float] = {}
            cross_coefs: Dict[str, float] = {}

            for target_var in self.variables:
                y = person_data[target_var].values
                lag_cols = [f"{target_var}_lag1"]
                if self.autoregressive:
                    pass
                if self.cross_lagged:
                    for other_var in self.variables:
                        if other_var != target_var:
                            lag_cols.append(f"{other_var}_lag1")

                X_cols = [c for c in lag_cols if c in person_data.columns]
                X = person_data[X_cols].values
                X = np.column_stack([np.ones(len(X)), X])

                try:
                    beta = np.linalg.lstsq(X, y, rcond=None)[0]
                except np.linalg.LinAlgError:
                    beta = np.zeros(X.shape[1])

                intercepts[target_var] = float(beta[0])

                col_idx = 0
                if self.autoregressive:
                    ar_coefs[target_var] = float(beta[1])
                    col_idx = 1
                else:
                    ar_coefs[target_var] = 0.0

                if self.cross_lagged:
                    for other_var in self.variables:
                        if other_var != target_var:
                            cross_key = f"{target_var}~{other_var}"
                            coef_idx = col_idx + 1 + (
                                [v for v in self.variables if v != target_var].index(other_var)
                                if self.autoregressive
                                else [v for v in self.variables if v != target_var].index(other_var)
                            )
                            if coef_idx < len(beta):
                                cross_coefs[cross_key] = float(beta[coef_idx])
                            else:
                                cross_coefs[cross_key] = 0.0

                all_within_rows.append({
                    "person": person_id,
                    "variable": target_var,
                    "intercept": intercepts[target_var],
                    "ar_coef": ar_coefs[target_var],
                    "n_obs": n_obs,
                })

            person_intercepts[person_id] = intercepts
            person_ar_coefs[person_id] = ar_coefs
            person_cross_coefs[person_id] = cross_coefs

        within_df = pd.DataFrame(all_within_rows)
        if within_df.empty:
            within_df = pd.DataFrame(columns=["person", "variable", "intercept", "ar_coef", "n_obs"])

        between_rows: List[Dict[str, Any]] = []
        all_intercepts = []
        all_ar = []

        for var in self.variables:
            var_intercepts = [person_intercepts[p].get(var, np.nan) for p in person_intercepts]
            var_ar = [person_ar_coefs[p].get(var, np.nan) for p in person_ar_coefs]
            var_intercepts_clean = [v for v in var_intercepts if not np.isnan(v)]
            var_ar_clean = [v for v in var_ar if not np.isnan(v)]

            all_intercepts.extend(var_intercepts_clean)
            all_ar.extend(var_ar_clean)

            between_rows.append({
                "parameter": f"intercept_{var}_mean",
                "estimate": float(np.mean(var_intercepts_clean)) if var_intercepts_clean else np.nan,
                "std": float(np.std(var_intercepts_clean)) if len(var_intercepts_clean) > 1 else np.nan,
                "type": "random_intercept",
            })
            between_rows.append({
                "parameter": f"intercept_{var}_var",
                "estimate": float(np.var(var_intercepts_clean)) if len(var_intercepts_clean) > 1 else np.nan,
                "std": np.nan,
                "type": "random_intercept_variance",
            })
            between_rows.append({
                "parameter": f"ar_{var}_mean",
                "estimate": float(np.mean(var_ar_clean)) if var_ar_clean else np.nan,
                "std": float(np.std(var_ar_clean)) if len(var_ar_clean) > 1 else np.nan,
                "type": "random_ar",
            })
            between_rows.append({
                "parameter": f"ar_{var}_var",
                "estimate": float(np.var(var_ar_clean)) if len(var_ar_clean) > 1 else np.nan,
                "std": np.nan,
                "type": "random_ar_variance",
            })

        if self.cross_lagged:
            for target_var in self.variables:
                for pred_var in self.variables:
                    if target_var != pred_var:
                        cross_key = f"{target_var}~{pred_var}"
                        var_cross = [
                            person_cross_coefs[p].get(cross_key, np.nan)
                            for p in person_cross_coefs
                        ]
                        var_cross_clean = [v for v in var_cross if not np.isnan(v)]
                        between_rows.append({
                            "parameter": f"cross_{target_var}_{pred_var}_mean",
                            "estimate": float(np.mean(var_cross_clean)) if var_cross_clean else np.nan,
                            "std": float(np.std(var_cross_clean)) if len(var_cross_clean) > 1 else np.nan,
                            "type": "random_crosslagged",
                        })

        between_df = pd.DataFrame(between_rows)

        re_rows: List[Dict[str, Any]] = []
        for person_id in persons:
            row: Dict[str, Any] = {"person": person_id}
            for var in self.variables:
                row[f"intercept_{var}"] = person_intercepts.get(person_id, {}).get(var, np.nan)
                row[f"ar_{var}"] = person_ar_coefs.get(person_id, {}).get(var, np.nan)
            if self.cross_lagged:
                for target_var in self.variables:
                    for pred_var in self.variables:
                        if target_var != pred_var:
                            cross_key = f"{target_var}~{pred_var}"
                            row[f"cross_{target_var}_{pred_var}"] = (
                                person_cross_coefs.get(person_id, {}).get(cross_key, np.nan)
                            )
            re_rows.append(row)

        random_effects_df = pd.DataFrame(re_rows)

        residuals = self.compute_residuals(prepared, {
            "person_intercepts": person_intercepts,
            "person_ar_coefs": person_ar_coefs,
            "person_cross_coefs": person_cross_coefs,
        })

        residual_ac = self._compute_residual_autocorrelation(prepared, residuals)

        person_counts = {
            str(pid): int(prepared[prepared[self.person_var] == pid].shape[0])
            for pid in persons
        }

        fit_stats = self._compute_two_step_fit_stats(prepared, residuals, person_intercepts)

        syntax = self._build_syntax()

        return DSEMResult(
            within_parameters=within_df,
            between_parameters=between_df,
            random_effects=random_effects_df,
            fit_stats=fit_stats,
            residual_autocorrelation=residual_ac,
            person_counts=person_counts,
            n_persons=n_persons,
            n_observations=len(prepared),
            model_syntax=syntax,
        )

    def _fit_bayesian(
        self,
        prepared: pd.DataFrame,
        original: pd.DataFrame,
        draws: int = 1000,
        tune: int = 500,
        chains: int = 2,
        target_accept: float = 0.9,
        random_seed: int = 42,
        **kwargs,
    ) -> DSEMResult:
        import pymc as pm
        import arviz as az

        persons = prepared[self.person_var].unique()
        person_codes = {pid: i for i, pid in enumerate(persons)}
        n_persons = len(persons)
        n_vars = len(self.variables)

        person_idx = prepared[self.person_var].map(person_codes).values.astype(int)
        n_obs = len(prepared)

        y_data = {}
        lag_data = {}
        cross_lag_data: Dict[Tuple[int, int], np.ndarray] = {}

        for i, var in enumerate(self.variables):
            y_data[var] = prepared[var].values.astype(np.float64)
            lag_data[var] = prepared[f"{var}_lag1"].values.astype(np.float64)
            if self.cross_lagged:
                for j, other_var in enumerate(self.variables):
                    if other_var != var:
                        cross_lag_data[(i, j)] = prepared[f"{other_var}_lag1"].values.astype(np.float64)

        with pm.Model() as model:
            mu_alpha = pm.Normal("mu_alpha", mu=0.0, sigma=1.0, shape=n_vars)
            sigma_alpha = pm.HalfNormal("sigma_alpha", sigma=1.0, shape=n_vars)
            alpha_offset = pm.Normal("alpha_offset", mu=0.0, sigma=1.0, shape=(n_persons, n_vars))
            alpha = pm.Deterministic("alpha", mu_alpha + sigma_alpha * alpha_offset)

            mu_phi = pm.Normal("mu_phi", mu=0.0, sigma=1.0, shape=n_vars)
            sigma_phi = pm.HalfNormal("sigma_phi", sigma=1.0, shape=n_vars)
            phi_offset = pm.Normal("phi_offset", mu=0.0, sigma=1.0, shape=(n_persons, n_vars))
            phi = pm.Deterministic("phi", mu_phi + sigma_phi * phi_offset)

            cross_coefs_raw: Dict[Tuple[int, int], Any] = {}
            if self.cross_lagged:
                mu_cross = pm.Normal("mu_cross", mu=0.0, sigma=0.5, shape=n_vars * (n_vars - 1))
                sigma_cross = pm.HalfNormal("sigma_cross", sigma=0.5, shape=n_vars * (n_vars - 1))
                cross_offset = pm.Normal(
                    "cross_offset",
                    mu=0.0,
                    sigma=1.0,
                    shape=(n_persons, n_vars * (n_vars - 1)),
                )
                cross_coefs = pm.Deterministic(
                    "cross_coefs", mu_cross + sigma_cross * cross_offset
                )

            sigma_eps = pm.HalfNormal("sigma_eps", sigma=1.0, shape=n_vars)

            for i, var in enumerate(self.variables):
                mu_y = alpha[person_idx, i]
                if self.autoregressive:
                    mu_y = mu_y + phi[person_idx, i] * lag_data[var]
                if self.cross_lagged:
                    cross_idx = 0
                    for j, other_var in enumerate(self.variables):
                        if other_var != var:
                            if (i, j) in cross_lag_data:
                                mu_y = mu_y + cross_coefs[person_idx, cross_idx] * cross_lag_data[(i, j)]
                            cross_idx += 1
                pm.Normal(f"y_{var}", mu=mu_y, sigma=sigma_eps[i], observed=y_data[var])

            trace = pm.sample(
                draws=draws,
                tune=tune,
                chains=chains,
                target_accept=target_accept,
                random_seed=random_seed,
                return_inferencedata=True,
                **kwargs,
            )

        summary = az.summary(trace)

        within_rows: List[Dict[str, Any]] = []
        for i, var in enumerate(self.variables):
            phi_key = f"mu_phi[{i}]"
            within_rows.append({
                "parameter": f"ar_{var}",
                "mean": float(summary.loc[phi_key, "mean"]) if phi_key in summary.index else np.nan,
                "sd": float(summary.loc[phi_key, "sd"]) if phi_key in summary.index else np.nan,
                "type": "autoregressive",
            })
            if self.cross_lagged:
                cross_idx = 0
                for j, other_var in enumerate(self.variables):
                    if other_var != var:
                        cross_key = f"mu_cross[{i * (n_vars - 1) + cross_idx}]"
                        within_rows.append({
                            "parameter": f"cross_{var}_{other_var}",
                            "mean": float(summary.loc[cross_key, "mean"]) if cross_key in summary.index else np.nan,
                            "sd": float(summary.loc[cross_key, "sd"]) if cross_key in summary.index else np.nan,
                            "type": "cross_lagged",
                        })
                        cross_idx += 1

        within_df = pd.DataFrame(within_rows)

        between_rows: List[Dict[str, Any]] = []
        for i, var in enumerate(self.variables):
            for param_name, base_key in [
                ("intercept_mean", "mu_alpha"),
                ("intercept_var", "sigma_alpha"),
                ("ar_mean", "mu_phi"),
                ("ar_var", "sigma_phi"),
            ]:
                key = f"{base_key}[{i}]"
                between_rows.append({
                    "parameter": f"{param_name}_{var}",
                    "mean": float(summary.loc[key, "mean"]) if key in summary.index else np.nan,
                    "sd": float(summary.loc[key, "sd"]) if key in summary.index else np.nan,
                    "type": param_name,
                })
            for res_key_base in ["sigma_eps"]:
                key = f"{res_key_base}[{i}]"
                between_rows.append({
                    "parameter": f"residual_sd_{var}",
                    "mean": float(summary.loc[key, "mean"]) if key in summary.index else np.nan,
                    "sd": float(summary.loc[key, "sd"]) if key in summary.index else np.nan,
                    "type": "residual",
                })

        between_df = pd.DataFrame(between_rows)

        post = trace.posterior
        alpha_post = post["alpha"].values
        phi_post = post["phi"].values

        re_rows: List[Dict[str, Any]] = []
        for p_idx, pid in enumerate(persons):
            row: Dict[str, Any] = {"person": pid}
            for i, var in enumerate(self.variables):
                row[f"intercept_{var}"] = float(alpha_post[:, :, p_idx, i].mean())
                row[f"ar_{var}"] = float(phi_post[:, :, p_idx, i].mean())
            if self.cross_lagged:
                cross_post = post["cross_coefs"].values
                cross_idx = 0
                for i, var in enumerate(self.variables):
                    for j, other_var in enumerate(self.variables):
                        if other_var != var:
                            row[f"cross_{var}_{other_var}"] = float(
                                cross_post[:, :, p_idx, cross_idx].mean()
                            )
                            cross_idx += 1
            re_rows.append(row)

        random_effects_df = pd.DataFrame(re_rows)

        fit_stats: Dict[str, float] = {}
        try:
            waic_result = az.waic(trace)
            fit_stats["waic"] = float(waic_result.waic)
        except Exception as e:
            warnings.warn(f"WAIC computation failed: {e}")
            fit_stats["waic"] = np.nan

        try:
            loo_result = az.loo(trace)
            fit_stats["loo"] = float(loo_result.loo)
        except Exception as e:
            warnings.warn(f"LOO computation failed: {e}")
            fit_stats["loo"] = np.nan

        try:
            log_lik = trace.log_likelihood
            if log_lik is not None:
                total_dims = [d for d in log_lik.dims if d not in ("chain", "draw")]
                ll = log_lik.to_array().sum(dim=total_dims) if total_dims else log_lik.to_array()
                mean_ll = float(ll.mean())
                deviance_mean = -2.0 * mean_ll
                pointwise = ll.values.flatten()
                deviance_at_mean = -2.0 * np.log(np.exp(pointwise).mean())
                p_dic = deviance_at_mean - deviance_mean
                fit_stats["dic"] = deviance_mean + 2.0 * p_dic
        except Exception:
            fit_stats["dic"] = np.nan

        params_for_residuals = {
            "person_intercepts": {
                pid: {
                    var: float(alpha_post[:, :, p_idx, vi].mean())
                    for vi, var in enumerate(self.variables)
                }
                for p_idx, pid in enumerate(persons)
            },
            "person_ar_coefs": {
                pid: {
                    var: float(phi_post[:, :, p_idx, vi].mean())
                    for vi, var in enumerate(self.variables)
                }
                for p_idx, pid in enumerate(persons)
            },
            "person_cross_coefs": {},
        }
        if self.cross_lagged:
            cross_post = post["cross_coefs"].values
            for p_idx, pid in enumerate(persons):
                cross_dict: Dict[str, float] = {}
                cross_idx = 0
                for i, var in enumerate(self.variables):
                    for j, other_var in enumerate(self.variables):
                        if other_var != var:
                            cross_dict[f"{var}~{other_var}"] = float(
                                cross_post[:, :, p_idx, cross_idx].mean()
                            )
                            cross_idx += 1
                params_for_residuals["person_cross_coefs"][pid] = cross_dict

        residuals = self.compute_residuals(prepared, params_for_residuals)
        residual_ac = self._compute_residual_autocorrelation(prepared, residuals)

        person_counts = {
            str(pid): int(prepared[prepared[self.person_var] == pid].shape[0])
            for pid in persons
        }

        syntax = self._build_syntax()

        return DSEMResult(
            within_parameters=within_df,
            between_parameters=between_df,
            random_effects=random_effects_df,
            fit_stats=fit_stats,
            residual_autocorrelation=residual_ac,
            person_counts=person_counts,
            n_persons=n_persons,
            n_observations=len(prepared),
            model_syntax=syntax,
        )

    def compute_residuals(self, data: pd.DataFrame, params: Dict) -> pd.DataFrame:
        result = data[[self.person_var, self.time_var] + self.variables].copy()
        for var in self.variables:
            result[f"resid_{var}"] = np.nan

        persons = data[self.person_var].unique()
        for person_id in persons:
            mask = data[self.person_var] == person_id
            person_data = data[mask]

            intercepts = params.get("person_intercepts", {}).get(person_id, {})
            ar_coefs = params.get("person_ar_coefs", {}).get(person_id, {})
            cross_coefs = params.get("person_cross_coefs", {}).get(person_id, {})

            for var in self.variables:
                observed = person_data[var].values
                lag_var = person_data[f"{var}_lag1"].values

                pred = np.full_like(observed, intercepts.get(var, 0.0), dtype=np.float64)

                if self.autoregressive:
                    pred = pred + ar_coefs.get(var, 0.0) * lag_var

                if self.cross_lagged:
                    for other_var in self.variables:
                        if other_var != var:
                            cross_key = f"{var}~{other_var}"
                            other_lag = person_data[f"{other_var}_lag1"].values
                            pred = pred + cross_coefs.get(cross_key, 0.0) * other_lag

                resid_idx = result.loc[mask, f"resid_{var}"].index
                result.loc[resid_idx, f"resid_{var}"] = observed - pred

        return result

    def _compute_residual_autocorrelation(
        self, data: pd.DataFrame, residuals: pd.DataFrame
    ) -> Dict[str, float]:
        result: Dict[str, float] = {}
        persons = data[self.person_var].unique()

        for var in self.variables:
            resid_col = f"resid_{var}"
            if resid_col not in residuals.columns:
                continue

            all_ac = []
            for person_id in persons:
                mask = residuals[self.person_var] == person_id
                resid = residuals.loc[mask, resid_col].dropna().values
                if len(resid) > 2:
                    mean_r = np.mean(resid)
                    resid_demeaned = resid - mean_r
                    denom = np.sum(resid_demeaned ** 2)
                    if denom > 0:
                        ac = np.sum(resid_demeaned[:-1] * resid_demeaned[1:]) / denom
                        all_ac.append(ac)

            result[var] = float(np.mean(all_ac)) if all_ac else np.nan

        return result

    def _compute_two_step_fit_stats(
        self,
        prepared: pd.DataFrame,
        residuals: pd.DataFrame,
        person_intercepts: Dict[str, Dict[str, float]],
    ) -> Dict[str, float]:
        stats: Dict[str, float] = {}
        n_obs = len(prepared)
        n_params = 0

        for var in self.variables:
            n_params += 2
            if self.cross_lagged:
                n_params += len(self.variables) - 1

        n_params *= len(prepared[self.person_var].unique())

        total_ss = 0.0
        resid_ss = 0.0
        for var in self.variables:
            resid_col = f"resid_{var}"
            if resid_col in residuals.columns:
                resid_vals = residuals[resid_col].dropna().values
                obs_vals = prepared[var].values[: len(resid_vals)]
                total_ss += float(np.sum((obs_vals - np.mean(obs_vals)) ** 2))
                resid_ss += float(np.sum(resid_vals ** 2))

        stats["n_obs"] = float(n_obs)
        stats["n_params_approx"] = float(n_params)
        stats["residual_ss"] = resid_ss
        stats["total_ss"] = total_ss

        if total_ss > 0:
            stats["pseudo_r2"] = 1.0 - resid_ss / total_ss
        else:
            stats["pseudo_r2"] = np.nan

        n_eff = max(n_obs - n_params, 1)
        stats["mse"] = resid_ss / n_eff
        stats["aic_approx"] = n_obs * np.log(resid_ss / n_obs + 1e-10) + 2 * n_params
        stats["bic_approx"] = n_obs * np.log(resid_ss / n_obs + 1e-10) + n_params * np.log(n_obs)

        return stats

    def check_stationarity(self, data: pd.DataFrame) -> Dict[str, Any]:
        prepared = self.prepare_data(data)
        persons = prepared[self.person_var].unique()
        n_persons = len(persons)

        result: Dict[str, Any] = {
            "per_variable": {},
            "overall_nonstationary_proportion": 0.0,
            "suggest_differencing": False,
            "nonstationary_persons": [],
        }

        total_checks = 0
        total_nonstationary = 0

        for var in self.variables:
            nonstationary_count = 0
            nonstationary_ids: List[Any] = []
            ar_values: List[float] = []

            for person_id in persons:
                person_data = prepared[prepared[self.person_var] == person_id]
                if len(person_data) < 3:
                    continue

                y = person_data[var].values
                y_lag = person_data[f"{var}_lag1"].values

                X = np.column_stack([np.ones(len(y_lag)), y_lag])
                try:
                    beta = np.linalg.lstsq(X, y, rcond=None)[0]
                except np.linalg.LinAlgError:
                    continue

                ar_coef = float(beta[1])
                ar_values.append(ar_coef)
                total_checks += 1

                if abs(ar_coef) >= 1.0:
                    nonstationary_count += 1
                    total_nonstationary += 1
                    nonstationary_ids.append(person_id)

            n_checked = len(ar_values)
            result["per_variable"][var] = {
                "mean_ar": float(np.mean(ar_values)) if ar_values else np.nan,
                "sd_ar": float(np.std(ar_values)) if len(ar_values) > 1 else np.nan,
                "n_nonstationary": nonstationary_count,
                "n_checked": n_checked,
                "proportion_nonstationary": nonstationary_count / n_checked if n_checked > 0 else 0.0,
            }

            for pid in nonstationary_ids:
                if pid not in result["nonstationary_persons"]:
                    result["nonstationary_persons"].append(pid)

        if total_checks > 0:
            result["overall_nonstationary_proportion"] = total_nonstationary / total_checks
            if result["overall_nonstationary_proportion"] > 0.1:
                result["suggest_differencing"] = True

        return result

    def _build_syntax(self) -> str:
        lines: List[str] = []

        lines.append("% WITHIN LEVEL")
        for var in self.variables:
            if self.autoregressive:
                lines.append(f"  {var} ON {var}_lag1;")
            if self.cross_lagged:
                for other_var in self.variables:
                    if other_var != var:
                        lines.append(f"  {var} ON {other_var}_lag1;")

        lines.append("")
        lines.append("% BETWEEN LEVEL")
        for var in self.variables:
            lines.append(f"  {var} ON intercept_{var};")
            lines.append(f"  intercept_{var};")
            if self.autoregressive:
                lines.append(f"  phi_{var};")

        if self.latent_vars:
            lines.append("")
            lines.append("% MEASUREMENT MODEL")
            for latent, indicators in self.latent_vars.items():
                lines.append(f"  {latent} BY {' '.join(indicators)};")

        return "\n".join(lines)


def plot_individual_trajectories(
    data: pd.DataFrame,
    person_var: str,
    variables: List[str],
    n_persons: int = 10,
) -> str:
    persons = data[person_var].unique()[:n_persons]
    lines: List[str] = []

    for person_id in persons:
        person_data = data[data[person_var] == person_id]
        lines.append(f"Person: {person_id} (n={len(person_data)})")
        for var in variables:
            if var in person_data.columns:
                vals = person_data[var].dropna().values
                if len(vals) > 0:
                    lines.append(
                        f"  {var}: mean={np.mean(vals):.3f}, "
                        f"sd={np.std(vals):.3f}, "
                        f"range=[{np.min(vals):.3f}, {np.max(vals):.3f}]"
                    )
                else:
                    lines.append(f"  {var}: no valid observations")
        lines.append("")

    return "\n".join(lines)


def simulate_dsem(
    n_persons: int,
    n_times: int,
    n_vars: int,
    ar_coefs: Optional[np.ndarray] = None,
    cross_coefs: Optional[np.ndarray] = None,
    seed: int = 42,
) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    if ar_coefs is None:
        ar_coefs = np.full(n_vars, 0.5)
    else:
        ar_coefs = np.asarray(ar_coefs, dtype=np.float64)
    if cross_coefs is None:
        cross_coefs = np.zeros((n_vars, n_vars))
    else:
        cross_coefs = np.asarray(cross_coefs, dtype=np.float64)
        if cross_coefs.ndim == 1:
            if len(cross_coefs) == n_vars * n_vars:
                cross_coefs = cross_coefs.reshape(n_vars, n_vars)
            else:
                cross_coefs_mat = np.zeros((n_vars, n_vars))
                np.fill_diagonal(cross_coefs_mat, 0)
                idx = 0
                for i in range(n_vars):
                    for j in range(n_vars):
                        if i != j and idx < len(cross_coefs):
                            cross_coefs_mat[i, j] = cross_coefs[idx]
                            idx += 1
                cross_coefs = cross_coefs_mat
        elif cross_coefs.ndim != 2 or cross_coefs.shape != (n_vars, n_vars):
            cross_coefs = np.zeros((n_vars, n_vars))

    var_names = [f"y{i+1}" for i in range(n_vars)]
    rows: List[Dict[str, Any]] = []

    for p in range(n_persons):
        intercepts = rng.normal(0, 1, size=n_vars)

        y_t = intercepts.copy() + rng.normal(0, 0.5, size=n_vars)

        for t in range(n_times):
            innovation = rng.normal(0, 0.5, size=n_vars)
            y_new = np.copy(intercepts)

            for v in range(n_vars):
                y_new[v] += ar_coefs[v] * y_t[v]
                for w in range(n_vars):
                    if w != v:
                        y_new[v] += cross_coefs[v, w] * y_t[w]
                y_new[v] += innovation[v]

            y_t = y_new.copy()

            row: Dict[str, Any] = {"person": p, "time": t}
            for v in range(n_vars):
                row[var_names[v]] = float(y_new[v])
            rows.append(row)

    df = pd.DataFrame(rows)
    return df
