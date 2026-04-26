#!/usr/bin/env python3
"""
SEM Model Templates for advanced analysis types.
Each template provides a semopy model syntax generator.
"""

from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass

import pandas as pd
import numpy as np

try:
    from semopy.efa import explore_cfa_model, find_latents
    _HAS_EFA = True
except ImportError:
    _HAS_EFA = False


def _normalize_items(items) -> List[str]:
    """Accept either a plain list or {'items': [...]} dict; return list."""
    if isinstance(items, list):
        return items
    if isinstance(items, dict) and 'items' in items:
        return items['items']
    return list(items)


@dataclass
class ModelTemplate:
    """Represents a reusable SEM model template."""
    name: str
    description: str
    required_vars: List[str]
    optional_vars: List[str] = None

    def generate(self, user_vars: Dict[str, List[str]]) -> str:
        raise NotImplementedError


class CFATemplate(ModelTemplate):
    """Confirmatory Factor Analysis (Measurement model only)"""
    def __init__(self):
        super().__init__(
            name="CFA",
            description="Confirmatory Factor Analysis (Measurement model)",
            required_vars=['latent', 'observed']
        )

    def generate(self, user_vars: Dict) -> str:
        lines = ["# CFA Model"]
        for lv, items in user_vars['latent'].items():
            items = _normalize_items(items)
            items_str = " + ".join(items)
            lines.append(f"{lv} =~ {items_str}")
        return "\n".join(lines)


class GrowthModelTemplate(ModelTemplate):
    """Latent Growth Curve Model (single-phase)"""
    def __init__(self):
        super().__init__(
            name="Latent Growth",
            description="Latent Growth Curve Model (Linear)",
            required_vars=['time_points', 'observed_pattern']
        )

    def generate(self, user_vars: Dict) -> str:
        lines = ["# Latent Growth Model"]
        items = user_vars.get('items', [])
        if not items:
            raise ValueError("Growth model requires 'items' list")
        lines.append(f"intercept =~ {' + '.join(items)}")
        loadings = user_vars.get('time_loadings')
        if loadings is None:
            loadings = list(range(len(items)))
        if len(loadings) != len(items):
            raise ValueError(f"time_loadings length ({len(loadings)}) must match items count ({len(items)})")
        slope_parts = [f"{load}*{item}" for load, item in zip(loadings, items)]
        lines.append(f"slope =~ {' + '.join(slope_parts)}")
        lines.append("intercept ~~ slope")
        return "\n".join(lines)


class MediationTemplate(ModelTemplate):
    """Simple mediation model (X -> M -> Y)"""
    def __init__(self):
        super().__init__(
            name="Mediation",
            description="Simple Mediation Model (X -> M -> Y)",
            required_vars=['cause', 'mediator', 'outcome']
        )

    def generate(self, user_vars: Dict) -> str:
        cause = user_vars['cause'][0] if isinstance(user_vars['cause'], list) else user_vars['cause']
        mediator = user_vars['mediator'][0] if isinstance(user_vars['mediator'], list) else user_vars['mediator']
        outcome = user_vars['outcome'][0] if isinstance(user_vars['outcome'], list) else user_vars['outcome']

        lines = [
            "# Mediation Model",
            "# Direct effect",
            f"{outcome} ~ {cause}",
            "# Indirect effect via mediator",
            f"{mediator} ~ {cause}",
            f"{outcome} ~ {mediator}"
        ]
        return "\n".join(lines)


class MultigroupTemplate(ModelTemplate):
    """Multi-group analysis (measurement invariance testing)"""
    def __init__(self):
        super().__init__(
            name="Multi-group",
            description="Multi-group Analysis (Measurement Invariance)",
            required_vars=['groups', 'latent', 'observed'],
            optional_vars=['invariance', 'paths']
        )

    def generate(self, user_vars: Dict) -> str:
        invariance = user_vars.get('invariance', 'configural')
        latent = user_vars.get('latent', {})
        lines = [f"# Multi-group SEM ({invariance} invariance)"]

        if invariance == 'configural':
            for lv, items in latent.items():
                items = _normalize_items(items)
                lines.append(f"{lv} =~ {' + '.join(items)}")
        elif invariance in ('metric', 'scalar'):
            for lv, items in latent.items():
                items = _normalize_items(items)
                parts = [f"1*{items[0]}"]
                for item in items[1:]:
                    parts.append(f"lam__{item}*{item}")
                lines.append(f"{lv} =~ {' + '.join(parts)}")
            if invariance == 'scalar':
                seen = set()
                for items in latent.values():
                    items = _normalize_items(items)
                    for item in items:
                        if item not in seen:
                            lines.append(f"{item} ~ int__{item}*1")
                            seen.add(item)

        paths = user_vars.get('paths', [])
        if paths:
            lines.append("")
            lines.append("# Structural paths:")
            for src, dst in paths:
                lines.append(f"{dst} ~ {src}")

        return "\n".join(lines)


