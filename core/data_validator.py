#!/usr/bin/env python3
"""Data validation for SEM analysis."""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple


class DataValidator:
    """Validates data suitability for SEM analysis."""

    def validate(self, df: pd.DataFrame) -> Tuple[bool, List[str]]:
        warnings = []

        if len(df.columns) < 3:
            warnings.append(f"BLOCKING: Only {len(df.columns)} column(s) detected. SEM typically requires multiple observed variables (at least 3).")

        if len(df) < 50:
            warnings.append(f"BLOCKING: Sample size N={len(df)} is very small for SEM. Recommend N >= 100.")

        missing_pct = df.isnull().mean() * 100
        high_missing = missing_pct[missing_pct > 20]
        if not high_missing.empty:
            for col, pct in high_missing.items():
                warnings.append(f"Variable '{col}' has {pct:.1f}% missing values.")

        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        non_numeric = [c for c in df.columns if c not in numeric_cols]
        if non_numeric:
            warnings.append(f"Non-numeric columns detected: {', '.join(non_numeric[:5])}. "
                           "These can be used as grouping variables for multigroup analysis, "
                           "or excluded from the model.")

        id_cols = self._detect_id_columns(df)
        for col in id_cols:
            if col not in non_numeric:
                warnings.append(f"Column '{col}' looks like an ID column (all unique values). "
                               "It will likely be excluded from the SEM model.")

        constant_cols = [c for c in df.columns if df[c].nunique() <= 1]
        if constant_cols:
            warnings.append(f"Constant columns (no variance): {', '.join(constant_cols)}")

        blocking = [w for w in warnings if w.startswith("BLOCKING:")]
        return len(blocking) == 0, warnings

    def _detect_id_columns(self, df: pd.DataFrame) -> List[str]:
        id_cols = []
        n = len(df)
        for col in df.columns:
            nunique = df[col].nunique()
            if n > 10 and nunique >= n * 0.9:
                name_lower = col.lower()
                if any(kw in name_lower for kw in ['id', '_id', 'id_', 'identifier', 'code', 'key', 'index', '编号', '序号']):
                    id_cols.append(col)
                elif df[col].dtype in [np.int64, np.float64]:
                    vals = df[col].dropna()
                    if len(vals) > 0:
                        is_monotone = (vals.diff().dropna() > 0).all() or (vals.diff().dropna() < 0).all()
                        if is_monotone and nunique >= n * 0.95:
                            id_cols.append(col)
        return id_cols

    def detect_variable_types(self, df: pd.DataFrame) -> Dict[str, str]:
        result = {}
        id_cols = self._detect_id_columns(df)
        for col in df.columns:
            if col in id_cols:
                result[col] = 'id'
                continue
            nunique = df[col].nunique()
            if df[col].dtype == object or nunique <= 5:
                result[col] = 'categorical'
            else:
                result[col] = 'continuous'
        return result
