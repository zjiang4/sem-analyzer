#!/usr/bin/env python3
"""
导出工具
将结果、报告、图表保存为文件
"""

from pathlib import Path
from typing import Dict, Any

def save_markdown_report(content: str, session_id: str, directory: str = "reports") -> Path:
    """保存 Markdown 报告"""
    dir_path = Path(directory)
    dir_path.mkdir(exist_ok=True)
    file_path = dir_path / f"sem_report_{session_id}.md"
    file_path.write_text(content, encoding="utf-8")
    return file_path

def save_results_json(results: Dict[str, Any], session_id: str, directory: str = "reports") -> Path:
    """保存原始结果为 JSON"""
    dir_path = Path(directory)
    dir_path.mkdir(exist_ok=True)
    file_path = dir_path / f"sem_results_{session_id}.json"
    import json
    file_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    return file_path

def load_results_json(session_id: str, directory: str = "reports") -> Dict[str, Any]:
    """从磁盘加载结果（供后续分析）"""
    file_path = Path(directory) / f"sem_results_{session_id}.json"
    if file_path.exists():
        import json
        return json.loads(file_path.read_text(encoding="utf-8"))
    return {}
