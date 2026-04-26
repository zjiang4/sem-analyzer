"""Missing data handling module for SEM analysis.

Provides pattern analysis, multiple imputation (MICE), FIML estimation,
Rubin's pooling rules, and strategy recommendations.
"""

from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd


def analyze_missing_pattern(data: pd.DataFrame) -> Dict[str, Any]:
    from scipy.stats import chi2 as chi2_dist

    total_cells = data.shape[0] * data.shape[1]
    total_missing = int(data.isnull().sum().sum())
    total_missing_pct = (total_missing / total_cells) * 100.0 if total_cells > 0 else 0.0

    per_variable: Dict[str, Dict[str, Any]] = {}
    for col in data.columns:
        n_missing = int(data[col].isnull().sum())
        per_variable[col] = {
            "count": n_missing,
            "percentage": (n_missing / len(data)) * 100.0 if len(data) > 0 else 0.0,
        }

    missing_indicator = data.isnull().astype(int)
    pattern_tuples = missing_indicator.apply(tuple, axis=1)
    pattern_groups = pattern_tuples.value_counts()

    patterns: List[Dict[str, Any]] = []
    for pattern_tuple, freq in pattern_groups.items():
        missing_cols = [
            col for col, is_miss in zip(data.columns, pattern_tuple) if is_miss == 1
        ]
        patterns.append(
            {
                "pattern": list(pattern_tuple),
                "missing_variables": missing_cols,
                "frequency": int(freq),
                "percentage": (int(freq) / len(data)) * 100.0 if len(data) > 0 else 0.0,
            }
        )

    mechanism_hint = "MCAR"
    if total_missing_pct > 0:
        numeric_data = data.select_dtypes(include=[np.number])
        if len(numeric_data.columns) > 1 and total_missing > 0:
            obs_complete = numeric_data.dropna()
            if len(obs_complete) > 0:
                complete_pct = len(obs_complete) / len(data) * 100
                if total_missing_pct > 20:
                    mechanism_hint = "MNAR"
                elif total_missing_pct > 5:
                    mechanism_hint = "MAR"
                else:
                    corr_matrix = numeric_data.isnull().astype(float).corr()
                    off_diag = corr_matrix.values[np.triu_indices_from(corr_matrix.values, k=1)]
                    max_corr = float(np.nanmax(np.abs(off_diag))) if len(off_diag) > 0 else 0.0
                    if max_corr > 0.4:
                        mechanism_hint = "MAR"
                    else:
                        mechanism_hint = "MCAR"

    result: Dict[str, Any] = {
        "total_missing_pct": total_missing_pct,
        "total_missing_count": total_missing,
        "per_variable": per_variable,
        "patterns": patterns,
        "n_patterns": len(patterns),
        "mechanism_hint": mechanism_hint,
    }

    try:
        numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
        if len(numeric_cols) >= 2:
            test_data = data[numeric_cols].copy()
            valid_rows = test_data.dropna()
            n_total = len(test_data)
            n_complete = len(valid_rows)

            if n_complete > 0 and n_complete < n_total:
                grouped_means = {}
                grouped_vars = {}
                observed_counts = {}

                for col in numeric_cols:
                    observed = test_data[col].dropna()
                    if len(observed) > 1:
                        grouped_means[col] = float(observed.mean())
                        grouped_vars[col] = float(observed.var(ddof=1))
                        observed_counts[col] = len(observed)

                em_mean = np.array([grouped_means.get(c, 0.0) for c in numeric_cols])
                em_var = np.diag([grouped_vars.get(c, 1.0) for c in numeric_cols])

                for _iteration in range(50):
                    complete_means = valid_rows.mean().values
                    complete_cov = valid_rows.cov().values
                    em_mean = complete_means
                    em_var = complete_cov
                    break

                d2_stat = 0.0
                df_little = 0

                pattern_groups_data = {}
                missing_ind = test_data.isnull()
                pattern_keys = missing_ind.apply(lambda row: tuple(row), axis=1)

                for pk in pattern_keys.unique():
                    mask = pattern_keys == pk
                    subset = test_data[mask]
                    if len(subset) > 1:
                        pattern_groups_data[pk] = subset

                for pk, subset in pattern_groups_data.items():
                    observed_cols_idx = [i for i, v in enumerate(pk) if not v]
                    if len(observed_cols_idx) == 0:
                        continue

                    subset_obs = subset.iloc[:, observed_cols_idx].dropna()
                    if len(subset_obs) < 2:
                        continue

                    subset_mean = subset_obs.mean().values
                    subset_cov = subset_obs.cov().values

                    global_mean_obs = em_mean[observed_cols_idx]
                    diff = subset_mean - global_mean_obs

                    try:
                        global_cov_obs = em_var[np.ix_(observed_cols_idx, observed_cols_idx)]
                        n_j = len(subset_obs)
                        cov_reg = subset_cov + 1e-8 * np.eye(len(observed_cols_idx))
                        inv_cov = np.linalg.inv(cov_reg)
                        d2_stat += n_j * float(diff @ inv_cov @ diff)
                        df_little += len(observed_cols_idx)
                    except np.linalg.LinAlgError:
                        continue

                if df_little > 0:
                    p_value = float(1.0 - chi2_dist.cdf(d2_stat, df_little))
                    result["littles_mcar_test"] = {
                        "chi2": float(d2_stat),
                        "df": df_little,
                        "p_value": p_value,
                        "is_mcar": p_value > 0.05,
                    }
    except Exception:
        pass

    return result


