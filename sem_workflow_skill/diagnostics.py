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
    def suggest_modifications(model, data: pd.DataFrame) -> List[Dict]:
        """
        Suggest model modifications based on diagnostics.

        Note: semopy doesn't have built-in modification indices,
        so this provides general suggestions.

        Args:
            model: Fitted semopy model
            data: Dataset

        Returns:
            List of suggested modifications
        """
        suggestions = []

        # These would be implemented based on:
        # 1. Residual correlations
        # 2. Modification indices
        # 3. Theoretical justification

        # Placeholder suggestions
        suggestions.append(
            {
                "type": "covariance",
                "suggestion": "Add error covariance between indicators with high residual correlation",
                "caveat": "Only add if theoretically justified",
            }
        )

        return suggestions