class EFATemplate(ModelTemplate):
    """Exploratory Factor Analysis leading to CFA syntax."""
    def __init__(self):
        super().__init__(
            name="EFA",
            description="Exploratory Factor Analysis (auto-suggest factor structure)",
            required_vars=['variables'],
            optional_vars=['n_factors', 'data']
        )

    def generate(self, user_vars: Dict) -> str:
        data = user_vars.get('data')
        variables = user_vars.get('variables', [])
        if data is None:
            raise ValueError("EFA requires 'data' (DataFrame) in user_vars")
        if not variables:
            variables = list(data.columns)
        subset = data[variables].dropna()
        if not _HAS_EFA:
            return self._fallback_efa_syntax(subset, variables, user_vars.get('n_factors'))
        try:
            n_factors = user_vars.get('n_factors')
            min_loadings = 2
            result = explore_cfa_model(subset, min_loadings=min_loadings)
            if isinstance(result, str) and result.strip():
                return "# EFA-derived CFA Model\n" + result.strip()
        except Exception:
            pass
        return self._fallback_efa_syntax(subset, variables, user_vars.get('n_factors'))

    def suggest_factors(self, data: pd.DataFrame, variables: List[str]) -> Dict[str, List[str]]:
        data_sub = data[variables].dropna()
        if _HAS_EFA:
            try:
                latents = find_latents(data_sub)
                if isinstance(latents, dict):
                    return latents
            except Exception:
                pass
        corr = data_sub.corr()
        n_vars = len(variables)
        eigenvalues = np.linalg.eigvalsh(corr.values)[::-1]
        n_factors = max(1, int(np.sum(eigenvalues > 1)))
        loadings = self._simple_factor_loadings(corr.values, n_factors)
        factor_map = {}
        for f_idx in range(n_factors):
            col_loadings = loadings[:, f_idx]
            items = [variables[v_idx] for v_idx in range(n_vars) if abs(col_loadings[v_idx]) > 0.3]
            if items:
                factor_map[f"F{f_idx + 1}"] = items
        return factor_map

    def _fallback_efa_syntax(self, data: pd.DataFrame, variables: List[str],
                             n_factors: Optional[int] = None) -> str:
        factor_map = self.suggest_factors(data, variables)
        if not factor_map:
            raise ValueError("EFA could not identify a factor structure from the data")
        lines = ["# EFA-derived CFA Model"]
        for factor, items in factor_map.items():
            lines.append(f"{factor} =~ {' + '.join(items)}")
        return "\n".join(lines)

    @staticmethod
    def _simple_factor_loadings(corr_matrix: np.ndarray, n_factors: int) -> np.ndarray:
        eigenvalues, eigenvectors = np.linalg.eigh(corr_matrix)
        idx = np.argsort(eigenvalues)[::-1]
        eigenvectors = eigenvectors[:, idx]
        loadings = eigenvectors[:, :n_factors] * np.sqrt(np.maximum(eigenvalues[idx[:n_factors]], 0))
        return loadings


class SecondOrderCFATemplate(ModelTemplate):
    """Second-order (hierarchical) CFA model."""
    def __init__(self):
        super().__init__(
            name="Second-Order CFA",
            description="Second-Order CFA (Hierarchical Factor Model)",
            required_vars=['latent', 'second_order'],
            optional_vars=[]
        )

    def generate(self, user_vars: Dict) -> str:
        latent = user_vars.get('latent', {})
        second_order = user_vars.get('second_order', {})
        lines = ["# Second-Order CFA Model"]
        for lv, items in latent.items():
            items = _normalize_items(items)
            lines.append(f"{lv} =~ {' + '.join(items)}")
        lines.append("")
        lines.append("# Second-order factors")
        for higher, first_order in second_order.items():
            if isinstance(first_order, str):
                first_order = [first_order]
            parts = " + ".join(first_order)
            lines.append(f"{higher} =~ {parts}")
        return "\n".join(lines)