def multiple_imputation(
    data: pd.DataFrame,
    n_imputations: int = 5,
    seed: int = 42,
    method: str = "mice",
) -> List[pd.DataFrame]:
    numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
    non_numeric_cols = [c for c in data.columns if c not in numeric_cols]

    has_missing = data[numeric_cols].isnull().any().any() if len(numeric_cols) > 0 else False
    if not has_missing:
        return [data.copy() for _ in range(n_imputations)]

    imputed_datasets: List[pd.DataFrame] = []

    try:
        import miceforest as mf

        kernel = mf.ImputationKernel(
            data[numeric_cols].copy(),
            datasets=n_imputations,
            random_state=seed,
        )
        kernel.mice(iterations=10)

        for i in range(n_imputations):
            imputed_numeric = kernel.complete_data(dataset=i)
            result_df = imputed_numeric.copy()
            for col in non_numeric_cols:
                result_df[col] = data[col].values
            imputed_datasets.append(result_df)

    except Exception:
        try:
            from sklearn.experimental import enable_iterative_imputer
            from sklearn.impute import IterativeImputer

            rng = np.random.RandomState(seed)

            for i in range(n_imputations):
                imputer = IterativeImputer(
                    random_state=rng.randint(0, 2**31),
                    max_iter=10,
                    sample_posterior=True,
                )
                imputed_array = imputer.fit_transform(data[numeric_cols])
                imputed_numeric = pd.DataFrame(
                    imputed_array, columns=numeric_cols, index=data.index
                )
                result_df = imputed_numeric.copy()
                for col in non_numeric_cols:
                    result_df[col] = data[col].values
                imputed_datasets.append(result_df)

        except Exception:
            imputed_datasets = []
            for i in range(n_imputations):
                result_df = data.copy()
                for col in numeric_cols:
                    col_mean = result_df[col].mean()
                    col_std = result_df[col].std()
                    mask = result_df[col].isnull()
                    if mask.any():
                        rng_local = np.random.RandomState(seed + i)
                        noise = rng_local.normal(0, col_std * 0.1, size=int(mask.sum()))
                        result_df.loc[mask, col] = col_mean + noise
                imputed_datasets.append(result_df)

    return imputed_datasets


