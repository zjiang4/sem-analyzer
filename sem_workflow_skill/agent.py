"""
SEM Workflow Agent: Interactive assistant for SEM analysis

This class provides the main interface for guiding researchers through
the complete SEM workflow from data upload through results interpretation.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
import warnings


class SEMWorkflowAgent:
    """
    Interactive SEM workflow assistant.

    Guides researchers through:
    - Data exploration and preparation
    - Model specification based on theory
    - Model fitting and diagnostics
    - Results interpretation and reporting

    Attributes:
        data (pd.DataFrame): The loaded dataset
        theory (dict): User's theoretical model
        model_desc (str): semopy model description string
        model (semopy.Model): Fitted semopy model
        fit_stats (pd.DataFrame): Model fit statistics
        parameter_estimates (pd.DataFrame): Parameter estimates
    """

    def __init__(self):
        """Initialize the agent."""
        self.data = None
        self.theory = {}
        self.model_desc = None
        self.model = None
        self.fit_stats = None
        self.parameter_estimates = None

    def load_data(self, filepath: str) -> Tuple[pd.DataFrame, Dict]:
        """
        Load CSV data and perform initial inspection.

        Args:
            filepath: Path to CSV file

        Returns:
            Tuple of (data, initial_inspection_dict)
        """
        try:
            data = pd.read_csv(filepath)
        except Exception as e:
            raise ValueError(f"Failed to load data: {e}")

        self.data = data

        # Initial inspection
        inspection = {
            "n_rows": len(data),
            "n_cols": len(data.columns),
            "columns": list(data.columns),
            "dtypes": data.dtypes.to_dict(),
            "missing_per_col": data.isnull().sum().to_dict(),
            "missing_total": data.isnull().sum().sum(),
            "missing_percent": (
                data.isnull().sum().sum() / (len(data) * len(data.columns))
            )
            * 100,
        }

        return data, inspection

    def assess_missing_data(self, data: pd.DataFrame) -> Dict:
        """
        Assess missing data patterns and provide recommendations.

        Args:
            data: The dataset

        Returns:
            Dictionary with missing data analysis
        """
        missing_analysis = {}

        # Overall missingness
        total_missing = data.isnull().sum().sum()
        total_cells = len(data) * len(data.columns)
        missing_percent = (total_missing / total_cells) * 100

        missing_analysis["total_missing"] = total_missing
        missing_analysis["missing_percent"] = missing_percent

        # Pattern analysis
        missing_per_row = data.isnull().sum(axis=1)
        complete_cases = (missing_per_row == 0).sum()

        missing_analysis["complete_cases"] = complete_cases
        missing_analysis["complete_percent"] = (complete_cases / len(data)) * 100

        # Recommendations
        if missing_percent < 5:
            missing_analysis["recommendation"] = (
                "Low missingness (<5%). Listwise deletion acceptable, or use FIML (default in semopy)."
            )
        elif missing_percent < 20:
            missing_analysis["recommendation"] = (
                "Moderate missingness (5-20%). Use FIML (recommended) or multiple imputation."
            )
        else:
            missing_analysis["recommendation"] = (
                "High missingness (>20%). Consider multiple imputation or data collection issues."
            )

        return missing_analysis

    def get_theory_from_user(self) -> Dict:
        """
        Interactively gather theoretical model from user.

        Returns:
            Dictionary with model specification
        """
        theory = {"latent_variables": {}, "structural_paths": [], "covariances": []}

        return theory

    def validate_theory(
        self, theory: Dict, data: pd.DataFrame
    ) -> Tuple[bool, List[str]]:
        """
        Validate theoretical model against data.

        Args:
            theory: User's theoretical specification
            data: The dataset

        Returns:
            Tuple of (is_valid, list_of_issues)
        """
        issues = []

        # Check if all variables in theory exist in data
        all_vars = set()
        for latent, indicators in theory["latent_variables"].items():
            all_vars.update(indicators)

        missing_vars = all_vars - set(data.columns)
        if missing_vars:
            issues.append(f"Variables in theory not found in data: {missing_vars}")

        # Check if each latent has sufficient indicators (min 3 recommended)
        for latent, indicators in theory["latent_variables"].items():
            if len(indicators) < 3:
                issues.append(
                    f"Latent variable '{latent}' has only {len(indicators)} indicators. Minimum 3 recommended for identification."
                )

        # Check sample size vs parameters
        n_parameters = self._count_parameters(theory)
        n_cases = len(data)
        if n_cases < 10 * n_parameters:
            issues.append(
                f"Sample size warning: {n_cases} cases for {n_parameters} parameters. Rule of thumb: N ≥ 10×parameters."
            )
        elif n_cases < 200:
            issues.append(
                f"Sample size caution: {n_cases} cases. For stable estimates, N ≥ 200 recommended."
            )

        is_valid = len(issues) == 0
        return is_valid, issues

    def _count_parameters(self, theory: Dict) -> int:
        """
        Count number of parameters in the model.

        Args:
            theory: Theoretical model specification

        Returns:
            Number of free parameters
        """
        count = 0

        # Measurement model parameters
        for latent, indicators in theory["latent_variables"].items():
            # First loading fixed to 1.0, rest free
            count += len(indicators) - 1

        # Structural paths
        count += len(theory["structural_paths"])

        # Covariances
        count += len(theory["covariances"])

        # Variances (one per variable)
        all_vars = set()
        for indicators in theory["latent_variables"].values():
            all_vars.update(indicators)
        count += len(all_vars)

        return count

    def build_model_description(self, theory: Dict) -> str:
        """
        Build semopy model description from theory.

        Args:
            theory: Theoretical model specification

        Returns:
            semopy model description string
        """
        lines = []

        # Add comments
        lines.append("# Measurement model")
        for latent, indicators in theory["latent_variables"].items():
            # First indicator gets fixed loading (implicit)
            latent_str = f"{latent} =~ {' + '.join(indicators)}"
            lines.append(latent_str)

        # Add structural paths
        if theory["structural_paths"]:
            lines.append("")
            lines.append("# Structural model")
            for path in theory["structural_paths"]:
                lines.append(f"{path['outcome']} ~ {' + '.join(path['predictors'])}")

        # Add covariances
        if theory["covariances"]:
            lines.append("")
            lines.append("# Residual correlations")
            for cov in theory["covariances"]:
                lines.append(f"{cov['var1']} ~~ {cov['var2']}")

        # Add factor covariances
        if len(theory["latent_variables"]) > 1:
            lines.append("")
            lines.append("# Factor correlations")
            latents = list(theory["latent_variables"].keys())
            for i in range(len(latents)):
                for j in range(i + 1, len(latents)):
                    lines.append(f"{latents[i]} ~~ {latents[j]}")

        self.model_desc = "\n".join(lines)
        return self.model_desc

    def fit_model(self, data: pd.DataFrame, obj: str = "MLW", solver: str = "SLSQP"):
        """
        Fit the SEM model to data.

        Args:
            data: The dataset
            obj: Objective function ('MLW', 'ULS', 'GLS', 'WLS', 'DWLS', 'FIML')
            solver: Optimization method ('SLSQP' default)

        Returns:
            Tuple of (success, results_dict)
        """
        try:
            from semopy import Model, calc_stats
        except ImportError:
            raise ImportError(
                "semopy is not installed. Install with: pip install semopy"
            )

        model = Model(self.model_desc)
        results = model.fit(data, obj=obj, solver=solver)

        self.model = model
        self.parameter_estimates = model.inspect()

        success = results is not None and "Optimization successful" in str(results)

        results_dict = {
            "success": success,
            "results": results,
            "objective": obj,
            "solver": solver,
        }

        return success, results_dict

    def get_fit_indices(self) -> pd.DataFrame:
        """
        Calculate and interpret fit indices.

        Returns:
            DataFrame with fit indices and interpretation
        """
        try:
            import semopy
        except ImportError:
            raise ImportError("semopy is not installed")

        stats = semopy.calc_stats(self.model)

        # Convert to DataFrame if needed
        if not isinstance(stats, pd.DataFrame):
            stats = pd.DataFrame([stats])

        self.fit_stats = stats

        # Add interpretation
        if "chi2" in stats.columns or "chi2" in stats.index:
            chi2 = stats.get("chi2", stats.at[0, "chi2"] if "chi2" in stats.index else None)
            if chi2 is not None:
                p_value = stats.get(
                    "chi2 p-value",
                    stats.at[0, "chi2 p-value"]
                    if "chi2 p-value" in stats.index
                    else None,
                )

        return stats

    def interpret_fit(self) -> Dict:
        """
        Interpret model fit based on common cutoffs.

        Returns:
            Dictionary with interpretation
        """
        if self.fit_stats is None:
            self.get_fit_indices()

        fit_interpretation = {
            "overall_fit": "Unknown",
            "issues": [],
            "recommendations": [],
        }

        # Get key indices
        stats = self.fit_stats

        # Helper function to extract scalar value from DataFrame/Series/dict
        def _get_value(key, default):
            val = stats.get(key, default)
            # If it's a Series or DataFrame, extract scalar
            if isinstance(val, (pd.Series, pd.DataFrame)):
                if isinstance(val, pd.DataFrame):
                    # Try to get from columns or index
                    if key in val.columns:
                        val = val[key].iloc[0]
                    elif key in val.index:
                        val = val.loc[key].iloc[0] if hasattr(val.loc[key], 'iloc') else val.loc[key]
                    else:
                        val = default
                else:  # Series
                    val = val.iloc[0] if len(val) > 0 else default
            return val

        rmsea = _get_value("RMSEA", 1.0)
        cfi = _get_value("CFI", 0.0)
        tli = _get_value("TLI", 0.0)
        srmr = _get_value("SRMR", 0.1)

        # RMSEA interpretation
        if rmsea < 0.05:
            rmsea_interp = "Excellent"
        elif rmsea < 0.08:
            rmsea_interp = "Good"
        elif rmsea < 0.10:
            rmsea_interp = "Acceptable"
        else:
            rmsea_interp = "Poor"
            fit_interpretation["issues"].append("RMSEA indicates poor fit (>0.10)")

        # CFI/TLI interpretation
        if cfi >= 0.95:
            cfi_interp = "Excellent"
        elif cfi >= 0.90:
            cfi_interp = "Good"
        elif cfi >= 0.80:
            cfi_interp = "Acceptable"
        else:
            cfi_interp = "Poor"
            fit_interpretation["issues"].append("CFI indicates poor fit (<0.80)")

        # SRMR interpretation
        if srmr < 0.08:
            srmr_interp = "Good"
        elif srmr < 0.10:
            srmr_interp = "Acceptable"
        else:
            srmr_interp = "Poor"
            fit_interpretation["issues"].append("SRMR indicates poor fit (>0.10)")

        # Overall fit
        if rmsea < 0.08 and cfi >= 0.90 and tli >= 0.90 and srmr < 0.10:
            fit_interpretation["overall_fit"] = "Good"
        else:
            fit_interpretation["overall_fit"] = "Poor"

        return fit_interpretation

    def explain_parameters(self) -> Dict:
        """
        Explain parameter estimates for user.

        Returns:
            Dictionary with organized parameter explanations
        """
        if self.parameter_estimates is None:
            return {"error": "Model not fitted yet"}

        explanation = {
            "measurement_model": {},
            "structural_model": {},
            "problematic": [],
        }

        # Helper to convert value to float safely
        def to_float(val, default=0.0):
            if isinstance(val, (int, float)):
                return float(val)
            if isinstance(val, str):
                # Handle special string formats like "<0.001"
                val_str = val.strip()
                if val_str.startswith('<'):
                    try:
                        return float(val_str[1:])
                    except:
                        return 0.001
                elif val_str.startswith('>'):
                    try:
                        return float(val_str[1:])
                    except:
                        return 0.999
                else:
                    try:
                        return float(val_str)
                    except:
                        return default
            return default

        # Separate measurement and structural paths
        for idx, row in self.parameter_estimates.iterrows():
            lval = row["lval"]
            rval = row["rval"]
            op = row["op"]

            # Convert numeric fields
            estimate = to_float(row["Estimate"])
            std_err = to_float(row["Std. Err"])
            p_val_raw = row["p-value"]
            p_value = to_float(p_val_raw)
            z_value = to_float(row["z-value"])

            # Determine parameter type using semopy's op and variable types
            # Measurement model: indicator ~ factor (lval is observed, rval is latent)
            # Structural model: outcome ~ predictor (lval is latent outcome)

            latent_vars = set(self.theory.get("latent_variables", {}).keys())
            observed_vars = set(self.data.columns) if self.data is not None else set()

            if op == "~":
                # Check if this is a factor loading (measurement) or path (structural)
                if lval in observed_vars and rval in latent_vars:
                    # Measurement model: factor =~ indicator
                    factor = rval
                    indicator = lval

                    if indicator not in explanation["measurement_model"]:
                        explanation["measurement_model"][indicator] = []
                    explanation["measurement_model"][indicator].append(
                        {
                            "indicator": indicator,
                            "factor": factor,
                            "estimate": estimate,
                            "std_error": std_err,
                            "p_value": p_value,
                            "z_value": z_value,
                            "significant": p_value < 0.05,
                        }
                    )

                    # Check loading quality
                    standardized = row.get("Value std", estimate)
                    if isinstance(standardized, str):
                        standardized = to_float(standardized, estimate)
                    std_abs = abs(standardized)
                    if std_abs < 0.5:
                        explanation["problematic"].append(
                            f"Low loading: {indicator} → {factor} ({standardized:.3f})"
                        )
                    elif std_abs > 1.0:
                        explanation["problematic"].append(
                            f"Problematic loading >1.0: {indicator} → {factor} ({standardized:.3f})"
                        )
                else:
                    # Structural model: outcome ~ predictor
                    outcome = lval
                    predictor = rval

                    if outcome not in explanation["structural_model"]:
                        explanation["structural_model"][outcome] = []

                    explanation["structural_model"][outcome].append(
                        {
                            "from": predictor,
                            "to": outcome,
                            "estimate": estimate,
                            "std_error": std_err,
                            "p_value": p_value,
                            "z_value": z_value,
                            "significant": p_value < 0.05,
                            "effect_size": self._interpret_effect_size(estimate),
                        }
                    )
            elif op == "~~":
                # Covariances: optionally handle
                pass

        return explanation

    def _interpret_effect_size(self, standardized_estimate: float) -> str:
        """
        Interpret standardized effect size using Cohen's conventions.

        Args:
            standardized_estimate: Standardized path coefficient

        Returns:
            Effect size interpretation string
        """
        abs_est = abs(standardized_estimate)

        if abs_est < 0.1:
            return "Very small"
        elif abs_est < 0.3:
            return "Small"
        elif abs_est < 0.5:
            return "Medium"
        else:
            return "Large"

    def _to_float(self, val, default=0.0):
        """
        Safely convert any value to float, handling special string formats.

        Handles p-values like "<0.001", ">0.999", etc.
        """
        if isinstance(val, (int, float)):
            return float(val)
        if isinstance(val, str):
            val_str = val.strip()
            if val_str.startswith('<'):
                try:
                    return float(val_str[1:])
                except:
                    return 0.001
            elif val_str.startswith('>'):
                try:
                    return float(val_str[1:])
                except:
                    return 0.999
            else:
                try:
                    return float(val_str)
                except:
                    return default
        return default

    def generate_report(self, output_file: str = None) -> str:
        """
        Generate comprehensive analysis report.

        Args:
            output_file: Optional path to save report

        Returns:
            Report text
        """
        report_lines = []
        report_lines.append("=" * 80)
        report_lines.append("STRUCTURAL EQUATION MODELING ANALYSIS REPORT")
        report_lines.append("=" * 80)
        report_lines.append("")

        # Data summary
        report_lines.append("1. DATA SUMMARY")
        report_lines.append("-" * 80)
        report_lines.append(f"Sample size: {len(self.data)}")
        report_lines.append(f"Variables: {len(self.data.columns)}")
        report_lines.append("")

        # Model specification
        report_lines.append("2. MODEL SPECIFICATION")
        report_lines.append("-" * 80)
        report_lines.append("Measurement Model:")
        for latent, indicators in self.theory.get("latent_variables", {}).items():
            report_lines.append(f"  {latent} =~ {' + '.join(indicators)}")
        report_lines.append("")

        if self.theory.get("structural_paths"):
            report_lines.append("Structural Model:")
            for path in self.theory["structural_paths"]:
                report_lines.append(
                    f"  {path['outcome']} ~ {' + '.join(path['predictors'])}"
                )
            report_lines.append("")

        # Fit indices
        report_lines.append("3. MODEL FIT")
        report_lines.append("-" * 80)
        fit_interp = self.interpret_fit()
        report_lines.append(f"Overall fit: {fit_interp['overall_fit']}")

        for idx, row in self.fit_stats.iterrows():
            report_lines.append(f"  {idx}: {row.get('Value', row.values[0]):.4f}")

        if fit_interp["issues"]:
            report_lines.append("")
            report_lines.append("Fit concerns:")
            for issue in fit_interp["issues"]:
                report_lines.append(f"  - {issue}")

        # Parameter estimates
        report_lines.append("")
        report_lines.append("4. PARAMETER ESTIMATES")
        report_lines.append("-" * 80)

        param_exp = self.explain_parameters()

        if "measurement_model" in param_exp:
            report_lines.append("Measurement Model (Factor Loadings):")
            for latent, loadings in param_exp["measurement_model"].items():
                report_lines.append(f"\n  {latent}:")
                for loading in loadings:
                    sig_marker = "*" if loading["significant"] else ""
                    report_lines.append(
                        f"    {loading['indicator']} → {loading['factor']}: "
                        f"{loading['estimate']:.4f} (SE={loading['std_error']:.4f}, "
                        f"z={loading['z_value']:.2f}, p={loading['p_value']:.4f}){sig_marker}"
                    )
            report_lines.append("\n  * p < 0.05")

        if "structural_model" in param_exp:
            report_lines.append("\nStructural Model (Path Coefficients):")
            for outcome, paths in param_exp["structural_model"].items():
                for path in paths:
                    sig_marker = "*" if path["significant"] else ""
                    report_lines.append(
                        f"  {path['from']} → {path['to']}: "
                        f"{path['estimate']:.4f} (SE={path['std_error']:.4f}, "
                        f"z={path['z_value']:.2f}, p={path['p_value']:.4f}) "
                        f"[{path['effect_size']} effect]{sig_marker}"
                    )
            report_lines.append("\n  * p < 0.05")

        if param_exp["problematic"]:
            report_lines.append("\n5. CONCERNS")
            report_lines.append("-" * 80)
            for concern in param_exp["problematic"]:
                report_lines.append(f"  - {concern}")

        # Recommendations
        report_lines.append("")
        report_lines.append("6. RECOMMENDATIONS")
        report_lines.append("-" * 80)
        fit_interp = self.interpret_fit()
        for rec in fit_interp.get("recommendations", []):
            report_lines.append(f"  - {rec}")

        report_lines.append("")
        report_lines.append("=" * 80)

        report = "\n".join(report_lines)

        if output_file:
            with open(output_file, "w") as f:
                f.write(report)

        return report

    def bootstrap_confidence_intervals(
        self,
        data: pd.DataFrame = None,
        n_bootstrap: int = 1000,
        alpha: float = 0.05,
        random_state: int = 42
    ) -> pd.DataFrame:
        """
        Calculate bootstrap confidence intervals for parameter estimates.

        Uses non-parametric bootstrap (resampling rows with replacement).

        Args:
            data: DataFrame to use (defaults to self.data)
            n_bootstrap: Number of bootstrap samples (default 1000)
            alpha: Significance level for CI (default 0.05 for 95% CI)
            random_state: Random seed for reproducibility

        Returns:
            DataFrame with columns:
            - parameter (e.g., 'sat1 ~ job_satisfaction')
            - estimate (original)
            - bootstrap_mean
            - bootstrap_std_error
            - ci_lower (percentile method)
            - ci_upper (percentile method)
            - bootstrap_samples (count of successful fits)
            - bootstrap_success_rate (%)

        Note: This can be time-consuming. For 1000 bootstrap samples,
        it fits the model 1000 times. Progress is printed during computation.
        """
        if data is None:
            data = self.data
        if self.model_desc is None:
            raise ValueError("No model specified. Build model description first.")
        if self.parameter_estimates is None:
            raise ValueError("Model not fitted yet. Run fit_model() first.")

        np.random.seed(random_state)

        # Store original estimates with parameter names
        original_params = {}
        for idx, row in self.parameter_estimates.iterrows():
            param_name = f"{row['lval']} {row['op']} {row['rval']}"
            original_params[param_name] = self._to_float(row["Estimate"])

        # Collect bootstrap estimates
        bootstrap_estimates = {param: [] for param in original_params.keys()}

        try:
            from semopy import Model, calc_stats
        except ImportError:
            raise ImportError("semopy is required for bootstrap")

        print(f"\n[Bootstrap] Starting {n_bootstrap} bootstrap samples...")
        print("  This may take a while. Progress: ", end="", flush=True)

        success_count = 0
        for i in range(n_bootstrap):
            # Sample with replacement
            boot_data = data.sample(frac=1.0, replace=True, random_state=random_state+i)

            try:
                model = Model(self.model_desc)
                results = model.fit(boot_data, obj='MLW', solver='SLSQP')
                if results is not None:
                    success_count += 1
                    boot_params = model.inspect()
                    for idx, row in boot_params.iterrows():
                        param_name = f"{row['lval']} {row['op']} {row['rval']}"
                        if param_name in bootstrap_estimates:
                            estimate = self._to_float(row["Estimate"])
                            bootstrap_estimates[param_name].append(estimate)
            except Exception:
                # Silently skip failed bootstrap iterations
                continue

            # Progress indicator every 100 iterations
            if (i + 1) % 100 == 0:
                print(f"{i+1}/{n_bootstrap}...", end="", flush=True)

        print(f" Done! ({success_count}/{n_bootstrap} successful fits)")

        # Build results DataFrame
        results_list = []
        ci_lower = alpha / 2 * 100
        ci_upper = (1 - alpha / 2) * 100

        for param, original in original_params.items():
            boot_vals = bootstrap_estimates[param]
            if len(boot_vals) > 0:
                mean_val = np.mean(boot_vals)
                std_val = np.std(boot_vals, ddof=1)
                ci_low = np.percentile(boot_vals, ci_lower)
                ci_high = np.percentile(boot_vals, ci_upper)
                success_rate = len(boot_vals) / n_bootstrap * 100
            else:
                mean_val = np.nan
                std_val = np.nan
                ci_low = np.nan
                ci_high = np.nan
                success_rate = 0.0

            results_list.append({
                'parameter': param,
                'estimate': original,
                'bootstrap_mean': mean_val,
                'bootstrap_std_error': std_val,
                'ci_lower': ci_low,
                'ci_upper': ci_high,
                'bootstrap_samples': len(boot_vals),
                'bootstrap_success_rate': success_rate
            })

        results_df = pd.DataFrame(results_list)
        self.bootstrap_results = results_df

        return results_df

    def test_measurement_invariance(
        self,
        data: pd.DataFrame = None,
        group_var: str = None,
        invariance_types: List[str] = ["configural"]
    ) -> Dict:
        """
        Test measurement invariance across groups (configural only).

        Args:
            data: DataFrame (default self.data)
            group_var: Column name for grouping
            invariance_types: Currently only 'configural' implemented.

        Returns:
            Dict with chi2, df, invariance_summary, summary
        """
        if data is None:
            data = self.data
        if group_var is None:
            raise ValueError("group_var must be specified")
        if group_var not in data.columns:
            raise ValueError(f"Group variable '{group_var}' not found")
        if self.model_desc is None:
            raise ValueError("No model specified")

        groups = sorted(data[group_var].unique())
        if len(groups) < 2:
            raise ValueError(f"Need >=2 groups, got {len(groups)}")

        print(f"\n[Measurement Invariance] {len(groups)} groups: {list(groups)}")

        total_chi2 = 0.0
        total_df = 0
        group_models = {}

        from semopy import Model, calc_stats
        for grp in groups:
            grp_data = data[data[group_var] == grp]
            print(f"\n  Group '{grp}' (n={len(grp_data)}):")
            model = Model(self.model_desc)
            try:
                res = model.fit(grp_data, obj='MLW', solver='SLSQP')
                stats = calc_stats(model)
                chi2 = self._to_float(stats.get('chi2', 0))
                df_val = self._to_float(stats.get('df', 0))
                total_chi2 += chi2
                total_df += df_val
                group_models[grp] = model
                print(f"    chi2 = {chi2:.2f}, df = {df_val}")
            except Exception as e:
                print(f"    Fit failed: {e}")
                group_models[grp] = None

        # Build result
        results = {
            'configural': {'chi2': total_chi2, 'df': total_df},
            'metric': None,
            'scalar': None,
            'chi2_differences': [],
            'invariance_summary': {'configural': True},
            'summary': f"Configural invariance: chi2={total_chi2:.2f}, df={total_df}"
        }

        return results

    def _create_mg_model_desc(self, groups: List) -> str:
        """Placeholder for advanced multi-group model generation."""
        return self.model_desc

    def _format_invariance_summary(self, results: Dict) -> str:
        """Format invariance results as a readable string."""
        return results.get('summary', '')

    def suggest_modifications(self, residual_threshold: float = 0.1) -> List[Dict]:
        """
        Get suggestions for model modifications based on residual analysis.

        Analyzes residuals between observed and model-implied covariances to
        identify indicator pairs with high residuals that could be freed.

        Args:
            residual_threshold: Threshold for normalized residual magnitude (default 0.1)

        Returns:
            List of modification suggestions, sorted by severity.
            Each suggestion includes: type, variables, residual_value, suggestion, caveat.

        Note: Always review suggestions theoretically before adding parameters.
        """
        from .diagnostics import SEMDiagnostics

        if self.model is None:
            raise ValueError("Model not fitted yet. Run fit_model() first.")

        suggestions = SEMDiagnostics.suggest_modifications(
            self.model, self.data, residual_threshold=residual_threshold
        )

        # Print summary
        print(f"\n[Modification Indices] Analysis complete")
        if suggestions:
            print(f"  Found {len(suggestions)} potential modifications:")
            for i, s in enumerate(suggestions[:5], 1):  # Show top 5
                print(f"  {i}. {s['suggestion']}")
            if len(suggestions) > 5:
                print(f"  ... and {len(suggestions)-5} more")
        else:
            print("  No problematic residuals detected.")

        return suggestions

    def analyze_mediation(self, mediator: str, outcome: str, predictor: str,
                          n_bootstrap: int = 1000, alpha: float = 0.05) -> Dict:
        """
        Analyze mediation effect: X (predictor) → M (mediator) → Y (outcome).

        This method tests whether the effect of X on Y is partially or fully
        transmitted through a mediator M. It calculates direct, indirect, and
        total effects, and uses bootstrap to obtain confidence intervals.

        Args:
            mediator: Name of the mediator variable (must be in the model)
            outcome: Name of the outcome variable (must be in the model)
            predictor: Name of the predictor variable (must be in the model)
            n_bootstrap: Number of bootstrap samples (default 1000)
            alpha: Significance level for CIs (default 0.05)

        Returns:
            Dictionary with:
                - direct_effect: Estimate of direct path X → Y
                - indirect_effect: Product of X → M and M → Y
                - total_effect: direct + indirect
                - direct_ci: (lower, upper) CI for direct effect
                - indirect_ci: (lower, upper) CI for indirect effect
                - total_ci: (lower, upper) CI for total effect
                - mediated: True if indirect effect is significant (CI excludes 0)
                - mediation_type: 'full', 'partial', or 'none'
                - bootstrap_success_rate: Percentage of successful bootstrap fits

        Raises:
            ValueError: If model not fitted or variables not found
        """
        if self.model is None:
            raise ValueError("Model not fitted yet. Run fit_model() first.")

        # Check if variables exist in model
        all_vars = set(self.model.vars['observed']) if hasattr(self.model, 'vars') else set()
        # Also check latent variables from theory
        if self.theory and 'latent_variables' in self.theory:
            all_vars.update(self.theory['latent_variables'].keys())

        for var in [mediator, outcome, predictor]:
            if var not in all_vars:
                raise ValueError(f"Variable '{var}' not found in model variables")

        # Get the parameter estimates
        if self.parameter_estimates is None:
            raise ValueError("No parameter estimates available")

        estimates = self.parameter_estimates

        # Extract the two paths needed for indirect effect
        # Path a: predictor → mediator
        path_a_mask = (estimates['lval'] == mediator) & (estimates['rval'] == predictor)
        # Path b: outcome ← mediator
        path_b_mask = (estimates['lval'] == outcome) & (estimates['rval'] == mediator)
        # Direct path c': outcome ← predictor
        path_c_mask = (estimates['lval'] == outcome) & (estimates['rval'] == predictor)

        path_a = estimates[path_a_mask]
        path_b = estimates[path_b_mask]
        path_c = estimates[path_c_mask]

        if len(path_a) == 0:
            raise ValueError(f"Path {predictor} → {mediator} not found in model")
        if len(path_b) == 0:
            raise ValueError(f"Path {mediator} → {outcome} not found in model")

        # Get estimates
        a_est = path_a['Estimate'].values[0]
        b_est = path_b['Estimate'].values[0]
        indirect_est = a_est * b_est

        direct_est = 0.0
        if len(path_c) > 0:
            direct_est = path_c['Estimate'].values[0]
        total_est = direct_est + indirect_est

        # Use bootstrap CIs from existing bootstrap method
        bootstrap_df = self.bootstrap_confidence_intervals(
            data=self.data,
            n_bootstrap=n_bootstrap,
            alpha=alpha
        )

        # Extract CIs for relevant parameters
        def get_ci(param_name: str):
            matches = bootstrap_df[bootstrap_df['parameter'] == param_name]
            if len(matches) > 0:
                row = matches.iloc[0]
                return (row['ci_lower'], row['ci_upper'])
            return (np.nan, np.nan)

        # Get parameter names as they appear in bootstrap output
        # They might be formatted like "mediator ~ predictor"
        a_param = f"{mediator} ~ {predictor}"
        b_param = f"{outcome} ~ {mediator}"
        c_param = f"{outcome} ~ {predictor}"

        a_ci = get_ci(a_param)
        b_ci = get_ci(b_param)
        c_ci = get_ci(c_param)

        # For indirect effect, we need to compute CI from bootstrap distribution
        # The bootstrap_confidence_intervals method returns individual parameters,
        # not products. We'll compute indirect effect CI manually from the bootstrap
        # samples if we can access the distribution. But our method only returns
        # summary stats. So we'll approximate using the delta method:
        # SE(indirect) ≈ sqrt( (b*SE(a))^2 + (a*SE(b))^2 )
        # CI = estimate ± z * SE

        a_se = bootstrap_df[bootstrap_df['parameter'] == a_param]['bootstrap_std_error'].values[0] if len(bootstrap_df[bootstrap_df['parameter'] == a_param]) > 0 else np.nan
        b_se = bootstrap_df[bootstrap_df['parameter'] == b_param]['bootstrap_std_error'].values[0] if len(bootstrap_df[bootstrap_df['parameter'] == b_param]) > 0 else np.nan

        if not np.isnan(a_se) and not np.isnan(b_se):
            # Approximate SE of product using delta method
            indirect_se = np.sqrt((b_est * a_se)**2 + (a_est * b_se)**2)
            z_val = 1.96 if alpha == 0.05 else 2.576  # 95% or 99% CI
            indirect_ci = (indirect_est - z_val * indirect_se, indirect_est + z_val * indirect_se)
        else:
            indirect_ci = (np.nan, np.nan)

        direct_se = bootstrap_df[bootstrap_df['parameter'] == c_param]['bootstrap_std_error'].values[0] if len(bootstrap_df[bootstrap_df['parameter'] == c_param]) > 0 else np.nan
        if not np.isnan(direct_se):
            z_val = 1.96 if alpha == 0.05 else 2.576
            direct_ci = (direct_est - z_val * direct_se, direct_est + z_val * direct_se)
        else:
            direct_ci = (np.nan, np.nan)

        total_se = np.sqrt(direct_se**2 + indirect_se**2) if not np.isnan(direct_se) and not np.isnan(indirect_se) else np.nan
        if not np.isnan(total_se):
            z_val = 1.96 if alpha == 0.05 else 2.576
            total_ci = (total_est - z_val * total_se, total_est + z_val * total_se)
        else:
            total_ci = (np.nan, np.nan)

        # Determine mediation type
        mediated = not (indirect_ci[0] <= 0 <= indirect_ci[1])  # CI excludes 0
        if mediated:
            if direct_ci[0] <= 0 <= direct_ci[1]:  # direct effect non-significant
                mediation_type = "full"
            else:
                mediation_type = "partial"
        else:
            mediation_type = "none"

        avg_success = bootstrap_df['bootstrap_success_rate'].mean() if 'bootstrap_success_rate' in bootstrap_df.columns else 100.0

        result = {
            'path_a': a_est,
            'path_b': b_est,
            'path_c_direct': direct_est,
            'indirect_effect': indirect_est,
            'total_effect': total_est,
            'direct_ci': direct_ci,
            'indirect_ci': indirect_ci,
            'total_ci': total_ci,
            'mediated': mediated,
            'mediation_type': mediation_type,
            'variables': {
                'mediator': mediator,
                'outcome': outcome,
                'predictor': predictor
            },
            'bootstrap_samples': n_bootstrap,
            'bootstrap_success_rate': avg_success
        }

        # Print summary
        print("\n[Mediation Analysis]")
        print(f"  Model: {predictor} → {mediator} → {outcome}")
        print(f"  Path a ({predictor} → {mediator}): {a_est:.3f}")
        print(f"  Path b ({mediator} → {outcome}): {b_est:.3f}")
        print(f"  Direct effect c' ({predictor} → {outcome}): {direct_est:.3f}")
        print(f"  Indirect effect (a×b): {indirect_est:.3f}")
        print(f"  Total effect: {total_est:.3f}")
        print(f"  Indirect effect 95% CI: [{indirect_ci[0]:.3f}, {indirect_ci[1]:.3f}]")
        if mediated:
            print(f"  ✓ Mediation is {'statistically significant' if mediated else 'not significant'}")
            print(f"  Type: {mediation_type} mediation")
        else:
            print(f"  ✗ No mediation detected (indirect effect CI includes 0)")

        return result

    def interactive_workflow(self, filepath: str):
        """
        Run the complete interactive workflow with a user.

        This is the main entry point for interacting with researchers.
        """
        print("\n" + "=" * 80)
        print("SEM WORKFLOW AGENT")
        print("=" * 80)
        print("\nThis agent will guide you through structural equation modeling")
        print("using the semopy package in Python.\n")

        # Step 1: Load data
        print("Step 1: Loading data...")
        data, inspection = self.load_data(filepath)

        print(f"\nData loaded successfully!")
        print(f"  Rows: {inspection['n_rows']}")
        print(f"  Columns: {inspection['n_cols']}")
        print(
            f"  Missing data: {inspection['missing_total']} cells ({inspection['missing_percent']:.1f}%)"
        )

        # Step 2: Assess missing data
        print("\nStep 2: Assessing missing data...")
        missing_analysis = self.assess_missing_data(data)

        print(f"\nMissing data analysis:")
        print(
            f"  Complete cases: {missing_analysis['complete_cases']} ({missing_analysis['complete_percent']:.1f}%)"
        )
        print(f"  Recommendation: {missing_analysis['recommendation']}")

        # Step 3: Get theory
        print("\nStep 3: Specifying theoretical model...")
        print("\nPlease provide your theoretical model:")
        print("1. What are your latent variables (constructs)?")
        print("2. Which observed variables (indicators) measure each construct?")
        print("3. Are there any structural relationships between constructs?")
        print("4. Any correlations you expect between indicators or factors?\n")

        # In interactive mode, we would ask questions here
        # For now, we'll use a placeholder
        print("\nFor this demo, we'll use a simple example theory.")
        self.theory = {
            "latent_variables": {
                "factor1": ["x1", "x2", "x3"],
                "factor2": ["y1", "y2", "y3"],
            },
            "structural_paths": [{"outcome": "factor2", "predictors": ["factor1"]}],
            "covariances": [],
        }

        print("\nTheoretical model specified:")
        print("  factor1 =~ x1 + x2 + x3")
        print("  factor2 =~ y1 + y2 + y3")
        print("  factor2 ~ factor1\n")

        # Step 4: Validate theory
        print("Step 4: Validating theory against data...")
        is_valid, issues = self.validate_theory(self.theory, data)

        if not is_valid:
            print("\n⚠️  Issues found:")
            for issue in issues:
                print(f"  - {issue}")
            print("\nPlease address these issues before proceeding.\n")
            return False

        print("\nOK Theory is valid for this data.\n")

        # Step 5: Build model
        print("Step 5: Building SEM model...")
        self.build_model_description(self.theory)
        print("Model description created:")
        print("-" * 40)
        print(self.model_desc)
        print("-" * 40)

        # Step 6: Fit model
        print("\nStep 6: Fitting model to data...")
        success, results = self.fit_model(data)

        if not success:
            print("\n❌ Model fitting failed!")
            print(f"Results: {results['results']}")
            print("\nTry:")
            print("  1. Checking for multicollinearity")
            print("  2. Simplifying the model")
            print("  3. Trying different optimization settings")
            return False

        print("\nOK Model fitted successfully!")
        print(f"  Optimizer: {results['solver']}")
        print(f"  Objective: {results['objective']}")
        print(f"  Results: {results['results']}")

        # Step 7: Diagnostics
        print("\nStep 7: Assessing model fit...")
        self.get_fit_indices()

        fit_interp = self.interpret_fit()
        print(f"\nOverall fit: {fit_interp['overall_fit']}")
        print(f"  RMSEA: {self.fit_stats.get('RMSEA', 'N/A'):.3f}")
        print(f"  CFI: {self.fit_stats.get('CFI', 'N/A'):.3f}")
        print(f"  TLI: {self.fit_stats.get('TLI', 'N/A'):.3f}")
        print(f"  SRMR: {self.fit_stats.get('SRMR', 'N/A'):.3f}")

        if fit_interp["issues"]:
            print("\n⚠️  Fit concerns:")
            for issue in fit_interp["issues"]:
                print(f"  - {issue}")

        # Step 8: Interpret results
        print("\nStep 8: Interpreting parameter estimates...")
        param_exp = self.explain_parameters()

        print("\nStructural paths:")
        if "structural_model" in param_exp:
            for outcome, paths in param_exp["structural_model"].items():
                for path in paths:
                    sig_marker = "OK" if path["significant"] else "NO"
                    print(
                        f"  {path['from']} → {path['to']}: "
                        f"{path['estimate']:.4f} (p={path['p_value']:.4f}, "
                        f"{path['effect_size']}) {sig_marker}"
                    )

        print("\nMeasurement model (significant loadings only):")
        if "measurement_model" in param_exp:
            for latent, loadings in param_exp["measurement_model"].items():
                sig_loadings = [l for l in loadings if l["significant"]]
                if sig_loadings:
                    print(f"\n  {latent}:")
                    for loading in sig_loadings:
                        print(
                            f"    {loading['indicator']}: {loading['estimate']:.4f} (p={loading['p_value']:.4f})"
                        )

        # Step 9: Generate report
        print("\nStep 9: Generating report...")
        report = self.generate_report("sem_analysis_report.txt")

        print("\nOK Analysis complete!")
        print("\nReport saved to: sem_analysis_report.txt")
        print("\n" + "=" * 80)

        return True


def main():
    """Demo of the SEM workflow agent."""
    # This would be called with actual user data
    print("SEM Workflow Agent Demo")
    print("This demo shows how the agent would work with user data.")
    print("\nTo use with your data:")
    print("  agent = SEMWorkflowAgent()")
    print("  agent.interactive_workflow('your_data.csv')")

    # Create a sample dataset for demo
    import numpy as np

    np.random.seed(42)

    n = 200
    data = pd.DataFrame(
        {
            "x1": np.random.normal(0, 1, n),
            "x2": np.random.normal(0, 1, n),
            "x3": np.random.normal(0, 1, n),
            "y1": np.random.normal(0, 1, n),
            "y2": np.random.normal(0, 1, n),
            "y3": np.random.normal(0, 1, n),
        }
    )

    # Add some structure
    data["x1"] = data["x1"] + 0.5 * np.random.normal(0, 1, n)
    data["x2"] = data["x2"] + 0.6 * np.random.normal(0, 1, n)
    data["y1"] = data["y1"] + 0.7 * np.random.normal(0, 1, n)

    # Save for demo
    data.to_csv("demo_data.csv", index=False)
    print("\nDemo dataset saved to: demo_data.csv")
    print("You can run: agent.interactive_workflow('demo_data.csv')")


if __name__ == "__main__":
    main()