class CrossLaggedTemplate(ModelTemplate):
    """Cross-lagged panel model for longitudinal data."""
    def __init__(self):
        super().__init__(
            name="Cross-Lagged Panel",
            description="Cross-Lagged Panel Model (Longitudinal)",
            required_vars=['variables', 'time_points'],
            optional_vars=['autoregressive']
        )

    def generate(self, user_vars: Dict) -> str:
        variables = user_vars.get('variables', [])
        time_points = user_vars.get('time_points', [])
        if len(variables) < 1:
            raise ValueError("Cross-lagged model requires at least one variable base name")
        if len(time_points) < 2:
            raise ValueError("Cross-lagged model requires at least two time points")
        lines = ["# Cross-Lagged Panel Model"]
        all_vars = []
        for var in variables:
            for tp in time_points:
                all_vars.append(f"{var}_{tp}")
        lines.append("")
        lines.append("# Autoregressive (stability) paths")
        for var in variables:
            for i in range(len(time_points) - 1):
                tp_curr = time_points[i + 1]
                tp_prev = time_points[i]
                lines.append(f"{var}_{tp_curr} ~ {var}_{tp_prev}")
        lines.append("")
        lines.append("# Cross-lagged paths")
        for i in range(len(time_points) - 1):
            tp_prev = time_points[i]
            tp_curr = time_points[i + 1]
            for src_var in variables:
                for dst_var in variables:
                    if src_var != dst_var:
                        lines.append(f"{dst_var}_{tp_curr} ~ {src_var}_{tp_prev}")
        lines.append("")
        lines.append("# Residual covariances at each time point")
        for i, tp in enumerate(time_points):
            tp_vars = [f"{v}_{tp}" for v in variables]
            for vi in range(len(tp_vars)):
                for vj in range(vi + 1, len(tp_vars)):
                    lines.append(f"{tp_vars[vi]} ~~ {tp_vars[vj]}")
        return "\n".join(lines)

    def auto_detect_time_vars(self, data: pd.DataFrame, variables: List[str]) -> Tuple[List[str], List[str]]:
        import re
        cols = list(data.columns)
        detected_vars = []
        time_points = set()
        for col in cols:
            for var in variables:
                if col.startswith(var):
                    suffix = col[len(var):].lstrip('_')
                    if suffix:
                        detected_vars.append(var)
                        time_points.add(suffix)
        detected_vars = list(dict.fromkeys(detected_vars))
        time_points = sorted(time_points, key=lambda x: (int(m.group(1)) if (m := re.search(r'(\d+)', x)) else 0))
        return detected_vars, time_points


class MultipleMediationTemplate(ModelTemplate):
    """Multiple parallel mediation model (X -> M1,M2,... -> Y)."""
    def __init__(self):
        super().__init__(
            name="Multiple Mediation",
            description="Multiple Parallel Mediation Model (X -> M1,M2,... -> Y)",
            required_vars=['cause', 'mediators', 'outcome'],
            optional_vars=[]
        )

    def generate(self, user_vars: Dict) -> str:
        cause = user_vars['cause'][0] if isinstance(user_vars['cause'], list) else user_vars['cause']
        mediators = user_vars.get('mediators', [])
        if isinstance(mediators, str):
            mediators = [mediators]
        outcome = user_vars['outcome'][0] if isinstance(user_vars['outcome'], list) else user_vars['outcome']
        if not mediators:
            raise ValueError("Multiple mediation requires at least one mediator in 'mediators' list")
        lines = ["# Multiple Mediation Model"]
        lines.append("")
        lines.append("# Direct effect")
        lines.append(f"{outcome} ~ direct*{cause}")
        for med in mediators:
            lines.append(f"{med} ~ a_{med}*{cause}")
        lines.append("")
        lines.append("# Mediator to outcome paths")
        for med in mediators:
            lines.append(f"{outcome} ~ b_{med}*{med}")
        lines.append("")
        lines.append("# Indirect effect definitions")
        for med in mediators:
            lines.append(f"# Indirect via {med}: a_{med} * b_{med}")
        return "\n".join(lines)


