"""
Model builder utilities for SEM workflow.
"""

from typing import Dict, List


class ModelBuilder:
    """
    Build SEM model descriptions from user specifications.

    Helps translate theoretical models into semopy syntax.
    """

    @staticmethod
    def build_cfa_model(latent_variables: Dict[str, List[str]]) -> str:
        """
        Build confirmatory factor analysis model.

        Args:
            latent_variables: Dict mapping latent var names to list of indicators

        Returns:
            semopy model description string
        """
        lines = ["# Measurement model"]

        for latent, indicators in latent_variables.items():
            latent_str = f"{latent} =~ {' + '.join(indicators)}"
            lines.append(latent_str)

        # Add factor correlations
        if len(latent_variables) > 1:
            lines.append("")
            lines.append("# Factor correlations")
            latents = list(latent_variables.keys())
            for i in range(len(latents)):
                for j in range(i + 1, len(latents)):
                    lines.append(f"{latents[i]} ~~ {latents[j]}")

        return "\n".join(lines)

    @staticmethod
    def build_sem_model(
        latent_variables: Dict[str, List[str]],
        structural_paths: List[Dict[str, List[str]]],
        covariances: List[Dict[str, str]] = None,
    ) -> str:
        """
        Build full structural equation model.

        Args:
            latent_variables: Measurement model specification
            structural_paths: List of dicts with 'outcome' and 'predictors'
            covariances: Optional list of variance/covariance specifications

        Returns:
            semopy model description string
        """
        lines = []

        # Measurement model
        lines.append("# Measurement model")
        for latent, indicators in latent_variables.items():
            latent_str = f"{latent} =~ {' + '.join(indicators)}"
            lines.append(latent_str)

        # Structural model
        if structural_paths:
            lines.append("")
            lines.append("# Structural model")
            for path in structural_paths:
                outcome = path["outcome"]
                predictors = path["predictors"]
                path_str = f"{outcome} ~ {' + '.join(predictors)}"
                lines.append(path_str)

        # Covariances
        if covariances:
            lines.append("")
            lines.append("# Residual correlations")
            for cov in covariances:
                lines.append(f"{cov['var1']} ~~ {cov['var2']}")

        return "\n".join(lines)

    @staticmethod
    def add_constraints(model_desc: str, constraints: List[str]) -> str:
        """
        Add constraints to model description.

        Args:
            model_desc: Base model description
            constraints: List of constraint strings

        Returns:
            Model description with constraints
        """
        lines = [model_desc, "", "# Constraints"]
        lines.extend(constraints)

        return "\n".join(lines)

    @staticmethod
    def add_parameter_names(model_desc: str, param_names: Dict[str, str]) -> str:
        """
        Add parameter names for easier identification.

        Args:
            model_desc: Base model description
            param_names: Dict mapping parameter to name

        Returns:
            Model description with parameter names
        """
        lines = [model_desc]

        # Replace paths with named parameters
        for param, name in param_names.items():
            lines.append(f"{name}*{param}")

        return "\n".join(lines)
