#!/usr/bin/env python3
"""Clarifier (Consultant Edition): multi-step collaborative design."""

from typing import Dict, Any, List, Tuple
import re
from core.data_loader import DataLoader
from core.model_draft import ModelDraft
from utils.state_manager import SessionState
from interaction.model_confirm import ModelConfirm


class Clarifier:
    """Step-by-step research design discovery."""

    def __init__(self):
        self.data_loader = DataLoader()

    # === Entry Point ===
    def start_clarification(self, session: SessionState) -> str:
        """Begin multi-step clarification after data loaded."""
        # Initialize session fields
        if not getattr(session, 'variables', None):
            session.variables = {}
        if not getattr(session, 'decision_log', None):
            session.decision_log = []
        if not getattr(session, 'hypotheses', None):
            session.hypotheses = []

        session.clarification_step = 0
        df = session.data
        cols = list(df.columns)
        session.available_columns = cols

        msg = [
            "Data loaded successfully ({} rows x {} columns).\n",
            "Let's define your research design together. I'll guide you step by step; you can revise at any time.\n",
            "===========================================",
            "Data Overview",
            f"Sample size: {len(df)}",
            f"Variables: {', '.join(cols)}",
            "===========================================",
            "",
            "**Q1: What is your dependent variable (outcome)?**\n",
            "  This is the variable you most want to explain or predict.\n",
            "Tip: Choose a variable name from the list, e.g., 'grade', 'satisfaction'."
        ]
        session.state = "clarifying_variables"
        return "\n".join(msg)

    # === Main Handler ===
    def handle_clarification(self, session: SessionState, user_input: str) -> str:
        """Process user input based on current step."""
        step = session.clarification_step
        user_input = user_input.strip()

        # Step 0: Dependent variable
        if step == 0:
            return self._step0_dependent(session, user_input)

        # Step 1: Independent variables
        elif step == 1:
            return self._step1_independent(session, user_input)

        # Step 2: Classify variables (latent vs observed)
        elif step == 2:
            return self._step2_classify(session, user_input)

        # Step 3: Define latent indicators
        elif step == 3:
            resp = self._step3_latent_indicators(session, user_input)
            # If in modification mode, jump to confirm after processing
            if getattr(session, 'modifying_component', None) == 'latent':
                draft = self._rebuild_draft(session)
                session.draft = draft
                session.clarification_step = 7
                return ModelConfirm().show_and_confirm(session, "")
            return resp

        # Step 4: Hypothesis / Structural paths
        elif step == 4:
            # First, if we have remaining variables to classify, handle that
            if getattr(session, 'remaining_vars', None):
                return self._handle_remaining_classification(session, user_input)
            resp = self._step4_hypothesis(session, user_input)
            if getattr(session, 'modifying_component', None) == 'paths':
                draft = self._rebuild_draft(session)
                session.draft = draft
                session.clarification_step = 7
                return ModelConfirm().show_and_confirm(session, "")
            return resp

        # Step 5: Missing data handling
        elif step == 5:
            return self._step5_missing(session, user_input)

        # Step 6: Confirmation summary (actually just advance to show summary)
        elif step == 6:
            # This step is reached after missing choice; just show final summary
            return self._step6_confirm(session, user_input)

        return "Unknown step. Please restart."

    # === Step 0: Dependent Variable ===
    def _append_textbook_references(self, session, stage: str, max_refs: int = 2) -> List[str]:
        """Append textbook teaching content for a given stage.
        Returns list of lines with summaries, not just titles.
        """
        retriever = getattr(session, 'textbook_retriever', None)
        if not retriever:
            return []
        try:
            text = retriever.format_teaching_for_stage(stage, max_sections=max_refs,
                                                       include_excerpt=True)
            if text:
                return [text]
            return []
        except Exception:
            return []

    def _step0_dependent(self, session: SessionState, user_input: str) -> str:
        cols = session.available_columns
        matched = None
        for col in cols:
            if col.lower() in user_input.lower():
                matched = col
                break

        if not matched:
            return ("Variable not recognized. Please choose from:\n" +
                    ", ".join(cols) + "\n\nExample: 'grade' or 'satisfaction'")

        session.variables['dependent'] = matched
        session.add_history("dependent_var", matched)
        session.clarification_step = 1

        remaining = [c for c in cols if c != matched]
        msg = [
            f"Dependent variable set: **{matched}**\n",
            "Q2: What are your **independent variables** (predictors)?\n",
            "  You may list multiple, separated by commas.\n",
            f"  Available: {', '.join(remaining)}\n",
            "Example: 'satisfaction, engagement'"
        ]
        # Append textbook references for model specification
        msg.extend(self._append_textbook_references(session, 'model_specification'))
        return "\n".join(msg)

    # === Step 1: Independent Variables ===
    def _step1_independent(self, session: SessionState, user_input: str) -> str:
        # Accept arbitrary names; don't restrict to column names yet.
        names = [n.strip() for n in re.split(r'[,，、\s]+', user_input.strip()) if n.strip()]
        # Deduplicate
        seen = set()
        valid = []
        for n in names:
            if n not in seen:
                seen.add(n)
                valid.append(n)
        if not valid:
            return "No independent variables recognized. Please enter at least one variable name (comma-separated)."

        session.variables['independent'] = valid
        session.add_history("independent_vars", valid)
        session.clarification_step = 2

        msg = [
            f"Independent variables set: {', '.join(valid)}\n",
            "Q3: Classify each variable as **latent** or **observed**.\n",
            "  - Latent: a construct measured by multiple items (e.g., satisfaction = sat1+sat2+sat3)\n",
            "  - Observed: directly measured or single-item indicator\n",
            "Format: variable_name: latent/observed\n",
            "Examples:",
            "  satisfaction: latent",
            "  grade: observed",
            "One per line. All independent variables must be classified."
        ]
        # Append references for variable classification and measurement
        msg.extend(self._append_textbook_references(session, 'measurement_model'))
        return "\n".join(msg)

    # === Step 2: Classify Variables ===
    def _step2_classify(self, session: SessionState, user_input: str) -> str:
        indep = session.variables.get('independent', [])
        lines = [l.strip() for l in user_input.split('\n') if l.strip() and ':' in l]

        classifications = {}
        for line in lines:
            parts = re.split(r'[:：]', line, 1)
            if len(parts) != 2:
                continue
            var, typ = parts[0].strip(), parts[1].strip()
            for orig in indep:
                if var in orig or orig in var:
                    if '潜' in typ or 'latent' in typ.lower():
                        classifications[orig] = 'latent'
                    elif '观' in typ or 'obs' in typ.lower():
                        classifications[orig] = 'observed'
                    break

        missing = [v for v in indep if v not in classifications]
        if missing:
            msg = (f"Please specify the type for: {', '.join(missing)}\n" +
                   "Format: variable_name: latent/observed")
            # Still offer references as user may be confused about classification
            msg += "\n"
            msg += "\n".join(self._append_textbook_references(session, 'measurement_model'))
            return msg

        session.variables['classifications'] = classifications
        session.add_history("variable_classifications", classifications)
        session.clarification_step = 3

        latent_vars = [v for v, t in classifications.items() if t == 'latent']
        if not latent_vars:
            session.clarification_step = 4
            return self._step4_hypothesis(session, "")

        msg = [
            f"Classification complete:\n" +
            "\n".join(f"  {v}: {classifications[v]}" for v in indep) + "\n",
            "Q4: Specify the **observed indicators** for each latent variable.\n",
            "Format: latent_name: item1, item2, ...\n",
            "Examples:",
            "  satisfaction: sat1, sat2, sat3",
            "  engagement: se1, se2",
            "One latent variable per line."
        ]
        # Append measurement model references
        msg.extend(self._append_textbook_references(session, 'measurement_model'))
        return "\n".join(msg)

    # === Step 3: Define Latent Indicators ===
    def _step3_latent_indicators(self, session: SessionState, user_input: str) -> str:
        classifications = session.variables.get('classifications', {})
        # If we are waiting for remaining variable classification, handle that first
        if getattr(session, "remaining_vars", None):
            return self._handle_remaining_classification(session, user_input)

        latent_names = [v for v, t in classifications.items() if t == 'latent']
        all_cols = set(session.available_columns)

        lines = [l.strip() for l in user_input.split('\n') if l.strip() and ':' in l]
        defined = {}
        for line in lines:
            parts = re.split(r'[:：]', line, 1)
            if len(parts) != 2:
                continue
            name, items_str = parts[0].strip(), parts[1].strip()
            matched_name = None
            for ln in latent_names:
                if name in ln or ln in name:
                    matched_name = ln
                    break
            if not matched_name:
                continue
            items = [i.strip() for i in re.split(r'[,，、\s]+', items_str) if i.strip()]
            valid_items = [i for i in items if i in all_cols]
            if valid_items:
                defined[matched_name] = valid_items

        missing_latent = [n for n in latent_names if n not in defined]
        if missing_latent:
            return (f"Please provide indicators for: {', '.join(missing_latent)}\n" +
                    "Format: variable_name: item1, item2")

        # Save
        session.variables['latent_indicators'] = defined
        session.add_history("latent_indicators", defined)
        session.clarification_step = 4

        msg = ["Latent variable definitions complete:"]
        for lv, items in defined.items():
            msg.append(f"  {lv} =~ {', '.join(items)}")
        msg.append("")

        # Compute which columns are actually used in the model so far
        all_defined_vars = set()
        all_defined_vars.update(session.variables.get('dependent', []))
        all_defined_vars.update(session.variables.get('independent', []))
        # Also add all indicator items from latent constructs
        for items in defined.values():
            all_defined_vars.update(items)
        remaining = [c for c in all_cols if c not in all_defined_vars]
        if remaining:
            session.remaining_vars = remaining
            msg.append(f"Remaining unused variables: {', '.join(remaining)}\n")
            msg.append("How would you like to handle these variables?")
            msg.append("Format: variable_name: observed/covariate")
            msg.append("Example: gender: covariate")
            msg.append("One per line, or type 'done' to skip.")
            # stay in clarifying_variables
            return "\n".join(msg)
        else:
            response = self._step4_hypothesis(session, "")
            # measurement model references already added after latent indicators, now add structural
            # But _step4_hypothesis already appends its own refs, so we just return the response
            return response

    # === Step 4: Hypothesis / Structural paths ===
    def _step4_hypothesis(self, session: SessionState, user_input: str) -> str:
        classifications = session.variables.get('classifications', {})
        latent_inds = session.variables.get('latent_indicators', {})
        deps = [session.variables.get('dependent')]
        indeps = session.variables.get('independent', [])

        # Initialize suggested paths if not yet
        if not hasattr(session, 'suggested_paths') or session.suggested_paths is None:
            session.suggested_paths = [(src, deps[0]) for src in indeps if src != deps[0]]

        text = user_input.strip()

        # Confirm paths
        if text in ("确认", "confirm"):
            session.add_history("paths_confirmed", session.suggested_paths)
            session.clarification_step = 5
            return self._step5_missing(session, "")

        # Process modifications
        added, deleted = [], []
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        rewrite = False

        for line in lines:
            if line.startswith(("增加:", "添加:", "增加：", "添加：", "add:")):
                expr = line.split(":", 1)[1].strip() if ":" in line else line.split("：", 1)[1].strip()
                arrow = "→" if "→" in expr else "->" if "->" in expr else None
                if arrow:
                    src, dst = [p.strip() for p in expr.split(arrow)]
                    pair = (src, dst)
                    if pair not in session.suggested_paths:
                        session.suggested_paths.append(pair)
                        added.append(pair)
                continue
            if line.startswith(("删除:", "删除：", "remove:")):
                expr = line.split(":", 1)[1].strip() if ":" in line else line.split("：", 1)[1].strip()
                arrow = "→" if "→" in expr else "->" if "->" in expr else None
                if arrow:
                    src, dst = [p.strip() for p in expr.split(arrow)]
                    pair = (src, dst)
                    if pair in session.suggested_paths:
                        session.suggested_paths.remove(pair)
                        deleted.append(pair)
                continue
            if ("→" in line or "->" in line) and not line.startswith(("增加", "删除", "add", "remove")):
                rewrite = True

        if rewrite:
            news = []
            for line in lines:
                if ("→" in line or "->" in line) and not line.startswith(("增加", "删除", "add", "remove")):
                    arrow = "→" if "→" in line else "->"
                    src, dst = [p.strip() for p in line.split(arrow)]
                    if src and dst:
                        news.append((src, dst))
            if news:
                session.suggested_paths = news
                added = news
                deleted = []

        if added or deleted:
            session.add_history("paths_modified", {"added": added, "deleted": deleted})

        msg = ["Current structural paths:"]
        if session.suggested_paths:
            for src, dst in session.suggested_paths:
                msg.append(f"  {src} → {dst}")
        else:
            msg.append("  (No paths defined)")
        msg.append("")
        msg.append("Choose an action:")
        msg.append("  - Type 'confirm' to finalize paths")
        msg.append("  - Type 'add: X -> Y' or 'remove: X -> Y' to adjust")
        msg.append("  - Or enter a new path list (one X -> Y per line) to overwrite")
        # Append references for structural model
        msg.extend(self._append_textbook_references(session, 'structural_model'))
        return "\n".join(msg)

    # === Step 5: Missing data handling ===
    def _step5_missing(self, session: SessionState, user_input: str) -> str:
        if not user_input.strip():
            df = session.data
            missing_info = []
            for col in df.columns:
                pct = df[col].isna().mean() * 100
                if pct > 0:
                    missing_info.append(f"{col}: {pct:.1f}%")
            summary = "No missing values detected" if not missing_info else "Missing values:\n  " + "\n  ".join(missing_info)
            draft = ModelDraft()
            self._apply_definitions_to_draft(session, draft)
            n_params = self._estimate_params(draft)
            n_obs = len(df)
            msg = [
                f"{summary}\n",
                "Sample size and parameters:",
                f"  Sample size N = {n_obs}",
                f"  Estimated parameters ~ {n_params}",
                ""
            ]
            if n_obs < n_params * 2:
                msg.append("Warning: Sample size is relatively small. Results may be unstable. Consider simplifying the model or increasing sample size.\n")
            else:
                msg.append("Sample size is adequate.\n")
            msg.extend([
                "Choose a missing data handling method:",
                "  1) FIML (Full Information Maximum Likelihood) - recommended",
                "  2) Listwise deletion",
                "  3) Mean imputation",
                "",
                "Reply with 1/2/3, or type 'default' to use recommended (1)."
            ])
            session.clarification_step = 5
            msg.append("")
            # Append references for missing data handling
            msg.extend(self._append_textbook_references(session, 'data_preparation'))
            return "\n".join(msg)

        choice = user_input.strip()
        methods = {'1': 'FIML', '2': 'listwise', '3': 'impute'}
        session.missing_handling = methods.get(choice, 'FIML')
        session.add_history("missing_handling", session.missing_handling)
        session.clarification_step = 6
        return self._step6_confirm(session, "")

    # === Step 6: Confirmation summary ===
    def _step6_confirm(self, session: SessionState, user_input: str) -> str:
        # Build final draft
        draft = ModelDraft()
        self._apply_definitions_to_draft(session, draft)
        session.draft = draft
        session.add_history("model_draft_created", True)
        session.clarification_step = 7
        # Delegate to ModelConfirm for consistent presentation and state management
        return ModelConfirm().show_and_confirm(session, "")

    # === Helpers ===
    def _apply_definitions_to_draft(self, session: SessionState, draft: ModelDraft):
        latent_inds = session.variables.get('latent_indicators', {})
        for lv, items in latent_inds.items():
            draft.add_latent(lv, items)

        classifications = session.variables.get('classifications', {})
        observed = [v for v, t in classifications.items() if t == 'observed']
        dep = session.variables.get('dependent')
        if dep and classifications.get(dep) != 'latent' and dep not in observed:
            observed.append(dep)
        if observed:
            # Dedup while preserving order
            seen = set()
            uniq = []
            for v in observed:
                if v not in seen:
                    seen.add(v)
                    uniq.append(v)
            draft.observed = uniq

        remaining_class = getattr(session, 'remaining_classification', {})
        for var, role in remaining_class.items():
            if role == 'covariate':
                draft.add_covariate(var)
            elif role == 'observed':
                # Add to observed if not already present
                if var not in draft.observed:
                    draft.observed.append(var)

        paths = getattr(session, 'suggested_paths', [])
        for src, dst in paths:
            try:
                draft.add_path(src, dst)
            except:
                pass

    def _estimate_params(self, draft: ModelDraft) -> int:
        count = 0
        for lv, info in draft.latent.items():
            count += len(info["items"]) - 1
        count += len(draft.paths)
        n_latent = len(draft.latent)
        count += n_latent
        if n_latent > 1:
            count += n_latent * (n_latent - 1) // 2
        count += sum(len(info["items"]) for info in draft.latent.values())
        count += len(draft.observed) + len(draft.covariates)
        return max(count, 1)



    # === Modification Support ===
    def start_latent_modification(self, session: SessionState) -> str:
        session.modifying_component = "latent"
        session.clarification_step = 3
        if not hasattr(session, 'available_columns'):
            session.available_columns = list(session.data.columns)
        return self._step3_latent_indicators(session, "")

    def start_path_modification(self, session: SessionState) -> str:
        session.modifying_component = "paths"
        session.clarification_step = 4
        if not hasattr(session, 'available_columns'):
            session.available_columns = list(session.data.columns)
        return self._step4_hypothesis(session, "")

    def _rebuild_draft(self, session: SessionState) -> ModelDraft:
        """Rebuild ModelDraft from session.variables."""
        draft = ModelDraft()
        latent_inds = session.variables.get('latent_indicators', {})
        for lv, items in latent_inds.items():
            draft.add_latent(lv, items)

        classifications = session.variables.get('classifications', {})
        observed = [v for v, t in classifications.items() if t == 'observed']
        dep = session.variables.get('dependent')
        if dep and classifications.get(dep) != 'latent' and dep not in observed:
            observed.append(dep)
        if observed:
            seen = set()
            uniq = []
            for v in observed:
                if v not in seen:
                    seen.add(v)
                    uniq.append(v)
            draft.observed = uniq

        remaining_class = getattr(session, 'remaining_classification', {})
        for var, role in remaining_class.items():
            if role == 'covariate':
                draft.add_covariate(var)
            elif role == 'observed':
                if var not in draft.observed:
                    draft.observed.append(var)

        paths = getattr(session, 'suggested_paths', [])
        for src, dst in paths:
            try:
                draft.add_path(src, dst)
            except:
                pass
        return draft

    # === Legacy compatibility ===
    def _handle_remaining_classification(self, session: SessionState, user_input: str) -> str:
        """Process classification of remaining unused variables."""
        remaining = getattr(session, 'remaining_vars', [])
        if not remaining:
            return self._step4_hypothesis(session, user_input)

        lines = [l.strip() for l in user_input.split('\n') if l.strip() and ':' in l]
        classification = {}
        for line in lines:
            parts = re.split(r'[:：]', line, 1)
            if len(parts) != 2:
                continue
            var, role = parts[0].strip(), parts[1].strip()
            if var in remaining:
                if '观测' in role or 'observed' in role.lower():
                    classification[var] = 'observed'
                elif '控制' in role or 'covariate' in role.lower():
                    classification[var] = 'covariate'
        # Save
        if not hasattr(session, 'remaining_classification'):
            session.remaining_classification = {}
        session.remaining_classification.update(classification)
        session.add_history('remaining_classified', classification)
        # Clear remaining flag
        session.remaining_vars = None
        # Advance to next step
        session.clarification_step = 4
        return self._step4_hypothesis(session, "")

    def collect_hypothesis(self, session: SessionState, user_text: str) -> str:
        return self.start_clarification(session)

    def define_latent_vars(self, session: SessionState, user_input: str) -> str:
        return self.handle_clarification(session, user_input)

    def classify_remaining(self, session: SessionState, user_input: str) -> str:
        # This is called from entry's legacy path? We'll map to appropriate step.
        # Assuming after initial latent def we ask remaining classification, step 3 leads to step 4 eventually.
        # For compatibility, just dispatch
        return self.handle_clarification(session, user_input)

    def define_paths(self, session: SessionState, user_input: str) -> str:
        return self.handle_clarification(session, user_input)
