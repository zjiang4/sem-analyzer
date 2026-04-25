#!/usr/bin/env python3
"""Data validation for SEM analysis."""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple


class DataValidator:
    """Validates data suitability for SEM analysis."""

    def validate(self, df: pd.DataFrame) -> Tuple[bool, List[str]]:
        warnings = []

        if len(df) < 50:
            warnings.append(f"Sample size N={len(df)} is very small for SEM. Recommend N >= 100.")

        missing_pct = df.isnull().mean() * 100
        high_missing = missing_pct[missing_pct > 20]
        if not high_missing.empty:
            for col, pct in high_missing.items():
                warnings.append(f"Variable '{col}' has {pct:.1f}% missing values.")

        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        non_numeric = [c for c in df.columns if c not in numeric_cols]
        if non_numeric:
            warnings.append(f"Non-numeric columns detected: {', '.join(non_numeric[:5])}. "
                           "SEM requires continuous variables.")

        constant_cols = [c for c in df.columns if df[c].nunique() <= 1]
        if constant_cols:
            warnings.append(f"Constant columns (no variance): {', '.join(constant_cols)}")

        return len(warnings) == 0, warnings

    def detect_variable_types(self, df: pd.DataFrame) -> Dict[str, str]:
        result = {}
        for col in df.columns:
            nunique = df[col].nunique()
            if df[col].dtype == object or nunique <= 5:
                result[col] = 'categorical'
            else:
                result[col] = 'continuous'
        return result
