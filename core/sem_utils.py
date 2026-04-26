#!/usr/bin/env python3
"""
SEM utility functions: reliability, model comparison, factor scores,
estimator suggestion, ordinal detection, and power analysis.
"""

import pandas as pd
import numpy as np
from typing import Dict, Any, List, Tuple, Optional

try:
    from scipy.stats import chi2 as chi2_dist
    _HAS_SCIPY = True
except ImportError:
    chi2_dist = None
    _HAS_SCIPY = False

import warnings


def compute_reliability(model, data: pd.DataFrame,
                        latent_dict: Dict[str, List[str]]) -> Dict[str, Any]:
    """
    Compute reliability indices for each latent factor.

    Args:
        model: A fitted semopy Model object.
        data: DataFrame used for fitting.
        latent_dict: Mapping of factor name -> list of indicator names.

    Returns:
        Dict with per-factor Cronbach alpha, CR, AVE, and overall assessment.
    """
    try:
        insp = model.inspect(mode='list')
    except Exception:
        insp = None

    loading_lookup = {}
    error_var_lookup = {}
    if insp is not None:
        for row in insp:
            if not isinstance(row, (list, tuple, dict)):
                continue
            if isinstance(row, dict):
                op = row.get('op', '')
                lval = str(row.get('lval', ''))
                rval = str(row.get('rval', ''))
                est = row.get('Estimate', row.get('estimate', 0))
            else:
                if len(row) < 4:
                    continue
                op = row[1] if len(row) > 1 else ''
                lval = str(row[0])
                rval = str(row[2]) if len(row) > 2 else ''
                est = row[3] if len(row) > 3 else 0
            try:
                est = float(est)
            except (TypeError, ValueError):
                est = 0.0
            if op == '~1':
                continue
            if op == '=~':
                loading_lookup[(lval, rval)] = abs(est)
            elif op == '~~' and lval == rval:
                error_var_lookup[lval] = est

    results = {}
    for factor, items in latent_dict.items():
        items = list(items)
        if not items:
            continue

        sub = data[items].dropna()
        n_items = len(items)
        if len(sub) < n_items + 2:
            results[factor] = {
                'cronbach_alpha': np.nan,
                'composite_reliability': np.nan,
                'average_variance_extracted': np.nan,
                'assessment': 'Insufficient data',
                'n_items': n_items,
            }
            continue

        corr_matrix = sub.corr().values
        variances = sub.var().values

        # Cronbach's alpha
        item_var_sum = np.sum(variances)
        total_var = sub.sum(axis=1).var(ddof=1)
        if total_var > 0 and n_items > 1:
            alpha = (n_items / (n_items - 1)) * (1 - item_var_sum / total_var)
        else:
            alpha = np.nan

        # Composite Reliability and AVE from model loadings
        loadings = []
        error_vars = []
        all_loadings_found = True
        for item in items:
            loading = loading_lookup.get((factor, item))
            if loading is None:
                all_loadings_found = False
                break
            loadings.append(loading)
            ev = error_var_lookup.get(item, 0.0)
            error_vars.append(max(ev, 0.0))

        if all_loadings_found and loadings:
            sum_load = sum(loadings)
            sum_err = sum(error_vars)
            cr = (sum_load ** 2) / ((sum_load ** 2) + sum_err) if ((sum_load ** 2) + sum_err) > 0 else np.nan
            sum_sq_load = sum(l ** 2 for l in loadings)
            ave = sum_sq_load / (sum_sq_load + sum_err) if (sum_sq_load + sum_err) > 0 else np.nan
        else:
            # Fallback: estimate from correlation matrix
            avg_corr = (np.sum(corr_matrix) - n_items) / (n_items * (n_items - 1)) if n_items > 1 else 0
            avg_corr = max(avg_corr, 0.01)
            loadings_est = [np.sqrt(avg_corr)] * n_items
            sum_load = sum(loadings_est)
            error_vars_est = [1.0 - l ** 2 for l in loadings_est]
            sum_err = sum(error_vars_est)
            cr = (sum_load ** 2) / ((sum_load ** 2) + sum_err) if ((sum_load ** 2) + sum_err) > 0 else np.nan
            sum_sq_load = sum(l ** 2 for l in loadings_est)
            ave = sum_sq_load / (sum_sq_load + sum_err) if (sum_sq_load + sum_err) > 0 else np.nan

        if cr is not np.nan and ave is not np.nan:
            if cr > 0.7 and ave > 0.5:
                assessment = "Good"
            elif cr > 0.6:
                assessment = "Acceptable"
            else:
                assessment = "Poor"
        else:
            assessment = "Could not compute"

        results[factor] = {
            'cronbach_alpha': float(alpha) if not np.isnan(alpha) else None,
            'composite_reliability': float(cr) if not np.isnan(cr) else None,
            'average_variance_extracted': float(ave) if not np.isnan(ave) else None,
            'assessment': assessment,
            'n_items': n_items,
        }

    return results


