#!/usr/bin/env python3
"""Result saving utility for SEM analysis sessions."""

import json
import os
from datetime import datetime
from typing import Any, Dict, Optional


class ResultSaver:
    """Saves SEM analysis results to disk."""

    def __init__(self, output_dir: str = '.'):
        self.output_dir = output_dir

    def save_json(self, results: Dict, filename: str = None) -> str:
        os.makedirs(self.output_dir, exist_ok=True)
        if filename is None:
            filename = f"sem_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        path = os.path.join(self.output_dir, filename)

        serializable = self._make_serializable(results)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(serializable, f, indent=2, ensure_ascii=False, default=str)
        return path

    def _make_serializable(self, obj: Any) -> Any:
        import numpy as np
        import pandas as pd
        if isinstance(obj, dict):
            return {k: self._make_serializable(v) for k, v in obj.items()}
        if isinstance(obj, (list, tuple)):
            return [self._make_serializable(v) for v in obj]
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, pd.DataFrame):
            return obj.to_dict(orient='records')
        if isinstance(obj, (pd.Timestamp, datetime)):
            return obj.isoformat()
        return obj
