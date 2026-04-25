#!/usr/bin/env python3
"""
SEM Model Templates for advanced analysis types.
Each template provides a semopy model syntax generator.
"""

from typing import Dict, List, Tuple, Any
from dataclasses import dataclass


def _normalize_items(items) -> List[str]:
    """Accept either a plain list or {'items': [...]} dict; return list."""
    if isinstance(items, list):
        return items
    if isinstance(items, dict) and 'items' in items:
        return items['items']
    return list(items)


@dataclass
class ModelTemplate:
    """Represents a reusable SEM model template."""
    name: str
    description: str
    required_vars: List[str]  # variable types needed
    optional_vars: List[str] = None

    def generate(self, user_vars: Dict[str, List[str]]) -> str:
        """
        Generate semopy model string given user's variable mapping.
        user_vars: {'latent': {...}, 'observed': [...], 'covariates': [...]}
        """
        raise NotImplementedError


class CFATemplate(ModelTemplate):
    """Confirmatory Factor Analysis (Measurement model only)"""
    def __init__(self):
        super().__init__(
            name="CFA",
            description="验证性因子分析（测量模型）",
            required_vars=['latent', 'observed']
        )

    def generate(self, user_vars: Dict) -> str:
        lines = ["# CFA Model"]
        for lv, items in user_vars['latent'].items():
            items = _normalize_items(items)
            items_str = " + ".join(items)
            lines.append(f"{lv} =~ {items_str}")
        return "\n".join(lines)


class GrowthModelTemplate(ModelTemplate):
    """Latent Growth Curve Model (single-phase)"""
    def __init__(self):
        super().__init__(
            name="Latent Growth",
            description="潜增长模型（线性）",
            required_vars=['time_points', 'observed_pattern']
        )

    def generate(self, user_vars: Dict) -> str:
        """
        user_vars should contain:
          - 'items': list of repeated measure items (in chronological order)
          - 'time_loadings': list of numeric loadings for slope factor, one per item (optional; default 0,1,2,...)
        """
        lines = ["# Latent Growth Model"]
        items = user_vars.get('items', [])
        if not items:
            raise ValueError("Growth model requires 'items' list")
        # Intercept factor: all items load with 1
        lines.append(f"intercept =~ {' + '.join(items)}")
        # Slope factor: use provided time_loadings or default ordinal
        loadings = user_vars.get('time_loadings')
        if loadings is None:
            loadings = list(range(len(items)))
        if len(loadings) != len(items):
            raise ValueError(f"time_loadings length ({len(loadings)}) must match items count ({len(items)})")
        slope_parts = [f"{load}*{item}" for load, item in zip(loadings, items)]
        lines.append(f"slope =~ {' + '.join(slope_parts)}")
        # Covariance between intercept and slope
        lines.append("intercept ~~ slope")
        return "\n".join(lines)


class MediationTemplate(ModelTemplate):
    """Simple mediation model (X -> M -> Y)"""
    def __init__(self):
        super().__init__(
            name="Mediation",
            description="中介效应模型",
            required_vars=['cause', 'mediator', 'outcome']
        )

    def generate(self, user_vars: Dict) -> str:
        cause = user_vars['cause'][0] if isinstance(user_vars['cause'], list) else user_vars['cause']
        mediator = user_vars['mediator'][0] if isinstance(user_vars['mediator'], list) else user_vars['mediator']
        outcome = user_vars['outcome'][0] if isinstance(user_vars['outcome'], list) else user_vars['outcome']

        lines = [
            "# Mediation Model",
            "# Direct effect",
            f"{outcome} ~ {cause}",
            "# Indirect effect via mediator",
            f"{mediator} ~ {cause}",
            f"{outcome} ~ {mediator}"
        ]
        return "\n".join(lines)


class MultigroupTemplate(ModelTemplate):
    """Multi-group analysis (measurement invariance testing)"""
    def __init__(self):
        super().__init__(
            name="Multi-group",
            description="多组分析（测量等值性）",
            required_vars=['groups', 'latent', 'observed'],
            optional_vars=['invariance', 'paths']
        )

    def generate(self, user_vars: Dict) -> str:
        invariance = user_vars.get('invariance', 'configural')
        latent = user_vars.get('latent', {})
        lines = [f"# Multi-group SEM ({invariance} invariance)"]

        if invariance == 'configural':
            for lv, items in latent.items():
                items = _normalize_items(items)
                lines.append(f"{lv} =~ {' + '.join(items)}")
        elif invariance in ('metric', 'scalar'):
            for lv, items in latent.items():
                items = _normalize_items(items)
                parts = [f"1*{items[0]}"]
                for item in items[1:]:
                    parts.append(f"lam__{item}*{item}")
                lines.append(f"{lv} =~ {' + '.join(parts)}")
            if invariance == 'scalar':
                seen = set()
                for items in latent.values():
                    items = _normalize_items(items)
                    for item in items:
                        if item not in seen:
                            lines.append(f"{item} ~ int__{item}*1")
                            seen.add(item)

        paths = user_vars.get('paths', [])
        if paths:
            lines.append("")
            lines.append("# Structural paths:")
            for src, dst in paths:
                lines.append(f"{dst} ~ {src}")

        return "\n".join(lines)


# Registry of available templates
TEMPLATES: Dict[str, ModelTemplate] = {
    'cfa': CFATemplate(),
    'growth': GrowthModelTemplate(),
    'mediation': MediationTemplate(),
    'multigroup': MultigroupTemplate()
}


def get_template(model_type: str) -> ModelTemplate:
    """Get template by name (case-insensitive)"""
    key = model_type.lower().replace(' ', '').replace('-', '')
    # Try exact match first
    if key in TEMPLATES:
        return TEMPLATES[key]
    # Try partial
    for k, tmpl in TEMPLATES.items():
        if k in key or key in k:
            return tmpl
    raise ValueError(f"Unknown model type: {model_type}")


def list_templates() -> List[Dict]:
    """Return list of available templates with descriptions"""
    return [
        {"name": t.name, "description": t.description, "required": t.required_vars}
        for t in TEMPLATES.values()
    ]


if __name__ == '__main__':
    print("Available templates:")
    for t in list_templates():
        print(f"- {t['name']}: {t['description']}")
        print(f"  Required: {t['required']}")