def compare_models(results_list: List) -> Dict[str, Any]:
    """
    Compare multiple fitted models.

    Args:
        results_list: List of AdvancedFitResult objects, each with fit_stats.

    Returns:
        Dict with comparison table, best model by AIC and BIC, and chi2
        difference tests for nested models.
    """
    if not results_list:
        return {'error': 'No models to compare'}

    rows = []
    for i, res in enumerate(results_list):
        fs = res.fit_stats if hasattr(res, 'fit_stats') else res
        if isinstance(fs, dict):
            rows.append({
                'model_index': i + 1,
                'model_type': getattr(res, 'model_type', f'Model {i+1}'),
                'aic': _safe_float(fs.get('aic')),
                'bic': _safe_float(fs.get('bic')),
                'chi2': _safe_float(fs.get('chi2')),
                'df': _safe_float(fs.get('df')),
                'cfi': _safe_float(fs.get('cfi')),
                'rmsea': _safe_float(fs.get('rmsea')),
            })
        else:
            rows.append({
                'model_index': i + 1,
                'model_type': f'Model {i+1}',
                'aic': np.nan, 'bic': np.nan,
                'chi2': np.nan, 'df': np.nan,
                'cfi': np.nan, 'rmsea': np.nan,
            })

    valid_rows = [r for r in rows if not np.isnan(r['aic'])]
    aic_values = [r['aic'] for r in valid_rows] if valid_rows else []
    bic_values = [r['bic'] for r in valid_rows] if valid_rows else []

    min_aic = min(aic_values) if aic_values else np.nan
    min_bic = min(bic_values) if bic_values else np.nan

    for r in valid_rows:
        r['delta_aic'] = r['aic'] - min_aic
        r['delta_bic'] = r['bic'] - min_bic

    best_aic_idx = None
    best_bic_idx = None
    if aic_values:
        best_aic_idx = valid_rows[aic_values.index(min_aic)]['model_index']
    if bic_values:
        best_bic_idx = valid_rows[bic_values.index(min_bic)]['model_index']

    chi2_diff_tests = []
    if _HAS_SCIPY and len(rows) >= 2:
        for i in range(len(rows) - 1):
            r1 = rows[i]
            r2 = rows[i + 1]
            d_chi2 = abs(r2['chi2'] - r1['chi2'])
            d_df = abs(r2['df'] - r1['df'])
            if d_df > 0 and not np.isnan(d_chi2) and d_chi2 >= 0:
                try:
                    p_val = 1.0 - chi2_dist.cdf(d_chi2, d_df)
                    chi2_diff_tests.append({
                        'models': f"Model {r1['model_index']} vs Model {r2['model_index']}",
                        'delta_chi2': d_chi2,
                        'delta_df': d_df,
                        'p_value': p_val,
                        'significant': p_val < 0.05,
                    })
                except Exception:
                    pass

    comparison_table = pd.DataFrame(rows)

    return {
        'comparison_table': comparison_table,
        'best_by_aic': best_aic_idx,
        'best_by_bic': best_bic_idx,
        'chi2_difference_tests': chi2_diff_tests,
    }


