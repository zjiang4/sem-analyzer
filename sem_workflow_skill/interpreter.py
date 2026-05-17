"""
Results interpretation utilities for SEM workflow.
"""

import pandas as pd
from typing import Dict, List


class ResultInterpreter:
    """
    Interpret SEM results for user.

    Provides:
    - Path coefficient interpretation
    - Factor loading interpretation
    - R² calculation
    - Effect size interpretation
    """

    @staticmethod
    def interpret_path_coefficient(
        estimate: float, std_error: float, p_value: float, standardized: bool = False
    ) -> Dict:
        """
        Interpret a path coefficient.

        Args:
            estimate: Path coefficient
            std_error: Standard error
            p_value: p-value
            standardized: Whether estimate is standardized

        Returns:
            Dictionary with interpretation
        """
        z_score = estimate / std_error if std_error > 0 else 0
        significant = p_value < 0.05

        # Effect size interpretation (Cohen's conventions for standardized)
        effect_size = ResultInterpreter._interpret_effect_size(
            estimate if standardized else 0
        )

        return {
            "estimate": estimate,
            "std_error": std_error,
            "z_score": z_score,
            "p_value": p_value,
            "significant": significant,
            "effect_size": effect_size,
        }

    @staticmethod
    def _interpret_effect_size(estimate: float) -> str:
        """
        Interpret effect size using Cohen's conventions.

        Args:
            estimate: Standardized estimate

        Returns:
            Effect size interpretation string
        """
        abs_est = abs(estimate)

        if abs_est < 0.1:
            return "Very small"
        elif abs_est < 0.3:
            return "Small"
        elif abs_est < 0.5:
            return "Medium"
        else:
            return "Large"

    @staticmethod
    def interpret_factor_loading(
        indicator: str, factor: str, loading: float, p_value: float
    ) -> Dict:
        """
        Interpret a factor loading.

        Args:
            indicator: Observed variable name
            factor: Latent variable name
            loading: Loading estimate
            p_value: p-value

        Returns:
            Dictionary with interpretation
        """
        abs_loading = abs(loading)
        significant = p_value < 0.05

        if abs_loading >= 0.70:
            quality = "Good"
        elif abs_loading >= 0.50:
            quality = "Acceptable"
        else:
            quality = "Poor"

        return {
            "indicator": indicator,
            "factor": factor,
            "loading": loading,
            "abs_loading": abs_loading,
            "p_value": p_value,
            "significant": significant,
            "quality": quality,
        }

    @staticmethod
    def calculate_r_squared(error_variance: float, total_variance: float) -> Dict:
        """
        Calculate and interpret R² value.

        Args:
            error_variance: Residual variance
            total_variance: Total variance

        Returns:
            Dictionary with R² interpretation
        """
        if total_variance == 0:
            return {
                "r_squared": 0,
                "interpretation": "Cannot calculate (zero variance)",
            }

        r_squared = 1 - (error_variance / total_variance)

        if r_squared >= 0.75:
            interpretation = "Substantial"
        elif r_squared >= 0.50:
            interpretation = "Moderate"
        elif r_squared >= 0.25:
            interpretation = "Weak"
        else:
            interpretation = "Very weak"

        return {"r_squared": r_squared, "interpretation": interpretation}

    @staticmethod
    def format_apa_results(estimates: pd.DataFrame, fit_stats: pd.DataFrame) -> str:
        """
        Format results in APA style.

        Args:
            estimates: Parameter estimates DataFrame
            fit_stats: Fit statistics DataFrame

        Returns:
            APA-formatted results string
        """
        lines = []

        # Fit indices
        lines.append("Model Fit Indices")
        lines.append("-" * 50)

        for idx, row in fit_stats.iterrows():
            lines.append(f"{idx}: {row.get('Value', row.values[0]):.4f}")

        lines.append("")

        # Parameter estimates
        lines.append("Parameter Estimates")
        lines.append("-" * 50)

        for idx, row in estimates.iterrows():
            if row["op"] == "~":
                lines.append(
                    f"{row['lval']} → {row['rval']}: "
                    f"B = {row['Estimate']:.4f}, SE = {row['Std. Err']:.4f}, "
                    f"p = {row['p-value']:.4f}"
                )

        return "\n".join(lines)
