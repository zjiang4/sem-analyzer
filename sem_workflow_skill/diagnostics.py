"""
Diagnostics and model evaluation utilities.
"""

import pandas as pd
from typing import Dict, List, Tuple


class SEMDiagnostics:
    """
    Model diagnostics for SEM analysis.

    Provides:
    - Fit index calculation and interpretation
    - Parameter diagnostics
    - Model modification suggestions
    """

    @staticmethod
    def interpret_fit_indices(stats: pd.DataFrame) -> Dict:
        """
        Interpret SEM fit indices.

        Args:
            stats: DataFrame with fit indices

        Returns:
            Dictionary with interpretation
        """
        interpretation = {
            "overall": "Unknown",
            "details": [],
            "issues": [],
            "recommendations": [],
        }

        # Extract key indices (handle different formats)
        if isinstance(stats, pd.DataFrame):
            # Try common column names
            rmsea = SEMDiagnostics._get_stat(stats, "RMSEA", "rmsea")
            cfi = SEMDiagnostics._get_stat(stats, "CFI", "cfi")
            tli = SEMDiagnostics._get_stat(stats, "TLI", "tli")
            srmr = SEMDiagnostics._get_stat(stats, "SRMR", "srmr")
            chi2 = SEMDiagnostics._get_stat(stats, "chi2", "chi2")
            p_chi2 = SEMDiagnostics._get_stat(stats, "chi2 p-value", "chi2_p")
        else:
            # Assume it's a dict-like object
            rmsea = stats.get("RMSEA", 1.0)
            cfi = stats.get("CFI", 0.0)
            tli = stats.get("TLI", 0.0)
            srmr = stats.get("SRMR", 0.1)
            chi2 = stats.get("chi2", 0)
            p_chi2 = stats.get("chi2 p-value", 0)

        # RMSEA
        if rmsea < 0.05:
            interpretation["details"].append(f"RMSEA = {rmsea:.3f}: Excellent")
        elif rmsea < 0.08:
            interpretation["details"].append(f"RMSEA = {rmsea:.3f}: Good")
        elif rmsea < 0.10:
            interpretation["details"].append(f"RMSEA = {rmsea:.3f}: Acceptable")
        else:
            interpretation["details"].append(f"RMSEA = {rmsea:.3f}: Poor")
            interpretation["issues"].append("RMSEA indicates poor fit (>0.10)")

        # CFI
        if cfi >= 0.95:
            interpretation["details"].append(f"CFI = {cfi:.3f}: Excellent")
        elif cfi >= 0.90:
            interpretation["details"].append(f"CFI = {cfi:.3f}: Good")
        elif cfi >= 0.80:
            interpretation["details"].append(f"CFI = {cfi:.3f}: Acceptable")
        else:
            interpretation["details"].append(f"CFI = {cfi:.3f}: Poor")
            interpretation["issues"].append("CFI indicates poor fit (<0.80)")

        # TLI
        if tli >= 0.95:
            interpretation["details"].append(f"TLI = {tli:.3f}: Excellent")
        elif tli >= 0.90:
            interpretation["details"].append(f"TLI = {tli:.3f}: Good")
        elif tli >= 0.80:
            interpretation["details"].append(f"TLI = {tli:.3f}: Acceptable")
        else:
            interpretation["details"].append(f"TLI = {tli:.3f}: Poor")
            interpretation["issues"].append("TLI indicates poor fit (<0.80)")

        # SRMR
        if srmr < 0.08:
            interpretation["details"].append(f"SRMR = {srmr:.3f}: Good")
        elif srmr < 0.10:
            interpretation["details"].append(f"SRMR = {srmr:.3f}: Acceptable")
        else:
            interpretation["details"].append(f"SRMR = {srmr:.3f}: Poor")
            interpretation["issues"].append("SRMR indicates poor fit (>0.10)")

        # χ² test
        if chi2 is not None and p_chi2 is not None:
            if p_chi2 > 0.05:
                interpretation["details"].append(
                    f"χ²({chi2:.2f}) = {p_chi2:.3f}: Non-significant (good fit)"
                )
            else:
                interpretation["details"].append(
                    f"χ²({chi2:.2f}) = {p_chi2:.3f}: Significant (poor fit)"
                )

        # Overall fit
        if rmsea < 0.08 and cfi >= 0.90 and tli >= 0.90 and srmr < 0.10:
            interpretation["overall"] = "Good"
        else:
            interpretation["overall"] = "Poor"

        return interpretation

    @staticmethod
    def _get_stat(stats: pd.DataFrame, *keys: str) -> float:
        """
        Helper to get statistic value from DataFrame.

        Tries multiple possible column names.
        """
        for key in keys:
            if key in stats.columns:
                return stats[key].values[0] if len(stats) > 0 else stats[key]
            if key.lower() in [c.lower() for c in stats.columns]:
                col = [c for c in stats.columns if c.lower() == key.lower()][0]
                return stats[col].values[0] if len(stats) > 0 else stats[col]

        return float("nan")

    @staticmethod
    def check_parameter_issues(estimates: pd.DataFrame) -> Dict:
        """
        Check parameter estimates for common issues.

        Args:
            estimates: DataFrame with parameter estimates

        Returns:
            Dictionary with issues
        """
        issues = {
            "negative_variances": [],
            "unreasonable_estimates": [],
            "large_standard_errors": [],
            "non_significant_paths": [],
        }

        for idx, row in estimates.iterrows():
            # Check for negative variances
            if row["op"] == "~~":
                if row["Estimate"] < 0:
                    issues["negative_variances"].append(
                        {
                            "parameter": f"{row['lval']} ~~ {row['rval']}",
                            "estimate": row["Estimate"],
                        }
                    )

            # Check for large standard errors
            se = row.get("Std. Err", row.get("std_error", 0))
            est = row.get("Estimate", 0)
            if se > abs(est):
                issues["large_standard_errors"].append(
                    {
                        "parameter": f"{row['lval']} {row['op']} {row['rval']}",
                        "se": se,
                        "estimate": est,
                    }
                )

            # Check for non-significant structural paths
            if row["op"] == "~":
                p_val = row.get("p-value", 1.0)
                if p_val >= 0.05:
                    issues["non_significant_paths"].append(
                        {
                            "parameter": f"{row['rval']} → {row['lval']}",
                            "p_value": p_val,
                        }
                    )

        return issues

    @staticmethod
    def suggest_modifications(model, data: pd.DataFrame, residual_threshold: float = 0.1) -> List[Dict]:
        """
        Suggest model modifications based on residual analysis.

        This implementation computes normalized residuals between observed
        and model-implied covariance matrices, and suggests adding error
        covariances for indicator pairs with large residuals.

        Args:
            model: Fitted semopy model
            data: Dataset used for fitting
            residual_threshold: Absolute residual value to trigger suggestion (default 0.1)

        Returns:
            List of suggested modifications, each with:
            - type: 'covariance'
            - variables: (var1, var2)
            - residual_value: the normalized residual magnitude
            - suggestion: what to add to model
            - caveat: theoretical justification needed
        """
        suggestions = []

        try:
            import numpy as np
            from semopy import calc_stats

            # Get observed and model-implied covariance matrices
            observed_cov = data.cov()
            # semopy's model object has mx_sigma (model-implied covariance)
            if hasattr(model, 'mx_sigma'):
                implied_cov = pd.DataFrame(
                    model.mx_sigma,
                    index=model.vars['observed'],
                    columns=model.vars['observed']
                )
            else:
                # Fallback: compute from stats
                stats = calc_stats(model)
                implied_cov = None

            if implied_cov is not None and observed_cov.shape == implied_cov.shape:
                # Compute normalized residuals: (obs - impl) / sqrt(impl_var)
                residuals = observed_cov - implied_cov
                # Standardize by square root of diagonal (approx. se)
                se_approx = np.sqrt(np.diag(implied_cov))
                se_matrix = np.outer(se_approx, se_approx)
                norm_residuals = residuals / se_matrix

                # Find large off-diagonal residuals
                upper_idx = np.triu_indices_from(norm_residuals, k=1)
                for i, j in zip(upper_idx[0], upper_idx[1]):
                    var1 = norm_residuals.index[i]
                    var2 = norm_residuals.columns[j]
                    resid_val = abs(norm_residuals.iloc[i, j])
                    if resid_val > residual_threshold:
                        suggestions.append({
                            "type": "covariance",
                            "variables": (var1, var2),
                            "residual_value": float(resid_val),
                            "suggestion": f"Add {var1} ~~ {var2} (normalized residual = {resid_val:.2f})",
                            "caveat": "Only add if theoretically justified (shared method variance, correlated errors)"
                        })

            # Sort by residual magnitude descending
            suggestions.sort(key=lambda x: x['residual_value'], reverse=True)

            # Add generic advice if no specific suggestions
            if len(suggestions) == 0:
                suggestions.append({
                    "type": "general",
                    "suggestion": "Model fit appears adequate; no large residuals detected",
                    "caveat": "Continue with current specification"
                })

        except Exception as e:
            suggestions.append({
                "type": "error",
                "suggestion": f"Could not compute modification indices: {e}",
                "caveat": "Manual review needed"
            })

        return suggestions