def compute_factor_scores(model, data: pd.DataFrame) -> pd.DataFrame:
    """
    Compute factor scores using the fitted model.

    Args:
        model: A fitted semopy Model object.
        data: DataFrame with observed variables.

    Returns:
        DataFrame with factor score columns.
    """
    try:
        scores = model.predict_factors(data)
        if isinstance(scores, pd.DataFrame):
            return scores
        if isinstance(scores, np.ndarray):
            latent_names = []
            try:
                insp = model.inspect()
                if isinstance(insp, pd.DataFrame):
                    latent_names = sorted(insp.loc[insp['op'] == '=~', 'lval'].unique().tolist())
            except Exception:
                pass
            if not latent_names:
                latent_names = [f"F{i+1}" for i in range(scores.shape[1])]
            return pd.DataFrame(scores, columns=latent_names[:scores.shape[1]],
                                index=data.index[:scores.shape[0]])
    except AttributeError:
        pass

    try:
        insp = model.inspect()
        if not isinstance(insp, pd.DataFrame):
            return pd.DataFrame()
        loadings_df = insp[insp['op'] == '=~'].copy()
        if loadings_df.empty:
            return pd.DataFrame()
        factors = loadings_df['lval'].unique()
        loading_matrix = {}
        for _, row in loadings_df.iterrows():
            loading_matrix[(row['lval'], row['rval'])] = float(row['Estimate'])
        factor_scores = {}
        for factor in factors:
            items = loadings_df[loadings_df['lval'] == factor]['rval'].tolist()
            loadings = [loading_matrix.get((factor, item), 0) for item in items]
            if not loadings or sum(abs(l) for l in loadings) == 0:
                continue
            available = [item for item in items if item in data.columns]
            if not available:
                continue
            avail_loadings = [loading_matrix.get((factor, item), 0) for item in available]
            denom = sum(l ** 2 for l in avail_loadings)
            if denom == 0:
                continue
            weights = [l / denom for l in avail_loadings]
            sub = data[available].fillna(data[available].mean())
            factor_scores[factor] = sub.values @ np.array(weights)
        if factor_scores:
            return pd.DataFrame(factor_scores, index=data.index)
    except Exception:
        pass

    return pd.DataFrame()


def suggest_estimator(data: pd.DataFrame) -> Dict[str, str]:
    """
    Recommend an estimation method based on data characteristics.

    Args:
        data: DataFrame to analyze.

    Returns:
        Dict with 'recommended' estimator name and 'reason' string.
    """
    n = len(data)
    numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
    if not numeric_cols:
        return {'recommended': 'ML', 'reason': 'No numeric columns detected; defaulting to ML.'}

    missing_pct = data[numeric_cols].isnull().mean().mean()

    n_ordinal = 0
    for col in numeric_cols:
        n_unique = data[col].dropna().nunique()
        if n_unique < 7:
            n_ordinal += 1

    ordinal_ratio = n_ordinal / len(numeric_cols)

    if missing_pct > 0.05:
        return {
            'recommended': 'FIML',
            'reason': (f"Missing data detected ({missing_pct:.1%} missing). "
                       "Full Information Maximum Likelihood (FIML) is recommended to handle missingness."),
        }

    if ordinal_ratio > 0.5:
        return {
            'recommended': 'DWLS',
            'reason': (f"{n_ordinal}/{len(numeric_cols)} variables have <7 unique values, suggesting ordinal data. "
                       "Diagonally Weighted Least Squares (DWLS) is recommended for ordinal indicators."),
        }

    if n < 100:
        return {
            'recommended': 'ML',
            'reason': (f"Sample size is small (N={n}). Maximum Likelihood (ML) with robust "
                       "standard errors is recommended. Consider bootstrap confidence intervals."),
        }

    return {
        'recommended': 'ML',
        'reason': (f"Continuous data with adequate sample size (N={n}). "
                   "Maximum Likelihood (ML) is the standard choice."),
    }


def detect_ordinal_variables(data: pd.DataFrame, threshold: int = 7) -> List[str]:
    """
    Detect ordinal variables by counting unique values.

    Args:
        data: DataFrame to analyze.
        threshold: Maximum unique values to consider ordinal.

    Returns:
        List of column names with fewer than threshold unique values.
    """
    ordinal = []
    for col in data.columns:
        try:
            if data[col].dropna().nunique() < threshold:
                ordinal.append(col)
        except Exception:
            pass
    return ordinal