class PathAnalysisTemplate(ModelTemplate):
    """Observed-variable path analysis (no latent variables)."""
    def __init__(self):
        super().__init__(
            name="Path Analysis",
            description="Path Analysis (Observed Variables Only)",
            required_vars=['predictors', 'outcome'],
            optional_vars=['mediators']
        )

    def generate(self, user_vars: Dict) -> str:
        predictors = user_vars.get('predictors', [])
        outcome = user_vars['outcome'][0] if isinstance(user_vars['outcome'], list) else user_vars['outcome']
        mediators = user_vars.get('mediators', [])
        if isinstance(mediators, str):
            mediators = [mediators]
        if not predictors:
            raise ValueError("Path analysis requires at least one predictor")
        lines = ["# Path Analysis Model"]
        if mediators:
            lines.append("")
            lines.append("# Predictor to mediator paths")
            for med in mediators:
                pred_parts = " + ".join(predictors)
                lines.append(f"{med} ~ {pred_parts}")
            lines.append("")
            lines.append("# Mediator and predictor to outcome paths")
            outcome_preds = " + ".join(predictors + mediators)
            lines.append(f"{outcome} ~ {outcome_preds}")
        else:
            lines.append("")
            pred_parts = " + ".join(predictors)
            lines.append(f"{outcome} ~ {pred_parts}")
        return "\n".join(lines)


class RICLPMTemplate(ModelTemplate):
    """Random Intercept Cross-Lagged Panel Model (Hamaker et al., 2015)."""
    def __init__(self):
        super().__init__(
            name="RI-CLPM",
            description="Random Intercept Cross-Lagged Panel Model",
            required_vars=['variables', 'time_points'],
            optional_vars=['autoregressive']
        )

    def generate(self, user_vars: Dict) -> str:
        variables = user_vars.get('variables', [])
        time_points = user_vars.get('time_points', [])
        if len(variables) < 1:
            raise ValueError("RI-CLPM requires at least one variable base name")
        if len(time_points) < 2:
            raise ValueError("RI-CLPM requires at least two time points")
        lines = ["# Random Intercept Cross-Lagged Panel Model"]
        lines.append("")
        lines.append("# Random intercepts (between-person stable component)")
        for var in variables:
            ri_items = " + ".join(f"1*{var}_{tp}" for tp in time_points)
            lines.append(f"RI_{var} =~ {ri_items}")
        lines.append("")
        lines.append("# Within-person components")
        for var in variables:
            for tp in time_points:
                lines.append(f"w{var}_{tp} =~ 1*{var}_{tp}")
        lines.append("")
        lines.append("# Autoregressive (within-person stability)")
        for var in variables:
            for i in range(len(time_points) - 1):
                tp_prev = time_points[i]
                tp_curr = time_points[i + 1]
                lines.append(f"w{var}_{tp_curr} ~ w{var}_{tp_prev}")
        lines.append("")
        lines.append("# Cross-lagged (within-person cross-effects)")
        for i in range(len(time_points) - 1):
            tp_prev = time_points[i]
            tp_curr = time_points[i + 1]
            for src_var in variables:
                for dst_var in variables:
                    if src_var != dst_var:
                        lines.append(f"w{dst_var}_{tp_curr} ~ w{src_var}_{tp_prev}")
        lines.append("")
        lines.append("# Within-person residual covariances at each time")
        for tp in time_points:
            tp_vars = [f"w{v}_{tp}" for v in variables]
            for vi in range(len(tp_vars)):
                for vj in range(vi + 1, len(tp_vars)):
                    lines.append(f"{tp_vars[vi]} ~~ {tp_vars[vj]}")
        lines.append("")
        lines.append("# Random intercept covariance")
        ri_vars = [f"RI_{v}" for v in variables]
        for vi in range(len(ri_vars)):
            for vj in range(vi + 1, len(ri_vars)):
                lines.append(f"{ri_vars[vi]} ~~ {ri_vars[vj]}")
        return "\n".join(lines)

    def auto_detect_time_vars(self, data: pd.DataFrame, variables: List[str]) -> Tuple[List[str], List[str]]:
        import re
        cols = list(data.columns)
        detected_vars = []
        time_points = set()
        for col in cols:
            for var in variables:
                if col.startswith(var):
                    suffix = col[len(var):].lstrip('_')
                    if suffix:
                        detected_vars.append(var)
                        time_points.add(suffix)
        detected_vars = list(dict.fromkeys(detected_vars))
        time_points = sorted(time_points, key=lambda x: (int(m.group(1)) if (m := re.search(r'(\d+)', x)) else 0))
        return detected_vars, time_points


