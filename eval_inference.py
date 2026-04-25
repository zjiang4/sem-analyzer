#!/usr/bin/env python3
"""Evaluate automated inference algorithms in FollowupProcessor."""

import sys
import os
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from interaction.followup_processor import FollowupProcessor
from utils.state_manager import SessionState
from core.model_draft import ModelDraft

fp = FollowupProcessor()
np.random.seed(42)
N = 200

# ============================================================================
# 1. Time-series detection
# ============================================================================
print("=" * 60)
print("1. Time-series detection accuracy")
print("=" * 60)

positive_patterns = [
    ["t1", "t2", "t3", "age", "gender"],
    ["sat_t1", "sat_t2", "sat_t3", "age"],
    ["wave1", "wave2", "wave3", "score"],
    ["time1", "time2", "time3", "height"],
    ["se1", "se2", "se3", "gender", "iq"],
    ["score_t1", "score_t2", "score_t3"],
    ["x_1", "x_2", "x_3", "x_4"],
    ["dep1", "dep2", "dep3", "age", "sex"],
    ["measure1", "measure2", "measure3", "group"],
    ["sat1", "sat2", "sat3", "gpa"],
    ["outcome_t1", "outcome_t2", "outcome_t3"],
    ["item1", "item2", "item3", "item4"],
    ["a1", "a2", "a3", "b1", "b2", "b3"],
    ["q1", "q2", "q3", "q4", "q5", "age"],
    ["var_t1", "var_t2", "var_t3", "var_t4", "group"],
    ["perf1", "perf2", "perf3", "education"],
    ["attitude1", "attitude2", "attitude3", "salary"],
    ["stress1", "stress2", "stress3", "tenure"],
    ["eng1", "eng2", "eng3", "dept"],
    ["mot1", "mot2", "mot3", "mot4"],
    ["behav1", "behav2", "behav3", "location"],
    ["knowledge1", "knowledge2", "knowledge3"],
    ["skill1", "skill2", "skill3", "skill4", "age"],
    ["resp1", "resp2", "resp3", "income"],
    ["sat1", "sat2", "sat3", "sat4", "sat5", "gender"],
]

negative_patterns = [
    ["age", "gender", "score", "height", "weight"],
    ["income", "education", "occupation", "region"],
    ["q_agree", "q_disagree", "q_neutral", "age"],
    ["apple", "banana", "cherry", "date"],
    ["cat", "dog", "fish", "bird"],
    ["red", "blue", "green", "yellow", "size"],
    ["north", "south", "east", "west"],
    ["alpha", "beta", "gamma", "delta"],
    ["monday", "tuesday", "wednesday", "thursday"],
    ["spring", "summer", "autumn", "winter"],
    ["math", "science", "english", "history"],
    ["john", "jane", "bob", "alice"],
    ["happy", "sad", "angry", "calm", "tired"],
    ["small", "medium", "large", "xlarge"],
    ["type_a", "type_b", "type_c", "value"],
    ["low", "medium", "high", "critical"],
    ["foo", "bar", "baz", "qux"],
    ["control", "treatment", "placebo", "outcome"],
    ["pre_score", "post_score", "followup_score", "age"],
    ["baseline", "midpoint", "endpoint", "group"],
    ["satisfaction", "loyalty", "trust", "commitment"],
    ["openness", "conscientiousness", "extraversion", "agreeableness"],
    ["speed", "accuracy", "efficiency", "quality"],
    ["price", "brand", "warranty", "rating"],
    ["comfort", "safety", "style", "performance"],
]

ts_tp = ts_fn = ts_tn = ts_fp = 0

for cols in positive_patterns:
    result = fp._detect_time_series_vars(cols)
    if len(result) >= 2:
        ts_tp += 1
    else:
        ts_fn += 1

for cols in negative_patterns:
    result = fp._detect_time_series_vars(cols)
    if len(result) >= 2:
        ts_fp += 1
    else:
        ts_tn += 1

ts_sensitivity = ts_tp / (ts_tp + ts_fn) if (ts_tp + ts_fn) > 0 else 0
ts_specificity = ts_tn / (ts_tn + ts_fp) if (ts_tn + ts_fp) > 0 else 0
print(f"  TP={ts_tp}, FN={ts_fn}, TN={ts_tn}, FP={ts_fp}")
print(f"  Sensitivity={ts_sensitivity:.3f}, Specificity={ts_specificity:.3f}")

# ============================================================================
# 2. Sobel mediation detection
# ============================================================================
print()
print("=" * 60)
print("2. Sobel mediation detection accuracy")
print("=" * 60)

sobel_tp = sobel_fn = sobel_tn = sobel_fp = 0
sobel_vals_pos = []
sobel_vals_neg = []