def compute_power_analysis(model_str: str, data: pd.DataFrame,
                           n_sim: int = 200, alpha: float = 0.05) -> Dict[str, Any]:
    """
    Monte Carlo power analysis for a given SEM model.

    Args:
        model_str: semopy model syntax string.
        data: Original DataFrame used for fitting.
        n_sim: Number of Monte Carlo simulations.
        alpha: Significance level for chi-square test.

    Returns:
        Dict with power estimate, CI, and simulation details.
    """
    try:
        model = semopy.Model(model_str)
        model.fit(data)
        stats_orig = semopy.calc_stats(model)
    except Exception as e:
        return {'error': f"Could not fit the base model: {e}"}

    n = len(data)
    n_reject = 0
    n_converged = 0
    sim_details = []

    try:
        import semopy.model_generation as mg
        has_mg = True
    except ImportError:
        has_mg = False

    for i in range(n_sim):
        try:
            if has_mg:
                sim_data = mg.generate_data(model, n)
            else:
                params = model.inspect()
                if isinstance(params, pd.DataFrame):
                    obs_vars = params.loc[params['op'] == '~1', 'lval'].tolist()
                    if not obs_vars:
                        obs_vars = list(data.columns)
                else:
                    obs_vars = list(data.columns)
                means = data[obs_vars].mean()
                cov = data[obs_vars].cov()
                sim_data = pd.DataFrame(
                    np.random.multivariate_normal(means.values, cov.values, size=n),
                    columns=obs_vars
                )

            sim_model = semopy.Model(model_str)
            sim_model.fit(sim_data)
            sim_stats = semopy.calc_stats(sim_model)

            if isinstance(sim_stats, pd.DataFrame) and len(sim_stats) > 0:
                p_val = _safe_float(sim_stats.iloc[0].get('chi2 p-value', sim_stats.iloc[0].get('p_value', 1.0)))
            elif isinstance(sim_stats, dict):
                p_val = _safe_float(sim_stats.get('p_value', 1.0))
            else:
                p_val = 1.0

            n_converged += 1
            if p_val < alpha:
                n_reject += 1

        except Exception:
            sim_details.append({'sim': i, 'converged': False})
            continue

    power = n_reject / n_converged if n_converged > 0 else np.nan
    se = np.sqrt(power * (1 - power) / n_converged) if n_converged > 0 and not np.isnan(power) else np.nan
    ci_lower = max(0, power - 1.96 * se) if not np.isnan(se) else np.nan
    ci_upper = min(1, power + 1.96 * se) if not np.isnan(se) else np.nan

    return {
        'power': float(power) if not np.isnan(power) else None,
        'ci_lower': float(ci_lower) if not np.isnan(ci_lower) else None,
        'ci_upper': float(ci_upper) if not np.isnan(ci_upper) else None,
        'n_simulations': n_sim,
        'n_converged': n_converged,
        'n_rejected': n_reject,
        'alpha': alpha,
    }


def parse_sem_syntax(model_str: str) -> Dict[str, List]:
    """Parse semopy syntax into measurement, regression, covariance parts."""
    measurement = []
    regression = []
    covariance = []
    for line in model_str.strip().split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if '=~' in line:
            parts = line.split('=~', 1)
            lv = parts[0].strip()
            rv_items = [x.strip() for x in parts[1].split('+')]
            for item in rv_items:
                item_clean = item.strip()
                if '*' in item_clean:
                    item_clean = item_clean.split('*', 1)[1].strip()
                if item_clean:
                    measurement.append((lv, item_clean))
        elif '~~' in line:
            parts = line.split('~~', 1)
            v1 = parts[0].strip()
            v2 = parts[1].strip()
            covariance.append((v1, v2))
        elif '~' in line and '~1' not in line:
            parts = line.split('~', 1)
            dep = parts[0].strip()
            preds = [x.strip() for x in parts[1].split('+')]
            for pred in preds:
                pred_clean = pred.strip()
                if '*' in pred_clean:
                    pred_clean = pred_clean.split('*', 1)[1].strip()
                if pred_clean:
                    regression.append((pred_clean, dep))
    return {'measurement': measurement, 'regression': regression, 'covariance': covariance}


