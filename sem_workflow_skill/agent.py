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
            from semopy import Model
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
            chi2 = stats.get(
                "chi2", stats.at[0, "chi2"] if "chi2" in stats.index else None
            )
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

        print("\n✓ Theory is valid for this data.\n")

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

        print("\n✓ Model fitted successfully!")
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
                    sig_marker = "✓" if path["significant"] else "✗"
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

        print("\n✓ Analysis complete!")
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