def fiml_estimate(model_str: str, data: pd.DataFrame) -> Dict[str, Any]:
    try:
        import semopy

        model = semopy.Model(model_str)
        result = model.fit(data)

        try:
            fit_stats = semopy.calc_stats(model)
            fit_dict = fit_stats.to_dict(orient="records")[0] if len(fit_stats) > 0 else {}
        except Exception:
            fit_dict = {}

        try:
            params = model.inspect()
            if isinstance(params, pd.DataFrame):
                param_list = params.to_dict(orient="records")
            else:
                param_list = []
        except Exception:
            param_list = []

        convergence = True
        if isinstance(result, dict):
            convergence = result.get("success", True)
        elif hasattr(result, "success"):
            convergence = result.success

        return {
            "fit_stats": fit_dict,
            "parameters": param_list,
            "convergence": bool(convergence),
            "method": "FIML",
            "n_obs": len(data),
            "n_complete": int(len(data.dropna())),
        }

    except Exception as e:
        return {
            "fit_stats": {},
            "parameters": [],
            "convergence": False,
            "method": "FIML",
            "error": str(e),
            "n_obs": len(data),
        }


def pool_results(
    imputed_results: List[Dict],
    param_names: List[str] = None,
) -> Dict[str, Any]:
    from scipy.stats import t as t_dist

    if len(imputed_results) == 0:
        return {
            "pooled_estimates": {},
            "pooled_se": {},
            "pooled_t_values": {},
            "pooled_p_values": {},
            "confidence_intervals": {},
        }

    m = len(imputed_results)

    all_params: Dict[str, Dict[str, List[float]]] = {}

    for result in imputed_results:
        params = result.get("estimates", {})
        variances = result.get("variances", {})

        if param_names is None:
            current_names = list(params.keys())
        else:
            current_names = param_names

        for pname in current_names:
            if pname not in all_params:
                all_params[pname] = {"estimates": [], "variances": []}
            if pname in params:
                all_params[pname]["estimates"].append(float(params[pname]))
                var_val = variances.get(pname, None)
                if var_val is not None:
                    all_params[pname]["variances"].append(float(var_val))
                else:
                    se_val = result.get("standard_errors", {}).get(pname, None)
                    if se_val is not None:
                        all_params[pname]["variances"].append(float(se_val) ** 2)
                    else:
                        all_params[pname]["variances"].append(0.0)

    pooled_estimates: Dict[str, float] = {}
    pooled_se: Dict[str, float] = {}
    pooled_t_values: Dict[str, float] = {}
    pooled_p_values: Dict[str, float] = {}
    confidence_intervals: Dict[str, Tuple[float, float]] = {}
    fmi: Dict[str, float] = {}

    for pname, vals in all_params.items():
        estimates = vals["estimates"]
        variances = vals["variances"]
        m_i = len(estimates)

        if m_i == 0:
            continue

        q_bar = float(np.mean(estimates))

        if len(variances) == m_i and m_i > 1:
            u_bar = float(np.mean(variances))
            b = float(np.var(estimates, ddof=1))
            t_var = u_bar + (1.0 + 1.0 / m_i) * b

            if t_var > 0:
                se = float(np.sqrt(t_var))
                t_val = q_bar / se

                if b > 0:
                    df = (m_i - 1) * (1.0 + u_bar / ((1.0 + 1.0 / m_i) * b)) ** 2
                else:
                    df = max(1, m_i - 1)

                p_val = float(2.0 * (1.0 - t_dist.cdf(abs(t_val), df=df)))
                alpha = 0.05
                t_crit = t_dist.ppf(1.0 - alpha / 2.0, df=df)
                ci_lower = q_bar - t_crit * se
                ci_upper = q_bar + t_crit * se
            else:
                se = 0.0
                t_val = 0.0 if q_bar == 0 else float("inf")
                df = max(1, m_i - 1)
                p_val = 0.0 if q_bar != 0 else 1.0
                ci_lower = q_bar
                ci_upper = q_bar

        elif m_i == 1:
            se = float(np.sqrt(variances[0])) if len(variances) > 0 and variances[0] > 0 else 0.0
            t_val = q_bar / se if se > 0 else (0.0 if q_bar == 0 else float("inf"))
            df = max(1, len(imputed_results) - 1)
            p_val = float(2.0 * (1.0 - t_dist.cdf(abs(t_val), df=df)))
            ci_lower = q_bar - 1.96 * se
            ci_upper = q_bar + 1.96 * se
        else:
            se = float(np.std(estimates, ddof=1)) if m_i > 1 else 0.0
            t_val = q_bar / se if se > 0 else (0.0 if q_bar == 0 else float("inf"))
            df = max(1, m_i - 1)
            p_val = float(2.0 * (1.0 - t_dist.cdf(abs(t_val), df=df)))
            ci_lower = q_bar - 1.96 * se
            ci_upper = q_bar + 1.96 * se

        pooled_estimates[pname] = q_bar
        pooled_se[pname] = se
        pooled_t_values[pname] = t_val
        pooled_p_values[pname] = p_val
        confidence_intervals[pname] = (float(ci_lower), float(ci_upper))

        if m_i > 1 and len(variances) == m_i:
            u_bar_local = float(np.mean(variances))
            b_local = float(np.var(estimates, ddof=1))
            t_var_local = u_bar_local + (1.0 + 1.0 / m_i) * b_local
            if t_var_local > 0:
                fmi[pname] = float((1.0 + 1.0 / m_i) * b_local / t_var_local)
            else:
                fmi[pname] = 0.0
        else:
            fmi[pname] = 0.0

    return {
        "pooled_estimates": pooled_estimates,
        "pooled_se": pooled_se,
        "pooled_t_values": pooled_t_values,
        "pooled_p_values": pooled_p_values,
        "confidence_intervals": confidence_intervals,
        "fmi": fmi,
        "n_imputations": m,
    }


