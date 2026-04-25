#!/usr/bin/env python3
"""Model confirmation and adjustment interface."""

from typing import Dict, Any
from core.model_draft import ModelDraft
from visualization.ascii_diagram import AsciiDiagram
from visualization.dot_generator import DotGenerator


class ModelConfirm:
    """Presents model draft and obtains user confirmation."""

    def __init__(self):
        self.ascii_diagram = AsciiDiagram()
        self.dot_generator = DotGenerator()

    def show_and_confirm(self, session: Any, user_input: str = "") -> str:
        """
        Display the model draft and ask for confirmation.
        """
        draft: ModelDraft = session.draft

        # Validate draft
        valid, errors = draft.validate()
        if not valid:
            msg = ["The model has the following issues, please correct:"]
            for err in errors:
                msg.append(f"   • {err}")
            msg.append("\nPlease go back and revise your definitions.")
            return "\n".join(msg)

        # Retrieve textbook references for model fitting stage
        retriever = getattr(session, 'textbook_retriever', None)
        textbook_refs = []
        if retriever:
            try:
                textbook_refs = retriever.get_by_stage('model_specification')[:2]
            except:
                pass

        # Build comprehensive summary
        parts = []

        # Add textbook references if available
        if textbook_refs:
            parts.append("Relevant textbook chapters for model specification (recommended):")
            for chapter in textbook_refs:
                title = chapter.title[:80]
                source = chapter.source.replace('MinerU_markdown_', '').replace('_', ' ')
                parts.append(f"  • {title} (Source: {source})")
            parts.append("")

        parts.append("Model draft generated. Please review:\n")

        # Measurement model summary
        parts.append("[Measurement Model]")
        if draft.latent:
            for lv, info in draft.latent.items():
                items_str = " + ".join(info["items"])
                parts.append(f"  {lv} =~ {items_str}")
        else:
            parts.append("  (No latent variables; all variables are observed)")

        parts.append("")

        # Observed and covariates
        if draft.observed:
            parts.append(f"Observed variables (non-latent): {', '.join(draft.observed)}")
        if draft.covariates:
            parts.append(f"Covariates: {', '.join(draft.covariates)}")

        parts.append("")

        # Structural paths
        parts.append("[Structural Model]")
        if draft.paths:
            for src, dst in draft.paths:
                parts.append(f"  {src} → {dst}")
        else:
            parts.append("  (No structural paths defined)")
        parts.append("")

        # Missing data handling
        missing = getattr(session, 'missing_handling', 'Not specified')
        parts.append(f"[Missing Data Handling] {missing}")
        parts.append("")

        # ASCII diagram
        parts.append("[Model Diagram]")
        parts.append(self.ascii_diagram.generate(draft))
        parts.append("")

        # Prompt for confirmation
        parts.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        parts.append("Does the model match your research design?")
        parts.append("  [confirm]  Start model fitting")
        parts.append("  [edit latent]  Redefine latent variables and indicators")
        parts.append("  [edit paths]  Add or remove structural paths")
        parts.append("  [restart]  Start over")
        parts.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        session.state = "model_ready_for_confirmation"
        return "\n".join(parts)

    def handle_confirmation(self, session: Any, user_input: str) -> str:
        """
        Handle user's response to model confirmation.
        Returns next step instruction.
        """
        text = user_input.strip().lower()

        if "确认" in text or "开始" in text or "拟合" in text or "confirm" in text or "start" in text or "fit" in text:
            session.state = "model_confirmed"
            return "Model confirmed. Type 'fit' to start analysis."

        if "修改潜变量" in text or "潜变量" in text or "edit latent" in text or "latent" in text:
            # Invoke clarifier latent modification (collaborative)
            from .clarifier import Clarifier
            clarifier = Clarifier()
            # Mark we are modifying, not starting over
            session.modifying_component = "latent"
            session.clarification_step = 3  # jump to latent definition step (after classifications)
            # Build prompt for editing
            return clarifier._step3_latent_indicators(session, "")

        if "修改结构" in text or "结构" in text or "路径" in text or "edit paths" in text or "paths" in text or "structure" in text:
            # Invoke clarifier path modification
            from .clarifier import Clarifier
            clarifier = Clarifier()
            session.modifying_component = "paths"
            session.clarification_step = 4  # hypothesis/path step
            return clarifier._step4_hypothesis(session, "")

        if "重新" in text or "从头" in text or "restart" in text or "start over" in text:
            # Reset session entirely
            session.state = "initial"
            session.draft = None
            session.variables = {}
            session.hypotheses = []
            session.decision_log = []
            return "Session reset. Please upload data to start again."

        # Default: ask for clarification
        return "Please choose: 'confirm' / 'edit latent' / 'edit paths' / 'restart'"

    def get_model_summary(self, session: Any) -> str:
        """Return a concise model summary for modification menu."""
        draft: ModelDraft = session.draft
        if not draft:
            return "(No model draft)"
        parts = ["[Current Model]"]
        if draft.latent:
            parts.append("Measurement:")
            for lv, items in draft.latent.items():
                parts.append(f"  {lv} =~ {', '.join(items)}")
        else:
            parts.append("Measurement: observed variables only")
        parts.append("Structure:")
        if draft.paths:
            for src, dst in draft.paths:
                parts.append(f"  {dst} ~ {src}")
        else:
            parts.append("  (No paths)")
        return "\n".join(parts)