def fit_penalized_sem(model_str: str, data: pd.DataFrame,
                      penalty: str = 'lasso', lambda_vals: List[float] = None,
                      n_folds: int = 5, penalize_paths: List[Tuple] = None) -> Dict[str, Any]:
    """Two-step penalized SEM: CFA for measurement, penalized regression for structural part."""
    import semopy
    from sklearn.linear_model import LassoCV, RidgeCV
    from sklearn.model_selection import KFold

    parsed = parse_sem_syntax(model_str)

    measurement_groups = {}
    for lv, item in parsed['measurement']:
        if lv not in measurement_groups:
            measurement_groups[lv] = []
        measurement_groups[lv].append(item)

    factor_scores = pd.DataFrame(index=data.index)
    if measurement_groups:
        cfa_lines = []
        for lv, items in measurement_groups.items():
            cfa_lines.append(f"{lv} =~ {' + '.join(items)}")
        cfa_str = "\n".join(cfa_lines)
        try:
            cfa_model = semopy.Model(cfa_str)
            cfa_model.fit(data)
            factor_scores = compute_factor_scores(cfa_model, data)
        except Exception as e:
            return {'error': f"Failed to fit measurement model: {e}"}

    combined = pd.concat([data, factor_scores], axis=1)

    endogenous_preds = {}
    for pred, outcome in parsed['regression']:
        if outcome not in endogenous_preds:
            endogenous_preds[outcome] = []
        endogenous_preds[outcome].append(pred)

    if lambda_vals is None:
        lambda_vals = list(np.logspace(-3, 1, 50))

    if penalize_paths is not None:
        target_paths = set(tuple(p) if not isinstance(p, tuple) else p for p in penalize_paths)
    else:
        target_paths = None

    zeroed_paths = []
    retained_paths = []
    path_coefficients = {}
    best_lambdas = []
    lambda_cv_results = {}

    for outcome, predictors in endogenous_preds.items():
        available_preds = [p for p in predictors if p in combined.columns]
        if not available_preds:
            continue

        y = combined[outcome].values
        X = combined[available_preds].values

        mask = ~(np.isnan(y) | np.any(np.isnan(X), axis=1))
        y_clean = y[mask]
        X_clean = X[mask]

        if len(y_clean) < n_folds + 1:
            for pred in available_preds:
                path_coefficients[(pred, outcome)] = None
            continue

        n_splits = min(n_folds, max(2, len(y_clean) - 1))

        if penalty.lower() == 'lasso':
            kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
            reg = LassoCV(alphas=lambda_vals, cv=kf, random_state=42, max_iter=10000)
            reg.fit(X_clean, y_clean)
            coefs = dict(zip(available_preds, reg.coef_))
            best_lambdas.append(float(reg.alpha_))
            if hasattr(reg, 'mse_path_') and hasattr(reg, 'alphas_'):
                for i, alpha in enumerate(reg.alphas_):
                    lambda_cv_results[float(alpha)] = {'mean_mse': float(np.mean(reg.mse_path_[:, i]))}
        else:
            reg = RidgeCV(alphas=lambda_vals, cv=n_splits)
            reg.fit(X_clean, y_clean)
            coefs = dict(zip(available_preds, reg.coef_))
            best_lambdas.append(float(reg.alpha_))

        for pred, coef in coefs.items():
            path_key = (pred, outcome)
            path_coefficients[path_key] = float(coef)
            is_penalizable = (target_paths is None) or (path_key in target_paths)
            if is_penalizable and abs(coef) < 1e-10:
                zeroed_paths.append(path_key)
            else:
                retained_paths.append(path_key)

    best_lambda = float(np.mean(best_lambdas)) if best_lambdas else None

    retained_lines = []
    for lv, items in measurement_groups.items():
        retained_lines.append(f"{lv} =~ {' + '.join(items)}")
    for pred, outcome in retained_paths:
        retained_lines.append(f"{outcome} ~ {pred}")
    for v1, v2 in parsed['covariance']:
        retained_lines.append(f"{v1} ~~ {v2}")
    reduced_str = "\n".join(retained_lines)

    fit_stats = {}
    try:
        final_model = semopy.Model(reduced_str)
        final_model.fit(data)
        final_stats = semopy.calc_stats(final_model)
        if isinstance(final_stats, pd.DataFrame) and len(final_stats) > 0:
            fit_stats = {col: _safe_float(final_stats.iloc[0][col]) for col in final_stats.columns}
    except Exception:
        pass

    return {
        'best_lambda': best_lambda,
        'lambda_path': lambda_cv_results,
        'final_model': {
            'syntax': reduced_str,
            'coefficients': {f"{k[0]}->{k[1]}": v for k, v in path_coefficients.items()},
        },
        'zeroed_paths': zeroed_paths,
        'retained_paths': retained_paths,
        'fit_stats': fit_stats,
    }


