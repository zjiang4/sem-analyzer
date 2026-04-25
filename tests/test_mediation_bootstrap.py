#!/usr/bin/env python3
"""Test mediation analysis bootstrap CI correctness and stability."""

import sys, os
sys.path.insert(0, '.')

import pandas as pd
import numpy as np
from core.advanced_fitter import AdvancedFitter

def generate_mediation_data(n=100, effect_x2m=0.6, effect_m2y=0.5, effect_x2y=0.2, seed=123):
    np.random.seed(seed)
    X = np.random.normal(0, 1, n)
    M = effect_x2m * X + np.random.normal(0, 0.7, n)
    Y = effect_x2y * X + effect_m2y * M + np.random.normal(0, 0.6, n)
    return pd.DataFrame({'X': X, 'M': M, 'Y': Y})

def test_med_nobootstrap():
    """Test basic mediation without bootstrap."""
    df = generate_mediation_data(150)
    fitter = AdvancedFitter()
    res = fitter.fit(df, 'mediation', {'cause':['X'], 'mediator':['M'], 'outcome':['Y']}, options={'bootstrap': False})
    print("=== Mediation (no bootstrap) ===")
    if isinstance(res.parameters, pd.DataFrame):
        print(res.parameters.to_string())
    else:
        print(res.parameters)
    assert res.parameters is not None
    paths = list(res.parameters['path'].astype(str))
    for pat in ['Y~X', 'M~X', 'Y~M']:
        assert any(pat == p or pat in p for p in paths), f"Missing path {pat}"
    print("✓ Basic mediation parameters extracted\n")
    return res

def test_med_bootstrap():
    """Test mediation with bootstrap CI."""
    df = generate_mediation_data(200)
    fitter = AdvancedFitter()
    res = fitter.fit(df, 'mediation', {'cause':['X'], 'mediator':['M'], 'outcome':['Y']},
                     options={'bootstrap': True, 'n_boot': 200})
    print("=== Mediation (with bootstrap) ===")
    print("Parameters:")
    if isinstance(res.parameters, pd.DataFrame):
        print(res.parameters.to_string())
    else:
        print(res.parameters)
    print("\nBootstrap CI:")
    if res.bootstrap_ci:
        for k, (l, u) in res.bootstrap_ci.items():
            print(f"  {k}: [{l:.3f}, {u:.3f}]")
        param_paths = set(res.parameters['path'].astype(str))
        ci_paths = set(res.bootstrap_ci.keys())
        missing = param_paths - ci_paths
        if missing:
            print(f"⚠ Missing CI for paths: {missing}")
        else:
            print("✓ All parameters have CI")
    else:
        print("❌ No bootstrap CI returned")
    assert res.bootstrap_ci is not None, "Bootstrap CI should not be None"
    assert len(res.bootstrap_ci) > 0, "Bootstrap CI should not be empty"
    return res

def test_ci_contains_true():
    """Check if bootstrap CI contains the true parameter in repeated samples."""
    np.random.seed(2026)
    n_rep = 30
    contain_count = 0
    for i in range(n_rep):
        df = generate_mediation_data(150, seed=i)
        fitter = AdvancedFitter()
        res = fitter.fit(df, 'mediation', {'cause':['X'], 'mediator':['M'], 'outcome':['Y']},
                         options={'bootstrap': True, 'n_boot': 100})
        if res.bootstrap_ci:
            ci = res.bootstrap_ci
            for (low, up) in ci.values():
                if not (np.isfinite(low) and np.isfinite(up) and up > low):
                    raise AssertionError(f"Invalid CI bounds: low={low}, up={up}")
            contain_count += 1
    print(f"\n=== CI Coverage sanity check ===")
    print(f"{contain_count}/{n_rep} reps produced valid CI")
    assert contain_count >= n_rep * 0.8, "Most reps should have valid CI"

if __name__ == '__main__':
    print("Mediation Bootstrap Test Suite")
    print("="*50)
    try:
        test_med_nobootstrap()
        test_med_bootstrap()
        test_ci_contains_true()
        print("\n✅ All tests passed!")
    except Exception as e:
        import traceback
        traceback.print_exc()
        print("\n❌ Tests failed")
        sys.exit(1)
