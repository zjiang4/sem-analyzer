"""Two-level multilevel Structural Equation Modeling via data decomposition and Bayesian integration."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import warnings


@dataclass
class MultilevelSEMResult:
    within_model: Any
    between_model: Any
    within_fit_stats: Dict[str, float]
    between_fit_stats: Dict[str, float]
    within_parameters: pd.DataFrame
    between_parameters: pd.DataFrame
    icc: Dict[str, float]
    decomposition: Dict[str, Any]
    cluster_var: str
    n_clusters: int
    n_obs: int
    model_syntax: str


def compute_icc(data: pd.DataFrame, cluster_var: str) -> Dict[str, float]:
    numeric_cols = [
        c for c in data.select_dtypes(include=[np.number]).columns
        if c != cluster_var
    ]
    icc_dict: Dict[str, float] = {}
    grouped = data.groupby(cluster_var)
    cluster_sizes = grouped.size()
    n_obs = len(data)
    n_clusters = len(cluster_sizes)
    mean_cluster_size = n_obs / n_clusters if n_clusters > 0 else 1.0
    for col in numeric_cols:
        grand_mean = data[col].mean()
        cluster_means = grouped[col].mean()
        ss_between = ((cluster_means - grand_mean) ** 2 * cluster_sizes).sum()
        ss_within = sum(
            group[col].var(ddof=0) * len(group)
            for _, group in grouped
        )
        ms_between = ss_between / (n_clusters - 1) if n_clusters > 1 else 0.0
        ms_within = ss_within / (n_obs - n_clusters) if n_obs > n_clusters else 1.0
        icc_val = (ms_between - ms_within) / (
            ms_between + (mean_cluster_size - 1) * ms_within
        ) if ms_between + (mean_cluster_size - 1) * ms_within > 0 else 0.0
        icc_dict[col] = max(0.0, min(1.0, icc_val))
    return icc_dict


def decompose_multilevel(
    data: pd.DataFrame, cluster_var: str
) -> Tuple[pd.DataFrame, pd.DataFrame, Dict]:
    grouped = data.groupby(cluster_var)
    cluster_means = grouped.mean(numeric_only=True)
    cluster_sizes = grouped.size().to_dict()

    numeric_cols = [
        c for c in data.select_dtypes(include=[np.number]).columns
        if c != cluster_var
    ]

    within_data = data.copy()
    for col in numeric_cols:
        mean_map = data.groupby(cluster_var)[col].transform("mean")
        within_data[col] = data[col] - mean_map

    between_data = cluster_means.reset_index()

    icc_vals = compute_icc(data, cluster_var)

    info: Dict[str, Any] = {
        "n_clusters": len(cluster_sizes),
        "cluster_sizes": cluster_sizes,
        "icc": icc_vals,
        "numeric_cols": numeric_cols,
    }
    return within_data, between_data, info


def compare_levels(
    within_result: MultilevelSEMResult, between_result: MultilevelSEMResult
) -> Dict[str, Any]:
    result: Dict[str, Any] = {}

    within_params = within_result.within_parameters
    between_params = between_result.between_parameters

    if isinstance(within_params, pd.DataFrame) and isinstance(between_params, pd.DataFrame):
        try:
            within_est = within_params.set_index(["lval", "op", "rval"])[["Estimate"]] if "Estimate" in within_params.columns else within_params
            between_est = between_params.set_index(["lval", "op", "rval"])[["Estimate"]] if "Estimate" in between_params.columns else between_params
            result["within_parameter_summary"] = within_est.to_dict()
            result["between_parameter_summary"] = between_est.to_dict()
        except Exception:
            result["within_parameter_summary"] = "could not summarize"
            result["between_parameter_summary"] = "could not summarize"

    result["icc"] = within_result.icc
    total_icc = sum(within_result.icc.values()) if within_result.icc else 0
    n_vars = len(within_result.icc) if within_result.icc else 1
    result["average_icc"] = total_icc / n_vars

    result["variance_attribution"] = {}
    for var_name, icc_val in within_result.icc.items():
        result["variance_attribution"][var_name] = {
            "between_proportion": icc_val,
            "within_proportion": 1.0 - icc_val,
            "dominant_level": "between" if icc_val > 0.5 else "within",
        }

    result["fit_comparison"] = {
        "within": within_result.within_fit_stats,
        "between": between_result.between_fit_stats,
    }

    return result


class MultilevelSEM:
    def __init__(self, within_syntax: str, between_syntax: Optional[str] = None):
        self.within_syntax = within_syntax
        self.between_syntax = between_syntax

    def fit(
        self,
        data: pd.DataFrame,
        cluster_var: str,
        estimator: str = "ML",
    ) -> MultilevelSEMResult:
        from semopy import Model, calc_stats

        icc_vals = compute_icc(data, cluster_var)
        within_data, between_data, decomp_info = decompose_multilevel(data, cluster_var)

        numeric_cols = decomp_info.get("numeric_cols", [])
        within_cols = [c for c in numeric_cols if c in within_data.columns]
        within_df = within_data[within_cols].dropna()
        between_cols = [c for c in numeric_cols if c in between_data.columns]
        between_df = between_data[between_cols].dropna()

        within_model = Model(self.within_syntax)
        within_model.load_dataset(within_df)
        within_model.fit()

        try:
            within_stats_df = calc_stats(within_model)
            within_fit_stats = within_stats_df.iloc[0].to_dict()
            within_fit_stats = {k: float(v) for k, v in within_fit_stats.items()}
        except Exception:
            within_fit_stats = {}

        try:
            within_params = within_model.inspect()
        except Exception:
            within_params = pd.DataFrame()

        between_syntax = self.between_syntax or self.within_syntax
        between_model = Model(between_syntax)
        between_model.load_dataset(between_df)
        between_model.fit()

        try:
            between_stats_df = calc_stats(between_model)
            between_fit_stats = between_stats_df.iloc[0].to_dict()
            between_fit_stats = {k: float(v) for k, v in between_fit_stats.items()}
        except Exception:
            between_fit_stats = {}

        try:
            between_params = between_model.inspect()
        except Exception:
            between_params = pd.DataFrame()

        return MultilevelSEMResult(
            within_model=within_model,
            between_model=between_model,
            within_fit_stats=within_fit_stats,
            between_fit_stats=between_fit_stats,
            within_parameters=within_params,
            between_parameters=between_params,
            icc=icc_vals,
            decomposition=decomp_info,
            cluster_var=cluster_var,
            n_clusters=decomp_info["n_clusters"],
            n_obs=len(data),
            model_syntax=self.within_syntax,
        )

    def fit_bayesian(
        self,
        data: pd.DataFrame,
        cluster_var: str,
        draws: int = 2000,
        tune: int = 1000,
        chains: int = 4,
    ) -> MultilevelSEMResult:
        import pymc as pm
        import arviz as az

        icc_vals = compute_icc(data, cluster_var)
        within_data, between_data, decomp_info = decompose_multilevel(data, cluster_var)

        numeric_cols = decomp_info.get("numeric_cols", [])
        clusters = data[cluster_var].astype("category").cat.codes.values
        n_clusters = decomp_info["n_clusters"]
        n_obs = len(data)
        cluster_idx = clusters

        within_parsed = self._parse_syntax(self.within_syntax)
        between_syntax = self.between_syntax or self.within_syntax
        between_parsed = self._parse_syntax(between_syntax)

        data_dict = {col: data[col].values.astype(np.float64) for col in numeric_cols}

        with pm.Model() as pymc_model:
            cluster_offsets = {}
            for col in numeric_cols:
                mu_between = pm.Normal(f"mu_between_{col}", mu=0.0, sigma=10.0)
                sigma_between = pm.HalfNormal(f"sigma_between_{col}", sigma=5.0)
                z_cluster = pm.Normal(f"z_cluster_{col}", mu=0.0, sigma=1.0, shape=n_clusters)
                cluster_offsets[col] = mu_between + sigma_between * z_cluster

            sigma_within = {}
            for col in numeric_cols:
                sigma_within[col] = pm.HalfNormal(f"sigma_within_{col}", sigma=5.0)

            within_latent_scores = {}
            for lv in sorted(within_parsed["latents"]):
                eta_w = pm.Normal(f"eta_within_{lv}", mu=0.0, sigma=1.0, shape=n_obs)
                within_latent_scores[lv] = eta_w

            between_latent_scores = {}
            for lv in sorted(between_parsed["latents"]):
                eta_b = pm.Normal(f"eta_between_{lv}", mu=0.0, sigma=1.0, shape=n_clusters)
                between_latent_scores[lv] = eta_b

            within_loadings = {}
            for latent, indicator, label in within_parsed["measurements"]:
                lname = f"w_loading_{latent}_{indicator}"
                loading = pm.Normal(lname, mu=0.0, sigma=1.0)
                within_loadings[(latent, indicator)] = loading

            between_loadings = {}
            for latent, indicator, label in between_parsed["measurements"]:
                lname = f"b_loading_{latent}_{indicator}"
                loading = pm.Normal(lname, mu=0.0, sigma=1.0)
                between_loadings[(latent, indicator)] = loading

            for latent, indicator, label in within_parsed["measurements"]:
                loading = within_loadings[(latent, indicator)]
                if latent in within_latent_scores:
                    mu_w = loading * within_latent_scores[latent]
                else:
                    mu_w = 0.0
                cluster_effect = cluster_offsets[indicator][cluster_idx]
                mu_total = cluster_effect + mu_w
                pm.Normal(
                    f"obs_within_{indicator}",
                    mu=mu_total,
                    sigma=sigma_within[indicator],
                    observed=data_dict.get(indicator, np.zeros(n_obs)),
                )

            for target, predictor, label in within_parsed["regressions"]:
                if target in within_parsed["latents"] and predictor in within_parsed["latents"]:
                    cname = f"w_reg_{target}_{predictor}"
                    coef = pm.Normal(cname, mu=0.0, sigma=1.0)
                    pm.Potential(
                        f"w_latent_reg_{target}_{predictor}",
                        pm.logp(
                            pm.Normal.dist(mu=coef * within_latent_scores[predictor], sigma=1.0),
                            within_latent_scores[target],
                        ),
                    )

            for target, predictor, label in between_parsed["regressions"]:
                if target in between_parsed["latents"] and predictor in between_parsed["latents"]:
                    cname = f"b_reg_{target}_{predictor}"
                    coef = pm.Normal(cname, mu=0.0, sigma=1.0)
                    pm.Potential(
                        f"b_latent_reg_{target}_{predictor}",
                        pm.logp(
                            pm.Normal.dist(mu=coef * between_latent_scores[predictor], sigma=1.0),
                            between_latent_scores[target],
                        ),
                    )

            trace = pm.sample(
                draws=draws,
                tune=tune,
                chains=chains,
                target_accept=0.9,
                random_seed=42,
                return_inferencedata=True,
            )

        summary = az.summary(trace)

        within_fit_stats: Dict[str, float] = {}
        between_fit_stats: Dict[str, float] = {}
        try:
            waic = az.waic(trace)
            within_fit_stats["waic"] = float(waic.waic)
            between_fit_stats["waic"] = float(waic.waic)
        except Exception:
            pass

        within_params = summary.copy()
        between_params = summary.copy()

        return MultilevelSEMResult(
            within_model=pymc_model,
            between_model=trace,
            within_fit_stats=within_fit_stats,
            between_fit_stats=between_fit_stats,
            within_parameters=within_params,
            between_parameters=between_params,
            icc=icc_vals,
            decomposition=decomp_info,
            cluster_var=cluster_var,
            n_clusters=n_clusters,
            n_obs=n_obs,
            model_syntax=self.within_syntax,
        )

    def _parse_syntax(self, syntax: str) -> Dict:
        measurements: List[Tuple[str, str, Optional[str]]] = []
        regressions: List[Tuple[str, str, Optional[str]]] = []
        covariances: List[Tuple[str, str]] = []
        latents: set = set()
        observed: set = set()

        for raw_line in syntax.strip().splitlines():
            line = raw_line.strip()
            if not line:
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
                covariances.append((lhs.strip(), rhs.strip()))
            elif "~" in line:
                lhs, rhs = line.split("~", 1)
                target = lhs.strip()
                rhs_stripped = rhs.strip()
                if rhs_stripped == "1":
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
                    if target not in latents:
                        observed.add(target)
                    if predictor not in latents:
                        observed.add(predictor)

        return {
            "measurements": measurements,
            "regressions": regressions,
            "covariances": covariances,
            "latents": latents,
            "observed": observed,
        }
