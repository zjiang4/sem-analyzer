# sem-workflow: Interactive SEM Workflow Assistant

A skill for guiding researchers through the complete structural equation modeling (SEM) workflow using the `semopy` package in Python.

## Overview

This skill provides comprehensive guidance for SEM analysis from CSV data upload through model interpretation. It covers:

- **Data exploration**: Understanding your dataset, missing data patterns, variable screening
- **Theory validation**: Checking if your model is theoretically sound and empirically supported
- **Model specification**: Building semopy model descriptions from your theory
- **Model fitting**: Optimizing model parameters and checking convergence
- **Diagnostics**: Interpreting fit indices and identifying issues
- **Results interpretation**: Explaining path coefficients, factor loadings, and effect sizes

## Installation

This skill is part of the opencode skills system. The skill itself doesn't require installation, but to use the Python utilities:

```bash
pip install pandas numpy scipy matplotlib seaborn semopy
```

## Core Components

The skill includes five main modules:

### 1. `agent.py` - SEMWorkflowAgent

Main interface for interactive SEM analysis.

```python
from sem_workflow.agent import SEMWorkflowAgent

agent = SEMWorkflowAgent()
agent.interactive_workflow('your_data.csv')
```

**Key methods:**
- `load_data()`: Load CSV and perform initial inspection
- `assess_missing_data()`: Analyze missing data patterns and recommend treatment
- `get_theory_from_user()`: Interactively gather theoretical model
- `validate_theory()`: Check if model is appropriate for data
- `build_model_description()`: Create semopy model syntax
- `fit_model()`: Fit model to data
- `get_fit_indices()`: Calculate and interpret fit statistics
- `explain_parameters()`: Interpret parameter estimates
- `generate_report()`: Create comprehensive analysis report

### 2. `data_preparator.py` - DataPreparator

Utilities for data preparation.

```python
from sem_workflow.data_preparator import DataPreparator

# Check normality
normality = DataPreparator.check_normality(data)

# Detect outliers
outliers = DataPreparator.detect_outliers(data, threshold=3.0)

# Check variance
variances = DataPreparator.check_variance(data, min_variance=0.1)

# Suggest missing data strategy
strategy, reasoning = DataPreparator.suggest_missing_strategy(data)
```

### 3. `model_builder.py` - ModelBuilder

Build SEM model descriptions from specifications.

```python
from sem_workflow.model_builder import ModelBuilder

# Build CFA model
cfa_model = ModelBuilder.build_cfa_model({
    'factor1': ['x1', 'x2', 'x3'],
    'factor2': ['y1', 'y2', 'y3']
})

# Build full SEM
sem_model = ModelBuilder.build_sem_model(
    latent_variables={...},
    structural_paths=[...],
    covariances=[...]
)
```

### 4. `diagnostics.py` - SEMDiagnostics

Model evaluation and diagnostics.

```python
from sem_workflow.diagnostics import SEMDiagnostics

# Interpret fit indices
interpretation = SEMDiagnostics.interpret_fit_indices(fit_stats)

# Check for parameter issues
issues = SEMDiagnostics.check_parameter_issues(estimates)

# Get modification suggestions
suggestions = SEMDiagnostics.suggest_modifications(model, data)
```

### 5. `interpreter.py` - ResultInterpreter

Interpret SEM results for reporting.

```python
from sem_workflow.interpreter import ResultInterpreter

# Interpret path coefficient
path_interp = ResultInterpreter.interpret_path_coefficient(
    estimate=0.45, std_error=0.08, p_value=0.001, standardized=True
)

# Interpret factor loading
loading_interp = ResultInterpreter.interpret_factor_loading(
    indicator='q1', factor='satisfaction', loading=0.72, p_value=0.01
)

# Calculate R²
r2 = ResultInterpreter.calculate_r_squared(error_variance=0.3, total_variance=1.0)

# Format APA results
apa_text = ResultInterpreter.format_apa_results(estimates, fit_stats)
```

### 6. `visualizer.py` - SEMVisualizer

Visualization tools for SEM analysis.

```python
from sem_workflow.visualizer import SEMVisualizer

# Generate path diagram
SEMVisualizer.plot_path_diagram(model, filename='model.png', show_covariances=True)

# Compare model fits
SEMVisualizer.plot_fit_comparison(
    fit_stats_list=[fit1, fit2, fit3],
    model_names=['Model A', 'Model B', 'Model C'],
    filename='comparison.png'
)

# Plot factor loadings heatmap
SEMVisualizer.plot_factor_loadings(loadings_dict, filename='loadings.png')
```

## Workflow Example

Here's a complete example of using the skill:

