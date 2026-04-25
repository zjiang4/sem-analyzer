#!/usr/bin/env python3
"""Test interactive multigroup invariance testing workflow."""

import sys, os
sys.path.insert(0, '.')

import pandas as pd
import numpy as np
from utils.state_manager import SessionState
from interaction.followup_processor import FollowupProcessor
from core.advanced_fitter import AdvancedFitter

def create_multigroup_data(n_per_group=80, seed=99):
    np.random.seed(seed)
    group = np.repeat([0,1], n_per_group)
    n = n_per_group * 2
    lat = np.random.normal(0, 1, n)
    e1 = np.random.normal(0, 0.5, n)
    e2 = np.random.normal(0, 0.5, n)
    e3 = np.random.normal(0, 0.5, n)
    sat1 = 1.0*lat + e1
    sat2 = 0.9*lat + e2
    sat3 = 0.8*lat + e3
    grade = 0.5*lat + np.random.normal(0, 0.6, n)
    df = pd.DataFrame({
        'group': group,
        'sat1': sat1,
        'sat2': sat2,
        'sat3': sat3,
        'grade': grade
    })
    return df

def test_multigroup_workflow():
    print("=== Multigroup Invariance Workflow Test ===")
    df = create_multigroup_data(100)
    print(f"Data shape: {df.shape}, groups: {df['group'].nunique()}")
    print(f"Group distribution: {df['group'].value_counts().to_dict()}")

    # Simulate a session
    session = SessionState(
        user_id="test",
        session_id="test_mg",
        created_at="2026-01-01",
        updated_at="2026-01-01"
    )
    session.data = df
    session.variables = {}

    # Mock a draft model
    from core.model_draft import ModelDraft
    draft = ModelDraft()
    draft.latent = {'satisfaction': ['sat1', 'sat2', 'sat3']}
    draft.observed = []
    draft.paths = [('satisfaction', 'grade')]
    draft.covariates = []
    session.draft = draft

    # Create processor
    proc = FollowupProcessor()
    session.advanced_fitter = AdvancedFitter()

    # Step 1: configural
    print("\n--- Step 1: configural ---")
    resp1 = proc.handle(session, "多组分析 group")
    print(resp1[:500])
    assert "configural" in resp1.lower()
    assert hasattr(session, 'multigroup_results')
    assert session.multigroup_results['current_level'] == 'configural'
    print("✓ Configural step completed\n")

    # Step 2: metric
    print("--- Step 2: metric ---")
    resp2 = proc.handle(session, "metric")
    print(resp2[:500])
    assert "metric" in resp2.lower()
    assert session.multigroup_results['current_level'] == 'metric'
    assert "CFI" in resp2
    print("Metric step with comparison\n")

    # Step 3: scalar
    print("--- Step 3: scalar ---")
    resp3 = proc.handle(session, "scalar")
    print(resp3[:500])
    assert "scalar" in resp3.lower()
    assert session.multigroup_results['current_level'] == 'scalar'
    print("✓ Scalar step completed\n")

    print("✅ Multigroup invariance interactive workflow passed!")

if __name__ == '__main__':
    try:
        test_multigroup_workflow()
    except Exception as e:
        import traceback
        traceback.print_exc()
        sys.exit(1)