class RILTATemplate(ModelTemplate):
    """Random Intercept Latent Transition Analysis (continuous approximation)."""
    def __init__(self):
        super().__init__(
            name="RI-LTA",
            description="Random Intercept Latent Transition Analysis",
            required_vars=['variables', 'time_points', 'n_classes'],
            optional_vars=['covariates']
        )

    def generate(self, user_vars: Dict) -> str:
        variables = user_vars.get('variables', [])
        time_points = user_vars.get('time_points', [])
        n_classes = user_vars.get('n_classes', 2)
        if isinstance(n_classes, list):
            n_classes = n_classes[0]
        n_classes = int(n_classes)
        covariates = user_vars.get('covariates', [])
        if len(variables) < 1:
            raise ValueError("RI-LTA requires at least one variable base name")
        if len(time_points) < 2:
            raise ValueError("RI-LTA requires at least two time points")
        lines = ["# Random Intercept Latent Transition Analysis"]
        lines.append("# NOTE: This is a continuous approximation of LTA.")
        lines.append("# semopy does not natively support latent categorical variables.")
        lines.append("# Latent factors represent continuous class tendency scores.")
        lines.append("")
        lines.append("# Random intercepts (between-person stable component)")
        for var in variables:
            ri_items = " + ".join(f"1*{var}_{tp}" for tp in time_points)
            lines.append(f"RI_{var} =~ {ri_items}")
        lines.append("")
        lines.append("# Latent class tendency factors at each time point")
        for var in variables:
            for tp in time_points:
                latent_parts = []
                for c in range(1, n_classes + 1):
                    latent_parts.append(f"lambda_{var}_{tp}_c{c}*{var}_{tp}_c{c}")
                lines.append(f"eta_{var}_{tp} =~ {' + '.join(latent_parts)}")
        lines.append("")
        lines.append("# Autoregressive (stability of class tendencies)")
        for var in variables:
            for i in range(len(time_points) - 1):
                tp_prev = time_points[i]
                tp_curr = time_points[i + 1]
                lines.append(f"eta_{var}_{tp_curr} ~ beta_{var}_{tp_prev}*eta_{var}_{tp_prev}")
        lines.append("")
        lines.append("# Cross-lagged (transition effects across variables)")
        for i in range(len(time_points) - 1):
            tp_prev = time_points[i]
            tp_curr = time_points[i + 1]
            for src_var in variables:
                for dst_var in variables:
                    if src_var != dst_var:
                        lines.append(f"eta_{dst_var}_{tp_curr} ~ gamma_{src_var}_{dst_var}_{tp_prev}*eta_{src_var}_{tp_prev}")
        lines.append("")
        lines.append("# Within-time covariances among latent tendencies")
        for tp in time_points:
            eta_vars = [f"eta_{v}_{tp}" for v in variables]
            for vi in range(len(eta_vars)):
                for vj in range(vi + 1, len(eta_vars)):
                    lines.append(f"{eta_vars[vi]} ~~ {eta_vars[vj]}")
        lines.append("")
        lines.append("# Random intercept covariances")
        ri_vars = [f"RI_{v}" for v in variables]
        for vi in range(len(ri_vars)):
            for vj in range(vi + 1, len(ri_vars)):
                lines.append(f"{ri_vars[vi]} ~~ {ri_vars[vj]}")
        if covariates:
            lines.append("")
            lines.append("# Covariate effects on latent tendencies")
            for cov in covariates:
                for var in variables:
                    for tp in time_points:
                        lines.append(f"eta_{var}_{tp} ~ {cov}")
        return "\n".join(lines)


