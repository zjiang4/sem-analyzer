#!/usr/bin/env python3
"""
Advanced SEM fitting using semopy templates.
"""

import pandas as pd
import numpy as np
from typing import Dict, Any, List, Tuple, Optional
from dataclasses import dataclass
from .templates import get_template, ModelTemplate
import semopy
import warnings

try:
    from scipy.stats import norm
except ImportError:
    norm = None


@dataclass
class AdvancedFitResult:
    """Result of advanced model fitting"""
    model_type: str
    model_string: str
    fit_stats: Dict[str, float]
    parameters: pd.DataFrame
    estimates: Dict[str, Any]
    bootstrap_ci: Optional[Dict[str, Tuple[float, float]]] = None
    modification_indices: Optional[pd.DataFrame] = None
    invariance: Optional[str] = None


class AdvancedFitter:
    """Handles advanced SEM models via templates."""

    def __init__(self, estimator: str = 'ML'):
        self.estimator = estimator
        self.available_estimators = ['ML', 'GLS', 'WLS', 'DWLS', 'ULS', 'FIML']

    def fit(self, data: pd.DataFrame, model_type: str, user_vars: Dict[str, Any],
            options: Dict[str, Any] = None) -> AdvancedFitResult:
        """
        Fit an advanced model.

        Args:
            data: DataFrame with columns
            model_type: e.g., 'cfa', 'growth', 'mediation', 'multigroup'
            user_vars: variable mapping required by template
            options: additional options like 'bootstrap'=True, 'estimator'='ML',
                     'invariance'='configural'/'metric'/'scalar'

        Returns:
            AdvancedFitResult
        """
        options = options or {}
        estimator = options.get('estimator', self.estimator)
        invariance = options.get('invariance', user_vars.get('invariance', 'configural'))

        group_var = None
        if model_type == 'multigroup':
            group_var = user_vars.pop('group', user_vars.pop('groups', None))
            user_vars['invariance'] = invariance

        template: ModelTemplate = get_template(model_type)
        model_str = template.generate(user_vars)

        if model_type == 'multigroup' and group_var is not None:
            config_user_vars = dict(user_vars)
            config_user_vars['invariance'] = 'configural'
            config_model_str = template.generate(config_user_vars)
            return self._fit_multigroup(
                data, model_str, config_model_str, group_var,
                invariance, estimator, options,
            )

        model = semopy.Model(model_str)
        try:
            model.fit(data)
        except Exception as e:
            raise RuntimeError(f"Model fitting failed: {e}\nModel:\n{model_str}")

        stats = semopy.calc_stats(model)
        fit_stats = self._extract_fit_stats(stats)
        params = self._get_parameters(model)

        result = AdvancedFitResult(
            model_type=model_type,
            model_string=model_str,
            fit_stats=fit_stats,
            parameters=params,
            estimates={'model': model, 'stats': stats},
            invariance=invariance if model_type == 'multigroup' else None,
        )

        if options.get('bootstrap', False):
            n_boot = options.get('n_boot', 500)
            result.bootstrap_ci = self._bootstrap_ci(model, data, n_boot)

        if fit_stats.get('cfi', 1.0) < 0.95 or fit_stats.get('rmsea', 0) > 0.06:
            result.modification_indices = self._compute_modification_indices(model, data)

        return result

    def _extract_fit_stats(self, stats) -> Dict[str, float]:
        """Extract key fit indices from semopy calc_stats output (DataFrame)."""
        if isinstance(stats, pd.DataFrame):
            row = stats.iloc[0] if len(stats) > 0 else {}
            col_map = {
                'chi2': 'chi2', 'df': 'DoF', 'p_value': 'chi2 p-value',
                'cfi': 'CFI', 'tli': 'TLI', 'rmsea': 'RMSEA',
                'srmr': 'SRMR', 'aic': 'AIC', 'bic': 'BIC',
            }
            result = {}
            for key, col in col_map.items():
                try:
                    val = row[col]
                    result[key] = float(val) if isinstance(val, (int, float, np.integer, np.floating)) else float(val)
                except (KeyError, TypeError, ValueError):
                    result[key] = np.nan
            return result
        metrics = ['chi2', 'df', 'p_value', 'cfi', 'tli', 'rmsea', 'srmr', 'aic', 'bic']
        return {k: stats.get(k, np.nan) for k in metrics}

    @staticmethod
    def _safe_float(val, default=0.0):
        if val is None:
            return default
        if isinstance(val, (int, float)):
            return float(val)
        if hasattr(val, 'iloc'):
            return float(val.iloc[0])
        try:
            return float(val)
        except (TypeError, ValueError):
            return default

    def _fit_multigroup(self, data, model_str, config_model_str, group_var,
                        invariance, estimator, options):
        group_data = {name: grp for name, grp in data.groupby(group_var)}
        group_names = list(group_data.keys())

        config_results = {}
        total_chi2 = 0.0
        total_df = 0.0

        for gname, gdf in group_data.items():
            try:
                m = semopy.Model(config_model_str)
                m.fit(gdf)
                stats = semopy.calc_stats(m)
                fs = self._extract_fit_stats(stats)
                config_results[gname] = {
                    'fit_stats': fs,
                    'parameters': self._get_parameters(m),
                }
                total_chi2 += self._safe_float(fs.get('chi2', 0.0))
                total_df += self._safe_float(fs.get('df', 0.0))
            except Exception as e:
                config_results[gname] = {'error': str(e)}

        constrained_result = None
        comparison = None

        if invariance in ('metric', 'scalar'):
            try:
                m = semopy.Model(model_str)
                m.fit(data, groups=group_var)
                stats = semopy.calc_stats(m)
                cfs = self._extract_fit_stats(stats)
                constrained_result = {
                    'fit_stats': cfs,
                    'parameters': self._get_parameters(m),
                }
                c_chi2 = self._safe_float(cfs.get('chi2', 0.0))
                c_df = self._safe_float(cfs.get('df', 0.0))
                comparison = {
                    'configural_chi2': total_chi2,
                    'configural_df': total_df,
                    'constrained_chi2': c_chi2,
                    'constrained_df': c_df,
                    'delta_chi2': c_chi2 - total_chi2,
                    'delta_df': c_df - total_df,
                }
            except Exception as e:
                constrained_result = {'error': str(e)}

        if invariance == 'configural':
            fit_stats = {'chi2': total_chi2, 'df': total_df}
            all_params = []
            for gname, gr in config_results.items():
                if 'parameters' in gr:
                    p = gr['parameters'].copy()
                    if isinstance(p, pd.DataFrame):
                        p['group'] = gname
                    all_params.append(p)
            params = pd.concat(all_params, ignore_index=True) if all_params else pd.DataFrame()
        elif constrained_result and 'fit_stats' in constrained_result:
            fit_stats = constrained_result['fit_stats']
            params = constrained_result.get('parameters', pd.DataFrame())
        else:
            fit_stats = {'chi2': total_chi2, 'df': total_df}
            params = pd.DataFrame()

        return AdvancedFitResult(
            model_type='multigroup',
            model_string=model_str,
            fit_stats=fit_stats,
            parameters=params,
            estimates={
                'configural': config_results,
                'constrained': constrained_result,
                'comparison': comparison,
                'group_names': group_names,
            },
            invariance=invariance,
        )

    def _get_parameters(self, model: semopy.Model) -> pd.DataFrame:
        """Get parameter estimates in a DataFrame."""
        insp = model.inspect()
        if isinstance(insp, pd.DataFrame):
            df = insp.rename(columns={
                'lval': 'lval', 'op': 'op', 'rval': 'rval',
                'Estimate': 'estimate', 'Std. Err': 'se',
                'z-value': 'z', 'p-value': 'p',
            })
            df['path'] = df['lval'].astype(str) + df['op'].astype(str) + df['rval'].astype(str)
            return df
        if isinstance(insp, dict):
            rows = []
            for k, vals in insp.items():
                if isinstance(vals, (list, tuple)) and len(vals) >= 4:
                    rows.append({
                        'path': str(k), 'estimate': vals[0],
                        'se': vals[1], 'z': vals[2], 'p': vals[3],
                    })
            return pd.DataFrame(rows) if rows else pd.DataFrame()
        return pd.DataFrame()

    def _bootstrap_ci(self, model: semopy.Model, data: pd.DataFrame, n_boot: int = 500, seed: int = 42) -> Dict[str, Tuple[float, float]]:
        """Bootstrap confidence intervals using BCa method with percentile fallback."""
        np.random.seed(seed)

        param_names = []
        try:
            inspect_result = model.inspect()
            if isinstance(inspect_result, dict):
                param_names = [str(k) for k in inspect_result.keys()]
            elif hasattr(inspect_result, 'index'):
                param_names = [str(idx) for idx in inspect_result.index]
            else:
                param_names = []
        except Exception:
            param_names = []

        def _extract_vec(m):
            insp = m.inspect()
            if isinstance(insp, pd.DataFrame):
                if 'Estimate' in insp.columns:
                    return insp['Estimate'].values.tolist()
                if 'estimate' in insp.columns:
                    return insp['estimate'].values.tolist()
            if isinstance(insp, dict):
                return [float(v[0]) if isinstance(v, (list, tuple)) else float(v) for v in insp.values()]
            return []

        original_vec = _extract_vec(model)

        model_str_src = getattr(model, 'description', None)
        if not model_str_src:
            warnings.warn("Cannot bootstrap: model definition not available")
            return {}

        n = len(data)
        estimates = []
        for _ in range(n_boot):
            sample = data.sample(n, replace=True, random_state=np.random.randint(0, 100000))
            try:
                m = semopy.Model(model_str_src)
                m.fit(sample)
                vec = _extract_vec(m)
                if len(vec) == len(param_names):
                    estimates.append(vec)
            except Exception:
                continue

        if len(estimates) < n_boot * 0.5:
            warnings.warn(f"Bootstrap only succeeded in {len(estimates)}/{n_boot} resamples")
        if not estimates:
            warnings.warn("Bootstrap failed for all resamples")
            return {}

        estimates = np.array(estimates)

        if len(param_names) != estimates.shape[1]:
            min_len = min(len(param_names), estimates.shape[1])
            param_names = param_names[:min_len]
            estimates = estimates[:, :min_len]
            original_vec = original_vec[:min_len]

        if norm is None:
            ci_lower = np.percentile(estimates, 2.5, axis=0)
            ci_upper = np.percentile(estimates, 97.5, axis=0)
            return {name: (float(lo), float(up))
                    for name, lo, up in zip(param_names, ci_lower, ci_upper)}

        jackknife_estimates = []
        for i in range(n):
            jack_data = data.drop(data.index[i])
            try:
                m = semopy.Model(model_str_src)
                m.fit(jack_data)
                vec = _extract_vec(m)
                if len(vec) == len(param_names):
                    jackknife_estimates.append(vec)
            except Exception:
                continue

        results = {}
        for j, name in enumerate(param_names):
            try:
                boot_vals = estimates[:, j]
                orig_val = original_vec[j]

                prop = np.mean(boot_vals < orig_val)
                prop = np.clip(prop, 0.001, 0.999)
                z0 = norm.ppf(prop)

                if jackknife_estimates:
                    jack_arr = np.array(jackknife_estimates)[:, j]
                    mean_jack = np.mean(jack_arr)
                    diff = mean_jack - jack_arr
                    num = np.sum(diff ** 3)
                    denom = np.sum(diff ** 2)
                    if denom > 0:
                        a = num / (6.0 * denom ** 1.5)
                    else:
                        a = 0.0
                else:
                    a = 0.0

                alpha_lower = norm.cdf(z0 + (z0 - 1.96) / (1 - a * (z0 - 1.96)))
                alpha_upper = norm.cdf(z0 + (z0 + 1.96) / (1 - a * (z0 + 1.96)))

                lower = np.percentile(boot_vals, alpha_lower * 100)
                upper = np.percentile(boot_vals, alpha_upper * 100)

                results[name] = (float(lower), float(upper))
            except Exception:
                boot_vals = estimates[:, j]
                results[name] = (float(np.percentile(boot_vals, 2.5)),
                                 float(np.percentile(boot_vals, 97.5)))

        return results

    def _compute_modification_indices(self, model: semopy.Model, data: pd.DataFrame) -> pd.DataFrame:
        """
        Compute Modification Indices (MI) for possible parameter releases.
        MI = chi2_released - chi2_restricted (roughly).
        This is a simplified version: compare each fixed path by freeing it.
        """
        # semopy doesn't directly provide MI; we estimate by fitting modified models.
        # For performance, only examine parameters that are typically freed:
        # - error covariances (between items of same construct)
        # - cross-loadings
        # - residual correlations
        base_stats = semopy.calc_stats(model)
        base_chi2 = base_stats.get('chi2', 0)

        # Get current fixed parameters (looking at model definition)
        # For now, we'll simulate: return empty with a note
        warnings.warn("Modification indices computation is placeholder; need full model traversal")
        return pd.DataFrame(columns=['path', 'mi', 'delta_chi2', 'p_change'])


def quick_cfa(data: pd.DataFrame, latent_vars: Dict[str, List[str]], estimator: str = 'ML') -> AdvancedFitResult:
    """Convenience function for CFA."""
    fitter = AdvancedFitter(estimator=estimator)
    return fitter.fit(data, 'cfa', {'latent': latent_vars, 'observed': []})


def quick_growth(data: pd.DataFrame, items: List[str], time_loadings: Optional[List[float]] = None) -> AdvancedFitResult:
    """Convenience for latent growth."""
    if time_loadings is None:
        time_loadings = list(range(len(items)))
    fitter = AdvancedFitter()
    user_vars = {
        'items': items,
        'time_loadings': time_loadings
    }
    return fitter.fit(data, 'growth', user_vars)


def quick_mediation(data: pd.DataFrame, x: str, m: str, y: str) -> AdvancedFitResult:
    """Convenience for mediation."""
    fitter = AdvancedFitter()
    user_vars = {'cause': [x], 'mediator': [m], 'outcome': [y]}
    return fitter.fit(data, 'mediation', user_vars)


if __name__ == '__main__':
    # Quick test
    print("Advanced Fitter module loaded.")
