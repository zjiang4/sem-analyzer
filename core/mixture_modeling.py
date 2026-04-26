"""Mixture SEM (Latent Class SEM) combining latent class analysis with SEM per class.

Uses sklearn GaussianMixture for initial class assignment, semopy for within-class
SEM fitting, and an EM-like iterative procedure to refine class assignments.
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import numpy as np
import pandas as pd
import warnings


@dataclass
class MixtureSEMResult:
    n_classes: int
    class_proportions: Dict[int, float]
    class_assignments: np.ndarray
    class_models: Dict[int, Any]
    class_fit_stats: Dict[int, Dict[str, float]]
    overall_stats: Dict[str, Any]
    comparison: Dict[str, Any]
    model_syntax: str


class MixtureSEM:
    def __init__(
        self,
        model_syntax: str,
        n_classes: int = 2,
        max_iter: int = 100,
        tol: float = 1e-6,
    ):
        self.model_syntax = model_syntax
        self.n_classes = n_classes
        self.max_iter = max_iter
        self.tol = tol

    def fit(
        self,
        data: pd.DataFrame,
        n_classes: int = None,
        method: str = "em",
    ) -> MixtureSEMResult:
        k = n_classes or self.n_classes
        if method == "em":
            return self._fit_em(data, k)
        elif method == "classify_analyze":
            return self._fit_classify_analyze(data, k)
        else:
            raise ValueError(f"Unknown method: {method}. Use 'em' or 'classify_analyze'.")

    def _fit_classify_analyze(
        self, data: pd.DataFrame, n_classes: int
    ) -> MixtureSEMResult:
        from sklearn.mixture import GaussianMixture

        import semopy

        obs_cols = data.select_dtypes(include=[np.number]).columns.tolist()
        obs_data = data[obs_cols].dropna()

        gm = GaussianMixture(n_components=n_classes, random_state=42, n_init=3)
        labels = gm.fit_predict(obs_data.values)

        proportions = {}
        for k_idx in range(n_classes):
            proportions[k_idx] = float(np.mean(labels == k_idx))

        assignments = np.zeros((len(obs_data), n_classes))
        for i, lbl in enumerate(labels):
            assignments[i, lbl] = 1.0

        class_models: Dict[int, Any] = {}
        class_fit_stats: Dict[int, Dict[str, float]] = {}

        for k_idx in range(n_classes):
            mask = labels == k_idx
            class_data = obs_data.loc[mask]
            if len(class_data) < 5:
                class_models[k_idx] = None
                class_fit_stats[k_idx] = {"error": "too few observations"}
                continue
            try:
                model = semopy.Model(self.model_syntax)
                model.fit(class_data)
                class_models[k_idx] = model
                try:
                    stats = semopy.calc_stats(model)
                    if isinstance(stats, pd.DataFrame) and len(stats) > 0:
                        class_fit_stats[k_idx] = stats.iloc[0].to_dict()
                    else:
                        class_fit_stats[k_idx] = {}
                except Exception:
                    class_fit_stats[k_idx] = {}
            except Exception as e:
                class_models[k_idx] = None
                class_fit_stats[k_idx] = {"error": str(e)}

        n_obs = len(obs_data)
        n_params = self._count_free_params(class_models, obs_data)
        log_likelihood = self._compute_gmm_log_likelihood(gm, obs_data.values)
        bic = -2.0 * log_likelihood + n_params * np.log(n_obs)
        aic = -2.0 * log_likelihood + 2.0 * n_params
        entropy = compute_entropy(assignments)

        overall_stats: Dict[str, Any] = {
            "BIC": float(bic),
            "AIC": float(aic),
            "log_likelihood": float(log_likelihood),
            "entropy": float(entropy),
            "n_params": int(n_params),
            "n_obs": int(n_obs),
            "method": "classify_analyze",
            "converged": True,
        }

        return MixtureSEMResult(
            n_classes=n_classes,
            class_proportions=proportions,
            class_assignments=assignments,
            class_models=class_models,
            class_fit_stats=class_fit_stats,
            overall_stats=overall_stats,
            comparison={},
            model_syntax=self.model_syntax,
        )

    def _fit_em(self, data: pd.DataFrame, n_classes: int) -> MixtureSEMResult:
        from scipy.stats import multivariate_normal as mvn

        import semopy

        obs_cols = data.select_dtypes(include=[np.number]).columns.tolist()
        obs_data = data[obs_cols].dropna().values
        n_obs, n_vars = obs_data.shape

        if n_obs < n_classes * 5:
            warnings.warn(
                f"Too few observations ({n_obs}) for {n_classes} classes. "
                "Falling back to classify_analyze."
            )
            return self._fit_classify_analyze(data[obs_cols].dropna(), n_classes)

        assignments = self._initialize_assignments(obs_data, n_classes)
        proportions = np.mean(assignments, axis=0)

        prev_ll = -np.inf
        class_models: Dict[int, Any] = {}
        class_fit_stats: Dict[int, Dict[str, float]] = {}
        class_means: Dict[int, np.ndarray] = {}
        class_covs: Dict[int, np.ndarray] = {}

        converged = False
        for iteration in range(self.max_iter):
            class_models = {}
            class_fit_stats = {}
            class_means = {}
            class_covs = {}

            for k_idx in range(n_classes):
                weights = assignments[:, k_idx]
                weight_sum = weights.sum()
                if weight_sum < 1.0:
                    class_models[k_idx] = None
                    class_fit_stats[k_idx] = {"error": "empty class"}
                    class_means[k_idx] = np.zeros(n_vars)
                    class_covs[k_idx] = np.eye(n_vars)
                    continue

                class_data = pd.DataFrame(obs_data, columns=obs_cols)
                try:
                    model = semopy.Model(self.model_syntax)
                    model.fit(class_data, group_weights=weights)
                    class_models[k_idx] = model

                    implied_cov = self._get_implied_covariance(model, obs_cols)
                    mean_vec = np.average(obs_data, axis=0, weights=weights)

                    if implied_cov is not None:
                        class_covs[k_idx] = implied_cov
                    else:
                        weighted_cov = np.cov(obs_data.T, aweights=weights)
                        class_covs[k_idx] = weighted_cov

                    class_means[k_idx] = mean_vec

                    try:
                        stats = semopy.calc_stats(model)
                        if isinstance(stats, pd.DataFrame) and len(stats) > 0:
                            class_fit_stats[k_idx] = stats.iloc[0].to_dict()
                        else:
                            class_fit_stats[k_idx] = {}
                    except Exception:
                        class_fit_stats[k_idx] = {}

                except Exception:
                    class_models[k_idx] = None
                    weighted_mean = np.average(obs_data, axis=0, weights=weights)
                    weighted_cov = np.cov(obs_data.T, aweights=weights)
                    class_means[k_idx] = weighted_mean
                    class_covs[k_idx] = weighted_cov
                    class_fit_stats[k_idx] = {"error": "SEM fitting failed"}

            log_likelihood = 0.0
            new_assignments = np.zeros((n_obs, n_classes))

            for k_idx in range(n_classes):
                cov = class_covs[k_idx] + 1e-6 * np.eye(n_vars)
                try:
                    rv = mvn(mean=class_means[k_idx], cov=cov, allow_singular=True)
                    new_assignments[:, k_idx] = np.log(proportions[k_idx] + 1e-300) + rv.logpdf(obs_data)
                except Exception:
                    new_assignments[:, k_idx] = np.log(proportions[k_idx] + 1e-300) - 0.5 * n_vars * np.log(
                        2.0 * np.pi
                    )

            log_sum = np.array(new_assignments.copy())
            max_log = np.max(log_sum, axis=1, keepdims=True)
            log_sum_shifted = log_sum - max_log
            sum_exp = np.sum(np.exp(log_sum_shifted), axis=1, keepdims=True)
            new_assignments = np.exp(new_assignments - max_log) / sum_exp

            row_sums = new_assignments.sum(axis=1, keepdims=True)
            new_assignments = new_assignments / np.maximum(row_sums, 1e-300)

            log_likelihood = float(np.sum(max_log.flatten() + np.log(sum_exp.flatten())))

            proportions = np.mean(new_assignments, axis=0)

            ll_change = abs(log_likelihood - prev_ll)
            assignments = new_assignments
            prev_ll = log_likelihood

            if ll_change < self.tol:
                converged = True
                break

        if not converged:
            warnings.warn(
                f"EM algorithm did not converge after {self.max_iter} iterations. "
                f"Last log-likelihood change: {ll_change:.2e}"
            )

        n_params = self._count_free_params(class_models, pd.DataFrame(obs_data, columns=obs_cols))
        bic = -2.0 * log_likelihood + n_params * np.log(n_obs)
        aic = -2.0 * log_likelihood + 2.0 * n_params
        entropy = compute_entropy(assignments)

        proportions_dict = {k_idx: float(proportions[k_idx]) for k_idx in range(n_classes)}

        overall_stats: Dict[str, Any] = {
            "BIC": float(bic),
            "AIC": float(aic),
            "log_likelihood": float(log_likelihood),
            "entropy": float(entropy),
            "n_params": int(n_params),
            "n_obs": int(n_obs),
            "method": "em",
            "converged": converged,
            "iterations": iteration + 1 if converged else self.max_iter,
        }

        return MixtureSEMResult(
            n_classes=n_classes,
            class_proportions=proportions_dict,
            class_assignments=assignments,
            class_models=class_models,
            class_fit_stats=class_fit_stats,
            overall_stats=overall_stats,
            comparison={},
            model_syntax=self.model_syntax,
        )

    def _initialize_assignments(
        self, data: np.ndarray, n_classes: int
    ) -> np.ndarray:
        from sklearn.mixture import GaussianMixture

        gm = GaussianMixture(n_components=n_classes, random_state=42, n_init=3)
        gm.fit(data)
        posteriors = gm.predict_proba(data)
        return posteriors

    def _get_implied_covariance(
        self, model: Any, obs_cols: list
    ) -> Optional[np.ndarray]:
        try:
            sigma = model.calc_sigma()[0]
            if sigma is not None:
                sigma_np = np.array(sigma, dtype=np.float64)
                if sigma_np.ndim == 2:
                    return sigma_np
        except Exception:
            pass

        try:
            insp = model.inspect()
            if isinstance(insp, pd.DataFrame):
                param_dict = {}
                for _, row in insp.iterrows():
                    key = (str(row.get("lval", "")), row.get("op", ""), str(row.get("rval", "")))
                    param_dict[key] = float(row.get("Estimate", 0.0))
                return None
        except Exception:
            pass

        return None

    def _count_free_params(
        self, class_models: Dict[int, Any], data: pd.DataFrame
    ) -> int:
        total = 0
        n_vars = data.shape[1] if isinstance(data, pd.DataFrame) else len(data.columns)
        for k_idx, model in class_models.items():
            if model is None:
                total += n_vars + n_vars * (n_vars + 1) // 2
                continue
            try:
                insp = model.inspect()
                if isinstance(insp, pd.DataFrame):
                    total += len(insp)
                else:
                    total += n_vars + n_vars * (n_vars + 1) // 2
            except Exception:
                total += n_vars + n_vars * (n_vars + 1) // 2
        total += (len(class_models) - 1)
        return total

    def _compute_gmm_log_likelihood(self, gm: Any, data: np.ndarray) -> float:
        return float(np.sum(gm.score_samples(data)))

    def select_n_classes(
        self,
        data: pd.DataFrame,
        min_k: int = 2,
        max_k: int = 6,
        method: str = "em",
    ) -> Dict[str, Any]:
        results: Dict[int, Dict[str, Any]] = {}
        comparison_rows = []

        for k in range(min_k, max_k + 1):
            try:
                result = self.fit(data, n_classes=k, method=method)
                stats = result.overall_stats
                results[k] = {
                    "result": result,
                    "BIC": stats.get("BIC", np.inf),
                    "AIC": stats.get("AIC", np.inf),
                    "log_likelihood": stats.get("log_likelihood", -np.inf),
                    "entropy": stats.get("entropy", 0.0),
                    "converged": stats.get("converged", False),
                }
                assignments = result.class_assignments
                n_obs = assignments.shape[0]
                icl_penalty = np.sum(
                    assignments * np.log(np.maximum(assignments, 1e-300))
                )
                ll = stats.get("log_likelihood", -np.inf)
                n_params = stats.get("n_params", 0)
                icl = -2.0 * ll + n_params * np.log(n_obs) - 2.0 * icl_penalty

                results[k]["ICL"] = float(icl)

                comparison_rows.append(
                    {
                        "n_classes": k,
                        "BIC": stats.get("BIC", np.inf),
                        "AIC": stats.get("AIC", np.inf),
                        "ICL": float(icl),
                        "log_likelihood": stats.get("log_likelihood", -np.inf),
                        "entropy": stats.get("entropy", 0.0),
                        "converged": stats.get("converged", False),
                        "n_params": stats.get("n_params", 0),
                    }
                )
            except Exception as e:
                comparison_rows.append(
                    {
                        "n_classes": k,
                        "BIC": np.inf,
                        "AIC": np.inf,
                        "ICL": np.inf,
                        "log_likelihood": -np.inf,
                        "entropy": 0.0,
                        "converged": False,
                        "error": str(e),
                    }
                )

        comparison_df = pd.DataFrame(comparison_rows)

        valid = comparison_df[comparison_df.get("error", pd.Series(dtype=bool)).isna()]
        if len(valid) == 0:
            valid = comparison_df

        recommended_k = int(valid.loc[valid["BIC"].idxmin(), "n_classes"]) if len(valid) > 0 else min_k

        bic_values = valid["BIC"].values
        n_classes_values = valid["n_classes"].values
        if len(bic_values) >= 3:
            diffs = np.diff(bic_values)
            if len(diffs) >= 2:
                second_diffs = np.diff(diffs)
                elbow_idx = int(np.argmax(second_diffs)) + 1
                elbow_k = int(n_classes_values[elbow_idx]) if elbow_idx < len(n_classes_values) else recommended_k
            else:
                elbow_k = recommended_k
        else:
            elbow_k = recommended_k

        return {
            "comparison_table": comparison_df,
            "results": results,
            "recommended_k_bic": recommended_k,
            "recommended_k_elbow": elbow_k,
            "recommended_k": recommended_k,
        }


def compute_entropy(class_assignments: np.ndarray) -> float:
    n_obs, n_classes = class_assignments.shape
    if n_obs == 0 or n_classes <= 1:
        return 1.0

    clamped = np.clip(class_assignments, 1e-300, 1.0)
    entropy_sum = -np.sum(clamped * np.log(clamped))
    max_entropy = n_obs * np.log(n_classes)

    if max_entropy == 0:
        return 1.0

    return 1.0 - entropy_sum / max_entropy


def compute_class_separation(results: MixtureSEMResult) -> Dict[str, Any]:
    class_params: Dict[int, Dict[str, float]] = {}

    for k_idx, model in results.class_models.items():
        if model is None:
            continue
        try:
            insp = model.inspect()
            if isinstance(insp, pd.DataFrame):
                params = {}
                for _, row in insp.iterrows():
                    key = (
                        f"{row.get('lval', '')}{row.get('op', '')}{row.get('rval', '')}"
                    )
                    est = row.get("Estimate", np.nan)
                    params[key] = float(est) if pd.notna(est) else np.nan
                class_params[k_idx] = params
        except Exception:
            pass

    if len(class_params) < 2:
        return {"error": "Need at least 2 classes with valid models"}

    param_diffs: Dict[str, Dict[str, float]] = {}
    class_indices = sorted(class_params.keys())

    all_keys = set()
    for cp in class_params.values():
        all_keys.update(cp.keys())
    all_keys = sorted(all_keys)

    for i in range(len(class_indices)):
        for j in range(i + 1, len(class_indices)):
            ki = class_indices[i]
            kj = class_indices[j]
            pair_key = f"class_{ki}_vs_class_{kj}"
            diffs = {}
            for pk in all_keys:
                vi = class_params[ki].get(pk, np.nan)
                vj = class_params[kj].get(pk, np.nan)
                if pd.notna(vi) and pd.notna(vj):
                    diffs[pk] = abs(vi - vj)
            param_diffs[pair_key] = diffs

    param_variability: Dict[str, float] = {}
    for pk in all_keys:
        values = []
        for cp in class_params.values():
            v = cp.get(pk, np.nan)
            if pd.notna(v):
                values.append(v)
        if len(values) >= 2:
            param_variability[pk] = float(np.std(values, ddof=1))

    sorted_variability = sorted(
        param_variability.items(), key=lambda x: x[1], reverse=True
    )
    most_different = sorted_variability[:10] if len(sorted_variability) > 10 else sorted_variability

    assignments = results.class_assignments
    class_means = {}
    for k_idx in range(results.n_classes):
        mask = np.argmax(assignments, axis=1) == k_idx
        if mask.sum() > 0:
            class_means[k_idx] = assignments[mask].mean(axis=0)

    mahalanobis: Dict[str, float] = {}
    mean_indices = sorted(class_means.keys())
    if len(mean_indices) >= 2:
        all_means = np.array([class_means[mi] for mi in mean_indices])
        pooled_cov = np.cov(all_means.T) if all_means.shape[0] > 1 else np.eye(all_means.shape[1])
        try:
            inv_cov = np.linalg.inv(pooled_cov + 1e-8 * np.eye(pooled_cov.shape[0]))
        except np.linalg.LinAlgError:
            inv_cov = np.eye(pooled_cov.shape[0])

        for i in range(len(mean_indices)):
            for j in range(i + 1, len(mean_indices)):
                ki = mean_indices[i]
                kj = mean_indices[j]
                diff = class_means[ki] - class_means[kj]
                dist = float(np.sqrt(diff @ inv_cov @ diff))
                mahalanobis[f"class_{ki}_vs_class_{kj}"] = dist

    return {
        "parameter_differences": param_diffs,
        "most_different_parameters": dict(most_different),
        "mahalanobis_distances": mahalanobis,
    }


def profile_classes(
    data: pd.DataFrame, class_assignments: np.ndarray
) -> pd.DataFrame:
    if class_assignments.ndim == 2:
        hard_labels = np.argmax(class_assignments, axis=1)
    else:
        hard_labels = class_assignments.astype(int)

    n_classes = int(hard_labels.max()) + 1
    obs_cols = data.select_dtypes(include=[np.number]).columns.tolist()

    rows = []
    for k_idx in range(n_classes):
        mask = hard_labels == k_idx
        class_data = data.loc[mask, obs_cols]
        n = int(mask.sum())
        row: Dict[str, Any] = {"class": k_idx, "n": n}
        for col in obs_cols:
            if n > 0:
                row[f"{col}_mean"] = float(class_data[col].mean())
                row[f"{col}_sd"] = float(class_data[col].std(ddof=1)) if n > 1 else 0.0
            else:
                row[f"{col}_mean"] = np.nan
                row[f"{col}_sd"] = np.nan
        rows.append(row)

    return pd.DataFrame(rows)


def simulate_mixture_data(
    n_obs: int,
    n_vars: int,
    n_classes: int,
    seed: int = 42,
) -> Tuple[pd.DataFrame, np.ndarray]:
    rng = np.random.RandomState(seed)

    proportions = rng.dirichlet(np.ones(n_classes) * 5.0)
    labels = rng.choice(n_classes, size=n_obs, p=proportions)

    means = {}
    covs = {}
    for k_idx in range(n_classes):
        means[k_idx] = rng.randn(n_vars) * 2.0
        A = rng.randn(n_vars, n_vars) * 0.5
        covs[k_idx] = A @ A.T + np.eye(n_vars)

    data_matrix = np.zeros((n_obs, n_vars))
    for k_idx in range(n_classes):
        mask = labels == k_idx
        n_k = int(mask.sum())
        if n_k > 0:
            data_matrix[mask] = rng.multivariate_normal(means[k_idx], covs[k_idx], size=n_k)

    var_names = [f"x{i + 1}" for i in range(n_vars)]
    df = pd.DataFrame(data_matrix, columns=var_names)

    return df, labels
