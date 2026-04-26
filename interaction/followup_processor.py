#!/usr/bin/env python3
"""Followup processor: handles commands after model is confirmed."""

import os
import re
import pandas as pd
from typing import Dict, Any, Tuple, Optional, List
from core.sem_fitter import SemFitter
from core.result_saver import ResultSaver
from visualization.dot_generator import DotGenerator
from interaction.report_formatter import ReportFormatter
from core.sem_utils import (
    compute_reliability, compute_factor_scores, compare_models,
    compute_power_analysis, suggest_estimator, detect_ordinal_variables,
)
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

        if cmd in ("help", "?", "commands"):
            return ("Available commands:\n"
                    "  fit / run model       - Fit the current model\n"
                    "  reliability           - Cronbach's alpha, CR, AVE\n"
                    "  factor scores         - Extract latent factor scores\n"
                    "  compare models        - Compare fitted models\n"
                    "  power                 - Power analysis\n"
                    "  missing data          - Analyze or impute missing data\n"
                    "  invariance test       - Measurement invariance testing\n"
                    "  bayesian fit          - Bayesian SEM via MCMC\n"
                    "  multilevel            - Multilevel SEM\n"
                    "  dsem                  - Dynamic SEM\n"
                    "  mixture               - Mixture / latent class SEM\n"
                    "  add path / remove path - Modify structural paths\n"
                    "  export report         - Generate report (MD or DOCX)\n"
                    "  diagram               - Generate path diagram (DOT)\n"
                    "  results               - Show full results\n")

        if cmd in ("help", "?"):
            return "Available: fit / reliability / factor scores / compare models / power / missing data / invariance test / bayesian / multilevel / dsem / mixture / diagram / export report"

        if getattr(session, 'data', None) is None:
            return "No data loaded. Please load a dataset first."

        if getattr(session, 'draft', None) is None and cmd not in ("help",):
            return "No model defined yet. Please complete the clarification steps first."

        # Multigroup state machine: metric/scalar progression
        mg = getattr(session, 'multigroup_results', None)
        if mg and mg.get('current_level') in ('configural', 'metric'):
            if cmd in ('metric', 'scalar'):
                return self._fit_advanced(session, 'multigroup', command)

        # Detect advanced/utility type early
        advanced_type = self._detect_advanced_type(command)

        # Utility-type handlers (don't need template fitting)
        if advanced_type == 'reliability':
            return self._handle_reliability(session)
        if advanced_type == 'factorscores':
            return self._handle_factor_scores(session)
        if advanced_type == 'modelcomparison':
            return self._handle_model_comparison(session)
        if advanced_type == 'power':
            return self._handle_power(session, command)
        if advanced_type == 'missingdata':
            return self._handle_missing_data(session, command)
        if advanced_type == 'invariance_test':
            return self._handle_invariance_test(session, command)
        if advanced_type == 'bayesian':
            return self._handle_bayesian(session, command)
        if advanced_type == 'multilevel':
            return self._handle_multilevel(session, command)
        if advanced_type == 'dsem':
            return self._handle_dsem(session, command)
        if advanced_type == 'mixture':
            return self._handle_mixture(session, command)

        # Fit command - detect if advanced model requested
        if cmd in ["拟合", "fit", "开始拟合", "运行模型", "run model"] or "增长" in cmd or "growth" in cmd or "trajectory" in cmd or "多组" in cmd or "multigroup" in cmd or "invariance" in cmd or "中介" in cmd or "mediation" in cmd or "ri-clpm" in cmd or "riclpm" in cmd or "ri-lta" in cmd or "rilta" in cmd or "esem" in cmd or "psem" in cmd or "penalized" in cmd or "bayesian" in cmd or "bsem" in cmd or "multilevel" in cmd or "dsem" in cmd or "mixture" in cmd:
            if advanced_type:
                return self._fit_advanced(session, advanced_type, command)
            else:
                return self._fit_model(session)

        # Also route if advanced_type detected but not caught above
        if advanced_type:
            return self._fit_advanced(session, advanced_type, command)

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

        return "Unknown command. Available: fit / add path / remove path / export report / results / diagram / reliability / factor scores / compare models / power / missing data / invariance test / bayesian / RI-CLPM / ESEM / PSEM"

    def _detect_advanced_type(self, command: str) -> Optional[str]:
        """Detect if command requests an advanced model or utility."""
        cmd_lower = command.lower()
        if "measurement invariance" in cmd_lower or "stepwise invariance" in cmd_lower or "invariance test" in cmd_lower or "alignment" in cmd_lower:
            return "invariance_test"
        if "multilevel" in cmd_lower or "multi-level" in cmd_lower or "hierarchical linear" in cmd_lower or "icc" in cmd_lower or "two-level" in cmd_lower:
            return "multilevel"
        if "dsem" in cmd_lower or "dynamic sem" in cmd_lower or "dynamic structural" in cmd_lower or "multilevel time series" in cmd_lower:
            return "dsem"
        if "mixture" in cmd_lower or "latent class" in cmd_lower or "latent profile" in cmd_lower or "lcsem" in cmd_lower or "class sem" in cmd_lower:
            return "mixture"
        if "增长" in cmd_lower or "growth" in cmd_lower or "trajectory" in cmd_lower or "latent growth" in cmd_lower:
            return "growth"
        if "multiple mediation" in cmd_lower or "parallel mediation" in cmd_lower:
            return "multiplemediation"
        if "中介" in cmd_lower or "mediation" in cmd_lower or "indirect" in cmd_lower:
            return "mediation"
        if "多组" in cmd_lower or "multigroup" in cmd_lower or "invariance" in cmd_lower:
            return "multigroup"
        if "second-order" in cmd_lower or "secondorder" in cmd_lower or "hierarchical" in cmd_lower:
            return "secondorder"
        if "cfa" in cmd_lower or "验证性因子" in cmd_lower or "confirmatory factor" in cmd_lower:
            return "cfa"
        if "efa" in cmd_lower or "exploratory factor" in cmd_lower:
            return "efa"
        if "cross-lagged" in cmd_lower or "crosslagged" in cmd_lower or "cross lagged" in cmd_lower:
            return "crosslagged"
        if "path analysis" in cmd_lower or "pathanalysis" in cmd_lower or "regression" in cmd_lower:
            return "pathanalysis"
        if "reliability" in cmd_lower or "cronbach" in cmd_lower or "ave" in cmd_lower:
            return "reliability"
        if "factor scores" in cmd_lower or "score" in cmd_lower:
            return "factorscores"
        if "compare models" in cmd_lower or "model comparison" in cmd_lower:
            return "modelcomparison"
        if "power" in cmd_lower or "sample size" in cmd_lower:
            return "power"
        if "ri-clpm" in cmd_lower or "riclpm" in cmd_lower or "random intercept cross" in cmd_lower:
            return "riclpm"
        if "ri-lta" in cmd_lower or "rilta" in cmd_lower or "random intercept latent transition" in cmd_lower:
            return "rilta"
        if "esem" in cmd_lower or "exploratory sem" in cmd_lower or "exploratory structural" in cmd_lower:
            return "esem"
        if "psem" in cmd_lower or "penalized sem" in cmd_lower or "penalised" in cmd_lower or "lasso sem" in cmd_lower or "ridge sem" in cmd_lower:
            return "psem"
        if "bayesian" in cmd_lower or "bsem" in cmd_lower or "bayes" in cmd_lower:
            return "bayesian"
        if "missing data" in cmd_lower or "impute" in cmd_lower or "imputation" in cmd_lower or "fiml" in cmd_lower or "mice" in cmd_lower:
            return "missingdata"
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

            suggestions = self._auto_suggest(session, 'sem')
            if suggestions:
                lines.append("")
                lines.append("You might also consider:")
                for s in suggestions:
                    lines.append(f"  - {s}")

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

            # Accumulate multigroup fit stats for cross-level comparison
            if model_type == 'multigroup':
                mg_results = getattr(session, 'multigroup_results', None)
                if mg_results:
                    if 'fits' not in mg_results:
                        mg_results['fits'] = {}
                    current_level = mg_results.get('current_level', 'configural')
                    mg_results['fits'][current_level] = {
                        'chi2': result.fit_stats.get('chi2', 0),
                        'df': result.fit_stats.get('df', 0),
                        'cfi': result.fit_stats.get('cfi', 0),
                        'rmsea': result.fit_stats.get('rmsea', 0),
                        'srmr': result.fit_stats.get('srmr', 0),
                        'p_value': result.fit_stats.get('p_value', 0),
                    }

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
            session.multigroup_var = explicit_var
            draft = session.draft
            user_vars = {
                'latent': draft.latent,
                'observed': draft.observed,
                'paths': draft.paths,
                'group': explicit_var
            }
            if hasattr(session, 'multigroup_results') and session.multigroup_results is not None:
                if 'metric' in command.lower():
                    invariance = 'metric'
                elif 'scalar' in command.lower():
                    invariance = 'scalar'
                else:
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
                user_vars['invariance'] = 'configural'
                session.multigroup_results = {'current_level': 'configural'}
            session.invariance_level = user_vars['invariance']
            return user_vars, None

        elif model_type == 'efa':
            variables = list(session.data.columns)
            user_vars = {
                'variables': variables,
                'data': session.data,
            }
            return user_vars, None

        elif model_type == 'secondorder':
            latent_defs = session.variables.get('latent_indicators', {})
            if not latent_defs:
                draft = getattr(session, 'draft', None)
                if draft and hasattr(draft, 'latent'):
                    latent_defs = draft.latent
            if not latent_defs:
                return {}, "Please define first-order latent factors before specifying a second-order model."
            second_order = {}
            parts = command.strip().split()
            so_factor = None
            for tok in parts:
                if tok not in ('second-order', 'secondorder', 'hierarchical', 'second_order'):
                    if tok in latent_defs or tok in session.data.columns:
                        continue
                    so_factor = tok
                    break
            first_order_names = list(latent_defs.keys())
            if so_factor and len(first_order_names) >= 2:
                second_order[so_factor] = first_order_names
            elif len(first_order_names) >= 2:
                second_order['General'] = first_order_names
            else:
                return {}, "Second-order CFA requires at least two first-order factors."
            user_vars = {
                'latent': latent_defs,
                'second_order': second_order,
            }
            return user_vars, None

        elif model_type == 'crosslagged':
            data_cols = list(session.data.columns)
            ts_vars = self._detect_time_series_vars(data_cols)
            if not ts_vars:
                return {}, "No time-series variables detected. Columns should follow patterns like var_t1, var_t2."
            base_vars, time_points = self._extract_crosslagged_structure(ts_vars, data_cols)
            if not base_vars or len(time_points) < 2:
                return {}, "Could not extract cross-lagged structure. Ensure variables follow pattern: varname_timepoint."
            user_vars = {
                'variables': base_vars,
                'time_points': time_points,
            }
            return user_vars, None

        elif model_type == 'multiplemediation':
            paths = getattr(session, 'suggested_paths', [])
            if len(paths) < 2:
                parts = command.strip().split()
                if len(parts) >= 3:
                    parsed = self._parse_mediation_command(parts)
                    if parsed:
                        user_vars = parsed
                        return user_vars, None
                return {}, ("Cannot infer multiple mediation from current paths. "
                            "Specify explicitly: 'multiple mediation X M1 M2 Y'.")
            chain = self._infer_multiple_mediation_chain(paths, session)
            if not chain:
                parts = command.strip().split()
                if len(parts) >= 4:
                    parsed = self._parse_mediation_command(parts)
                    if parsed:
                        user_vars = parsed
                        return user_vars, None
                return {}, ("Cannot infer multiple mediation chain. "
                            "Specify explicitly: 'multiple mediation X M1 M2 Y'.")
            user_vars = chain
            return user_vars, None

        elif model_type == 'pathanalysis':
            draft = getattr(session, 'draft', None)
            predictors = []
            outcome = None
            if draft:
                predictors = list(draft.covariates) if hasattr(draft, 'covariates') else []
                outcome = getattr(draft, 'outcome', None)
                if not outcome:
                    dep_vars = session.variables.get('dependent', [])
                    outcome = dep_vars[0] if dep_vars else None
                indep = session.variables.get('independent', [])
                predictors = list(set(predictors + indep))
            if not predictors:
                parts = command.strip().split()
                predictors = [p for p in parts[1:] if p in session.data.columns]
            if not outcome:
                remaining = [c for c in session.data.columns if c not in predictors]
                outcome = remaining[0] if remaining else None
            if not predictors or not outcome:
                return {}, "Cannot determine predictors and outcome. Specify: 'path analysis pred1 pred2 -> outcome'."
            user_vars = {
                'predictors': predictors,
                'outcome': outcome,
            }
            return user_vars, None

        elif model_type == 'esem':
            variables = list(session.data.columns)
            numeric_vars = [v for v in variables if session.data[v].dtype != object]
            n_factors = None
            for tok in command.strip().split():
                if tok.startswith('k=') or tok.startswith('factors='):
                    try:
                        n_factors = int(tok.split('=')[1])
                    except ValueError:
                        pass
            latent_defs = session.variables.get('latent_indicators', {})
            if not latent_defs:
                draft = getattr(session, 'draft', None)
                if draft and hasattr(draft, 'latent'):
                    latent_defs = draft.latent
            if latent_defs and n_factors is None:
                n_factors = len(latent_defs)
            user_vars = {
                'variables': numeric_vars,
                'data': session.data,
                'n_factors': n_factors,
            }
            return user_vars, None

        elif model_type in ('riclpm', 'rilta'):
            data_cols = list(session.data.columns)
            ts_vars = self._detect_time_series_vars(data_cols)
            if not ts_vars:
                return {}, "No time-series variables detected. Columns should follow patterns like var_t1, var_t2."
            base_vars, time_points = self._extract_crosslagged_structure(ts_vars, data_cols)
            if not base_vars or len(time_points) < 2:
                return {}, "Could not extract panel structure. Ensure variables follow pattern: varname_timepoint."
            person_var = None
            for tok in command.strip().split():
                if tok.startswith("person="):
                    person_var = tok.split("=")[1]
            user_vars = {
                'variables': base_vars,
                'time_points': time_points,
                'person_var': person_var,
            }
            return user_vars, None

        elif model_type == 'psem':
            latent_inds = session.variables.get('latent_indicators', {})
            if not latent_inds:
                draft = getattr(session, 'draft', None)
                if draft and hasattr(draft, 'latent'):
                    latent_inds = draft.latent
            if not latent_inds:
                return {}, "Please define latent variables first."
            dep = session.variables.get('dependent', '')
            paths = getattr(session, 'suggested_paths', [])
            user_vars = {
                'latent': latent_inds,
                'observed': [],
                'paths': paths,
                'outcome': dep,
            }
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
        elif model_type == 'esem':
            estimates = getattr(result, 'estimates', {})
            loadings = estimates.get('loading_matrix')
            if loadings is not None and isinstance(loadings, pd.DataFrame):
                lines.append("\nRotated Loading Matrix:")
                header = "| Item | " + " | ".join(loadings.columns[:-1] if 'communality' in loadings.columns else loadings.columns) + " |"
                sep = "|------|" + "|".join(["-------" for _ in range(len(loadings.columns) - (1 if 'communality' in loadings.columns else 0))]) + "|"
                lines.append(header)
                lines.append(sep)
                display_cols = [c for c in loadings.columns if c != 'communality']
                for idx, row in loadings.iterrows():
                    vals = []
                    for col in display_cols:
                        v = row[col]
                        if isinstance(v, (int, float, np.floating)):
                            marker = "**" if abs(v) >= 0.30 else ""
                            vals.append(f"{marker}{v:.2f}{marker}")
                        else:
                            vals.append(str(v))
                    lines.append(f"| {idx} | " + " | ".join(vals) + " |")
            lines.append("\nESEM notes:")
            lines.append("  Primary loadings (|β| >= 0.30) are shown in bold.")
            lines.append("  Cross-loadings below 0.30 are typically negligible.")
            lines.append("  Compare CFI and RMSEA to your previous CFA model to assess improvement.")
            cfa_result = session.advanced_results.get('cfa') if hasattr(session, 'advanced_results') else None
            if cfa_result and hasattr(cfa_result, 'fit_stats'):
                cfa_fit = cfa_result.fit_stats
                esem_cfi = fit.get('cfi', 0)
                cfa_cfi = cfa_fit.get('cfi', 0)
                esem_rmsea = fit.get('rmsea', 0)
                cfa_rmsea = cfa_fit.get('rmsea', 0)
                lines.append(f"\n  CFA fit:   CFI = {cfa_cfi:.3f}, RMSEA = {cfa_rmsea:.3f}")
                lines.append(f"  ESEM fit:  CFI = {esem_cfi:.3f}, RMSEA = {esem_rmsea:.3f}")
                lines.append(f"  ΔCFI = {esem_cfi - cfa_cfi:+.3f}, ΔRMSEA = {esem_rmsea - cfa_rmsea:+.3f}")

        # Multigroup-specific: show guidance and comparison
        if model_type == 'multigroup' and session is not None:
            mg_results = getattr(session, 'multigroup_results', None)
            if mg_results:
                current = mg_results.get('current_level', 'configural')
                lines.append(f"\nMultigroup analysis - {current} invariance")

                # Show per-group fit for configural
                estimates = getattr(result, 'estimates', {})
                per_group = estimates.get('configural', {})
                if per_group and current == 'configural':
                    lines.append("\nPer-group fit:")
                    group_table = "| Group | χ² (df) | CFI | RMSEA | SRMR |"
                    lines.append(group_table)
                    lines.append("|-------|---------|------|-------|------|")
                    pooled_chi2 = 0
                    pooled_df = 0
                    pooled_cfi_vals = []
                    pooled_rmsea_vals = []
                    for gname, gres in per_group.items():
                        gfit = gres.get('fit_stats', {}) if isinstance(gres, dict) else {}
                        if gfit:
                            chi2 = gfit.get('chi2', 0)
                            df = gfit.get('df', 0)
                            cfi = gfit.get('cfi', 0)
                            rmsea = gfit.get('rmsea', 0)
                            srmr = gfit.get('srmr', 0)
                            lines.append(f"| {gname} | {chi2:.1f} ({df}) | {cfi:.3f} | {rmsea:.3f} | {srmr:.3f} |")
                            pooled_chi2 += chi2
                            pooled_df += df
                            pooled_cfi_vals.append(cfi)
                            pooled_rmsea_vals.append(rmsea)
                    if pooled_cfi_vals:
                        avg_cfi = sum(pooled_cfi_vals) / len(pooled_cfi_vals)
                        avg_rmsea = sum(pooled_rmsea_vals) / len(pooled_rmsea_vals)
                        lines.append(f"| **Pooled** | **{pooled_chi2:.1f} ({pooled_df})** | **{avg_cfi:.3f}** | **{avg_rmsea:.3f}** | — |")

                if current == 'configural':
                    lines.append("\n  Baseline: same measurement structure, parameters freely estimated (no constraints).")
                    lines.append("\n  You can also test stricter invariance:")
                    lines.append("  - Metric: constrain factor loadings equal across groups")
                    lines.append("  - Scalar: constrain both loadings and intercepts equal")
                    lines.append("\n  Reply 'metric' or 'scalar' to proceed.")
                elif current == 'metric':
                    lines.append("  Factor loadings constrained equal across groups.")
                    lines.append("\n  Test scalar invariance (add intercept constraints)? Reply 'scalar'.")
                elif current == 'scalar':
                    lines.append("  Loadings and intercepts constrained equal. Invariance testing complete.")
                    lines.append("\n  Scalar invariance supported → you may now compare latent factor *means* across groups.")
                    lines.append("  Metric invariance only → you may compare factor *correlations* and *regression paths*.")

                # Show comparison of fit indices across levels
                fits = mg_results.get('fits', {})
                if len(fits) > 1:
                    levels = ['configural', 'metric', 'scalar']
                    lines.append("\nFit index comparison (ΔCFI < -0.010 or ΔRMSEA > +0.015 suggests invariance not supported):")
                    table = "| Level | χ² (df) | CFI | RMSEA | ΔCFI | ΔRMSEA |"
                    lines.append(table)
                    lines.append("|-------|---------|------|-------|------|--------|")
                    prev_cfi = None
                    prev_rmsea = None
                    for level in levels:
                        if level in fits:
                            f = fits[level]
                            cf = f.get('cfi', 0)
                            rm = f.get('rmsea', 0)
                            chi2 = f.get('chi2', 0)
                            df = f.get('df', 0)
                            if prev_cfi is not None:
                                dcfi = cf - prev_cfi
                                drmsea = rm - prev_rmsea
                                lines.append(f"| {level} | {chi2:.1f} ({df}) | {cf:.3f} | {rm:.3f} | {dcfi:+.3f} | {drmsea:+.3f} |")
                            else:
                                lines.append(f"| {level} | {chi2:.1f} ({df}) | {cf:.3f} | {rm:.3f} | — | — |")
                            prev_cfi = cf
                            prev_rmsea = rm

        # Textbook references
        retriever = getattr(session, 'textbook_retriever', None)
        if retriever:
            lines.append("\nRelevant textbook chapters:")
            stage_map = {
                'cfa': 'measurement_model',
                'growth': 'growth_modeling',
                'mediation': 'structural_model',
                'multigroup': 'multigroup_analysis',
                'esem': 'measurement_model',
                'efa': 'measurement_model',
                'secondorder': 'measurement_model',
                'crosslagged': 'growth_modeling',
                'multiplemediation': 'structural_model',
                'pathanalysis': 'structural_model',
                'riclpm': 'growth_modeling',
                'rilta': 'growth_modeling',
                'psem': 'model_fitting',
            }
            stage = stage_map.get(model_type, 'model_fitting')
            teaching = retriever.format_teaching_for_stage(stage, max_sections=2)
            if teaching:
                lines.append(teaching)

        suggestions = self._auto_suggest(session, model_type)
        if suggestions:
            lines.append("")
            lines.append("You might also consider:")
            for s in suggestions:
                lines.append(f"  - {s}")

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

    def _auto_suggest(self, session, current_model_type: str = "") -> List[str]:
        suggestions = []
        data = getattr(session, 'data', None)
        if data is None:
            return suggestions

        cols = list(data.columns)

        ts_vars = self._detect_time_series_vars(cols)
        if ts_vars and current_model_type not in ('growth', 'crosslagged', 'riclpm', 'rilta'):
            base, tps = self._extract_crosslagged_structure(ts_vars, cols)
            if base and len(tps) >= 3:
                suggestions.append(
                    "Time-series pattern detected in your data. "
                    "Consider 'growth' (latent growth curve) or 'cross-lagged' panel analysis."
                )
            elif base and len(tps) >= 2:
                suggestions.append(
                    "Repeated-measures pattern detected. "
                    "Consider 'cross-lagged' or 'RI-CLPM' analysis."
                )

        draft = getattr(session, 'draft', None)
        if draft and hasattr(draft, 'paths'):
            paths = draft.paths
            if len(paths) >= 2 and current_model_type != 'mediation':
                node_targets = {}
                for src, dst in paths:
                    node_targets.setdefault(dst, []).append(src)
                for target, sources in node_targets.items():
                    if len(sources) >= 2:
                        for s1 in sources:
                            for s2 in sources:
                                if s1 != s2:
                                    has_s1_to_s2 = any(
                                        a == s1 and b == s2 for a, b in paths
                                    )
                                    if has_s1_to_s2:
                                        suggestions.append(
                                            f"Indirect path detected: {s1} -> {s2} -> {target}. "
                                            f"Consider 'mediation' analysis to test indirect effects."
                                        )
                                        break
                            if any("mediation" in s for s in suggestions):
                                break
                    if any("mediation" in s for s in suggestions):
                        break

        group_vars = self._suggest_grouping_vars(session)
        if group_vars and current_model_type not in ('multigroup',):
            var_list = ", ".join(group_vars[:3])
            suggestions.append(
                f"Potential grouping variable(s) detected: {var_list}. "
                f"Consider 'multigroup {group_vars[0]}' for measurement invariance testing."
            )

        results = getattr(session, 'results', None) or {}
        model_result = results.get('model')
        if model_result and current_model_type in ('cfa', 'sem'):
            fit = {}
            if hasattr(model_result, 'fit_indices'):
                fit = model_result.fit_indices if isinstance(model_result.fit_indices, dict) else {}
            cfi = fit.get('cfi', 1.0)
            rmsea = fit.get('rmsea', 0.0)
            if (cfi < 0.90 or rmsea > 0.08) and current_model_type != 'esem':
                suggestions.append(
                    "CFA fit is below ideal thresholds. "
                    "Consider 'ESEM' (Exploratory Structural Equation Modeling) "
                    "for a more flexible factor structure."
                )

        return suggestions

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

    # === New handler methods ===

    def _handle_reliability(self, session) -> str:
        """Compute and report reliability indices (Cronbach alpha, CR, AVE)."""
        try:
            if getattr(session, 'data', None) is None:
                return "No data loaded. Please load data first."

            advanced_results = getattr(session, 'advanced_results', {}) or {}
            cfa_result = advanced_results.get('cfa')
            model = None

            if cfa_result and hasattr(cfa_result, 'estimates'):
                model = cfa_result.estimates.get('model')

            latent_dict = session.variables.get('latent_indicators', {})
            if not latent_dict:
                draft = getattr(session, 'draft', None)
                if draft and hasattr(draft, 'latent'):
                    latent_dict = draft.latent
                elif draft and hasattr(draft, 'latent_vars'):
                    latent_dict = draft.latent_vars

            if not latent_dict:
                return "No latent variable definitions found. Please define a CFA model first."

            if model is None:
                results = getattr(session, 'results', None)
                if results and isinstance(results, dict):
                    model = results.get('model')

            if model is None:
                fitter = getattr(session, 'advanced_fitter', None)
                if not fitter:
                    return "Advanced analysis engine not ready."
                try:
                    cfa_result = fitter.fit(session.data, 'cfa',
                                            {'latent': latent_dict, 'observed': []})
                    if not hasattr(session, 'advanced_results') or session.advanced_results is None:
                        session.advanced_results = {}
                    session.advanced_results['cfa'] = cfa_result
                    model = cfa_result.estimates.get('model')
                except Exception as e:
                    return f"CFA fitting failed (needed for reliability): {e}"

            if model is None:
                return "No fitted model available. Please fit a CFA model first."

            results = compute_reliability(model, session.data, latent_dict)

            lines = ["Reliability Analysis Report", "=" * 40, ""]
            for factor, metrics in results.items():
                lines.append(f"Factor: {factor} ({metrics.get('n_items', '?')} items)")
                alpha = metrics.get('cronbach_alpha')
                cr = metrics.get('composite_reliability')
                ave = metrics.get('average_variance_extracted')
                alpha_str = f"{alpha:.3f}" if alpha is not None else "N/A"
                cr_str = f"{cr:.3f}" if cr is not None else "N/A"
                ave_str = f"{ave:.3f}" if ave is not None else "N/A"
                lines.append(f"  Cronbach's Alpha: {alpha_str}")
                lines.append(f"  Composite Reliability (CR): {cr_str}")
                lines.append(f"  Average Variance Extracted (AVE): {ave_str}")
                lines.append(f"  Assessment: {metrics.get('assessment', 'Unknown')}")
                lines.append("")

            lines.append("Thresholds:")
            lines.append("  Cronbach's Alpha: >0.7 good, >0.6 acceptable")
            lines.append("  CR: >0.7 good, >0.6 acceptable")
            lines.append("  AVE: >0.5 indicates adequate convergent validity")

            return "\n".join(lines)

        except Exception as e:
            return f"Reliability analysis failed: {e}"

    def _handle_factor_scores(self, session) -> str:
        """Extract and report factor scores from the fitted model."""
        try:
            advanced_results = getattr(session, 'advanced_results', {}) or {}
            model = None
            for key in ['cfa', 'secondorder', 'growth', 'multigroup']:
                result = advanced_results.get(key)
                if result and hasattr(result, 'estimates'):
                    model = result.estimates.get('model')
                    if model:
                        break

            if model is None and hasattr(session, 'results') and session.results:
                model = session.results.get('model')

            if model is None:
                return "No fitted model found. Please fit a model first."

            scores = compute_factor_scores(model, session.data)
            if scores.empty:
                return "Could not compute factor scores. The model may not contain latent variables."

            lines = ["Factor Scores Summary", "=" * 40, ""]
            for col in scores.columns:
                desc = scores[col].describe()
                lines.append(f"Factor: {col}")
                lines.append(f"  Mean: {desc['mean']:.3f}")
                lines.append(f"  Std:  {desc['std']:.3f}")
                lines.append(f"  Min:  {desc['min']:.3f}")
                lines.append(f"  Max:  {desc['max']:.3f}")
                lines.append("")

            corr = scores.corr()
            if len(corr) > 1:
                lines.append("Factor Score Correlations:")
                lines.append(corr.to_string())

            lines.append("")
            lines.append(f"Total observations with scores: {len(scores)}")

            session.factor_scores = scores

            return "\n".join(lines)

        except Exception as e:
            return f"Factor score extraction failed: {e}"

    def _handle_model_comparison(self, session) -> str:
        """Compare multiple models stored in the session."""
        try:
            advanced_results = getattr(session, 'advanced_results', {}) or {}
            if not advanced_results:
                return "No advanced model results found. Please fit at least two models first."

            results_list = list(advanced_results.values())
            if len(results_list) < 2:
                return ("Only one model found in session. Fit additional models before comparing. "
                        "(e.g., fit a CFA, then a mediation model)")

            comparison = compare_models(results_list)

            if 'error' in comparison:
                return comparison['error']

            lines = ["Model Comparison Report", "=" * 40, ""]

            table = comparison.get('comparison_table')
            if table is not None and isinstance(table, pd.DataFrame):
                lines.append("Fit Indices Comparison:")
                lines.append(table.to_string(index=False))
                lines.append("")

            best_aic = comparison.get('best_by_aic')
            best_bic = comparison.get('best_by_bic')
            if best_aic is not None:
                lines.append(f"Best model by AIC: Model {best_aic}")
            if best_bic is not None:
                lines.append(f"Best model by BIC: Model {best_bic}")

            chi2_tests = comparison.get('chi2_difference_tests', [])
            if chi2_tests:
                lines.append("")
                lines.append("Chi-Square Difference Tests (for nested models):")
                for test in chi2_tests:
                    sig = "Significant" if test['significant'] else "Not significant"
                    lines.append(f"  {test['models']}: "
                                 f"delta-chi2={test['delta_chi2']:.2f}, "
                                 f"delta-df={test['delta_df']:.0f}, "
                                 f"p={test['p_value']:.4f} ({sig})")

            return "\n".join(lines)

        except Exception as e:
            return f"Model comparison failed: {e}"

    def _handle_power(self, session, command: str) -> str:
        """Run power analysis on the current model."""
        try:
            advanced_results = getattr(session, 'advanced_results', {}) or {}
            model_str = None
            for key in ['cfa', 'secondorder', 'growth', 'mediation',
                        'multigroup', 'multiplemediation', 'pathanalysis',
                        'crosslagged', 'efa']:
                result = advanced_results.get(key)
                if result and hasattr(result, 'model_string'):
                    model_str = result.model_string
                    break

            if model_str is None and hasattr(session, 'results') and session.results:
                model_str = session.results.get('model_string')

            if not model_str:
                return "No model found. Please fit a model before running power analysis."

            n_sim = 200
            alpha = 0.05
            parts = command.strip().split()
            for i, tok in enumerate(parts):
                try:
                    val = int(tok)
                    if val > 10:
                        n_sim = min(val, 1000)
                except ValueError:
                    pass

            lines = ["Power Analysis", "=" * 40, ""]
            lines.append(f"Running Monte Carlo power analysis with {n_sim} simulations...")
            lines.append("This may take a moment.")
            lines.append("")

            result = compute_power_analysis(model_str, session.data, n_sim=n_sim, alpha=alpha)

            if 'error' in result:
                return f"Power analysis failed: {result['error']}"

            power = result.get('power')
            ci_lower = result.get('ci_lower')
            ci_upper = result.get('ci_upper')

            if power is not None:
                lines.append(f"Estimated power: {power:.3f}")
                if ci_lower is not None and ci_upper is not None:
                    lines.append(f"95% CI: [{ci_lower:.3f}, {ci_upper:.3f}]")
            else:
                lines.append("Power could not be estimated.")

            lines.append(f"Simulations run: {result.get('n_simulations', 0)}")
            lines.append(f"Converged: {result.get('n_converged', 0)}")
            lines.append(f"Rejected H0: {result.get('n_rejected', 0)}")
            lines.append(f"Alpha level: {result.get('alpha', 0.05)}")

            if power is not None:
                if power >= 0.8:
                    lines.append("")
                    lines.append("Power is adequate (>= 0.80). Sample size appears sufficient.")
                elif power >= 0.6:
                    lines.append("")
                    lines.append("Power is moderate (0.60-0.79). Consider increasing sample size.")
                else:
                    lines.append("")
                    lines.append("Power is low (< 0.60). The sample size may be insufficient for this model.")

            return "\n".join(lines)

        except Exception as e:
            return f"Power analysis failed: {e}"

    def _handle_missing_data(self, session, command: str) -> str:
        try:
            from core.missing_data import (
                analyze_missing_pattern, suggest_missing_strategy,
                multiple_imputation, impute_and_fit,
            )
        except ImportError:
            return "Missing data module not available. Install required packages."

        try:
            data = session.data
            if data is None:
                return "No data loaded."

            cmd = command.lower()
            lines = ["Missing Data Analysis", "=" * 40, ""]

            if "analyze" in cmd or "pattern" in cmd or "analysis" in cmd or "analyse" in cmd:
                pattern = analyze_missing_pattern(data)
                pct = pattern.get("total_missing_pct", 0)
                lines.append(f"Total missing: {pct:.1f}%")

                n_complete = len(data.dropna())
                n_total = len(data)
                loss_pct = (1 - n_complete / n_total) * 100
                lines.append(f"Complete cases: {n_complete} / {n_total} ({loss_pct:.1f}% would be lost with listwise deletion)")

                lines.append(f"\nMechanism hint: {pattern.get('mechanism_hint', 'Unknown')}")
                lines.append("")
                lines.append("Per-variable missingness:")
                lines.append("| Variable | Missing | % |")
                lines.append("|----------|---------|---|")
                for col, info in pattern.get("per_variable", {}).items():
                    if info.get("count", 0) > 0:
                        lines.append(f"| {col} | {info['count']} | {info['percentage']:.1f}% |")
                lines.append("")
                lines.append("Missing patterns:")
                for p in pattern.get("patterns", [])[:5]:
                    miss_vars = p.get("missing_variables", [])
                    freq = p.get("frequency", 0)
                    pct_p = p.get("percentage", 0)
                    if miss_vars:
                        lines.append(f"  {', '.join(miss_vars)}: {freq} cases ({pct_p:.1f}%)")
                    else:
                        lines.append(f"  Complete cases: {freq} ({pct_p:.1f}%)")
                strategy = suggest_missing_strategy(data)
                strategy_name = self._human_readable_strategy(strategy.get('strategy', 'N/A'))
                lines.append("")
                lines.append(f"Recommended strategy: {strategy_name}")
                lines.append(f"Reason: {strategy.get('reason', 'N/A')}")

                if loss_pct > 20:
                    lines.append(f"\nWARNING: Listwise deletion would discard {loss_pct:.0f}% of cases. This may introduce bias if data are not MCAR.")
                elif loss_pct > 5:
                    lines.append(f"\nNote: Listwise deletion would retain {100-loss_pct:.0f}% of cases.")
                return "\n".join(lines)

            if "impute" in cmd or "mice" in cmd or "imputation" in cmd:
                strategy = suggest_missing_strategy(data)
                n_imp = strategy.get("n_imputations", 5)
                try:
                    n_imp = int(n_imp)
                except (TypeError, ValueError):
                    n_imp = 5

                if "fit" in cmd:
                    model_str = self._get_model_string(session)
                    if not model_str:
                        return "No model found. Please fit a model first, or specify a model."
                    lines.append(f"Running impute-and-fit pipeline (m={n_imp})...")
                    result = impute_and_fit(model_str, data)
                    if "error" in result:
                        return f"Impute-and-fit failed: {result['error']}"
                    pooled_dict = result.get("pooled", {})
                    pooled_est = pooled_dict.get("pooled_estimates", {})
                    pooled_se = pooled_dict.get("pooled_se", {})
                    pooled_p = pooled_dict.get("pooled_p", {})
                    pooled_ci = pooled_dict.get("confidence_intervals", {})
                    fmi = pooled_dict.get("fmi", {})
                    lines.append(f"Pooled parameters: {len(pooled_est)} estimates (Rubin's rules)")
                    lines.append("")
                    lines.append("| Parameter | Estimate | SE | t | p | 95% CI |")
                    lines.append("|-----------|----------|----|---|---|--------|")
                    for param, est in list(pooled_est.items())[:15]:
                        se = pooled_se.get(param, "?")
                        p_val = pooled_p.get(param, "?")
                        ci = pooled_ci.get(param, ("?", "?"))
                        fmi_val = fmi.get(param)
                        se_s = f"{se:.3f}" if isinstance(se, (int, float, np.floating)) else str(se)
                        p_s = f"{p_val:.3f}" if isinstance(p_val, (int, float, np.floating)) else str(p_val)
                        est_s = f"{est:.3f}" if isinstance(est, (int, float, np.floating)) else str(est)
                        if isinstance(ci, (list, tuple)) and len(ci) == 2:
                            ci_s = f"[{ci[0]:.3f}, {ci[1]:.3f}]" if isinstance(ci[0], (int, float, np.floating)) else str(ci)
                        else:
                            ci_s = "N/A"
                        lines.append(f"| {param} | {est_s} | {se_s} | — | {p_s} | {ci_s} |")
                    if fmi:
                        lines.append("")
                        lines.append("Fraction of Missing Information (FMI):")
                        for param, val in list(fmi.items())[:10]:
                            lines.append(f"  {param}: {val:.3f}")
                    lines.append("")
                    lines.append(f"Successful imputations: {result.get('n_successful', '?')}/{result.get('n_total', '?')}")
                    return "\n".join(lines)

                lines.append(f"Running Multiple Imputation (m={n_imp})...")
                imputed = multiple_imputation(data, n_imputations=n_imp)
                lines.append(f"Generated {len(imputed)} imputed datasets.")
                session.imputed_datasets = imputed
                lines.append("")
                lines.append("Imputed datasets stored in session.")
                lines.append("Use 'impute and fit' to fit models on imputed data with Rubin's rules pooling.")
                return "\n".join(lines)

            strategy = suggest_missing_strategy(data)
            strategy_name = self._human_readable_strategy(strategy.get('strategy', 'N/A'))
            lines.append(f"Recommended strategy: {strategy_name}")
            lines.append(f"Reason: {strategy.get('reason', 'N/A')}")
            lines.append("")
            lines.append("Commands: 'analyze missing data', 'impute data', 'impute and fit'")
            return "\n".join(lines)

        except Exception as e:
            return f"Missing data analysis failed: {e}"

    def _handle_invariance_test(self, session, command: str) -> str:
        try:
            from core.sem_utils import stepwise_invariance_test, alignment_optimization
        except ImportError:
            return "Invariance testing module not available."

        try:
            data = session.data
            if data is None:
                return "No data loaded."

            cmd = command.lower()

            if "alignment" in cmd:
                model_str = self._get_model_string(session)
                if not model_str:
                    return "No model found for alignment analysis."
                draft = session.draft
                latent_dict = getattr(draft, 'latent_vars', {})
                group_var = getattr(draft, 'group_var', None)
                if not group_var:
                    for col in data.columns:
                        if data[col].dtype == object or data[col].nunique() <= 10:
                            group_var = col
                            break
                if not group_var or not latent_dict:
                    return "Need group variable and latent structure for alignment. Specify grouping variable."
                result = alignment_optimization(data, model_str, group_var, latent_dict)
                lines = ["Alignment Optimization", "=" * 40, ""]
                quality = result.get("alignment_quality", {})
                lines.append(f"Proportion well-aligned parameters: {quality.get('proportion_well_aligned', 'N/A')}")
                lines.append("")
                for rec in result.get("recommendation", "").split("."):
                    if rec.strip():
                        lines.append(rec.strip())
                return "\n".join(lines)

            model_str = self._get_model_string(session)
            if not model_str:
                return "No model found. Please fit a CFA model first."

            draft = session.draft
            latent_dict = getattr(draft, 'latent_vars', {})
            if not latent_dict:
                latent_dict = {}
                insp_lines = model_str.strip().split("\n")
                for line in insp_lines:
                    if "=~" in line:
                        parts = line.split("=~")
                        if len(parts) == 2:
                            lv = parts[0].strip().split()[-1]
                            items = [i.strip().lstrip("0123456789*") for i in parts[1].split("+")]
                            latent_dict[lv] = items

            group_var = getattr(draft, 'group_var', None)
            if not group_var:
                for col in data.columns:
                    if col not in latent_dict and data[col].dtype == object and data[col].nunique() <= 10:
                        group_var = col
                        break
            if not group_var:
                return "No grouping variable found. Specify which column defines groups (e.g., 'invariance test by gender')."

            lines = ["Stepwise Measurement Invariance Test", "=" * 40, ""]
            result = stepwise_invariance_test(data, model_str, group_var, latent_dict)

            for level in result.get("levels_tested", []):
                res = result.get("results", {}).get(level, {})
                chi2 = res.get("chi2", "N/A")
                df = res.get("df", "N/A")
                cfi = res.get("cfi", "N/A")
                rmsea = res.get("rmsea", "N/A")
                converged = res.get("converged", False)
                status = "OK" if converged else "FAILED"
                if isinstance(chi2, float):
                    lines.append(f"{level.upper()}: chi2={chi2:.2f}, df={df}, CFI={cfi:.3f}, RMSEA={rmsea:.3f} [{status}]")
                else:
                    lines.append(f"{level.upper()}: {status}")

            lines.append("")
            for comp in result.get("comparisons", []):
                models = comp.get("models", "")
                d_chi2 = comp.get("delta_chi2", "N/A")
                d_df = comp.get("delta_df", "N/A")
                p = comp.get("p_value", "N/A")
                sig = comp.get("significant", False)
                if isinstance(d_chi2, float):
                    lines.append(f"  {models}: Delta-chi2={d_chi2:.2f}, Delta-df={d_df}, p={p:.4f} {'*' if sig else 'ns'}")

            lines.append("")
            achieved = result.get("invariance_achieved", "Unknown")
            lines.append(f"Highest invariance level achieved: {achieved.upper()}")
            rec = result.get("recommendation", "")
            if rec:
                lines.append("")
                lines.append(rec)

            return "\n".join(lines)

        except Exception as e:
            return f"Invariance test failed: {e}"

    def _handle_bayesian(self, session, command: str) -> str:
        try:
            from core.bayesian_sem import BayesianSEM, quick_bayesian_cfa
        except ImportError:
            return "Bayesian SEM module not available. Install pymc: pip install pymc arviz"

        try:
            import pymc
        except ImportError:
            return "PyMC is not installed. Bayesian SEM requires PyMC.\nInstall with: pip install pymc arviz"

        try:
            data = session.data
            if data is None:
                return "No data loaded."
            if len(data) < 20:
                return f"Insufficient data (N={len(data)}). Bayesian SEM requires at least 20 observations."

            cmd = command.lower()

            if "fit" in cmd or "run" in cmd or "estimate" in cmd or "sample" in cmd:
                model_str = self._get_model_string(session)
                if not model_str:
                    draft = session.draft
                    latent_dict = getattr(draft, 'latent_vars', {})
                    if latent_dict:
                        lines = ["Running Bayesian CFA..."]
                        lines.append("This uses MCMC sampling and may take several minutes.")
                        lines.append("")
                        bsem = BayesianSEM(model_str) if model_str else None
                        if bsem is None:
                            return "No model syntax available. Please define a model first."
                    else:
                        return "No model found. Please define a CFA or SEM model first."
                else:
                    lines = ["Running Bayesian SEM...", ""]
                    bsem = BayesianSEM(model_str)

                draws = 2000
                tune = 1000
                for tok in cmd.split():
                    if tok.startswith("draws="):
                        try:
                            draws = int(tok.split("=")[1])
                        except ValueError:
                            pass
                    if tok.startswith("tune="):
                        try:
                            tune = int(tok.split("=")[1])
                        except ValueError:
                            pass

                lines.append(f"MCMC: {draws} draws, {tune} tuning, 4 chains")
                lines.append("Sampling in progress...")
                result = bsem.fit(data, draws=draws, tune=tune, chains=4, target_accept=0.9)

                lines.append("")
                lines.append("Bayesian SEM Results")
                lines.append("=" * 40)
                summary = result.summary
                if isinstance(summary, pd.DataFrame) and not summary.empty:
                    lines.append(summary.to_string(max_rows=20))
                else:
                    lines.append("(Summary not available)")

                fit = result.fit_stats
                if fit:
                    lines.append("")
                    lines.append("Model Fit:")
                    for k, v in fit.items():
                        if isinstance(v, float):
                            lines.append(f"  {k}: {v:.3f}")
                        else:
                            lines.append(f"  {k}: {v}")

                diag = result.convergence_diagnostics
                if diag:
                    lines.append("")
                    lines.append("Convergence:")
                    divergent = diag.get("n_divergent", "?")
                    lines.append(f"  Divergent transitions: {divergent}")
                    rhat_info = diag.get("max_rhat", "?")
                    lines.append(f"  Max R-hat: {rhat_info}")

                session.bayesian_result = result
                lines.append("")
                lines.append("Bayesian results stored in session.")
                return "\n".join(lines)

            model_str = self._get_model_string(session)
            if model_str:
                bsem = BayesianSEM(model_str)
                priors = bsem.get_default_priors(data)
                lines = ["Bayesian SEM - Default Priors", "=" * 40, ""]
                for param, prior in priors.items():
                    lines.append(f"  {param}: {prior.name}({prior.params})")
                lines.append("")
                lines.append("Use 'bayesian fit' to run MCMC estimation.")
                lines.append("Options: 'bayesian fit draws=4000 tune=2000'")
                return "\n".join(lines)
            else:
                return "No model found. Please define a model first, then use 'bayesian fit'."

        except Exception as e:
            return f"Bayesian SEM failed: {e}"

    def _handle_multilevel(self, session, command: str) -> str:
        try:
            from core.multilevel_sem import MultilevelSEM, compute_icc, decompose_multilevel
        except ImportError:
            return "Multilevel SEM module not available. Install required packages: pip install pymc arviz"

        try:
            data = session.data
            if data is None:
                return "No data loaded."
            if len(data) < 20:
                return f"Insufficient data (N={len(data)}). Multilevel SEM requires at least 20 observations."

            cmd = command.lower()
            lines = ["Multilevel SEM Analysis", "=" * 40, ""]

            draft = session.draft if hasattr(session, "draft") else None
            cluster_var = None
            if draft:
                cluster_var = getattr(draft, "cluster_var", None) or getattr(draft, "group_var", None)
            if not cluster_var:
                for col in data.columns:
                    if data[col].dtype == object or (data[col].nunique() <= 20 and data[col].nunique() < len(data) * 0.1):
                        cluster_var = col
                        break
            if not cluster_var:
                return "No clustering variable detected. Specify a cluster/group variable (e.g., 'multilevel cluster=school')."

            if "icc" in cmd or "decompose" in cmd:
                icc = compute_icc(data, cluster_var)
                lines.append(f"Cluster variable: {cluster_var}")
                lines.append(f"N clusters: {data[cluster_var].nunique()}")
                lines.append("")
                lines.append("Intraclass Correlations (ICC):")
                for var, val in icc.items():
                    level = "high" if val > 0.15 else "moderate" if val > 0.05 else "low"
                    lines.append(f"  {var}: {val:.3f} ({level})")
                if all(v < 0.05 for v in icc.values()):
                    lines.append("")
                    lines.append("All ICCs < 0.05: multilevel structure may not be needed. Single-level SEM is sufficient.")
                return "\n".join(lines)

            model_str = self._get_model_string(session)
            if not model_str:
                return "No model found. Please define a model first, then use 'multilevel fit cluster=varname'."

            between_syntax = None
            for tok in cmd.split():
                if tok.startswith("between="):
                    between_syntax = tok.split("=")[1]

            mlsem = MultilevelSEM(within_syntax=model_str, between_syntax=between_syntax)
            method = "frequentist"
            if "bayesian" in cmd or "bayes" in cmd:
                method = "bayesian"

            lines.append(f"Cluster variable: {cluster_var}")
            lines.append(f"Method: {method}")
            lines.append("")

            if method == "bayesian":
                result = mlsem.fit_bayesian(data, cluster_var)
            else:
                result = mlsem.fit(data, cluster_var)

            lines.append(f"N clusters: {result.n_clusters}")
            lines.append(f"N observations: {result.n_obs}")
            lines.append("")

            lines.append("ICC values:")
            for var, val in result.icc.items():
                lines.append(f"  {var}: {val:.3f}")

            lines.append("")
            lines.append("Within-level fit:")
            for k, v in result.within_fit_stats.items():
                if isinstance(v, float):
                    lines.append(f"  {k}: {v:.3f}")

            lines.append("")
            lines.append("Between-level fit:")
            for k, v in result.between_fit_stats.items():
                if isinstance(v, float):
                    lines.append(f"  {k}: {v:.3f}")

            session.multilevel_result = result
            lines.append("")
            lines.append("Multilevel results stored in session.")
            return "\n".join(lines)

        except Exception as e:
            return f"Multilevel SEM failed: {e}"

    def _handle_dsem(self, session, command: str) -> str:
        try:
            from core.dsem import DSEM, simulate_dsem
        except ImportError:
            return "DSEM module not available. Install required packages."

        try:
            data = session.data
            if data is None:
                return "No data loaded."
            if len(data) < 20:
                return f"Insufficient data (N={len(data)}). DSEM requires at least 20 observations."

            cmd = command.lower()
            lines = ["Dynamic SEM (DSEM) Analysis", "=" * 40, ""]

            draft = session.draft if hasattr(session, "draft") else None
            person_var = None
            time_var = None
            variables = []

            for tok in cmd.split():
                if tok.startswith("person="):
                    person_var = tok.split("=")[1]
                elif tok.startswith("time="):
                    time_var = tok.split("=")[1]
                elif tok.startswith("vars="):
                    variables = tok.split("=")[1].split(",")

            if not person_var:
                for col in data.columns:
                    if any(k in col.lower() for k in ["person", "id", "subject", "participant"]):
                        person_var = col
                        break
            if not time_var:
                for col in data.columns:
                    if any(k in col.lower() for k in ["time", "wave", "occasion"]):
                        time_var = col
                        break

            if not person_var or not time_var:
                return "Need person and time variables. Specify: 'dsem person=id time=wave vars=y1,y2'"

            if not variables:
                numeric_cols = [c for c in data.select_dtypes(include=["number"]).columns
                                if c not in [person_var, time_var]]
                variables = numeric_cols[:5]

            lines.append(f"Person variable: {person_var}")
            lines.append(f"Time variable: {time_var}")
            lines.append(f"Variables: {variables}")
            n_persons = data[person_var].nunique()
            mean_times = len(data) / n_persons if n_persons > 0 else 0
            lines.append(f"N persons: {n_persons}, Mean observations/person: {mean_times:.0f}")
            lines.append("")

            method = "two_step"
            if "bayesian" in cmd or "bayes" in cmd:
                method = "bayesian"

            dsem = DSEM(variables=variables, time_var=time_var, person_var=person_var)
            prepared = dsem.prepare_data(data)
            lines.append(f"Prepared data: {len(prepared)} observations (after lagging)")
            lines.append("")

            stationarity = dsem.check_stationarity(prepared)
            lines.append("Stationarity check:")
            overall = stationarity.get("overall_nonstationary_proportion", "?")
            suggest = stationarity.get("suggest_differencing", False)
            lines.append(f"  Non-stationary proportion: {overall}")
            if suggest:
                lines.append("  WARNING: Some persons show non-stationarity. Consider differencing.")
            lines.append("")

            lines.append(f"Fitting DSEM ({method} method)...")
            result = dsem.fit(data, method=method)

            lines.append("")
            lines.append("DSEM Results:")
            lines.append(f"  N persons: {result.n_persons}")
            lines.append(f"  N observations: {result.n_observations}")

            if isinstance(result.within_parameters, pd.DataFrame) and not result.within_parameters.empty:
                lines.append("")
                lines.append("Within-person parameters (AR/Cross-lagged):")
                lines.append(result.within_parameters.to_string(max_rows=15))

            if isinstance(result.between_parameters, pd.DataFrame) and not result.between_parameters.empty:
                lines.append("")
                lines.append("Between-person parameters:")
                lines.append(result.between_parameters.to_string(max_rows=10))

            session.dsem_result = result
            lines.append("")
            lines.append("DSEM results stored in session.")
            return "\n".join(lines)

        except Exception as e:
            return f"DSEM failed: {e}"

    def _handle_mixture(self, session, command: str) -> str:
        try:
            from core.mixture_modeling import MixtureSEM, compute_entropy, profile_classes
        except ImportError:
            return "Mixture modeling module not available. Install scikit-learn: pip install scikit-learn"

        try:
            data = session.data
            if data is None:
                return "No data loaded."
            if len(data) < 30:
                return f"Insufficient data (N={len(data)}). Mixture SEM requires at least 30 observations."

            cmd = command.lower()
            lines = ["Mixture SEM Analysis", "=" * 40, ""]

            n_classes = 2
            for tok in cmd.split():
                if tok.startswith("k=") or tok.startswith("classes="):
                    try:
                        n_classes = int(tok.split("=")[1])
                    except ValueError:
                        pass

            if "select" in cmd or "compare" in cmd or "choose" in cmd:
                model_str = self._get_model_string(session)
                if not model_str:
                    return "No model found. Define a model first for class comparison."
                lines.append(f"Comparing models with 2-6 latent classes...")
                lines.append("")
                mix = MixtureSEM(model_syntax=model_str)
                comparison = mix.select_n_classes(data, min_k=2, max_k=6, method="classify_analyze")
                if "comparison_table" in comparison:
                    lines.append(comparison["comparison_table"].to_string())
                recommended = comparison.get("recommended_k", "N/A")
                reason = comparison.get("recommendation", "")
                lines.append("")
                lines.append(f"Recommended number of classes: {recommended}")
                if reason:
                    lines.append(reason)
                return "\n".join(lines)

            model_str = self._get_model_string(session)
            if not model_str:
                return "No model found. Please define a model first (e.g., CFA with measurement structure)."

            method = "classify_analyze"
            if "em" in cmd:
                method = "em"

            lines.append(f"N classes: {n_classes}")
            lines.append(f"Method: {method}")
            lines.append("")

            mix = MixtureSEM(model_syntax=model_str, n_classes=n_classes)
            result = mix.fit(data, n_classes=n_classes, method=method)

            lines.append(f"Class proportions:")
            for cls, prop in result.class_proportions.items():
                lines.append(f"  Class {cls}: {prop:.1%}")

            entropy = compute_entropy(result.class_assignments)
            lines.append(f"Classification entropy: {entropy:.3f}")
            if entropy > 0.8:
                lines.append("  Good classification quality.")
            elif entropy > 0.6:
                lines.append("  Moderate classification quality. Classes may overlap.")
            else:
                lines.append("  Low classification quality. Consider different k or model.")

            if isinstance(result.class_fit_stats, dict):
                lines.append("")
                lines.append("Per-class fit:")
                for cls, stats in result.class_fit_stats.items():
                    lines.append(f"  Class {cls}:")
                    for k, v in stats.items():
                        if isinstance(v, float) and not np.isnan(v):
                            lines.append(f"    {k}: {v:.3f}")

            profiles = profile_classes(data, result.class_assignments)
            if isinstance(profiles, pd.DataFrame) and not profiles.empty:
                lines.append("")
                lines.append("Class profiles (means):")
                lines.append(profiles.to_string(max_rows=20))

            session.mixture_result = result
            lines.append("")
            lines.append("Mixture SEM results stored in session.")
            lines.append("Use 'mixture select k=2-6' to compare different numbers of classes.")
            return "\n".join(lines)

        except Exception as e:
            return f"Mixture SEM failed: {e}"

    def _get_model_string(self, session) -> Optional[str]:
        advanced_results = getattr(session, 'advanced_results', {}) or {}
        for key in ['cfa', 'secondorder', 'growth', 'mediation',
                    'multigroup', 'multiplemediation', 'pathanalysis',
                    'crosslagged', 'efa', 'riclpm', 'rilta', 'esem', 'psem']:
            result = advanced_results.get(key)
            if result and hasattr(result, 'model_string'):
                return result.model_string
        if hasattr(session, 'results') and session.results:
            return session.results.get('model_string')
        if hasattr(session, 'draft') and session.draft:
            draft = session.draft
            if hasattr(draft, 'model_syntax'):
                return draft.model_syntax
        return None

    def _extract_crosslagged_structure(self, ts_vars: List[str],
                                       all_cols: List[str]) -> Tuple[List[str], List[str]]:
        """Extract base variable names and time point labels from detected time-series vars."""
        prefix_map = {}
        for var in ts_vars:
            m = re.match(r'^(.+?)_+(t\d+|wave\d+|time\d+|\d+)$', var, re.IGNORECASE)
            if m:
                prefix = m.group(1)
                tp = m.group(2)
                prefix_map.setdefault(prefix, []).append(tp)
            else:
                m2 = re.match(r'^([a-zA-Z]+)_?(\d+)$', var)
                if m2:
                    prefix = m2.group(1)
                    tp = m2.group(2)
                    prefix_map.setdefault(prefix, []).append(tp)

        if not prefix_map:
            return [], []

        all_time_points = set()
        for tps in prefix_map.values():
            all_time_points.update(tps)

        def sort_key(tp):
            m = re.search(r'(\d+)', tp)
            return int(m.group(1)) if m else 0

        time_points = sorted(all_time_points, key=sort_key)
        base_vars = list(prefix_map.keys())

        return base_vars, time_points

    def _infer_multiple_mediation_chain(self, paths: List[Tuple[str, str]],
                                         session=None) -> Optional[Dict]:
        """Infer a multiple mediation chain from path list."""
        graph = {}
        targets = set()
        for src, dst in paths:
            graph.setdefault(src, []).append(dst)
            targets.add(dst)

        sources = set(graph.keys()) - targets
        if not sources:
            return None

        cause = None
        mediators = []
        outcome = None

        for src in sources:
            dsts = graph[src]
            downstream = []
            for d in dsts:
                if d in graph:
                    downstream.extend(graph[d])
            if downstream:
                cause = src
                mediators = dsts
                outcome = downstream[0]
                break

        if not cause or not mediators or not outcome:
            return None

        return {'cause': [cause], 'mediators': mediators, 'outcome': [outcome]}

    def _parse_mediation_command(self, parts: List[str]) -> Optional[Dict]:
        """Parse a mediation command into user_vars dict.
        Expected formats: 'mediation X M1 M2 Y' or 'multiple mediation X M1 M2 Y'
        """
        tokens = [t for t in parts if t.lower() not in (
            'mediation', 'multiple', 'parallel', '中介'
        )]
        if len(tokens) >= 4:
            cause = tokens[0]
            outcome = tokens[-1]
            mediators = tokens[1:-1]
            return {'cause': [cause], 'mediators': mediators, 'outcome': [outcome]}
        elif len(tokens) == 3:
            return {'cause': [tokens[0]], 'mediators': [tokens[1]], 'outcome': [tokens[2]]}
        return None

    def _human_readable_strategy(self, strategy_token: str) -> str:
        labels = {
            'listwise_deletion_or_fiml': 'FIML (Full Information Maximum Likelihood) — little missing data',
            'fiml': 'FIML (Full Information Maximum Likelihood)',
            'fiml_or_mi': 'FIML or Multiple Imputation (both valid for this level of missingness)',
            'mi': 'Multiple Imputation (recommended for this level of missingness)',
            'drop_or_sensitivity': 'Multiple Imputation with sensitivity analysis — very high missingness',
        }
        return labels.get(strategy_token, strategy_token)
