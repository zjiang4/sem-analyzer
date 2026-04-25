#!/usr/bin/env python3
"""Model draft builder: represents measurement and structural model before fitting."""

from typing import Dict, List, Tuple, Optional
import json


class ModelDraft:
    """Represents a SEM model draft: measurement + structural parts."""

    def __init__(self):
        # Latent variables: name -> {items: [], type: "reflective"/"formative"}
        self.latent: Dict[str, Dict] = {}
        # Observed variables that are not part of any latent construct
        self.observed: List[str] = []
        # Covariates (control variables)
        self.covariates: List[str] = []
        # Structural paths: list of (from, to)
        self.paths: List[Tuple[str, str]] = []
        # Notes
        self.notes: str = ""

    def add_latent(self, name: str, items: List[str], var_type: str = "reflective") -> None:
        """Add or update a latent variable."""
        if name in self.latent:
            # Update items (merge)
            existing = set(self.latent[name]["items"])
            new_items = list(existing.union(items))
            self.latent[name]["items"] = new_items
        else:
            self.latent[name] = {
                "items": items,
                "type": var_type
            }

    def remove_latent(self, name: str) -> None:
        """Remove a latent variable (and its items from observed if they were there)."""
        if name in self.latent:
            del self.latent[name]

    def set_observed(self, variables: List[str]) -> None:
        """Set observed variables (excluding those in latent)."""
        self.observed = variables[:]

    def add_covariate(self, var: str) -> None:
        """Add a control variable."""
        if var not in self.covariates:
            self.covariates.append(var)

    def remove_covariate(self, var: str) -> None:
        """Remove a control variable."""
        if var in self.covariates:
            self.covariates.remove(var)

    def add_path(self, src: str, dst: str) -> None:
        """Add a structural path."""
        if (src, dst) not in self.paths:
            self.paths.append((src, dst))

    def remove_path(self, src: str, dst: str) -> None:
        """Remove a structural path."""
        if (src, dst) in self.paths:
            self.paths.remove((src, dst))

    def to_semopy_model(self) -> str:
        """Convert to semopy Model format string."""
        lines = []

        # Measurement model
        for lv, info in self.latent.items():
            items_str = " + ".join(info["items"])
            lines.append(f"{lv} =~ {items_str}")

        # Add observed variables as constants if needed? semopy ignores them unless in paths
        # We only declare paths for variables that appear

        # Structural model
        for src, dst in self.paths:
            lines.append(f"{dst} ~ {src}")

        return "\n".join(lines)

    def to_dict(self) -> Dict:
        """Export as dictionary (for storage)."""
        return {
            "latent": self.latent,
            "observed": self.observed,
            "covariates": self.covariates,
            "paths": self.paths,
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'ModelDraft':
        """Reconstruct from dictionary."""
        draft = cls()
        draft.latent = data.get("latent", {})
        draft.observed = data.get("observed", [])
        draft.covariates = data.get("covariates", [])
        draft.paths = [tuple(p) for p in data.get("paths", [])]
        draft.notes = data.get("notes", "")
        return draft

    def get_all_variables(self) -> List[str]:
        """Get all variables mentioned in the model."""
        all_vars = set()
        for lv, info in self.latent.items():
            all_vars.add(lv)
            all_vars.update(info["items"])
        all_vars.update(self.observed)
        all_vars.update(self.covariates)
        for src, dst in self.paths:
            all_vars.add(src)
            all_vars.add(dst)
        return sorted(list(all_vars))

    def validate(self) -> Tuple[bool, List[str]]:
        """Validate model structure; return (is_valid, messages)."""
        errors = []

        # Check each latent has at least 2 items
        for lv, info in self.latent.items():
            if len(info["items"]) < 2:
                errors.append(f"潜变量 '{lv}' 至少需要2个题项（当前{len(info['items'])}个）")

        # Check that all variables in paths exist
        all_vars = self.get_all_variables()
        for src, dst in self.paths:
            if src not in all_vars:
                errors.append(f"路径起点 '{src}' 未定义")
            if dst not in all_vars:
                errors.append(f"路径终点 '{dst}' 未定义")

        # Check for circular paths (not allowed in recursive models? warn only)
        # Simple cycle detection in directed graph
        if self._has_cycle():
            errors.append("检测到路径循环（如 A→B→A），这会导致模型不可识别")

        return (len(errors) == 0, errors)

    def _has_cycle(self) -> bool:
        """Check if structural paths contain a cycle."""
        # Build adjacency list
        graph = {}
        for src, dst in self.paths:
            graph.setdefault(src, []).append(dst)

        # DFS to detect cycle
        visited = set()
        rec_stack = set()

        def dfs(node):
            visited.add(node)
            rec_stack.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
            rec_stack.remove(node)
            return False

        for node in graph:
            if node not in visited:
                if dfs(node):
                    return True
        return False

    def get_paths_summary(self) -> str:
        """Human-readable paths."""
        lines = []
        for src, dst in self.paths:
            lines.append(f"{src} → {dst}")
        return "\n".join(lines) if lines else "（无结构路径）"

    def get_measurement_summary(self) -> str:
        """Human-readable measurement model."""
        lines = []
        for lv, info in self.latent.items():
            items = " + ".join(info["items"])
            lines.append(f"{lv} =~ {items}")
        return "\n".join(lines) if lines else "（无潜变量）"
