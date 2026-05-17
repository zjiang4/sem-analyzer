"""
Data preparation utilities for SEM workflow.
"""

import pandas as pd
import numpy as np
from typing import Dict, Tuple, Optional


class DataPreparator:
    """
    Data preparation helper for SEM analysis.

    Handles:
    - Missing data assessment
    - Variable screening
    - Data cleaning
    - Variable coding verification
    """

    @staticmethod
    def check_normality(data: pd.DataFrame) -> Dict:
        """
        Check normality assumptions for continuous variables.

        Args:
            data: DataFrame to check

        Returns:
            Dictionary with normality statistics
        """
        from scipy import stats

        normality = {}
        for col in data.select_dtypes(include=[np.number]).columns:
            # Skewness and kurtosis
            skew = stats.skew(data[col].dropna())
            kurt = stats.kurtosis(data[col].dropna())

            # Shapiro-Wilk test (for n < 5000)
            if len(data[col].dropna()) < 5000:
                stat_sw, p_sw = stats.shapiro(data[col].dropna())
                normality[col] = {
                    "skewness": skew,
                    "kurtosis": kurt,
                    "shapiro_stat": stat_sw,
                    "shapiro_p": p_sw,
                    "normal": p_sw > 0.05,
                }
            else:
                normality[col] = {
                    "skewness": skew,
                    "kurtosis": kurt,
                    "normal": "Not tested (n too large)",
                }

        return normality

    @staticmethod
    def detect_outliers(data: pd.DataFrame, threshold: float = 3.0) -> Dict:
        """
        Detect outliers using z-score method.

        Args:
            data: DataFrame to check
            threshold: Z-score threshold (default 3.0)

        Returns:
            Dictionary with outlier information
        """
        outliers = {}

        for col in data.select_dtypes(include=[np.number]).columns:
            col_data = data[col].dropna()
            if len(col_data) < 2:
                continue
            # Calculate z-scores manually
            mean = col_data.mean()
            std = col_data.std()
            if std == 0:
                continue
            z_scores = np.abs((col_data - mean) / std)
            outlier_indices = np.where(z_scores > threshold)[0]
            outlier_count = len(outlier_indices)
            outlier_percent = (outlier_count / len(data)) * 100

            if outlier_count > 0:
                outliers[col] = {
                    "count": outlier_count,
                    "percent": outlier_percent,
                    "indices": list(outlier_indices),
                }

        return outliers

    @staticmethod
    def check_variance(data: pd.DataFrame, min_variance: float = 0.1) -> Dict:
        """
        Check for low variance variables.

        Args:
            data: DataFrame to check
            min_variance: Minimum acceptable variance

        Returns:
            Dictionary with variance information
        """
        variances = {}

        for col in data.select_dtypes(include=[np.number]).columns:
            var = data[col].var()

            if var < min_variance:
                variances[col] = {"variance": var, "low_variance": True}

        return variances

    @staticmethod
    def suggest_missing_strategy(data: pd.DataFrame) -> Tuple[str, str]:
        """
        Suggest missing data handling strategy.

        Args:
            data: DataFrame to assess

        Returns:
            Tuple of (strategy, reasoning)
        """
        total_cells = len(data) * len(data.columns)
        missing_cells = data.isnull().sum().sum()
        missing_percent = (missing_cells / total_cells) * 100

        # Check pattern (simple heuristic)
        missing_per_row = data.isnull().sum(axis=1)
        complete_cases = (missing_per_row == 0).sum()
        complete_percent = (complete_cases / len(data)) * 100

        if missing_percent < 5:
            strategy = "Listwise deletion or FIML"
            reasoning = f"Low missingness ({missing_percent:.1f}%). Listwise deletion acceptable, or use FIML (default in semopy)."
        elif missing_percent < 20:
            strategy = "Full Information Maximum Likelihood (FIML)"
            reasoning = f"Moderate missingness ({missing_percent:.1f}%). FIML recommended for MAR data."
        elif complete_percent > 50:
            strategy = "Listwise deletion"
            reasoning = f"High missingness ({missing_percent:.1f}%), but {complete_percent:.1f}% complete cases. Deletion may be acceptable."
        else:
            strategy = "Multiple imputation"
            reasoning = f"High missingness ({missing_percent:.1f}%). Consider multiple imputation (MICE) before SEM analysis."

        return strategy, reasoning