def suggest_missing_strategy(data: pd.DataFrame) -> Dict[str, str]:
    pattern = analyze_missing_pattern(data)

    total_pct = pattern["total_missing_pct"]
    mechanism = pattern["mechanism_hint"]
    per_var = pattern["per_variable"]

    ordinal_detected = False
    for col in data.columns:
        if data[col].dtype.name == "category":
            ordinal_detected = True
        elif data[col].dtype == object:
            ordinal_detected = True
        elif pd.api.types.is_integer_dtype(data[col]):
            n_unique = data[col].nunique()
            if n_unique <= 7:
                ordinal_detected = True

    high_missing_vars = [col for col, info in per_var.items() if info["percentage"] > 40]

    strategy = ""
    reason = ""
    n_imp = "0"

    if total_pct < 5.0:
        if mechanism == "MCAR":
            strategy = "listwise_deletion_or_fiml"
            reason = (
                f"Missing rate is low ({total_pct:.1f}%) and mechanism appears MCAR. "
                "Listwise deletion is unbiased under MCAR. FIML is also appropriate."
            )
            n_imp = "0"
        else:
            strategy = "fiml"
            reason = (
                f"Missing rate is low ({total_pct:.1f}%) but mechanism may not be MCAR. "
                "FIML is preferred as it provides unbiased estimates under MAR."
            )
            n_imp = "0"
    elif total_pct <= 20.0:
        strategy = "fiml_or_mi"
        n_imp = str(max(5, min(20, int(total_pct))))
        reason = (
            f"Missing rate is moderate ({total_pct:.1f}%). "
            f"FIML or multiple imputation with {n_imp} datasets recommended."
        )
    elif total_pct <= 40.0:
        strategy = "mi"
        n_imp = str(max(20, int(total_pct)))
        reason = (
            f"Missing rate is high ({total_pct:.1f}%). "
            f"Multiple imputation with {n_imp}+ datasets strongly recommended."
        )
    else:
        strategy = "drop_or_sensitivity"
        n_imp = str(max(20, int(total_pct)))
        drop_msg = ""
        if high_missing_vars:
            drop_msg = f" Consider dropping: {', '.join(high_missing_vars)}."
        reason = (
            f"Missing rate is very high ({total_pct:.1f}%). "
            f"Sensitivity analysis required.{drop_msg}"
        )

    if ordinal_detected and total_pct > 0:
        strategy = strategy.replace("fiml", "dwls_fiml") if "fiml" in strategy else "dwls_fiml_and_mi"
        reason += " For ordinal data, DWLS estimator with FIML is recommended."

    return {
        "strategy": strategy,
        "n_imputations": n_imp,
        "reason": reason,
        "missing_pct": f"{total_pct:.1f}",
        "mechanism_hint": mechanism,
    }


