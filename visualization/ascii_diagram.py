#!/usr/bin/env python3
"""ASCII diagram generator for SEM models."""

def generate_ascii(model_draft) -> str:
    """Generate ASCII diagram string."""
    latent = model_draft.latent if hasattr(model_draft, 'latent') else {}
    observed = model_draft.observed if hasattr(model_draft, 'observed') else []
    covariates = model_draft.covariates if hasattr(model_draft, 'covariates') else []
    paths = model_draft.paths if hasattr(model_draft, 'paths') else []

    lines = ["Model Variable Overview:", ""]

    if latent:
        lines.append("Latent Variables")
        for name, info in latent.items():
            items = ", ".join(info.get("items", []))
            lines.append(f"  {name} =~ {items}")
        lines.append("")

    if observed:
        lines.append("Observed Variables")
        for v in observed:
            lines.append(f"  {v}")
        lines.append("")

    if covariates:
        lines.append("Covariates")
        for v in covariates:
            lines.append(f"  {v}")
        lines.append("")

    lines.append("Structural Paths (Causal Direction)")
    if not paths:
        lines.append("  (No paths defined)")
    else:
        if isinstance(paths, list):
            for outcome, predictor in paths:
                lines.append(f"  {predictor} -> {outcome}")
        elif isinstance(paths, dict):
            for (src, dst) in paths:
                lines.append(f"  {src} -> {dst}")
        else:
            lines.append("  (Invalid path format)")

    lines.append("")
    lines.append("Full SEM Model (semopy syntax):")
    lines.append("-"*40)
    lines.append("# Measurement Model")
    for lv, info in latent.items():
        items = " + ".join(info.get("items", []))
        lines.append(f"{lv} =~ {items}")
    lines.append("")
    lines.append("# Structural Model")
    if isinstance(paths, list):
        for outcome, predictor in paths:
            lines.append(f"{predictor} -> {outcome}")
    elif isinstance(paths, dict):
        for (src, dst) in paths:
            lines.append(f"{src} -> {dst}")
    lines.append("-"*40)

    return "\n".join(lines)


class AsciiDiagram:
    """Wrapper for ASCII diagram generation."""
    @staticmethod
    def generate(model_draft) -> str:
        return generate_ascii(model_draft)