class ESEMTemplate(ModelTemplate):
    """Exploratory SEM: EFA with oblique rotation then CFA with cross-loadings."""
    def __init__(self):
        super().__init__(
            name="ESEM",
            description="Exploratory Structural Equation Modeling (EFA\u2192CFA with cross-loadings)",
            required_vars=['variables'],
            optional_vars=['n_factors', 'rotation', 'data', 'target_loadings']
        )

    def generate(self, user_vars: Dict) -> str:
        data = user_vars.get('data')
        variables = list(user_vars.get('variables', []))
        target_loadings = user_vars.get('target_loadings')
        if data is not None:
            return self._generate_from_data(data, variables, user_vars)
        if target_loadings is not None:
            return self._generate_from_target(target_loadings)
        raise ValueError("ESEM requires either 'data' (DataFrame) or 'target_loadings' dict in user_vars")

    def _generate_from_data(self, data: pd.DataFrame, variables: List[str], user_vars: Dict) -> str:
        if not variables:
            variables = list(data.columns)
        n_factors = user_vars.get('n_factors', 3)
        rotation = user_vars.get('rotation', 'oblimin')
        loadings_df = self.get_loading_matrix(data, variables, n_factors, rotation)
        factor_cols = [c for c in loadings_df.columns if c.startswith('F') and c != 'communality']
        primary_factor = {}
        for var in variables:
            best_col = None
            best_abs = 0.0
            for col in factor_cols:
                val = abs(loadings_df.loc[var, col])
                if val > best_abs:
                    best_abs = val
                    best_col = col
            primary_factor[var] = best_col
        factor_items = {col: [] for col in factor_cols}
        for var in variables:
            pf = primary_factor[var]
            factor_items[pf].append((var, loadings_df.loc[var, pf], True))
        for var in variables:
            pf = primary_factor[var]
            for col in factor_cols:
                if col == pf:
                    continue
                val = loadings_df.loc[var, col]
                if abs(val) > 0.2:
                    factor_items[col].append((var, val, False))
        lines = ["# ESEM Model (EFA-derived CFA with cross-loadings)"]
        lines.append(f"# Rotation: {rotation}, Factors: {len(factor_cols)}")
        for col in factor_cols:
            items = factor_items[col]
            if not items:
                continue
            parts = []
            for var, loading, is_primary in items:
                if is_primary:
                    parts.append(var)
                else:
                    parts.append(f"cl__{var}")
            lines.append(f"{col} =~ {' + '.join(parts)}")
        lines.append("")
        lines.append("# Factor covariances (oblique rotation)")
        for i in range(len(factor_cols)):
            for j in range(i + 1, len(factor_cols)):
                lines.append(f"{factor_cols[i]} ~~ {factor_cols[j]}")
        return "\n".join(lines)

    def _generate_from_target(self, target_loadings: Dict[str, Dict[str, float]]) -> str:
        lines = ["# ESEM Model (target rotation specification)"]
        for factor, item_dict in target_loadings.items():
            parts = []
            for item, loading in item_dict.items():
                if loading != 0:
                    if abs(loading - 1.0) < 1e-9:
                        parts.append(item)
                    else:
                        parts.append(f"{loading:.4f}*{item}")
            if parts:
                lines.append(f"{factor} =~ {' + '.join(parts)}")
        factor_names = list(target_loadings.keys())
        if len(factor_names) > 1:
            lines.append("")
            lines.append("# Factor covariances")
            for i in range(len(factor_names)):
                for j in range(i + 1, len(factor_names)):
                    lines.append(f"{factor_names[i]} ~~ {factor_names[j]}")
        return "\n".join(lines)

    def suggest_n_factors(self, data: pd.DataFrame, variables: List[str], method: str = 'parallel') -> Dict[str, Any]:
        data_sub = data[variables].dropna()
        n_vars = len(variables)
        try:
            from factor_analyzer import FactorAnalyzer
            if method == 'parallel':
                try:
                    from factor_analyzer import calculate_bartlett_sphericity, calculate_kmo
                    fa_test = FactorAnalyzer(n_factors=n_vars, rotation=None, method='ml')
                    fa_test.fit(data_sub)
                    ev = fa_test.get_eigenvalues()[0]
                except Exception:
                    ev = self._eigenvalues_from_corr(data_sub)
            else:
                ev = self._eigenvalues_from_corr(data_sub)
            n_kaiser = max(1, int(np.sum(ev > 1)))
            fa_parallel = FactorAnalyzer(n_factors=n_vars, rotation=None, method='ml')
            fa_parallel.fit(data_sub)
            variance = fa_parallel.get_factor_variance()
            var_explained = variance[1].tolist() if len(variance) > 1 else []
            return {
                'n_factors_kaiser': n_kaiser,
                'suggested_n_factors': n_kaiser,
                'eigenvalues': ev.tolist(),
                'variance_explained': var_explained
            }
        except ImportError:
            ev = self._eigenvalues_from_corr(data_sub)
            n_kaiser = max(1, int(np.sum(ev > 1)))
            return {
                'n_factors_kaiser': n_kaiser,
                'suggested_n_factors': n_kaiser,
                'eigenvalues': ev.tolist(),
                'variance_explained': [],
                'note': 'factor_analyzer not available; using eigenvalue > 1 rule only'
            }

    def get_loading_matrix(self, data: pd.DataFrame, variables: List[str], n_factors: int = 3, rotation: str = 'oblimin') -> pd.DataFrame:
        data_sub = data[variables].dropna()
        try:
            from factor_analyzer import FactorAnalyzer
            fa = FactorAnalyzer(n_factors=n_factors, rotation=rotation, method='ml')
            fa.fit(data_sub)
            loadings = fa.loadings_
            communality = fa.get_communalities()
        except ImportError:
            loadings, communality = self._fallback_loadings(data_sub, n_factors)
        factor_cols = [f"F{i + 1}" for i in range(n_factors)]
        df = pd.DataFrame(loadings, index=variables, columns=factor_cols)
        df['communality'] = communality
        return df

    def _eigenvalues_from_corr(self, data: pd.DataFrame) -> np.ndarray:
        corr = data.corr().values
        return np.linalg.eigvalsh(corr)[::-1]

    def _fallback_loadings(self, data: pd.DataFrame, n_factors: int) -> Tuple[np.ndarray, np.ndarray]:
        corr = data.corr().values
        eigenvalues, eigenvectors = np.linalg.eigh(corr)
        idx = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]
        loadings = eigenvectors[:, :n_factors] * np.sqrt(np.maximum(eigenvalues[:n_factors], 0))
        communality = np.sum(loadings ** 2, axis=1)
        return loadings, communality


