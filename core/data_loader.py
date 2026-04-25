#!/usr/bin/env python3
"""Data loading and initial inspection for SEM Analyzer."""

import os
from typing import Optional
import pandas as pd


class DataLoader:
    """Loads CSV/Excel files into pandas DataFrames with basic validation."""

    SUPPORTED_EXTENSIONS = {'.csv', '.xlsx', '.xls', '.tsv'}

    def load(self, path: str, **kwargs) -> pd.DataFrame:
        ext = os.path.splitext(path)[1].lower()
        if ext == '.csv':
            df = pd.read_csv(path, **kwargs)
        elif ext in ('.xlsx', '.xls'):
            df = pd.read_excel(path, **kwargs)
        elif ext == '.tsv':
            df = pd.read_csv(path, sep='\t', **kwargs)
        else:
            raise ValueError(f"Unsupported file format: {ext}. Supported: {self.SUPPORTED_EXTENSIONS}")
        if df.empty:
            raise ValueError("Loaded DataFrame is empty.")
        return df

    def load_from_string(self, text: str, sep: str = ',') -> pd.DataFrame:
        import io
        return pd.read_csv(io.StringIO(text), sep=sep)
