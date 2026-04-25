#!/usr/bin/env python3
"""SEM fitting using semopy."""

import os
import pandas as pd
import numpy as np
from typing import Dict, Any, Optional, Tuple, List
import warnings
import traceback

# Debug mode control via environment variable
DEBUG = os.getenv('SEM_ANALYZER_DEBUG', '').lower() in ('1', 'true', 'yes')

def _debug_write(filename: str, content: str):
    """Write debug information only if DEBUG mode is enabled."""
    if DEBUG:
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception:
            pass  # Fail silently in debug mode

# Will be imported when skill is properly installed with semopy
try:
    from semopy import Model, Optimizer, calc_stats
    SEMOPY_AVAILABLE = True
except ImportError:
    SEMOPY_AVAILABLE = False
    warnings.warn("semopy 未安装，将无法执行拟合。请运行: pip install semopy")


class SemFitter:
    """Fits SEM models using semopy."""

    def __init__(self, estimator: str = "ML", missing_method: str = "fiml"):
        """
        Args:
            estimator: 'ML' (maximum likelihood), 'GLS', 'WLS', 'DWLS', 'ULS'
            missing_method: 'fiml' (full info max likelihood), 'listwise', 'mean'
        """
        self.estimator = estimator
        self.missing_method = missing_method
        self.model: Optional[Any] = None

    def fit(self, df: pd.DataFrame, model_draft: Any) -> Dict[str, Any]:
        """Fit SEM model to data.

        Returns:
            Dictionary with fit results and diagnostics.
        """
        if not SEMOPY_AVAILABLE:
            raise RuntimeError("请先安装 semopy: pip install semopy")

        model_spec = model_draft.to_semopy_model()
        _debug_write('debug_model_spec.txt', model_spec)
        try:
            self.model = Model(model_spec)
            self.model.load_dataset(df)
            self.model.fit()
            return self._extract_results()
        except Exception as e:
            error_text = f"Exception: {e}\n" + traceback.format_exc()
            _debug_write('fit_exception.txt', error_text)
            raise RuntimeError(f"模型拟合失败: {str(e)}")

    def _extract_results(self) -> Dict[str, Any]:
        """Extract and organize results from fitted model."""
        res = {}

        # Fit indices (calc_stats returns DataFrame with one row)
        try:
            fit_stats = calc_stats(self.model)
            row = fit_stats.iloc[0]
            res["fit_indices"] = {
                "chi2": float(row["chi2"]),
                "df": int(row["DoF"]),
                "p_value": float(row["chi2 p-value"]),
                "cfi": float(row["CFI"]),
                "tli": float(row["TLI"]),
                "rmsea": float(row["RMSEA"]),
                "srmr": float(row["SRMR"]),
                "aic": float(row["AIC"]),
                "bic": float(row["BIC"])
            }
        except Exception as e:
            res["fit_indices"] = {"error": str(e)}

        # Parameter estimates
        try:
            params = self.model.inspect()
            _debug_write('debug_params.txt', str(params))
            res["parameters"] = params.to_dict()
            # Extract structural paths (regressions)
            path_coef = {}
            for idx, row in params.iterrows():
                # row is a pandas Series
                if row.get("op") == "~":
                    lval = row.get("lval")
                    rval = row.get("rval")
                    if lval != rval:
                        def safe_float(v):
                            try:
                                return float(v)
                            except (ValueError, TypeError):
                                return None
                        path_coef[(rval, lval)] = {
                            "estimate": safe_float(row["Estimate"]),
                            "se": safe_float(row["Std. Err"]),
                            "z": safe_float(row["z-value"]),
                            "p": safe_float(row["p-value"])
                        }
                        
            res["paths"] = path_coef
            res["n_parameters"] = len(params)
        except Exception as e:
            error_text = f"Parameter extraction failed: {e}\n" + traceback.format_exc()
            _debug_write('extract_params_error.txt', error_text)
            res["paths"] = {"error": str(e)}
            res["n_parameters"] = None

        # Sample size used
        try:
            res["n_obs"] = self.model.n_obs if hasattr(self.model, 'n_obs') else None
        except:
            res["n_obs"] = None

        return res

    @staticmethod
    def interpret_fit(fit_indices: Dict[str, float]) -> List[str]:
        """Generate human-readable fit assessment."""
        msgs = []
        if fit_indices.get("cfi", 0) > 0.95:
            msgs.append("CFI 优秀 (>0.95)")
        elif fit_indices.get("cfi", 0) > 0.90:
            msgs.append("CFI 良好 (>0.90)")
        else:
            msgs.append("CFI 不足，建议改进模型")
        rmsea = fit_indices.get("rmsea", 1)
        if rmsea < 0.05:
            msgs.append("RMSEA 优秀 (<0.05)")
        elif rmsea < 0.08:
            msgs.append("RMSEA 可接受 (<0.08)")
        else:
            msgs.append("RMSEA 偏高，模型可能需要修正")
        return msgs