class PenalizedSEMTemplate(ModelTemplate):
    """Penalized SEM using LASSO/Ridge regularization."""
    def __init__(self):
        super().__init__(
            name="PSEM",
            description="Penalized Structural Equation Modeling (LASSO/Ridge)",
            required_vars=['latent', 'paths'],
            optional_vars=['penalty', 'lambda_val']
        )

    def generate(self, user_vars: Dict) -> str:
        lines = ["# Penalized SEM"]
        latent = user_vars.get('latent', {})
        for lv, items in latent.items():
            items = _normalize_items(items)
            items_str = " + ".join(items)
            lines.append(f"{lv} =~ {items_str}")
        paths = user_vars.get('paths', [])
        if paths:
            lines.append("")
            lines.append("# Structural paths")
            for src, dst in paths:
                lines.append(f"{dst} ~ {src}")
        return "\n".join(lines)

    def get_penalizable_paths(self, user_vars: Dict) -> List[Tuple[str, str]]:
        return list(user_vars.get('paths', []))


# Registry of available templates
TEMPLATES: Dict[str, ModelTemplate] = {
    'cfa': CFATemplate(),
    'growth': GrowthModelTemplate(),
    'mediation': MediationTemplate(),
    'multigroup': MultigroupTemplate(),
    'efa': EFATemplate(),
    'esem': ESEMTemplate(),
    'secondorder': SecondOrderCFATemplate(),
    'crosslagged': CrossLaggedTemplate(),
    'multiplemediation': MultipleMediationTemplate(),
    'pathanalysis': PathAnalysisTemplate(),
    'riclpm': RICLPMTemplate(),
    'rilta': RILTATemplate(),
    'psem': PenalizedSEMTemplate(),
}


def get_template(model_type: str) -> ModelTemplate:
    """Get template by name (case-insensitive)"""
    key = model_type.lower().replace(' ', '').replace('-', '')
    # Try exact match first
    if key in TEMPLATES:
        return TEMPLATES[key]
    # Try partial
    for k, tmpl in TEMPLATES.items():
        if k in key or key in k:
            return tmpl
    raise ValueError(f"Unknown model type: {model_type}")


def list_templates() -> List[Dict]:
    """Return list of available templates with descriptions"""
    return [
        {"name": t.name, "description": t.description, "required": t.required_vars}
        for t in TEMPLATES.values()
    ]


if __name__ == '__main__':
    print("Available templates:")
    for t in list_templates():
        print(f"- {t['name']}: {t['description']}")
        print(f"  Required: {t['required']}")