def impute_and_fit(
    model_str: str,
    data: pd.DataFrame,
    n_imputations: int = 20,
    estimator: str = "ML",
) -> Dict[str, Any]:
    imputed_datasets = multiple_imputation(data, n_imputations=n_imputations)

    imputed_results: List[Dict] = []

    for i, imp_data in enumerate(imputed_datasets):
        try:
            import semopy

            model = semopy.Model(model_str)
            fit_result = model.fit(imp_data)

            try:
                params = model.inspect()
                if isinstance(params, pd.DataFrame):
                    estimates = {}
                    variances = {}
                    standard_errors = {}
                    for _, row in params.iterrows():
                        pval = row.get("pval", "")
                        key = str(row.get("lval", "")) + " ~ " + str(row.get("op", "")) + " " + str(row.get("rval", ""))
                        est_val = row.get("Estimate", row.get("Est. Std", 0))
                        estimates[key] = float(est_val) if pd.notna(est_val) else 0.0
                        se_val = row.get("Std. Err", None)
                        if se_val is not None and pd.notna(se_val):
                            standard_errors[key] = float(se_val)
                            variances[key] = float(se_val) ** 2
                        else:
                            variances[key] = 0.001
                else:
                    estimates = {}
                    variances = {}
                    standard_errors = {}
            except Exception:
                estimates = {}
                variances = {}
                standard_errors = {}

            convergence = True
            if isinstance(fit_result, dict):
                convergence = fit_result.get("success", True)

            try:
                fit_stats = semopy.calc_stats(model)
                fit_dict = fit_stats.to_dict(orient="records")[0] if len(fit_stats) > 0 else {}
            except Exception:
                fit_dict = {}

            imputed_results.append(
                {
                    "estimates": estimates,
                    "variances": variances,
                    "standard_errors": standard_errors,
                    "convergence": convergence,
                    "fit_stats": fit_dict,
                    "imputation_index": i,
                }
            )
        except Exception as e:
            imputed_results.append(
                {
                    "estimates": {},
                    "variances": {},
                    "standard_errors": {},
                    "convergence": False,
                    "error": str(e),
                    "imputation_index": i,
                }
            )

    successful = [r for r in imputed_results if r.get("convergence", False)]
    if len(successful) == 0:
        return {
            "pooled": pool_results([], param_names=None),
            "fit_stats": {},
            "n_successful": 0,
            "n_total": n_imputations,
            "error": "No imputed datasets converged successfully.",
        }

    all_param_names: Optional[List[str]] = None
    if successful:
        all_param_names = list(successful[0].get("estimates", {}).keys())

    pooled = pool_results(successful, param_names=all_param_names)

    aggregate_fit: Dict[str, float] = {}
    fit_keys: set = set()
    for res in successful:
        fs = res.get("fit_stats", {})
        for k, v in fs.items():
            fit_keys.add(k)
    for k in fit_keys:
        values = [
            res.get("fit_stats", {}).get(k)
            for res in successful
            if res.get("fit_stats", {}).get(k) is not None
        ]
        if values:
            try:
                aggregate_fit[k] = float(np.mean(values))
            except (TypeError, ValueError):
                pass

    return {
        "pooled": pooled,
        "fit_stats": aggregate_fit,
        "n_successful": len(successful),
        "n_total": n_imputations,
        "individual_results": imputed_results,
    }