def _build_constrained_syntax(model_syntax, latent_dict, level):
    lines = model_syntax.strip().split('\n')
    new_lines = []
    for line in lines:
        stripped = line.strip()
        if '=~' not in stripped:
            new_lines.append(stripped)
            continue
        parts = stripped.split('=~', 1)
        lhs = parts[0].strip()
        rhs = parts[1].strip()
        items = latent_dict.get(lhs, [])
        if not items or level == 'configural':
            new_lines.append(stripped)
            continue
        indicators = [x.strip() for x in rhs.split('+')]
        if len(indicators) <= 1:
            new_lines.append(stripped)
            continue
        new_indicators = [indicators[0]]
        for ind in indicators[1:]:
            new_indicators.append(f'lam__{ind}*{ind}')
        new_lines.append(f'{lhs} =~ {" + ".join(new_indicators)}')
    if level == 'scalar':
        for factor, items in latent_dict.items():
            for item in items[1:]:
                new_lines.append(f'{item} ~ int__{item}*1')
    return '\n'.join(new_lines)


def stepwise_invariance_test(data, model_syntax, group_var, latent_dict, levels=None):
    """
    Stepwise measurement invariance testing across groups.

    Tests configural, metric, and scalar invariance with Chen (2007) criteria
    (Delta-CFI <= -0.010 AND Delta-RMSEA >= 0.015).

    Args:
        data: DataFrame with observed variables and grouping column.
        model_syntax: semopy model syntax string (configural model).
        group_var: Column name for the grouping variable.
        latent_dict: Mapping of factor names to indicator lists.
        levels: Invariance levels to test. Default ['configural', 'metric', 'scalar'].

    Returns:
        Dict with levels_tested, results per level, comparisons,
        invariance_achieved, and recommendation.
    """
    import semopy

    if levels is None:
        levels = ['configural', 'metric', 'scalar']

    groups = data[group_var].dropna().unique().tolist()
    if len(groups) < 2:
        return {
            'levels_tested': [],
            'results': {},
            'comparisons': [],
            'invariance_achieved': 'none',
            'recommendation': 'At least two groups are required for invariance testing.',
        }

    group_data = {}
    for g in groups:
        gdata = data[data[group_var] == g].copy()
        group_data[g] = gdata

    level_results = {}

    if 'configural' in levels:
        total_chi2 = 0.0
        total_df = 0.0
        total_aic = 0.0
        total_bic = 0.0
        cfi_vals = []
        rmsea_vals = []
        all_converged = True

        for g, gdata in group_data.items():
            try:
                m = semopy.Model(model_syntax)
                m.fit(gdata)
                st = semopy.calc_stats(m)
                s = st.iloc[0] if isinstance(st, pd.DataFrame) else st
                raw_chi2 = _safe_float(s.get('chi2', s.get('Chi2', np.nan)))
                raw_df = _safe_float(s.get('DoF', s.get('df', np.nan)))
                raw_aic = _safe_float(s.get('AIC', s.get('aic', np.nan)))
                raw_bic = _safe_float(s.get('BIC', s.get('bic', np.nan)))
                raw_cfi = _safe_float(s.get('CFI', s.get('cfi', np.nan)))
                raw_rmsea = _safe_float(s.get('RMSEA', s.get('rmsea', np.nan)))
                total_chi2 += raw_chi2 if not np.isnan(raw_chi2) else 0.0
                total_df += raw_df if not np.isnan(raw_df) else 0.0
                total_aic += raw_aic if not np.isnan(raw_aic) else 0.0
                total_bic += raw_bic if not np.isnan(raw_bic) else 0.0
                if not np.isnan(raw_cfi):
                    cfi_vals.append(raw_cfi)
                if not np.isnan(raw_rmsea):
                    rmsea_vals.append(raw_rmsea)
            except Exception:
                all_converged = False

        level_results['configural'] = {
            'chi2': _safe_float(total_chi2),
            'df': _safe_float(total_df),
            'cfi': _safe_float(np.mean(cfi_vals) if cfi_vals else np.nan),
            'rmsea': _safe_float(np.mean(rmsea_vals) if rmsea_vals else np.nan),
            'aic': _safe_float(total_aic),
            'bic': _safe_float(total_bic),
            'converged': all_converged,
        }

    for lvl in ['metric', 'scalar']:
        if lvl not in levels:
            continue
        constrained_syntax = _build_constrained_syntax(model_syntax, latent_dict, lvl)
        try:
            m = semopy.Model(constrained_syntax)
            m.fit(data)
            st = semopy.calc_stats(m)
            s = st.iloc[0] if isinstance(st, pd.DataFrame) else st
            level_results[lvl] = {
                'chi2': _safe_float(s.get('chi2', s.get('Chi2', np.nan))),
                'df': _safe_float(s.get('DoF', s.get('df', np.nan))),
                'cfi': _safe_float(s.get('CFI', s.get('cfi', np.nan))),
                'rmsea': _safe_float(s.get('RMSEA', s.get('rmsea', np.nan))),
                'aic': _safe_float(s.get('AIC', s.get('aic', np.nan))),
                'bic': _safe_float(s.get('BIC', s.get('bic', np.nan))),
                'converged': True,
            }
        except Exception:
            level_results[lvl] = {
                'chi2': np.nan, 'df': np.nan, 'cfi': np.nan,
                'rmsea': np.nan, 'aic': np.nan, 'bic': np.nan,
                'converged': False,
            }

    comparisons = []
    level_order = [l for l in ['configural', 'metric', 'scalar'] if l in levels]

    for i in range(len(level_order) - 1):
        r1 = level_results.get(level_order[i], {})
        r2 = level_results.get(level_order[i + 1], {})

        if not r1.get('converged') or not r2.get('converged'):
            comparisons.append({
                'comparison': f'{level_order[i]} vs {level_order[i + 1]}',
                'delta_chi2': np.nan,
                'delta_df': np.nan,
                'p_value': np.nan,
                'significant': None,
            })
            continue

        d_chi2 = abs(_safe_float(r2.get('chi2', np.nan)) - _safe_float(r1.get('chi2', np.nan)))
        d_df = abs(_safe_float(r2.get('df', np.nan)) - _safe_float(r1.get('df', np.nan)))
        d_cfi = _safe_float(r2.get('cfi', np.nan)) - _safe_float(r1.get('cfi', np.nan))
        d_rmsea = _safe_float(r2.get('rmsea', np.nan)) - _safe_float(r1.get('rmsea', np.nan))

        p_val = np.nan
        if _HAS_SCIPY and d_df > 0 and not np.isnan(d_chi2) and d_chi2 >= 0:
            try:
                p_val = float(1.0 - chi2_dist.cdf(d_chi2, d_df))
            except Exception:
                p_val = np.nan

        chen_met = (d_cfi <= -0.010) and (d_rmsea >= 0.015)

        if not np.isnan(p_val):
            sig = (p_val <= 0.01) and chen_met
        else:
            sig = chen_met

        comparisons.append({
            'comparison': f'{level_order[i]} vs {level_order[i + 1]}',
            'delta_chi2': _safe_float(d_chi2),
            'delta_df': _safe_float(d_df),
            'p_value': _safe_float(p_val),
            'significant': sig,
        })

    invariance_achieved = 'configural' if 'configural' in levels else 'none'
    for comp in comparisons:
        sig = comp.get('significant')
        if sig is None:
            break
        if not sig:
            higher = comp['comparison'].split(' vs ')[1]
            invariance_achieved = higher
        else:
            break

    if invariance_achieved == 'scalar':
        rec = ('Full scalar measurement invariance is supported. '
               'Factor means and variances can be compared across groups.')
    elif invariance_achieved == 'metric':
        rec = ('Metric invariance holds but scalar invariance is not supported. '
               'Factor covariances and variances can be compared, but factor means should not. '
               'Consider partial scalar invariance.')
    elif invariance_achieved == 'configural':
        rec = ('Configural invariance holds but metric invariance is not supported. '
               'The same factor structure applies across groups, but loadings differ. '
               'Consider partial metric invariance or alignment optimization.')
    else:
        rec = ('Measurement invariance could not be established. '
               'Check model specification and group sample sizes.')

    any_failed = any(
        not level_results.get(lvl, {}).get('converged', False)
        for lvl in level_order
    )
    if any_failed:
        rec += ' Note: one or more models failed to converge, which may affect results.'

    return {
        'levels_tested': level_order,
        'results': level_results,
        'comparisons': comparisons,
        'invariance_achieved': invariance_achieved,
        'recommendation': rec,
    }