```python
from sem_workflow.agent import SEMWorkflowAgent

# Initialize agent
agent = SEMWorkflowAgent()

# Load data
data, inspection = agent.load_data('survey_data.csv')

print(f"Loaded {inspection['n_rows']} rows, {inspection['n_cols']} columns")

# Assess missing data
missing_analysis = agent.assess_missing_data(data)
print(f"Missing data: {missing_analysis['missing_percent']:.1f}%")
print(f"Recommendation: {missing_analysis['recommendation']}")

# Specify theory (in practice, this would be interactive)
agent.theory = {
    'latent_variables': {
        'satisfaction': ['sat1', 'sat2', 'sat3', 'sat4'],
        'engagement': ['eng1', 'eng2', 'eng3'],
        'loyalty': ['loy1', 'loy2', 'loy3']
    },
    'structural_paths': [
        {'outcome': 'engagement', 'predictors': ['satisfaction']},
        {'outcome': 'loyalty', 'predictors': ['engagement', 'satisfaction']}
    ],
    'covariances': []
}

# Validate theory
is_valid, issues = agent.validate_theory(agent.theory, data)
if not is_valid:
    print("Theory validation issues:")
    for issue in issues:
        print(f"  - {issue}")
    # Address issues...

# Build model
model_desc = agent.build_model_description(agent.theory)

# Fit model
success, results = agent.fit_model(data, obj='MLW', solver='SLSQP')
if not success:
    print("Model fitting failed. Try different optimization settings.")

# Get diagnostics
fit_stats = agent.get_fit_indices()
fit_interp = agent.interpret_fit()
print(f"Overall fit: {fit_interp['overall_fit']}")

# Explain results
param_exp = agent.explain_parameters()

# Generate report
report = agent.generate_report('analysis_report.txt')
print(report)
```

## When to Use This Skill

Use this skill when:

- User provides CSV data for SEM analysis
- User needs help specifying their theoretical model in semopy syntax
- User is unsure about missing data handling
- User wants guidance on model diagnostics and fit interpretation
- User needs help interpreting path coefficients and factor loadings
- User wants to generate APA-style results for reporting

## Key Features

### Theory-First Approach

The skill emphasizes theory validation before data analysis. It:

1. **Asks about research questions**: What are you testing?
2. **Confirms theoretical model**: Are the latent variables correct?
3. **Validates against data**: Do you have enough sample size?
4. **Documents justification**: Why were certain paths included/excluded?

### Comprehensive Diagnostics

The skill provides:

- **Fit index interpretation**: χ², RMSEA, CFI, TLI, SRMR with cutoffs
- **Parameter checks**: Negative variances, large standard errors, non-significant paths
- **Model modification suggestions**: Based on residuals and modification indices
- **Effect size interpretation**: Cohen's conventions for standardized coefficients

### Interactive Guidance

The skill is designed for interactive use:

- **Step-by-step workflow**: Clear progression through analysis
- **Questions at each stage**: Confirm assumptions and theory
- **Explainations**: Why certain decisions are recommended
- **Warnings**: Potential issues before proceeding

### Academic-Ready Output

Generates:

- **APA-formatted tables**: Ready for publication
- **Path diagrams**: Using semopy's visualization
- **Comprehensive reports**: Data summary, fit, parameters, recommendations
- **Fit comparison plots**: When comparing multiple models

## Common Use Cases

### 1. Confirmatory Factor Analysis (CFA)

Testing whether a set of indicators measure latent constructs.

```python
agent.theory = {
    'latent_variables': {
        'factor1': ['x1', 'x2', 'x3'],
        'factor2': ['y1', 'y2', 'y3']
    },
    'structural_paths': [],
    'covariances': []
}
```

### 2. Structural Equation Modeling

Testing relationships between latent variables.

```python
agent.theory = {
    'latent_variables': {...},  # Measurement model
    'structural_paths': [
        {'outcome': 'outcome_var', 'predictors': ['predictor1', 'predictor2']}
    ],
    'covariances': []
}
```

### 3. Mediation Analysis

Testing whether one variable mediates the relationship between others.

```python
agent.theory = {
    'latent_variables': {...},
    'structural_paths': [
        {'outcome': 'mediator', 'predictors': ['independent']},
        {'outcome': 'dependent', 'predictors': ['mediator', 'independent']}
    ]
}
```

### 4. Multi-Group Analysis

Comparing models across groups.

```python
# Group 1
agent1 = SEMWorkflowAgent()
agent1.interactive_workflow('group1_data.csv')

# Group 2
agent2 = SEMWorkflowAgent()
agent2.interactive_workflow('group2_data.csv')

# Compare fit statistics
# (Implementation would compare fit_stats across groups)
```

## Troubleshooting

### Model Won't Converge

**Symptoms:**
- Optimization fails after max iterations
- Gradient never reaches zero

**Solutions:**
1. Check sample size vs parameters
2. Simplify model
3. Try different optimizer (`solver='L-BFGS-B'`)
4. Set starting values: `START(value) param_name`

### Poor Fit Despite Good Theory

**Symptoms:**
- CFI < 0.90, RMSEA > 0.08
- Significant χ² (p < 0.05)

**Solutions:**
1. Review measurement model
2. Add theoretically justified paths
3. Include error covariances
4. Check for method effects

### Negative Variances (Heywood Cases)

**Symptoms:**
- Error variance estimate < 0
- Standardized estimate > 1.0

**Solutions:**
1. Constrain to small positive value: `BOUND(0.001, 1.0) error_var`
2. Remove problematic variable
3. Check multicollinearity

## References

- Geletkanycz, A. (2019). semopy: A Python Package for Structural Equation Modeling. *Journal of Statistical Software*.
- Kline, R. B. (2015). *Principles and Practice of Structural Equation Modeling* (4th ed.). Guilford Press.
- Hu, L. T., & Bentler, P. M. (1999). Cutoff criteria for fit indexes in covariance structure analysis. *Structural Equation Modeling*, 6(1), 1-55.
- Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum.

## License

This skill is distributed under the GPL-3.0 license, consistent with the semopy package.
