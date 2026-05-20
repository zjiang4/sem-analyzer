---
name: sem-workflow
description: Use when user provides CSV data for structural equation modeling analysis and needs complete workflow from data exploration through model fitting, diagnostics, and interpretation
---

# SEM Workflow with semopy

## Overview

Complete SEM workflow assistant that guides researchers from CSV data upload through theory specification, data preparation, model building, fitting, diagnostics, and interpretation.

**Core principle:** Interactive guidance with theory validation at each step, ensuring methodological soundness before proceeding.

## When to Use

**Triggering conditions:**
- User provides CSV dataset for SEM analysis
- User needs help with model specification or data preparation
- User is uncertain about missing data handling or variable coding
- User wants to validate their theoretical model with data

**Use cases:**
- Social science researchers analyzing survey data
- Psychology researchers testing measurement models
- Economics researchers estimating path models
- Any SEM analysis requiring data preparation through interpretation

**Don't use when:**
- User already has fitted model and only needs basic diagnostics (use systematic-debugging instead)
- User wants exploratory factor analysis without theoretical framework (use semopy's EFA module)
- User's data is non-numeric categorical without ordinal specification

## The Process

### Phase 1: Initial Assessment

**Step 1.1: Load and Inspect Data**
```python
import pandas as pd
data = pd.read_csv('your_data.csv')
print(data.info())
print(data.describe())
```

**Ask user:**
1. What is your research question?
2. What latent variables (constructs) does your theory propose?
3. Which observed variables measure each latent variable?
4. Are there any ordinal variables that need special treatment?

**Step 1.2: Validate Data Compatibility**

Check for:
- Sufficient sample size (N ≥ 10 parameters recommended, N ≥ 200 for stable estimates)
- Variable types (numeric for continuous, specify for ordinal)
- Missing data patterns (MCAR, MAR, MNAR)

**If issues found:**
- Sample size too small: Warn about power issues, suggest bootstrap
- Mixed variable types: Confirm with user how to handle
- Non-numeric variables: Discuss encoding or exclusion

### Phase 2: Data Preparation

**Step 2.1: Handle Missing Data**

Assess missingness pattern:
```python
import missingno as msno
msno.matrix(data)
```

**Consult user on approach:**
- **Listwise deletion**: If <5% missing and MCAR
- **FIML**: semopy's default for MAR (Full Information Maximum Likelihood)
- **Multiple imputation**: If MNAR or complex patterns

**Step 2.2: Variable Screening**

Check for:
- Low variance variables (<0.1)
- Outliers (z-scores > 3 or < -3)
- Normality (skewness > 2, kurtosis > 7)

**Step 2.3: Variable Confirmation**

For each latent variable, confirm:
- Indicator variables (observed measures)
- Directionality (positive/negative wording if relevant)
- Coding scheme (e.g., Likert 1-5 vs 0-4)

**Present to user:**
```
Latent Variable: [name]
Indicators: [list]
Coding: [scale]
Concerns: [any issues]
```

Ask: "Is this correct for [variable]?"

### Phase 3: Model Specification

**Step 3.1: Define Measurement Model**

Build measurement model based on user's theory:
```python
# Example: CFA with two factors
model_desc = '''
# Measurement model
factor1 =~ ind1 + ind2 + ind3
factor2 =~ ind4 + ind5 + ind6

# Factor covariance
factor1 ~~ factor2
'''
```

**Step 3.2: Define Structural Model** (if applicable)

Add regression relationships between latent variables:
```python
# Add structural paths
factor2 ~ factor1 + covariate1
```

**Step 3.3: Add Covariances** (if needed)

Add residual correlations based on theory or modification indices:
```python
# Error covariances
ind1 ~~ ind2
```

**Step 3.4: Show Model to User**

```python
from semopy import Model
model = Model(model_desc)

# Visualize
import semopy
semopy.semplot(model, "model_diagram.png")

print("Proposed model:")
print(model_desc)
```

**Ask:**
1. Does this match your theoretical model?
2. Any missing paths or covariances?
3. Any paths that should be fixed/constrained?

### Phase 4: Model Fitting

**Step 4.1: Choose Optimization Method**

Recommend based on data characteristics:
- **MLW** (default): Multivariate normal assumption, efficient
- **ULS**: For non-normal data, distribution-free
- **DWLS**: For ordinal/categorical data, robust

**Step 4.2: Fit Model**
```python
from semopy import Model

model = Model(model_desc)
results = model.fit(data, obj='MLW')

print("Optimization successful:", results)
```

**Step 4.3: Check Convergence**

Verify:
- Optimization status (successful or not)
- Number of iterations (reasonable, <200)
- Gradient near zero

**If convergence fails:**
- Try different starting values
- Check for multicollinearity
- Simplify model (remove complex paths)

### Phase 5: Model Diagnostics

**Step 5.1: Calculate Fit Indices**
```python
stats = semopy.calc_stats(model)

# Key indices to report
print(f"χ² = {stats['chi2']:.2f}, p = {stats['chi2 p-value']:.3f}")
print(f"RMSEA = {stats['RMSEA']:.3f}")
print(f"CFI = {stats['CFI']:.3f}")
print(f"TLI = {stats['TLI']:.3f}")
print(f"SRMR = {stats['SRMR']:.3f}")
```

**Interpretation guidelines:**
- χ² p > 0.05: Good fit (not significant)
- RMSEA < 0.05: Excellent; < 0.08: Good
- CFI > 0.95: Excellent; > 0.90: Good
- TLI > 0.95: Excellent; > 0.90: Good
- SRMR < 0.08: Good

**Step 5.2: Check Parameter Estimates**
```python
estimates = model.inspect()

# Check for:
# 1. Non-significant paths (p > 0.05)
# 2. Unreasonable estimates (e.g., negative variances)
# 3. Standard errors too large
# 4. Standardized estimates > 1 or < -1
```

**Step 5.3: Identify Problems**

Common issues and solutions:

| Problem | Diagnosed by | Solution |
|---------|---------------|----------|
| Poor fit (CFI < 0.90) | Low fit indices | Add theoretically justified paths or covariances |
| Negative variance | estimates < 0 | Constrain to small positive value or remove variable |
| Large SE | Std. Err >> Estimate | Check multicollinearity, sample size |
| Non-significant paths | p > 0.05 | Consider removing if theoretically weak |
| Standardized > 1 | standardized estimate > 1 | Check multicollinearity, measurement error |

**Step 5.4: Suggest Model Modification**

Use modification indices to identify improvements:
```python
# semopy doesn't have built-in MI, but you can calculate residuals
# Suggest adding paths/covariances with largest positive MIs
```

**Caveat:** Only accept modifications if theoretically justified.

### Phase 6: Results Interpretation

**Step 6.1: Explain Standardized Estimates**

```python
estimates_std = model.inspect(std_est=True)

# Show standardized path coefficients
print("Standardized estimates:")
for idx, row in estimates_std.iterrows():
    if row['op'] == '~':
        print(f"{row['lval']} → {row['rval']}: {row['Estimate']:.3f}")
```

**Interpretation:**
- 0.1-0.3: Small effect
- 0.3-0.5: Medium effect
- > 0.5: Large effect (Cohen's conventions for standardized coefficients)

**Step 6.2: Explain Factor Loadings**

```python
# Filter for measurement model
loadings = estimates_std[estimates_std['op'] == '~']

print("Factor loadings:")
for latent in loadings['rval'].unique():
    print(f"\n{latent}:")
    latent_loadings = loadings[loadings['rval'] == latent]
    for _, row in latent_loadings.iterrows():
        print(f"  {row['lval']}: {row['Estimate']:.3f} (p={row['p-value']:.3f})")
```

**Quality criteria:**
- Loading > 0.70: Good
- 0.50-0.70: Acceptable
- < 0.50: Poor, consider removing indicator

**Step 6.3: Explain R² Values**

For each endogenous variable:
```python
# Calculate R² from model matrices
# R² = 1 - (error variance / total variance)

print("R² values:")
for var in endogenous_vars:
    r2 = calculate_r2(model, var)
    print(f"{var}: {r2:.3f}")
```

**Interpretation:**
- > 0.75: Substantial
- 0.50-0.75: Moderate
- 0.25-0.50: Weak
- < 0.25: Very weak

**Step 6.4: Answer Research Questions**

Map results back to user's original questions:
```
Research Question 1: [Does X influence Y?]
Answer: Yes (β=0.45, p<0.001), medium effect

Research Question 2: [How well does the measurement model fit?]
Answer: Good fit (CFI=0.95, RMSEA=0.04), all loadings significant
```

### Phase 7: Reporting

**Step 7.1: Generate Tables**

```python
# Table 1: Fit Indices
fit_table = pd.DataFrame({
    'Index': ['χ²', 'df', 'p-value', 'RMSEA', 'CFI', 'TLI', 'SRMR'],
    'Value': [stats['chi2'], stats['DoF'], stats['chi2 p-value'],
              stats['RMSEA'], stats['CFI'], stats['TLI'], stats['SRMR']]
})

# Table 2: Parameter Estimates
params_table = model.inspect()

# Export to CSV or LaTeX
fit_table.to_csv('fit_indices.csv', index=False)
params_table.to_csv('parameter_estimates.csv', index=False)
```

**Step 7.2: Generate Visualizations**

```python
# Path diagram
semopy.semplot(model, 'model_diagram.png', plot_covs=True)

# Residual plots (if needed)
# Plot observed vs predicted correlations
```

**Step 7.3: Create APA-Style Writeup Template**

```python
writeup_template = f"""
A structural equation model was estimated using the semopy package (v{semopy.__version__}) in Python.
The model included {n_latent} latent variables and {n_observed} observed indicators.
Maximum likelihood estimation was used.

Model fit indices indicated a {'good' if cfi > 0.90 else 'poor'} fit to the data (CFI = {cfi:.2f},
RMSEA = {rmsea:.3f}, χ²({df}) = {chi2:.2f}, p = {p_value:.3f}).
All factor loadings were statistically significant (p < 0.05).
The structural path from X to Y was significant (β = {beta:.3f}, p = {p_beta:.3f}),
explaining {r2:.1%} of the variance in Y.
"""
```

## Quick Reference

| Phase | Key Functions | Output |
|--------|---------------|---------|
| **Data Load** | `pd.read_csv()`, `data.info()` | Variable list, types, missingness |
| **Missing Data** | `msno.matrix()`, user consultation | Treatment strategy |
| **Model Build** | `Model(model_desc)` | semopy Model object |
| **Fit** | `model.fit(data, obj='MLW')` | Optimization results |
| **Diagnostics** | `calc_stats(model)` | Fit indices, parameter estimates |
| **Visualization** | `semplot(model, filename)` | Path diagram |
| **Export** | `model.inspect().to_csv()` | Results tables |

## Common Mistakes

### ❌ Skipping Theory Validation

**Problem:** Building model purely empirically without theoretical justification.

**Fix:**
```python
# BEFORE building model, ask user:
print("Please confirm your theory:")
print("1. What are your latent variables?")
print("2. Which indicators measure each latent variable?")
print("3. What structural relationships do you expect?")
```

**Why it matters:** SEM is confirmatory, not exploratory. Theory must guide specification.

### ❌ Ignoring Missing Data Mechanism

**Problem:** Using listwise deletion without considering missingness pattern.

**Fix:**
```python
# Assess pattern first
print("Missing data analysis:")
print(f"Missing: {data.isnull().sum().sum()} cells")
print(f"Pattern: MCAR/MAR/MNAR (requires additional tests)")

# Consult user
print("Recommendation: Use FIML (semopy default) for MAR data")
```

### ❌ Overfitting with Modification Indices

**Problem:** Adding all paths suggested by MI to improve fit.

**Fix:**
```python
# Only accept if theoretically justified
print("Modification Index: ind1 ~~ ind2 (MI = 15.3)")
print("Question: Is there theoretical reason for this correlation?")
print("If yes: Add to model. If no: Ignore MI.")
```

### ❌ Not Checking Convergence

**Problem:** Proceeding with failed optimization results.

**Fix:**
```python
# Always verify
results = model.fit(data)
if not results:
    print("Optimization FAILED!")
    print("Try: 1) Different starting values, 2) Simpler model")
    return False

print(f"Optimization successful in {results.iterations} iterations")
```

### ❌ Misinterpreting Fit Indices

**Problem:** Relying on single index, ignoring others.

**Fix:**
```python
# Always report multiple indices
print("Fit assessment:")
print(f"  χ² p-value: {p_chi2:.3f} {'✓' if p_chi2 > 0.05 else '✗'}")
print(f"  RMSEA: {rmsea:.3f} {'✓' if rmsea < 0.08 else '✗'}")
print(f"  CFI: {cfi:.3f} {'✓' if cfi > 0.90 else '✗'}")
print(f"  TLI: {tli:.3f} {'✓' if tli > 0.90 else '✗'}")
```

## Implementation Examples

### Example 1: Simple CFA

```python
import pandas as pd
from semopy import Model

# Load data
data = pd.read_csv('survey_data.csv')

# User's theory: Three-factor model
model_desc = '''
# Measurement model
satisfaction =~ q1 + q2 + q3 + q4
engagement =~ q5 + q6 + q7 + q8
loyalty =~ q9 + q10 + q11 + q12

# Factor correlations
satisfaction ~~ engagement
satisfaction ~~ loyalty
engagement ~~ loyalty
'''

# Build and fit
model = Model(model_desc)
results = model.fit(data)

# Diagnostics
stats = semopy.calc_stats(model)
print(f"CFI: {stats['CFI']:.3f}")
print(f"RMSEA: {stats['RMSEA']:.3f}")

# Visualize
semopy.semplot(model, 'cfa_model.png')

# Estimates
estimates = model.inspect()
print(estimates)
```

### Example 2: Full SEM with Control Variables

```python
import pandas as pd
from semopy import Model

data = pd.read_csv('customer_data.csv')

# Theory: Satisfaction mediates effect of Service on Loyalty
model_desc = '''
# Measurement model
service =~ s1 + s2 + s3
satisfaction =~ sat1 + sat2 + sat3 + sat4
loyalty =~ loy1 + loy2 + loy3

# Structural model
loyalty ~ satisfaction + service + age + income
satisfaction ~ service

# Covariances
s1 ~~ s2
age ~~ income
'''

# Fit
model = Model(model_desc)
results = model.fit(data, obj='MLW')

# Full diagnostics
stats = semopy.calc_stats(model)
estimates = model.inspect(std_est=True)

# Report key paths
structural_paths = estimates[estimates['op'] == '~']
print("Structural paths (standardized):")
for _, row in structural_paths.iterrows():
    if row['lval'] not in ['s1', 's2', 's3', 'sat1', 'sat2', 'sat3', 'sat4', 'loy1', 'loy2', 'loy3']:
        print(f"{row['lval']} → {row['rval']}: β = {row['Estimate']:.3f}, p = {row['p-value']:.3f}")
```

## Integration with semopy Features

### Ordinal Variables

If user has Likert-scale data:

```python
model_desc = '''
DEFINE(ordinal) q1 q2 q3 q4
factor1 =~ q1 + q2 + q3 + q4
'''

model = Model(model_desc)
results = model.fit(data)  # Uses polychoric correlations
```

### Multi-Group Analysis (Measurement Invariance)

```python
# Using the agent method
agent.theory = your_theory
agent.build_model_description(your_theory)
agent.fit_model(data)

# Test configural invariance across groups
invariance = agent.test_measurement_invariance(
    data=data,
    group_var='group',
    invariance_types=['configural', 'metric', 'scalar']
)

print(f"Configural: {invariance['summary']}")
print(f"Invariance achieved: {invariance['invariance_summary']}")
```

**Note:** Currently supports configural invariance. Metric and scalar invariance require additional implementation.

### Bootstrap Confidence Intervals

For robust standard errors and confidence intervals:

```python
# After fitting model
agent.fit_model(data)

# Run bootstrap (e.g., 1000 samples)
bootstrap_results = agent.bootstrap_confidence_intervals(
    data=data,
    n_bootstrap=1000,
    alpha=0.05,
    random_state=42
)

# View CIs for parameters
print(bootstrap_results[['parameter', 'estimate', 'bootstrap_std_error', 'ci_lower', 'ci_upper']])
```

### Mediation Analysis

Test indirect effects (X → M → Y):

```python
# Model must include: M ~ X and Y ~ M + X
agent.fit_model(data)

mediation = agent.analyze_mediation(
    mediator='work_engagement',
    outcome='organizational_loyalty',
    predictor='job_satisfaction',
    n_bootstrap=1000,
    alpha=0.05
)

print(f"Indirect effect: {mediation['indirect_effect']:.3f}")
print(f"95% CI: [{mediation['indirect_ci'][0]:.3f}, {mediation['indirect_ci'][1]:.3f}]")
print(f"Mediation type: {mediation['mediation_type']}")
```

**Interpretation:**
- If indirect effect CI excludes 0 → mediation present
- If direct effect also non-significant → full mediation
- If direct effect remains significant → partial mediation

## Verification Before Completion

**Before claiming analysis complete, verify:**

- [ ] User confirmed theoretical model specification
- [ ] Missing data strategy documented and agreed upon
- [ ] All variable codings verified with user
- [ ] Model converged successfully
- [ ] Fit indices reported and interpreted
- [ ] All parameters checked for reasonableness
- [ ] Research questions answered with results
- [ ] Results exported to tables
- [ ] Visualization generated

**If any check fails:**
- STOP
- Address the issue
- Re-verify before proceeding

## Troubleshooting

### Model Won't Converge

**Symptoms:**
- Optimization fails after max iterations
- Gradient never reaches zero

**Solutions (in order):**
1. **Check sample size:** N should be > 5x number of parameters
2. **Simplify model:** Remove complex interactions, reduce latent variables
3. **Check starting values:** Use `START()` operation for problematic parameters
4. **Scale variables:** Standardize if scales differ widely
5. **Try different optimizer:** Change from SLSQP to L-BFGS-B

```python
# Example: Set starting values
model_desc = '''
START(0.5) path1
path1 ~ x1 + x2
'''

model = Model(model_desc)
results = model.fit(data, solver='L-BFGS-B')
```

### Heywood Cases (Negative Variance)

**Symptoms:**
- Error variance estimate < 0
- Standardized estimate > 1.0

**Solutions:**
1. **Constrain to small positive value:**
   ```python
   model_desc = '''
   BOUND(0.001, 1.0) error_var
   y ~~ error_var
   '''
   ```
2. **Remove problematic variable:** Check multicollinearity
3. **Check measurement:** Ensure indicators load on correct factor

### Poor Fit Despite Good Theory

**Symptoms:**
- CFI < 0.90, RMSEA > 0.08
- Significant χ² (p < 0.05)

**Solutions:**
1. **Review measurement model:** Are all indicators valid?
2. **Add theoretically justified paths:** Not empirically driven
3. **Include error covariances:** Based on theory or MI
4. **Consider method effects:** If using same items across contexts

### Small Sample Size

**Symptoms:**
- N < 10x parameters
- Unstable estimates across bootstrap samples

**Solutions:**
1. **Simplify model:** Reduce number of latent variables
2. **Use Bayesian estimation:** If semopy supports
3. **Report caution:** Acknowledge limitation in writeup
4. **Bootstrap standard errors:** Assess stability

## Advanced Topics

### Longitudinal SEM

For repeated measures data:

```python
# Model with cross-lagged effects
model_desc = '''
# Latent variables at Time 1 and Time 2
lat_t1 =~ ind1_t1 + ind2_t1 + ind3_t1
lat_t2 =~ ind1_t2 + ind2_t2 + ind3_t2

# Autoregressive effects
lat_t2 ~ lat_t1

# Cross-lagged effects
lat_t2 ~ cov_t1
'''
```

### Mediation Analysis

Testing indirect effects:

```python
# Mediator model: X → M → Y
model_desc = '''
X =~ x1 + x2
M =~ m1 + m2
Y =~ y1 + y2

# Structural paths
M ~ X
Y ~ M + X
'''

# After fitting, calculate indirect effect
# Indirect = (X→M) × (M→Y)
# Total = Direct + Indirect
```

### Moderation Analysis

Interaction effects between latent variables (if supported by semopy version):

```python
# Note: semopy may not support latent interactions directly
# Alternative: Use observed interaction terms or product indicators
```

## Best Practices

### Always Consult Theory First

Before touching data:
1. Ask user about theoretical framework
2. Confirm all hypothesized relationships
3. Document theoretical justification

### Document Every Decision

Keep record of:
- Why certain paths were included/excluded
- Rationale for missing data treatment
- Theory behind model modifications

### Report Full Results

Always provide:
- Fit indices (χ², RMSEA, CFI, TLI, SRMR)
- Both unstandardized and standardized estimates
- Standard errors and p-values
- R² values for endogenous variables
- Factor loadings with significance

### Use Appropriate Sample Size Rules

Guidelines:
- N ≥ 10 parameters (minimum)
- N ≥ 200 for stable estimates (recommended)
- N ≥ 10 per indicator (for CFA)

### Validate Model Assumptions

Check:
- Multivariate normality (for ML)
- Linearity
- No extreme multicollinearity (VIF < 5)

## References

- Geletkanycz, A. (2019). semopy: A Python Package for Structural Equation Modeling. *Journal of Statistical Software*. https://doi.org/10.18637/jss.v000.i000
- Rosseel, Y. (2012). lavaan: An R Package for Structural Equation Modeling. *Journal of Statistical Software*, 48(2), 1-36.
- Kline, R. B. (2015). *Principles and Practice of Structural Equation Modeling* (4th ed.). Guilford Press.
- Hu, L. T., & Bentler, P. M. (1999). Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives. *Structural Equation Modeling*, 6(1), 1-55.