def alignment_optimization(data, model_syntax, group_var, latent_dict, n_groups=None):
    """
    Simplified alignment optimization for approximate measurement invariance.

    Fits configural model per group and extracts parameter estimates to assess
    the degree of non-invariance across groups (Asparouhov & Muthen, 2014).

    Args:
        data: DataFrame with observed variables and grouping column.
        model_syntax: semopy model syntax string (configural model).
        group_var: Column name for the grouping variable.
        latent_dict: Mapping of factor names to indicator lists.
        n_groups: Optional maximum number of groups to use.

    Returns:
        Dict with group_parameters, factor_comparisons, alignment_quality,
        and recommendation.
    """
    import semopy

    groups = data[group_var].dropna().unique().tolist()
    if n_groups is not None:
        groups = groups[:n_groups]

    if len(groups) < 2:
        return {
            'group_parameters': {},
            'factor_comparisons': {},
            'alignment_quality': np.nan,
            'n_parameters_compared': 0,
            'n_noninvariant': 0,
            'recommendation': ('Alignment optimization requires at least two groups. '
                               'Use configural invariance testing with partial invariance.'),
        }

    group_params = {}
    for g in groups:
        gdata = data[data[group_var] == g].copy()
        try:
            m = semopy.Model(model_syntax)
            m.fit(gdata)
            insp = m.inspect()
            if not isinstance(insp, pd.DataFrame):
                group_params[g] = {'loadings': {}, 'intercepts': {}, 'converged': False}
                continue
            loadings = {}
            intercepts = {}
            for _, row in insp.iterrows():
                if row['op'] == '=~':
                    loadings[(row['lval'], row['rval'])] = _safe_float(row['Estimate'])
                elif row['op'] == '~1':
                    intercepts[row['lval']] = _safe_float(row['Estimate'])
            group_params[g] = {
                'loadings': loadings,
                'intercepts': intercepts,
                'converged': True,
            }
        except Exception:
            group_params[g] = {'loadings': {}, 'intercepts': {}, 'converged': False}

    factor_comparisons = {}
    for factor, items in latent_dict.items():
        group_loadings = {}
        group_intercepts = {}
        for g in groups:
            gp = group_params.get(g, {})
            for item in items:
                ld = gp.get('loadings', {}).get((factor, item), np.nan)
                ic = gp.get('intercepts', {}).get(item, np.nan)
                group_loadings.setdefault(item, {})[g] = ld
                group_intercepts.setdefault(item, {})[g] = ic

        loading_range = {}
        for item, gvals in group_loadings.items():
            vals = [v for v in gvals.values() if not np.isnan(v)]
            if len(vals) >= 2:
                loading_range[item] = {
                    'min': _safe_float(min(vals)),
                    'max': _safe_float(max(vals)),
                    'range': _safe_float(max(vals) - min(vals)),
                }

        intercept_range = {}
        for item, gvals in group_intercepts.items():
            vals = [v for v in gvals.values() if not np.isnan(v)]
            if len(vals) >= 2:
                intercept_range[item] = {
                    'min': _safe_float(min(vals)),
                    'max': _safe_float(max(vals)),
                    'range': _safe_float(max(vals) - min(vals)),
                }

        factor_comparisons[factor] = {
            'loading_range': loading_range,
            'intercept_range': intercept_range,
        }

    n_noninvariant = 0
    n_total = 0
    for factor, comp in factor_comparisons.items():
        for item, rng in comp.get('loading_range', {}).items():
            n_total += 1
            if rng.get('range', 0) > 0.1:
                n_noninvariant += 1
        for item, rng in comp.get('intercept_range', {}).items():
            n_total += 1
            if rng.get('range', 0) > 0.1:
                n_noninvariant += 1

    quality = _safe_float(1.0 - (n_noninvariant / n_total)) if n_total > 0 else np.nan

    rec = ('Alignment optimization is a specialized method for approximate '
           'measurement invariance (Asparouhov & Muthen, 2014). '
           'For full alignment analysis, consider using Mplus or the R package sirt. ')
    if quality is not np.nan and quality > 0.8:
        rec += ('Based on configural model comparisons, parameters appear relatively '
                'similar across groups, suggesting approximate invariance may hold.')
    elif quality is not np.nan and quality > 0.5:
        rec += ('Some parameters show notable group differences. '
                'Partial invariance or alignment is recommended.')
    elif quality is not np.nan:
        rec += ('Substantial group differences exist in measurement parameters. '
                'Configural invariance may be the highest achievable level.')
    else:
        rec += 'Could not assess alignment quality due to insufficient estimates.'

    return {
        'group_parameters': group_params,
        'factor_comparisons': factor_comparisons,
        'alignment_quality': quality,
        'n_parameters_compared': n_total,
        'n_noninvariant': n_noninvariant,
        'recommendation': rec,
    }


def _safe_float(val, default=np.nan):
    if val is None:
        return default
    if isinstance(val, (int, float, np.integer, np.floating)):
        return float(val)
    try:
        return float(val)
    except (TypeError, ValueError):
        return default
