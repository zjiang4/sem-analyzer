#!/usr/bin/env python3
"""Test bootstrap CI for mediation analysis."""

import sys, os
sys.path.insert(0, '.')

import pandas as pd
import numpy as np
from core.advanced_fitter import AdvancedFitter

def create_mediation_data(n=200, seed=42):
    np.random.seed(seed)
    # X -> M -> Y chain with some noise
    X = np.random.normal(0, 1, n)
    M = 0.6*X + np.random.normal(0, 0.8, n)
    Y = 0.4*X + 0.5*M + np.random.normal(0, 0.7, n)
    df = pd.DataFrame({
        'X': X,
        'M': M,
        'Y': Y
    })
    return df

def test_bootstrap_ci():
    print("=== Bootstrap CI Test ===\n")
    df = create_mediation_data(150)

    fitter = AdvancedFitter()
    # Fit mediation without bootstrap first
    result = fitter.fit(df, 'mediation', {'cause':['X'], 'mediator':['M'], 'outcome':['Y']}, options={'bootstrap': False})
    print("Original fit:")
    print("  Parameters:")
    if isinstance(result.parameters, pd.DataFrame):
        print(result.parameters.to_string())
    else:
        print(result.parameters)
    print("\n  Fit indices:", result.fit_stats)

    # Now with bootstrap
    result_boot = fitter.fit(df, 'mediation', {'cause':['X'], 'mediator':['M'], 'outcome':['Y']}, options={'bootstrap': True, 'n_boot': 200})
    print("\nBootstrap CI:")
    if result_boot.bootstrap_ci:
        for param, (lo, up) in result_boot.bootstrap_ci.items():
            print(f"  {param}: [{lo:.3f}, {up:.3f}]")
    else:
        print("  (No bootstrap CI computed)")

    # Check that all parameters have CI
    if result_boot.bootstrap_ci:
        param_count = len(result.parameters)
        ci_count = len(result_boot.bootstrap_ci)
        print(f"\n  Parameters count: {param_count}, CI count: {ci_count}")
        if param_count == ci_count:
            print("  ✓ All parameters have CI")
        else:
            print("  ⚠ Mismatch in parameter count vs CI count")

if __name__ == '__main__':
    try:
        test_bootstrap_ci()
    except Exception as e:
        import traceback
        traceback.print_exc()
        sys.exit(1)
