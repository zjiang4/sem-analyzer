#!/usr/bin/env python3
"""Followup processor: handles commands after model is confirmed."""

import os
import pandas as pd
from typing import Dict, Any, Tuple, Optional, List
from core.sem_fitter import SemFitter
from core.result_saver import ResultSaver
from visualization.dot_generator import DotGenerator
from interaction.report_formatter import ReportFormatter
import numpy as np

try:
    from scipy.stats import ks_2samp
    _HAS_SCIPY = True
except ImportError:
    _HAS_SCIPY = False

# Debug mode control via environment variable
DEBUG = os.getenv('SEM_ANALYZER_DEBUG', '').lower() in ('1', 'true', 'yes')

def _debug_write(filename: str, content: str):
    """Write debug information only if DEBUG mode is enabled."""
    if DEBUG:
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception:
            pass


class FollowupProcessor:
    """Handles post-confirmation commands."""

    def __init__(self):
        self.fitter = SemFitter()
        self.saver = ResultSaver()
        self.dot_gen = DotGenerator()
        self.reporter = ReportFormatter()

    def handle(self, session, command: str) -> str:
        """Process a follow-up command."""
        cmd = command.strip().lower()

        # Multigroup state machine: metric/scalar progression
        mg = getattr(session, 'multigroup_results', None)
        if mg and mg.get('current_level') in ('configural', 'metric'):
            if cmd in ('metric', 'scalar'):
                return self._fit_advanced(session, 'multigroup', command)

        # Fit command - detect if advanced model requested
        if cmd in ["拟合", "fit", "开始拟合", "运行模型", "run model"] or "增长" in cmd or "growth" in cmd or "trajectory" in cmd or "多组" in cmd or "multigroup" in cmd or "invariance" in cmd or "中介" in cmd or "mediation" in cmd:
            # Check if the command indicates an advanced model
            advanced_type = self._detect_advanced_type(command)
            if advanced_type:
                return self._fit_advanced(session, advanced_type, command)
            else:
                return self._fit_model(session)

        # Add path
        if "增加" in cmd or "添加" in cmd or "add" in cmd:
            return self._add_path(session, command)

        # Remove path
        if "删除" in cmd or "remove" in cmd:
            return self._remove_path(session, command)

        # Change missing method
        if "缺失" in cmd or "missing" in cmd:
            return self._change_missing(session, command)

        # Calculate indirect effect
        if "间接" in cmd or "indirect" in cmd:
            return self._calc_indirect(session, command)

        # Export report
        if "导出" in cmd or "生成报告" in cmd or "report" in cmd or "export" in cmd:
            return self._export_report(session, command)

        # Show diagram
        if "图" in cmd or "diagram" in cmd or "plot" in cmd:
            return self._generate_diagram(session)

        # Show results
        if "结果" in cmd or "results" in cmd or "show results" in cmd:
            return self._show_results(session)

        return "Unknown command. Available: fit / add path / remove path / export report / results / diagram"

    def _detect_advanced_type(self, command: str) -> Optional[str]:
        """Detect if command requests an advanced model."""
        cmd_lower = command.lower()
        if "增长" in cmd_lower or "growth" in cmd_lower or "trajectory" in cmd_lower or "latent growth" in cmd_lower:
            return "growth"
        if "中介" in cmd_lower or "mediation" in cmd_lower or "indirect" in cmd_lower:
            return "mediation"
        if "多组" in cmd_lower or "multigroup" in cmd_lower or "invariance" in cmd_lower:
            return "multigroup"
        if "cfa" in cmd_lower or "验证性因子" in cmd_lower or "confirmatory factor" in cmd_lower:
            return "cfa"
        return None

    def _fit_model(self, session) -> str:
        """Fit the current draft model and provide textbook references."""
        try:
            df = session.data
            draft = session.draft
            # Debug: log draft (conditional)
            _debug_write('debug_draft.txt', str(draft.__dict__))
            # Validate parameters
            n_obs = len(df)
            n_params = self._estimate_params(draft)
            if n_obs < n_params * 2:
                warning = (f"Warning: Sample size N={n_obs} is small relative to parameters (~{n_params}). "
                           "Results may be unstable. Consider increasing sample size or simplifying the model.")
            else:
                warning = ""

            # Perform fit
            results = self.fitter.fit(df, draft)

            # Save results to session
            session.results = results
            session.add_history("model_fitted", True)

            # Build response
            fit = results.get("fit_indices", {})
            lines = [
                "Model fitting complete!",
                "",
                "Fit indices:",
                f"  χ²({fit.get('df','?')}) = {fit.get('chi2',0):.2f}, p = {fit.get('p_value',0):.3f}",
                f"  CFI = {fit.get('cfi',0):.3f}, TLI = {fit.get('tli',0):.3f}",
                f"  RMSEA = {fit.get('rmsea',0):.3f}, SRMR = {fit.get('srmr',0):.3f}",
                "",
                "Key path coefficients:"
            ]

            # Summarize significant paths
            paths = results.get("paths", {})
            for (src, dst), stats in list(paths.items())[:10]:
                beta = stats.get("estimate", 0)
                p = stats.get("p")
                if p is None:
                    sig = ""
                else:
                    sig = "***" if p < 0.001 else ("**" if p < 0.01 else ("*" if p < 0.05 else ""))
                beta_str = f"{beta:.3f}" if beta is not None else "N/A"
                p_str = f"{p:.3f}" if p is not None else "N/A"
                lines.append(f"  {src} → {dst}: β={beta_str}, p={p_str} {sig}")

            if warning:
                lines.append("")
                lines.append(f"WARNING: {warning}")

            # Add textbook references based on fit quality
            retriever = getattr(session, 'textbook_retriever', None)
            if retriever:
                lines.append("")
                cfi = fit.get('cfi', 0)
                rmsea = fit.get('rmsea', 1)
                if cfi < 0.9 or rmsea > 0.08:
                    lines.append("Fit indices below ideal thresholds. Recommended reading:")
                    teaching = retriever.format_teaching_for_stage('model_modification', max_sections=2)
                else:
                    lines.append("Good fit. Recommended reading for interpretation and reporting:")
                    teaching = retriever.format_teaching_for_stage('reporting', max_sections=2)
                if teaching:
                    lines.append(teaching)

            lines.extend([
                "",
                "Next steps:",
                "  - Type 'export report' for full Word/PDF",
                "  - Type 'diagram' for path diagram (DOT)",
                "  - Type 'results' for full coefficient table",
                "  - Type 'bootstrap' for indirect effect CI",
                "  - Type 'multigroup <var>' for cross-group comparison"
            ])

            return "\n".join(lines)

        except Exception as e:
            import traceback
            error_text = f"Exception: {e}\n" + traceback.format_exc()
            _debug_write('fitmodel_exception.txt', error_text)
            return f"Fitting failed: {str(e)}\nPlease check model specification or data quality."

    def _estimate_params(self, draft) -> int:
        """Rough estimate of free parameters."""
        count = 0
        # Factor loadings (one per item, minus one fixed per factor)
        for lv, info in draft.latent.items():
            count += len(info["items"]) - 1  # one loading fixed to 1 for scaling
        # Path coefficients
        count += len(draft.paths)
        # Variances/covariances of latent variables and disturbances
        # Simplistic: number of latent vars squared /2?
        n_latent = len(draft.latent)
        count += n_latent  # variances
        if n_latent > 1:
            count += n_latent * (n_latent - 1) // 2  # covariances
        # Error variances for observed indicators
        count += sum(len(info["items"]) for info in draft.latent.values())
        # Plus observed vars' variances if not included in latent
        count += len(draft.observed) + len(draft.covariates)
        return max(count, 1)

    # === Advanced Model Fitting ===
    def _fit_advanced(self, session, model_type: str, command: str) -> str:
        """Fit advanced SEM models (growth, mediation, multigroup, CFA)."""
        try:
            # Ensure advanced_fitter is available
            fitter = getattr(session, 'advanced_fitter', None)
            if not fitter:
                return "Advanced analysis engine not ready. Please contact administrator."

            # Dispatch to model-specific builder
            user_vars, error = self._build_advanced_vars(session, model_type, command)
            if error:
                return error

            # Prepare options
            options = {
                'bootstrap': 'bootstrap' in command.lower() or 'ci' in command.lower()
            }
            # Extract invariance for multigroup
            if model_type == 'multigroup':
                invariance = user_vars.pop('invariance', 'configural')
                options['invariance'] = invariance
            # Perform fit
            result = fitter.fit(session.data, model_type, user_vars, options=options)

            # Save to session
            if not hasattr(session, 'advanced_results') or session.advanced_results is None:
                session.advanced_results = {}
            session.advanced_results[model_type] = result
            session.add_history(f"advanced_{model_type}", True)

            # Format result with textbook refs and guidance
            response = self._format_advanced_result(result, model_type, session=session)
            return response

        except Exception as e:
            return f"Advanced analysis failed: {str(e)}\nPlease check parameter settings or data format."

    def _build_advanced_vars(self, session, model_type: str, command: str) -> Tuple[Dict, Optional[str]]:
        """Construct user_vars dict for the template based on session info and command.
        Returns (user_vars, error_message)."""
        data_cols = list(session.data.columns)
        user_vars = {}

        if model_type == 'cfa':
            latent_inds = session.variables.get('latent_indicators', {})
            if not latent_inds:
                return {}, "Please define at least one latent variable first."
            user_vars = {'latent': latent_inds, 'observed': []}
            return user_vars, None

        elif model_type == 'growth':
            repeated = self._detect_time_series_vars(data_cols)
            if not repeated:
                return {}, "No time-point items detected. Ensure columns follow patterns like sat_t1, sat_t2 or prefix+number (e.g., se1, se2, se3)."
            # Parse optional time loadings from command
            time_loadings = self._parse_time_loadings(command, repeated)
            if time_loadings is None:
                time_loadings = list(range(len(repeated)))
            user_vars = {'items': repeated, 'time_loadings': time_loadings}
            return user_vars, None

        elif model_type == 'mediation':
            paths = getattr(session, 'suggested_paths', [])
            if len(paths) < 2:
                return {}, "At least two structural paths (e.g., X->M, M->Y) are needed for a mediation chain."
            chain = self._infer_mediation_chain(paths, session)
            if not chain:
                # Attempt explicit command extraction: '中介 X M Y'
                parts = command.strip().split()
                if len(parts) >= 4 and parts[0] in ['中介', 'mediation']:
                    x, m, y = parts[1], parts[2], parts[3]
                    user_vars = {'cause': [x], 'mediator': [m], 'outcome': [y]}
                    return user_vars, None
                return {}, "Cannot infer mediation chain from current paths. Define X->M and M->Y, or specify explicitly: 'mediation X M Y'."
            x, m, y = chain
            user_vars = {'cause': [x], 'mediator': [m], 'outcome': [y]}
            return user_vars, None

        elif model_type == 'multigroup':
            parts = command.strip().split()
            explicit_var = None
            for tok in parts:
                if tok in session.data.columns:
                    explicit_var = tok
                    break
            if not explicit_var:
                explicit_var = getattr(session, 'multigroup_var', None)
            if not explicit_var:
                group_vars = self._suggest_grouping_vars(session)
                if not group_vars:
                    return {}, "No grouping variables found. Ensure the data contains categorical variables (e.g., gender, group)."
                explicit_var = group_vars[0]
            # Store chosen group in session for multi-step invariance testing
            session.multigroup_var = explicit_var
            # Build base user_vars (no invariance yet; configural will be first step)
            draft = session.draft
            user_vars = {
                'latent': draft.latent,
                'observed': draft.observed,
                'paths': draft.paths,
                'group': explicit_var
            }
            # Check if we are continuing with a higher invariance level
            # (state machine: if session already has 'multigroup_results' dict)
            if hasattr(session, 'multigroup_results') and session.multigroup_results is not None:
                # User is requesting next level, parse invariance from command
                if 'metric' in command.lower():
                    invariance = 'metric'
                elif 'scalar' in command.lower():
                    invariance = 'scalar'
                else:
                    # Default to next level
                    levels = ['configural', 'metric', 'scalar']
                    current = session.multigroup_results.get('current_level', 'configural')
                    try:
                        idx = levels.index(current)
                        invariance = levels[idx+1]
                    except:
                        invariance = 'metric'
                user_vars['invariance'] = invariance
                session.multigroup_results['current_level'] = invariance
            else:
                # First time: start with configural
                user_vars['invariance'] = 'configural'
                session.multigroup_results = {'current_level': 'configural'}
            session.invariance_level = user_vars['invariance']
            return user_vars, None

        return {}, f"Unknown advanced analysis type: {model_type}"

    def _format_advanced_result(self, result, model_type: str, session=None) -> str:
        """Format result with explanations, textbook references, and multigroup guidance."""
        lines = [f"{model_type.upper()} analysis complete!\n"]

        fit = result.fit_stats
        lines.append("Fit indices:")
        lines.append(f"  CFI = {fit.get('cfi',0):.3f}, TLI = {fit.get('tli',0):.3f}")
        lines.append(f"  RMSEA = {fit.get('rmsea',0):.3f}, SRMR = {fit.get('srmr',0):.3f}")
        lines.append(f"  χ²({fit.get('df','?')}) = {fit.get('chi2',0):.2f}, p = {fit.get('p_value',0):.3f}")

        # Parameters
        lines.append("\nParameter estimates:")
        params = result.parameters
        if isinstance(params, pd.DataFrame):
            for _, row in params.head(10).iterrows():
                est = row.get('estimate', 0)
                p_val = row.get('p', 1)
                est_s = f"{est:.3f}" if isinstance(est, (int, float, np.floating)) else str(est)
                p_s = f"{p_val:.3f}" if isinstance(p_val, (int, float, np.floating)) else str(p_val)
                lines.append(f"  {row.get('path','?')}: β={est_s}, p={p_s}")
        else:
            lines.append("  (See full report)")

        # Model-specific explanations
        if model_type == 'growth':
            lines.append("\nLatent Growth Model notes:")
            lines.append("  Intercept and slope means and variances have been estimated.")
        elif model_type == 'mediation':
            lines.append("\nMediation effects:")
            lines.append("  Use Bootstrap CI to judge indirect effect significance (significant if CI excludes 0).")
            if result.bootstrap_ci:
                for path, (lo, up) in list(result.bootstrap_ci.items())[:5]:
                    lines.append(f"  {path}: 95% CI [{lo:.3f}, {up:.3f}]")

        # Multigroup-specific: show guidance and comparison
        if model_type == 'multigroup' and session is not None:
            mg_results = getattr(session, 'multigroup_results', None)
            if mg_results:
                current = mg_results.get('current_level', 'configural')
                lines.append(f"\nMultigroup analysis - {current} invariance")
                if current == 'configural':
                    lines.append("  Baseline: same measurement structure, parameters freely estimated (no constraints).")
                    lines.append("\n  You can also test stricter invariance:")
                    lines.append("  - Metric: constrain factor loadings equal across groups")
                    lines.append("  - Scalar: constrain both loadings and intercepts equal")
                    lines.append("\n  Reply 'metric' or 'scalar' to proceed.")
                elif current == 'metric':
                    lines.append("  Factor loadings constrained equal.")
                    lines.append("\n  Test scalar invariance (add intercept constraints)? Reply 'scalar'.")
                elif current == 'scalar':
                    lines.append("  Loadings and intercepts constrained. Invariance testing complete.")

                # Show comparison of fit indices across levels if available
                fits = mg_results.get('fits', {})
                if len(fits) > 1:
                    lines.append("\nFit index comparison (dCFI < -0.01 or dRMSEA > 0.015 suggests invariance not supported):")
                    table = "| Level | CFI | RMSEA |\n|------|-----|-------|"
                    for level in ['configural', 'metric', 'scalar']:
                        if level in fits:
                            cf = fits[level].get('cfi', '?')
                            rm = fits[level].get('rmsea', '?')
                            cf_str = f"{cf:.3f}" if isinstance(cf, (int,float)) else str(cf)
                            rm_str = f"{rm:.3f}" if isinstance(rm, (int,float)) else str(rm)
                            table += f"\n| {level} | {cf_str} | {rm_str} |"
                    lines.append(table)

        # Textbook references
        retriever = getattr(session, 'textbook_retriever', None)
        if retriever:
            lines.append("\nRelevant textbook chapters:")
            stage_map = {
                'cfa': 'measurement_model',
                'growth': 'growth_modeling',
                'mediation': 'structural_model',
                'multigroup': 'multigroup_analysis'
            }
            stage = stage_map.get(model_type, 'model_fitting')
            teaching = retriever.format_teaching_for_stage(stage, max_sections=2)
            if teaching:
                lines.append(teaching)

        lines.extend([
            "",
            "Next steps:",
            "  - Type 'results' for full parameter table",
            "  - Type 'export report' to save analysis results"
        ])
        return "\n".join(lines)

    def _add_path(self, session, command: str) -> str:
        """Add a structural path."""
        # Extract after '增加' or 'add'
        arrow = "→" if "→" in command else "->" if "->" in command else None
        if not arrow:
            return "Specify the path to add, e.g., 'add: satisfaction -> grade'"

        try:
            parts = command.split(arrow)
            if len(parts) != 2:
                return "Format error. Use 'add: X -> Y'"
            src = parts[0].split(":")[-1].strip()
            dst = parts[1].strip()
            session.draft.add_path(src, dst)
            return f"Path added: {src} -> {dst}\n\nType 'fit' to re-run the model."
        except Exception as e:
            return f"Add failed: {e}"

    def _remove_path(self, session, command: str) -> str:
        """Remove a structural path."""
        arrow = "→" if "→" in command else "->" if "->" in command else None
        if not arrow:
            return "Specify the path to remove, e.g., 'remove: satisfaction -> grade'"

        try:
            parts = command.split(arrow)
            src = parts[0].split(":")[-1].strip()
            dst = parts[1].strip()
            session.draft.remove_path(src, dst)
            return f"Path removed: {src} -> {dst}\n\nType 'fit' to re-run the model."
        except Exception as e:
            return f"Remove failed: {e}"

    def _change_missing(self, session, command: str) -> str:
        """Change missing data handling (future implementation)."""
        return "Missing data handling change not yet implemented. Currently using default (FIML)."

    def _calc_indirect(self, session, command: str) -> str:
        """Calculate indirect effect for a given mediator chain."""
        # Requires results and paths
        if not session.results:
            return "Please fit the model first."
        try:
            # Simple example: X -> M -> Y
            # Need to parse user command to get X, M, Y
            return "Indirect effect calculation is under development."
        except Exception as e:
            return f"Calculation failed: {e}"

    def _export_report(self, session, command: str) -> str:
        """Export report to file."""
        try:
            # Determine format
            if "word" in command or "docx" in command:
                filepath = "sem_report.docx"
                # Generate directly to docx
                result_path = self.reporter.generate(session, output_path=filepath, format='docx')
                # Also generate md version for convenience
                md_path = filepath.replace('.docx', '.md')
                self.reporter.generate(session, output_path=md_path, format='md')
                return f"Report saved as Word document: {result_path}\n(Markdown also generated: {md_path})"
            else:
                filepath = "sem_report.md"
                md_text = self.reporter.generate(session, output_path=filepath, format='md')

                # Append textbook references for reporting stage
                retriever = getattr(session, 'textbook_retriever', None)
                if retriever:
                    teaching = retriever.format_teaching_for_stage('reporting', max_sections=2)
                    if teaching:
                        extra = ["\nRelevant textbook chapters for report writing:"]
                        extra.append(teaching)
                        with open(filepath, 'a', encoding='utf-8') as f:
                            f.write("\n".join(extra))
                        md_text += "\n".join(extra)

                return f"Report saved to {filepath}\n\nContent preview:\n" + md_text[:500] + "..."
        except Exception as e:
            import traceback
            traceback.print_exc()
            return f"Report generation failed: {e}"

    def _generate_diagram(self, session) -> str:
        """Generate model diagram."""
        try:
            dot_code = self.dot_gen.generate(session.draft)
            filepath = "model_diagram.dot"
            self.dot_gen.save(session.draft, filepath)
            return (f"Diagram DOT code saved to {filepath}\n\n"
                    f"Use Graphviz to render: `dot -Tpng {filepath} -o model.png`\n\n"
                    f"Preview (DOT):\n```\n{dot_code[:300]}...\n```")
        except Exception as e:
            return f"Diagram generation failed: {e}"

    def _detect_time_series_vars(self, cols: List[str]) -> List[str]:
        """Detect variables that look like repeated measures across time."""
        patterns = [
            ('t1', 't2', 't3', 't4', 't5'),
            ('time1', 'time2', 'time3'),
            ('wave1', 'wave2', 'wave3'),
            ('_t1', '_t2', '_t3'),
            ('-t1', '-t2', '-t3')
        ]
        # Also detect numeric suffixes
        candidates = []
        for col in cols:
            col_low = col.lower()
            # Check against known patterns
            for pat in patterns:
                if any(p in col_low for p in pat):
                    candidates.append(col)
                    break
        # If none found via patterns, try to find groups with same prefix ending with digit
        if not candidates:
            import re
            prefix_map = {}
            for col in cols:
                m = re.match(r'^([a-zA-Z]+)_?(\d+)$', col)
                if m:
                    prefix, num = m.group(1).lower(), m.group(2)
                    prefix_map.setdefault(prefix, []).append(col)
            for prefix, items in prefix_map.items():
                if len(items) >= 2:
                    # Sort by numeric suffix
                    try:
                        sorted_items = sorted(items, key=lambda x: int(re.search(r'(\d+)', x).group(1)))
                        candidates.extend(sorted_items)
                    except:
                        pass
        # Deduplicate while preserving order
        seen = set()
        result = []
        for c in candidates:
            if c not in seen:
                seen.add(c)
                result.append(c)
        return result

    def _infer_mediation_chain(self, paths: List[Tuple[str, str]], session=None) -> Optional[Tuple[str, str, str]]:
        """Find a chain X -> M -> Y from list of (src, dst) pairs."""
        graph = {}
        for src, dst in paths:
            graph.setdefault(src, []).append(dst)
        for src, dsts in graph.items():
            for dst in dsts:
                if dst in graph:
                    chain = (src, dst, graph[dst][0])
                    if session is not None:
                        _, is_mediation = self._compute_jsd_mediation(
                            session, chain[0], chain[1], chain[2])
                        if is_mediation:
                            return chain
                    else:
                        return chain
        return None

    def _compute_jsd_mediation(self, session, cause, mediator, outcome) -> Tuple[float, bool]:
        """Sobel test for indirect effect X -> M -> Y.

        Returns (z_statistic, is_significant) where is_significant means
        |z| > 1.96 (p < .05 two-tailed).  Uses OLS to estimate path a
        (X -> M) and path b (M -> Y controlling for X), then applies the
        Sobel (1982) product-of-coefficients standard error.
        """
        df = session.data
        if cause not in df.columns or outcome not in df.columns or mediator not in df.columns:
            return (0.0, False)
        try:
            vals = df[[cause, mediator, outcome]].dropna()
            n = len(vals)
            if n < 20:
                return (0.0, False)
            X = vals[cause].values
            M = vals[mediator].values
            Y = vals[outcome].values
            Xc = X - X.mean()
            X_with_c = np.column_stack([np.ones(n), X])
            a_coef = np.linalg.lstsq(X_with_c, M, rcond=None)[0]
            a = a_coef[1]
            M_hat = X_with_c @ a_coef
            se_a = np.sqrt(np.sum((M - M_hat) ** 2) / (n - 2)) / np.sqrt(np.sum(Xc ** 2))
            XM_with_c = np.column_stack([np.ones(n), X, M])
            b_coef = np.linalg.lstsq(XM_with_c, Y, rcond=None)[0]
            b = b_coef[2]
            Y_hat = XM_with_c @ b_coef
            mse = np.sum((Y - Y_hat) ** 2) / (n - 3)
            xtx_inv = np.linalg.inv(XM_with_c.T @ XM_with_c)
            se_b = np.sqrt(mse * xtx_inv[2, 2])
            indirect = a * b
            se_sobel = np.sqrt(b ** 2 * se_a ** 2 + a ** 2 * se_b ** 2)
            if se_sobel < 1e-10:
                return (0.0, False)
            z_sobel = indirect / se_sobel
            return (float(z_sobel), abs(z_sobel) > 1.96)
        except Exception:
            return (0.0, False)

    def _ks_test_grouping(self, session, candidate_var) -> Tuple[int, int, bool]:
        df = session.data
        if candidate_var not in df.columns:
            return (0, 0, False)
        try:
            groups = df[candidate_var].dropna().unique()
            if len(groups) < 2:
                return (0, 0, False)
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            numeric_cols = [c for c in numeric_cols if c != candidate_var]
            if not numeric_cols:
                return (0, 0, False)
            significant_count = 0
            total_tests = 0
            group_list = list(groups)
            for i in range(len(group_list)):
                for j in range(i + 1, len(group_list)):
                    g1 = df[df[candidate_var] == group_list[i]]
                    g2 = df[df[candidate_var] == group_list[j]]
                    for col in numeric_cols:
                        vals1 = g1[col].dropna().values
                        vals2 = g2[col].dropna().values
                        if len(vals1) < 5 or len(vals2) < 5:
                            continue
                        total_tests += 1
                        stat, p_val = ks_2samp(vals1, vals2)
                        if p_val < 0.05:
                            significant_count += 1
            is_recommended = significant_count > 0 and total_tests > 0
            return (significant_count, total_tests, is_recommended)
        except Exception:
            return (0, 0, False)

    def _suggest_grouping_vars(self, session) -> List[str]:
        """Suggest possible grouping (categorical) variables."""
        df = session.data
        cols = list(df.columns)
        used = set()
        for inds in session.variables.get('latent_indicators', {}).values():
            used.update(inds)
        used.update(session.variables.get('independent', []))
        dep = session.variables.get('dependent')
        if dep:
            used.add(dep)
        if hasattr(session, 'draft'):
            used.update(session.draft.observed)
            used.update(session.draft.covariates)
        remaining = [c for c in cols if c not in used]
        group_candidates = []
        for col in remaining:
            try:
                nuni = df[col].nunique()
                if 2 <= nuni <= 5:
                    group_candidates.append(col)
            except:
                pass
        if _HAS_SCIPY:
            scored = []
            for col in group_candidates:
                sig, total, rec = self._ks_test_grouping(session, col)
                score = sig if rec else 0
                scored.append((col, score, rec))
            scored.sort(key=lambda x: x[1], reverse=True)
            return [col for col, score, rec in scored if rec]
        return group_candidates

    def _parse_time_loadings(self, command: str, items: List[str]) -> Optional[List[float]]:
        """Parse custom time loadings from command.
        Expected format: '增长模型 载荷 0 1 2' or '增长模型 0,1,2' after items are inferred.
        Returns a list of floats if valid and count matches items; else None.
        """
        tokens = command.strip().split()
        # Look for numeric tokens that could be loadings
        numbers = []
        for tok in tokens:
            try:
                num = float(tok)
                numbers.append(num)
            except ValueError:
                continue
        # If we found at least 2 numbers and count matches items, use them
        if numbers and len(numbers) == len(items):
            return numbers
        # Also try comma-separated after '载荷' keyword
        if '载荷' in command:
            parts = command.split('载荷')
            if len(parts) >= 2:
                comma_list = parts[-1].strip()
                maybe = comma_list.replace(',', ' ').split()
                nums = []
                for tok in maybe:
                    try:
                        nums.append(float(tok))
                    except:
                        pass
                if len(nums) == len(items):
                    return nums
        return None

    def _show_results(self, session) -> str:
        """Show detailed results."""
        if not session.results:
            return "No results yet. Please fit the model first."

        res = session.results
        lines = ["Full results:", ""]

        fi = res.get("fit_indices", {})
        lines.append("Fit indices:")
        for k, v in fi.items():
            lines.append(f"  {k}: {v}")

        lines.append("")
        lines.append("Path coefficients:")
        paths = res.get("paths", {})
        for (src, dst), stats in paths.items():
            lines.append(f"  {src} → {dst}: β={stats.get('estimate'):.3f}, p={stats.get('p'):.3f}")

        return "\n".join(lines)
