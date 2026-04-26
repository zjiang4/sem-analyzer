"""Bayesian Structural Equation Modeling via PyMC with semopy-style syntax parsing."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Tuple

import numpy as np
import pandas as pd
import warnings


@dataclass
class PriorSpec:
    name: str
    params: Dict[str, float] = field(default_factory=dict)


@dataclass
class BayesianSEMResult:
    trace: Any
    model: Any
    summary: pd.DataFrame
    fit_stats: Dict[str, float]
    posterior_predictive: Optional[Dict]
    convergence_diagnostics: Dict[str, Any]
    model_syntax: str


def _default_loading_prior() -> PriorSpec:
    return PriorSpec("normal", {"mu": 0.0, "sigma": 1.0})


def _default_residual_prior(sigma: float = 1.0) -> PriorSpec:
    return PriorSpec("half_normal", {"sigma": sigma})


def _default_regression_prior(sigma: float = 1.0) -> PriorSpec:
    return PriorSpec("normal", {"mu": 0.0, "sigma": sigma})


def _default_variance_prior(sigma: float = 1.0) -> PriorSpec:
    return PriorSpec("half_normal", {"sigma": sigma})


def _default_correlation_prior() -> PriorSpec:
    return PriorSpec("lkj", {"eta": 2.0})


class BayesianSEM:
    def __init__(self, model_syntax: str, priors: Optional[Dict[str, PriorSpec]] = None):
        self.model_syntax = model_syntax
        self.priors = priors or {}
        self._parsed = self._parse_syntax(model_syntax)

    def _parse_syntax(self, syntax: str) -> Dict:
        measurements: List[Tuple[str, str, Optional[str]]] = []
        regressions: List[Tuple[str, str, Optional[str]]] = []
        covariances: List[Tuple[str, str]] = []
        intercepts: List[str] = set()
        latents: Set[str] = set()
        observed: Set[str] = set()

        for raw_line in syntax.strip().splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue

            if "=~" in line:
                lhs, rhs = line.split("=~", 1)
                latent = lhs.strip()
                latents.add(latent)
                for term in rhs.split("+"):
                    term = term.strip()
                    if not term:
                        continue
                    label = None
                    if "*" in term:
                        parts = term.split("*", 1)
                        label = parts[0].strip()
                        indicator = parts[1].strip()
                    else:
                        indicator = term
                    observed.add(indicator)
                    measurements.append((latent, indicator, label))

            elif "~~" in line:
                lhs, rhs = line.split("~~", 1)
                var1 = lhs.strip()
                var2 = rhs.strip()
                covariances.append((var1, var2))

            elif "~" in line:
                lhs, rhs = line.split("~", 1)
                target = lhs.strip()
                rhs_stripped = rhs.strip()
                if rhs_stripped == "1":
                    intercepts.add(target)
                    continue
                for term in rhs_stripped.split("+"):
                    term = term.strip()
                    if not term:
                        continue
                    label = None
                    if "*" in term:
                        parts = term.split("*", 1)
                        label = parts[0].strip()
                        predictor = parts[1].strip()
                    else:
                        predictor = term
                    regressions.append((target, predictor, label))
                    if target in latents:
                        latents.add(target)
                    else:
                        observed.add(target)
                    if predictor in latents:
                        pass
                    else:
                        observed.add(predictor)

        latent_in_reg = {t for t, _, _ in regressions} | {p for _, p, _ in regressions}
        for v in latent_in_reg:
            if v not in observed:
                latents.add(v)

        return {
            "measurements": measurements,
            "regressions": regressions,
            "covariances": covariances,
            "intercepts": list(intercepts),
            "latents": latents,
            "observed": observed,
        }

    def _build_pymc_model(self, data: pd.DataFrame) -> Any:
        import pymc as pm

        n_obs = len(data)
        parsed = self._parsed
        latents = parsed["latents"]
        observed_vars = sorted(parsed["observed"])
        latent_list = sorted(latents)

        data_dict = {col: data[col].values.astype(np.float64) for col in data.columns}

        with pm.Model() as pymc_model:
            latent_scores = {}
            for lv in latent_list:
                eta = pm.Normal(f"eta_{lv}", mu=0.0, sigma=1.0, shape=n_obs)
                latent_scores[lv] = eta

            loadings = {}
            for latent, indicator, label in parsed["measurements"]:
                lname = f"loading_{latent}_{indicator}"
                loading_prior = self.priors.get(lname, _default_loading_prior())
                loading = pm.Normal(
                    lname,
                    mu=loading_prior.params.get("mu", 0.0),
                    sigma=loading_prior.params.get("sigma", 1.0),
                )
                loadings[(latent, indicator)] = loading

            intercept_params = {}
            all_indicator_vars = [ind for _, ind, _ in parsed["measurements"]]
            for var_name in set(all_indicator_vars + list(data.columns)):
                if var_name in data.columns:
                    iname = f"intercept_{var_name}"
                    intercept_params[var_name] = pm.Normal(iname, mu=0.0, sigma=10.0)

            residual_sd = {}
            for latent, indicator, label in parsed["measurements"]:
                rname = f"residual_{indicator}"
                res_prior = self.priors.get(rname, _default_residual_prior())
                residual_sd[indicator] = pm.HalfNormal(
                    rname, sigma=res_prior.params.get("sigma", 1.0)
                )

            for latent, indicator, label in parsed["measurements"]:
                mu = intercept_params.get(indicator, 0.0) + loadings[(latent, indicator)] * latent_scores[latent]
                pm.Normal(
                    f"obs_{indicator}",
                    mu=mu,
                    sigma=residual_sd[indicator],
                    observed=data_dict.get(indicator, np.zeros(n_obs)),
                )

            regression_latent_targets = [t for t, _, _ in parsed["regressions"] if t in latents]
            if regression_latent_targets:
                for lv in regression_latent_targets:
                    lname = f"latent_intercept_{lv}"
                    if lname not in [v.name for v in pymc_model.free_RVs]:
                        pass

                for target, predictor, label in parsed["regressions"]:
                    if target in latents and predictor in latents:
                        cname = f"reg_{target}_{predictor}"
                        reg_prior = self.priors.get(cname, _default_regression_prior())
                        coef = pm.Normal(
                            cname,
                            mu=reg_prior.params.get("mu", 0.0),
                            sigma=reg_prior.params.get("sigma", 1.0),
                        )
                        mu_lat = coef * latent_scores[predictor]
                        idx_target = latent_list.index(target)
                        existing = pymc_model.rvs_to_values.get(latent_scores[target])
                        pm.Potential(
                            f"latent_reg_{target}_{predictor}",
                            pm.logp(
                                pm.Normal.dist(mu=mu_lat, sigma=1.0),
                                latent_scores[target],
                            ),
                        )

            for target, predictor, label in parsed["regressions"]:
                if target not in latents and target in data.columns:
                    cname = f"reg_{target}_{predictor}"
                    reg_prior = self.priors.get(cname, _default_regression_prior())
                    coef = pm.Normal(
                        cname,
                        mu=reg_prior.params.get("mu", 0.0),
                        sigma=reg_prior.params.get("sigma", 1.0),
                    )
                    reg_res_name = f"reg_residual_{target}"
                    if reg_res_name not in [v.name for v in pymc_model.free_RVs]:
                        reg_res_sd = pm.HalfNormal(reg_res_name, sigma=1.0)
                    else:
                        reg_res_sd = [v for v in pymc_model.free_RVs if v.name == reg_res_name][0]

                    if predictor in latents:
                        mu = intercept_params.get(target, 0.0) + coef * latent_scores[predictor]
                    else:
                        mu = intercept_params.get(target, 0.0) + coef * data_dict.get(predictor, np.zeros(n_obs))
                    pm.Normal(
                        f"obs_reg_{target}_{predictor}",
                        mu=mu,
                        sigma=reg_res_sd,
                        observed=data_dict.get(target, np.zeros(n_obs)),
                    )

            if len(parsed["covariances"]) > 0:
                cov_latents = []
                for v1, v2 in parsed["covariances"]:
                    if v1 in latent_list and v1 not in cov_latents:
                        cov_latents.append(v1)
                    if v2 in latent_list and v2 not in cov_latents:
                        cov_latents.append(v2)
                if len(cov_latents) >= 2:
                    corr_prior = self.priors.get("correlation", _default_correlation_prior())
                    n_cov = len(cov_latents)
                    chol, corr, stds = pm.LKJCholeskyCov(
                        "cov_chol",
                        n=n_cov,
                        eta=corr_prior.params.get("eta", 2.0),
                        sd_dist=pm.HalfNormal.dist(sigma=1.0),
                        compute_corr=True,
                    )

        return pymc_model

    def fit(
        self,
        data: pd.DataFrame,
        draws: int = 2000,
        tune: int = 1000,
        chains: int = 4,
        target_accept: float = 0.9,
        random_seed: int = 42,
        **kwargs,
    ) -> BayesianSEMResult:
        import pymc as pm
        import arviz as az

        pymc_model = self._build_pymc_model(data)

        with pymc_model:
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

        fit_stats: Dict[str, float] = {}
        try:
            with pymc_model:
                waic = az.waic(trace)
                fit_stats["waic"] = float(waic.waic)
                fit_stats["waic_se"] = float(waic.se)
            loo = az.loo(trace)
            fit_stats["loo"] = float(loo.loo)
            fit_stats["loo_se"] = float(loo.se)
        except Exception as e:
            warnings.warn(f"Could not compute WAIC/LOO: {e}")

        try:
            with pymc_model:
                log_lik = pm.compute_log_likelihood(trace)
                dic_val = _compute_dic(log_lik)
                fit_stats["dic"] = dic_val
        except Exception as e:
            warnings.warn(f"Could not compute DIC: {e}")

        convergence_diagnostics: Dict[str, Any] = {}
        try:
            rhats = summary["r_hat"].to_dict() if "r_hat" in summary.columns else {}
            ess_bulk = summary["ess_bulk"].to_dict() if "ess_bulk" in summary.columns else {}
            ess_tail = summary["ess_tail"].to_dict() if "ess_tail" in summary.columns else {}
            convergence_diagnostics = {
                "r_hat": rhats,
                "ess_bulk": ess_bulk,
                "ess_tail": ess_tail,
                "max_rhat": float(max(rhats.values())) if rhats else float("nan"),
                "min_ess_bulk": float(min(ess_bulk.values())) if ess_bulk else float("nan"),
            }
            if convergence_diagnostics["max_rhat"] > 1.05:
                warnings.warn(
                    f"Max R-hat = {convergence_diagnostics['max_rhat']:.3f} > 1.05. "
                    "Consider increasing tune or target_accept."
                )
            if convergence_diagnostics["min_ess_bulk"] < 400:
                warnings.warn(
                    f"Min ESS_bulk = {convergence_diagnostics['min_ess_bulk']:.0f} < 400. "
                    "Consider increasing draws."
                )
        except Exception:
            pass

        posterior_predictive = None
        try:
            with pymc_model:
                ppc = pm.sample_posterior_predictive(trace, predictions=True)
            posterior_predictive = {
                k: v.values for k, v in ppc.predictions.items()
            }
        except Exception:
            pass

        return BayesianSEMResult(
            trace=trace,
            model=pymc_model,
            summary=summary,
            fit_stats=fit_stats,
            posterior_predictive=posterior_predictive,
            convergence_diagnostics=convergence_diagnostics,
            model_syntax=self.model_syntax,
        )

    def get_default_priors(self, data: pd.DataFrame) -> Dict[str, PriorSpec]:
        scales: Dict[str, float] = {}
        for col in data.columns:
            scales[col] = float(data[col].std()) if col in data.columns else 1.0
        overall_scale = float(np.mean(list(scales.values()))) if scales else 1.0

        priors: Dict[str, PriorSpec] = {}
        for latent, indicator, label in self._parsed["measurements"]:
            lname = f"loading_{latent}_{indicator}"
            priors[lname] = PriorSpec("normal", {"mu": 0.0, "sigma": 1.0})
            rname = f"residual_{indicator}"
            priors[rname] = PriorSpec("half_normal", {"sigma": scales.get(indicator, overall_scale)})

        for target, predictor, label in self._parsed["regressions"]:
            cname = f"reg_{target}_{predictor}"
            pred_scale = scales.get(predictor, overall_scale)
            priors[cname] = PriorSpec("normal", {"mu": 0.0, "sigma": max(pred_scale, 0.1)})

        for lv in self._parsed["latents"]:
            priors[f"eta_{lv}"] = PriorSpec("normal", {"mu": 0.0, "sigma": 1.0})

        priors["correlation"] = PriorSpec("lkj", {"eta": 2.0})
        return priors

    def posterior_predictive_check(
        self, data: pd.DataFrame, n_samples: int = 100
    ) -> Dict:
        import pymc as pm

        if not hasattr(self, "_result") or self._result is None:
            pymc_model = self._build_pymc_model(data)
            with pymc_model:
                trace = pm.sample(
                    draws=n_samples, tune=500, chains=2, random_seed=42
                )
        else:
            trace = self._result.trace
            pymc_model = self._result.model

        with pymc_model:
            ppc = pm.sample_posterior_predictive(trace, predictions=True)

        observed_cols = sorted(self._parsed["observed"])
        result: Dict[str, Any] = {"predictions": {}, "fit_stats": {}}

        for col in observed_cols:
            key = f"obs_{col}"
            if key in ppc.predictions:
                pred_vals = ppc.predictions[key].values.flatten()
                obs_vals = data[col].values if col in data.columns else None
                result["predictions"][col] = pred_vals
                if obs_vals is not None:
                    result["fit_stats"][col] = {
                        "mean_pred": float(np.mean(pred_vals)),
                        "mean_obs": float(np.mean(obs_vals)),
                        "sd_pred": float(np.std(pred_vals)),
                        "sd_obs": float(np.std(obs_vals)),
                        "coverage_95": float(
                            np.mean(
                                (obs_vals >= np.percentile(pred_vals, 2.5))
                                & (obs_vals <= np.percentile(pred_vals, 97.5))
                            )
                        ),
                    }

        return result

    def compare_models(self, other_result: BayesianSEMResult) -> Dict:
        import arviz as az

        comparison: Dict[str, Any] = {}
        trace_self = self._result.trace if hasattr(self, "_result") and self._result else None
        if trace_self is None:
            raise ValueError("Call fit() before comparing models.")

        try:
            df_compare = az.compare(
                {"model_1": trace_self, "model_2": other_result.trace},
                ic="loo",
            )
            comparison["comparison_table"] = df_compare
            comparison["preferred"] = df_compare.index[0] if len(df_compare) > 0 else None
        except Exception as e:
            comparison["error"] = str(e)

        return comparison


def _compute_dic(trace) -> float:
    import arviz as az

    log_lik = trace.log_likelihood
    if log_lik is None:
        return float("nan")
    total_dims = [d for d in log_lik.dims if d not in ("chain", "draw")]
    ll = log_lik.to_array().sum(dim=total_dims) if total_dims else log_lik.to_array()
    mean_ll = float(ll.mean())
    deviance_mean = -2.0 * mean_ll
    pointwise = ll.values.flatten()
    deviance_at_mean = -2.0 * np.log(np.exp(pointwise).mean())
    p_dic = deviance_at_mean - deviance_mean
    return deviance_mean + 2.0 * p_dic


def quick_bayesian_cfa(
    data: pd.DataFrame,
    latent_dict: Dict[str, List[str]],
    draws: int = 2000,
    tune: int = 1000,
    chains: int = 4,
    random_seed: int = 42,
) -> BayesianSEMResult:
    lines: List[str] = []
    for latent, indicators in latent_dict.items():
        lines.append(f"{latent} =~ {' + '.join(indicators)}")
    syntax = "\n".join(lines)
    bsem = BayesianSEM(syntax)
    result = bsem.fit(
        data, draws=draws, tune=tune, chains=chains, random_seed=random_seed
    )
    return result


def bayesian_model_comparison(
    results: Dict[str, BayesianSEMResult],
) -> pd.DataFrame:
    import arviz as az

    traces = {name: r.trace for name, r in results.items()}
    try:
        comparison = az.compare(traces, ic="loo")
    except Exception:
        try:
            comparison = az.compare(traces, ic="waic")
        except Exception as e:
            warnings.warn(f"Model comparison failed: {e}")
            return pd.DataFrame(
                {"model": list(results.keys()), "error": str(e)}
            )

    rows = []
    for name in results:
        if name in comparison.index:
            row = comparison.loc[name]
            rows.append({
                "model": name,
                "rank": int(row.get("rank", -1)) if "rank" in row else -1,
                "loo": float(row.get("loo", np.nan)),
                "p_loo": float(row.get("p_loo", np.nan)),
                "d_loo": float(row.get("d_loo", np.nan)),
                "weight": float(row.get("weight", np.nan)),
                "se": float(row.get("se", np.nan)),
                "warning": bool(row.get("warning", False)),
            })
        else:
            rows.append({
                "model": name,
                "rank": -1,
                "loo": np.nan,
                "p_loo": np.nan,
                "d_loo": np.nan,
                "weight": np.nan,
                "se": np.nan,
                "warning": True,
            })

    return pd.DataFrame(rows).sort_values("rank")
