"""
Visualization utilities for SEM workflow.
"""

from typing import Optional


class SEMVisualizer:
    """
    Visualization tools for SEM analysis.

    Provides:
    - Path diagram generation
    - Fit index plots
    - Residual plots
    """

    @staticmethod
    def plot_path_diagram(
        model, filename: str = "sem_model.png", show_covariances: bool = False
    ):
        """
        Generate path diagram for SEM model.

        Args:
            model: semopy Model object
            filename: Output filename
            show_covariances: Whether to show covariance arrows
        """
        try:
            import semopy

            semopy.semplot(model, filename, plot_covs=show_covariances)
            print(f"Path diagram saved to: {filename}")
        except ImportError:
            print("Error: semopy is not installed.")
        except Exception as e:
            print(f"Error generating path diagram: {e}")

    @staticmethod
    def plot_fit_comparison(
        fit_stats_list: list, model_names: list, filename: str = "fit_comparison.png"
    ):
        """
        Compare fit indices across multiple models.

        Args:
            fit_stats_list: List of fit statistics DataFrames
            model_names: List of model names
            filename: Output filename
        """
        import matplotlib.pyplot as plt
        import pandas as pd

        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        fig.suptitle("Model Fit Comparison", fontsize=16, fontweight="bold")

        indices_to_plot = ["RMSEA", "CFI", "TLI", "SRMR"]
        colors = ["blue", "green", "orange", "red"]

        for idx, (ax, index) in enumerate(zip(axes.flat, indices_to_plot)):
            values = []
            for stats in fit_stats_list:
                # Try to get the value
                if isinstance(stats, pd.DataFrame):
                    if index in stats.columns:
                        values.append(
                            stats[index].values[0] if len(stats) > 0 else stats[index]
                        )
                    elif index.lower() in [c.lower() for c in stats.columns]:
                        col = [c for c in stats.columns if c.lower() == index.lower()][
                            0
                        ]
                        values.append(
                            stats[col].values[0] if len(stats) > 0 else stats[col]
                        )

            if values:
                ax.bar(model_names, values, color=colors[idx])
                ax.set_title(index, fontweight="bold")
                ax.set_ylabel("Value")
                ax.axhline(
                    y=0.08
                    if index == "RMSEA"
                    else 0.90
                    if index in ["CFI", "TLI"]
                    else 0.10,
                    color="red",
                    linestyle="--",
                    alpha=0.5,
                    label="Threshold",
                )

                if index in ["CFI", "TLI"]:
                    ax.set_ylim(0, 1.0)
                elif index == "RMSEA":
                    ax.set_ylim(0, 0.15)
                elif index == "SRMR":
                    ax.set_ylim(0, 0.15)

                ax.legend()

        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches="tight")
        plt.close()

        print(f"Fit comparison plot saved to: {filename}")

    @staticmethod
    def plot_factor_loadings(loadings: dict, filename: str = "factor_loadings.png"):
        """
        Visualize factor loadings as heatmap.

        Args:
            loadings: Dictionary mapping latent vars to loading data
            filename: Output filename
        """
        import matplotlib.pyplot as plt
        import seaborn as sns
        import pandas as pd

        # Convert to DataFrame
        data_list = []
        for latent, loading_data in loadings.items():
            if isinstance(loading_data, pd.DataFrame):
                for idx, row in loading_data.iterrows():
                    data_list.append(
                        {
                            "latent": latent,
                            "indicator": row["lval"],
                            "loading": row["Estimate"],
                        }
                    )

        df = pd.DataFrame(data_list)

        # Create heatmap
        pivot_df = df.pivot(index="indicator", columns="latent", values="loading")

        plt.figure(figsize=(10, 8))
        sns.heatmap(
            pivot_df,
            annot=True,
            cmap="RdBu_r",
            center=0,
            fmt=".3f",
            cbar_kws={"label": "Loading"},
        )

        plt.title("Factor Loadings", fontweight="bold", pad=20)
        plt.xlabel("Latent Variables", fontweight="bold")
        plt.ylabel("Indicators", fontweight="bold")
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches="tight")
        plt.close()

        print(f"Factor loadings heatmap saved to: {filename}")