for i in range(25):
    n = N
    cause = np.random.randn(n)
    mediator = 0.6 * cause + 0.3 * np.random.randn(n)
    outcome = 0.5 * cause + 0.4 * mediator + 0.2 * np.random.randn(n)
    df = pd.DataFrame({"X": cause, "M": mediator, "Y": outcome})
    session = SessionState(
        user_id="test", session_id=f"med_pos_{i}",
        created_at="2026-01-01", updated_at="2026-01-01",
        data=df
    )
    z_val, is_med = fp._compute_jsd_mediation(session, "X", "M", "Y")
    sobel_vals_pos.append(z_val)
    if is_med:
        sobel_tp += 1
    else:
        sobel_fn += 1

for i in range(25):
    n = N
    cause = np.random.randn(n)
    outcome = 0.5 * cause + 0.3 * np.random.randn(n)
    mediator = np.random.randn(n)
    df = pd.DataFrame({"X": cause, "M": mediator, "Y": outcome})
    session = SessionState(
        user_id="test", session_id=f"med_neg_{i}",
        created_at="2026-01-01", updated_at="2026-01-01",
        data=df
    )
    z_val, is_med = fp._compute_jsd_mediation(session, "X", "M", "Y")
    sobel_vals_neg.append(z_val)
    if is_med:
        sobel_fp += 1
    else:
        sobel_tn += 1

sobel_sensitivity = sobel_tp / (sobel_tp + sobel_fn) if (sobel_tp + sobel_fn) > 0 else 0
sobel_specificity = sobel_tn / (sobel_tn + sobel_fp) if (sobel_tn + sobel_fp) > 0 else 0
print(f"  TP={sobel_tp}, FN={sobel_fn}, TN={sobel_tn}, FP={sobel_fp}")
print(f"  Sensitivity={sobel_sensitivity:.3f}, Specificity={sobel_specificity:.3f}")
print(f"  Sobel z (positive cases): mean={np.mean(sobel_vals_pos):.4f}, "
      f"std={np.std(sobel_vals_pos):.4f}, min={np.min(sobel_vals_pos):.4f}, max={np.max(sobel_vals_pos):.4f}")
print(f"  Sobel z (negative cases): mean={np.mean(sobel_vals_neg):.4f}, "
      f"std={np.std(sobel_vals_neg):.4f}, min={np.min(sobel_vals_neg):.4f}, max={np.max(sobel_vals_neg):.4f}")

# ============================================================================
# 3. KS Grouping variable detection
# ============================================================================
print()
print("=" * 60)
print("3. KS Grouping variable detection accuracy")
print("=" * 60)

ks_tp = ks_fn = ks_tn = ks_fp = 0

for i in range(25):
    n = N
    group = np.random.choice([0, 1], n)
    score = 0.8 * group + np.random.randn(n) * 0.5
    income = 2.0 * group + np.random.randn(n) * 0.5
    age = np.random.randn(n) * 2 + 30
    df = pd.DataFrame({"group": group, "score": score, "income": income, "age": age})
    draft = ModelDraft()
    draft.observed = ["score"]
    draft.covariates = ["age"]
    session = SessionState(
        user_id="test", session_id=f"grp_pos_{i}",
        created_at="2026-01-01", updated_at="2026-01-01",
        data=df, draft=draft,
        variables={"independent": ["income"], "dependent": "score"}
    )
    result = fp._suggest_grouping_vars(session)
    if "group" in result:
        ks_tp += 1
    else:
        ks_fn += 1

for i in range(25):
    n = N
    group = np.random.choice([0, 1], n)
    score = np.random.randn(n)
    income = np.random.randn(n)
    age = np.random.randn(n) * 2 + 30
    df = pd.DataFrame({"group": group, "score": score, "income": income, "age": age})
    draft = ModelDraft()
    draft.observed = ["score"]
    draft.covariates = ["age"]
    session = SessionState(
        user_id="test", session_id=f"grp_neg_{i}",
        created_at="2026-01-01", updated_at="2026-01-01",
        data=df, draft=draft,
        variables={"independent": ["income"], "dependent": "score"}
    )
    result = fp._suggest_grouping_vars(session)
    if "group" in result:
        ks_fp += 1
    else:
        ks_tn += 1

ks_sensitivity = ks_tp / (ks_tp + ks_fn) if (ks_tp + ks_fn) > 0 else 0
ks_specificity = ks_tn / (ks_tn + ks_fp) if (ks_tn + ks_fp) > 0 else 0
print(f"  TP={ks_tp}, FN={ks_fn}, TN={ks_tn}, FP={ks_fp}")
print(f"  Sensitivity={ks_sensitivity:.3f}, Specificity={ks_specificity:.3f}")

# ============================================================================
# Final results table
# ============================================================================
print()
print()
print("=== Automated Inference Evaluation ===")
print("| Algorithm       | Sensitivity | Specificity | N  |")
print("|-----------------|------------|-------------|-----|")
print(f"| Time-series     | {ts_sensitivity:10.3f} | {ts_specificity:11.3f} |  50 |")
print(f"| Sobel mediation | {sobel_sensitivity:10.3f} | {sobel_specificity:11.3f} |  50 |")
print(f"| KS grouping     | {ks_sensitivity:10.3f} | {ks_specificity:11.3f} |  50 |")
