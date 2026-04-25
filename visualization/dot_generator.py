#!/usr/bin/env python3
"""Generate Graphviz DOT representation for SEM model."""

from typing import Dict, List


class DotGenerator:
    """Generates Graphviz DOT code for model visualization."""

    def __init__(self):
        self.node_styles = {
            "latent": {"shape": "box", "style": "filled", "fillcolor": "#E1F5FE"},
            "observed": {"shape": "ellipse", "style": "filled", "fillcolor": "#F3E5F5"},
            "covariate": {"shape": "diamond", "style": "filled", "fillcolor": "#FFF3E0"},
            "outcome": {"shape": "ellipse", "style": "filled", "fillcolor": "#FFEBEE"}
        }

    def generate(self, draft, highlight_paths: bool = True) -> str:
        """
        Generate DOT code.

        Args:
            draft: ModelDraft instance
            highlight_paths: whether to make arrows bold for significant paths

        Returns:
            DOT string
        """
        lines = ["digraph SEM {"]
        lines.append("  rankdir=LR;")
        lines.append("  node [fontname=\"Arial\"];")
        lines.append("  edge [fontname=\"Arial\"];")

        # Collect all nodes and classify
        nodes = {}
        # Latent nodes
        for lv in draft.latent.keys():
            nodes[lv] = "latent"

        # Observed variables (items from latent and standalone)
        for lv, info in draft.latent.items():
            for item in info["items"]:
                nodes[item] = "observed"

        for ov in draft.observed:
            nodes[ov] = "observed"

        # Determine outcome variables (targets of structural paths)
        # Typically variables that are only on left side of ~ (dependents)
        dependent_vars = set(dst for _, dst in draft.paths)
        for var in dependent_vars:
            if var in nodes and nodes[var] == "observed":
                nodes[var] = "outcome"

        # Covariates
        for cov in draft.covariates:
            if cov not in nodes:
                nodes[cov] = "covariate"

        # Define nodes
        for name, ntype in nodes.items():
            style = self.node_styles.get(ntype, self.node_styles["observed"])
            attrs = [f"{k}={v}" for k, v in style.items()]
            lines.append(f'  "{name}" [{", ".join(attrs)}];')

        # Define edges (measurement)
        for lv, info in draft.latent.items():
            for item in info["items"]:
                lines.append(f'  "{item}" -> "{lv}" [style=dashed, arrowhead=none, color=gray];')

        # Define edges (structural)
        for src, dst in draft.paths:
            edge_attrs = ""
            if highlight_paths:
                edge_attrs = "penwidth=2, color=blue"
            lines.append(f'  "{src}" -> "{dst}" [{edge_attrs}];')

        lines.append("}")
        return "\n".join(lines)

    def save(self, draft, filepath: str):
        """Save DOT to file."""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(self.generate(draft))
