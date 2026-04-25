#!/usr/bin/env python3
"""
Evaluation: sem-analyzer output quality vs. known LLM failure patterns.
Tests 5 realistic SEM specification scenarios.
"""

import sys
import os
import traceback
import warnings
import numpy as np
import pandas as pd
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.model_draft import ModelDraft
from core.data_validator import DataValidator
from core.advanced_fitter import AdvancedFitter
from interaction.clarifier import Clarifier
from interaction.followup_processor import FollowupProcessor
from interaction.model_confirm import ModelConfirm
from utils.state_manager import SessionState, SessionManager

warnings.filterwarnings("ignore")

SEPARATOR = "=" * 60


def make_test_data(n=200, seed=42):
    """Generate synthetic SEM-friendly data."""
    rng = np.random.RandomState(seed)
    sat1 = rng.normal(3.5, 0.8, n)
    sat2 = sat1 + rng.normal(0, 0.3, n)
    sat3 = sat1 + rng.normal(0, 0.3, n)
    eng1 = rng.normal(3.0, 0.9, n)
    eng2 = eng1 + rng.normal(0, 0.3, n)
    eng3 = eng1 + rng.normal(0, 0.3, n)
    grade = 0.5 * sat1 + 0.3 * eng1 + rng.normal(0, 0.5, n)
    gender = rng.choice([0, 1], n)
    group = rng.choice(["A", "B", "C"], n)
    x = rng.normal(0, 1, n)
    m = 0.4 * x + rng.normal(0, 0.5, n)
    y = 0.3 * m + 0.2 * x + rng.normal(0, 0.5, n)
    t1 = rng.normal(2, 1, n)
    t2 = t1 + 0.5 + rng.normal(0, 0.5, n)
    t3 = t2 + 0.5 + rng.normal(0, 0.5, n)
    cat3 = rng.choice([1, 2, 3], n)

    return pd.DataFrame({
        "sat1": sat1, "sat2": sat2, "sat3": sat3,
        "eng1": eng1, "eng2": eng2, "eng3": eng3,
        "grade": grade, "gender": gender, "group": group,
        "x": x, "m": m, "y": y,
        "score_t1": t1, "score_t2": t2, "score_t3": t3,
        "cat3level": cat3,
    })


def make_session(df=None):
    """Create a fresh session with data attached."""
    if df is None:
        df = make_test_data()
    mgr = SessionManager()
    session = mgr.get_or_create("eval_user")
    session.data = df
    session.data_path = "eval_data.csv"
    session.available_columns = list(df.columns)
    session.textbook_retriever = None
    session.advanced_fitter = AdvancedFitter()
    return session


def task1_underidentified():
    """Task 1: Underidentified model — latent with only 1 indicator."""
    print(SEPARATOR)
    print("=== Task 1: Underidentified Model ===")
    print("Description: Latent variable with only 1 indicator")
    print("LLM typical mistake: Generates model silently (underidentified)")
    print()

    draft = ModelDraft()
    draft.add_latent("satisfaction", ["sat1"])
    draft.add_path("satisfaction", "grade")
    draft.set_observed(["grade"])

    is_valid, errors = draft.validate()

    if not is_valid:
        has_indicator_warning = any("2" in e or "题项" in e for e in errors)
        if has_indicator_warning:
            status = "PASS"
            detail = (f"validate() correctly rejected the model. "
                      f"Errors: {errors}")
        else:
            status = "PARTIAL"
            detail = (f"Rejected but for wrong reason. Errors: {errors}")
    else:
        status = "FAIL"
        detail = "validate() accepted an underidentified model without warning!"

    # Also test through ModelConfirm path
    session = make_session()
    session.draft = draft
    confirm = ModelConfirm()
    confirm_msg = confirm.show_and_confirm(session, "")

    confirm_rejects = "issue" in confirm_msg.lower() or "correct" in confirm_msg.lower()

    print(f"  ModelDraft.validate(): valid={is_valid}, errors={errors}")
    print(f"  ModelConfirm message contains rejection: {confirm_rejects}")
    print(f"  sem-analyzer behavior: {status}")
    print(f"  Details: {detail}")
    print()

    return status, detail


def task2_wrong_measurement():
    """Task 2: Wrong measurement level — categorical in growth model."""
    print(SEPARATOR)
    print("=== Task 2: Wrong Measurement Level ===")
    print("Description: Categorical variable (3 levels) used in growth model")
    print("LLM typical mistake: Accepts categorical as continuous silently")
    print()

    df = make_test_data()
    validator = DataValidator()

    types = validator.detect_variable_types(df)
    cat3_detected = types.get("cat3level") == "categorical"

    is_valid, warnings_list = validator.validate(df)
    cat3_warned = any("cat3level" in w or "Non-numeric" in w for w in warnings_list)

    # Check if growth model pipeline detects categorical
    # The growth model uses _detect_time_series_vars which looks for patterns
    # Let's check if cat3level could be accidentally picked up
    fp = FollowupProcessor()
    detected_ts = fp._detect_time_series_vars(list(df.columns))
    cat3_in_ts = "cat3level" in detected_ts

    # Check what happens if we try to use cat3level as a growth variable
    # The DataValidator at least warns about it
    # But does the growth template or fitter catch it?
    growth_attempt_ok = True
    growth_error_msg = ""
    try:
        from core.templates import GrowthModelTemplate
        tmpl = GrowthModelTemplate()
        model_str = tmpl.generate({"items": ["cat3level", "score_t2", "score_t3"],
                                    "time_loadings": [0, 1, 2]})
    except Exception as e:
        growth_attempt_ok = False
        growth_error_msg = str(e)

    # The key question: does the system warn before fitting?
    # DataValidator.detect_variable_types catches it
    # DataValidator.validate() warns about non-numeric
    if cat3_detected:
        status = "PASS"
        detail = (f"DataValidator.detect_variable_types() correctly identifies "
                  f"'cat3level' as categorical. validate() warnings: {warnings_list}. "
                  f"cat3level in time-series detection: {cat3_in_ts}. "
                  f"Growth template accepts it: {growth_attempt_ok}")
    else:
        status = "FAIL"
        detail = "DataValidator did not detect categorical variable"

    print(f"  detect_variable_types(): {types.get('cat3level', 'NOT FOUND')}")
    print(f"  validate() warnings: {warnings_list}")
    print(f"  cat3level in growth time-series detection: {cat3_in_ts}")
    print(f"  Growth template generates model with cat3level: {growth_attempt_ok}")
    print(f"  sem-analyzer behavior: {status}")
    print(f"  Details: {detail}")
    print()

    return status, detail


def task3_circular_paths():
    """Task 3: Circular paths — A→B→C→A."""
    print(SEPARATOR)
    print("=== Task 3: Circular Paths ===")
    print("Description: User specifies A -> B -> C -> A (a cycle)")
    print("LLM typical mistake: Generates syntax with cycles silently")
    print()

    draft = ModelDraft()
    draft.set_observed(["A", "B", "C"])
    draft.add_path("A", "B")
    draft.add_path("B", "C")
    draft.add_path("C", "A")

    has_cycle = draft._has_cycle()
    is_valid, errors = draft.validate()

    cycle_detected = any("循环" in e or "cycle" in e.lower() for e in errors)

    if not is_valid and has_cycle and cycle_detected:
        status = "PASS"
        detail = (f"_has_cycle()={has_cycle}, validate() errors: {errors}")
    elif has_cycle and not cycle_detected:
        status = "PARTIAL"
        detail = f"_has_cycle() detects cycle but validate() message unclear: {errors}"
    else:
        status = "FAIL"
        detail = f"Cycle not detected! _has_cycle()={has_cycle}, errors={errors}"

    # Also test through ModelConfirm
    session = make_session()
    session.draft = draft
    confirm = ModelConfirm()
    confirm_msg = confirm.show_and_confirm(session, "")
    confirm_catches = "issue" in confirm_msg.lower() or "循环" in confirm_msg

    print(f"  _has_cycle(): {has_cycle}")
    print(f"  validate(): valid={is_valid}, errors={errors}")
    print(f"  ModelConfirm catches cycle: {confirm_catches}")
    print(f"  sem-analyzer behavior: {status}")
    print(f"  Details: {detail}")
    print()

    return status, detail


def task4_mediation_bootstrap():
    """Task 4: Mediation with bootstrap CI."""
    print(SEPARATOR)
    print("=== Task 4: Mediation with Bootstrap CI ===")
    print("Description: Indirect effect needs BCa bootstrap CI, not normal-theory SE")
    print("LLM typical mistake: Uses delta-method / normal-theory SE for indirect effect")
    print()

    df = make_test_data(n=200)
    fitter = AdvancedFitter()

    mediation_result = None
    error_msg = ""
    try:
        mediation_result = fitter.fit(
            df, "mediation",
            {"cause": ["x"], "mediator": ["m"], "outcome": ["y"]},
            options={"bootstrap": True, "n_boot": 50}
        )
    except Exception as e:
        error_msg = str(e)
        traceback.print_exc()

    if mediation_result is None:
        status = "FAIL"
        detail = f"Mediation fitting failed: {error_msg}"
    else:
        has_bca = mediation_result.bootstrap_ci is not None
        ci_nonempty = bool(mediation_result.bootstrap_ci) if has_bca else False

        # Check that it's actually BCa by inspecting the method
        import inspect
        source = inspect.getsource(fitter._bootstrap_ci)
        has_jackknife = "jackknife" in source
        has_bias_correction = "z0" in source and "norm.ppf" in source
        has_acceleration = "acceleration" in source or "num / (6.0" in source

        is_bca = has_jackknife and has_bias_correction and has_acceleration

        if has_bca and ci_nonempty and is_bca:
            status = "PASS"
            detail = (f"BCa bootstrap CI computed. "
                      f"CI entries: {len(mediation_result.bootstrap_ci)}. "
                      f"Jackknife: {has_jackknife}, bias correction (z0): {has_bias_correction}, "
                      f"acceleration: {has_acceleration}")
        elif has_bca and ci_nonempty:
            status = "PARTIAL"
            detail = (f"Bootstrap CI returned but may not be full BCa. "
                      f"Jackknife: {has_jackknife}, z0: {has_bias_correction}, "
                      f"acceleration: {has_acceleration}")
        else:
            status = "FAIL"
            detail = f"No bootstrap CI returned. bootstrap_ci={mediation_result.bootstrap_ci}"

    print(f"  Mediation fit successful: {mediation_result is not None}")
    if mediation_result:
        print(f"  bootstrap_ci present: {mediation_result.bootstrap_ci is not None}")
        print(f"  bootstrap_ci non-empty: {bool(mediation_result.bootstrap_ci) if mediation_result.bootstrap_ci is not None else False}")
        if mediation_result.bootstrap_ci:
            for k, (lo, hi) in list(mediation_result.bootstrap_ci.items())[:3]:
                print(f"    {k}: [{lo:.3f}, {hi:.3f}]")
    else:
        print(f"  Error: {error_msg[:200]}")
    print(f"  sem-analyzer behavior: {status}")
    print(f"  Details: {detail}")
    print()

    return status, detail


def task5_progressive_invariance():
    """Task 5: Multigroup progressive invariance testing."""
    print(SEPARATOR)
    print("=== Task 5: Multigroup Progressive Invariance ===")
    print("Description: Should fit configural first, then progressively metric/scalar")
    print("LLM typical mistake: Fits all invariance levels at once without comparisons")
    print()

    df = make_test_data()
    session = make_session(df)

    # Set up session as if user went through clarification
    session.variables = {
        "dependent": "grade",
        "independent": ["satisfaction", "engagement"],
        "classifications": {"satisfaction": "latent", "engagement": "latent"},
        "latent_indicators": {
            "satisfaction": ["sat1", "sat2", "sat3"],
            "engagement": ["eng1", "eng2", "eng3"],
        }
    }
    session.suggested_paths = [("satisfaction", "grade"), ("engagement", "grade")]
    session.missing_handling = "FIML"

    draft = ModelDraft()
    draft.add_latent("satisfaction", ["sat1", "sat2", "sat3"])
    draft.add_latent("engagement", ["eng1", "eng2", "eng3"])
    draft.add_path("satisfaction", "grade")
    draft.add_path("engagement", "grade")
    draft.set_observed(["grade"])
    session.draft = draft
    session.state = "model_confirmed"

    fp = FollowupProcessor()

    # Step 1: Request multigroup
    result1 = fp.handle(session, "multigroup group")
    starts_configural = "configural" in result1.lower()

    # Check state machine
    has_mg_state = hasattr(session, "multigroup_results")
    if has_mg_state:
        current_level = session.multigroup_results.get("current_level", "unknown")
    else:
        current_level = "no state"

    # Check if user is prompted for next steps
    prompts_next = "metric" in result1.lower() and "scalar" in result1.lower()

    # Step 2: Check if waiting for user command (not auto-proceeding)
    waits_for_user = "reply" in result1.lower() or "type" in result1.lower() or "proceed" in result1.lower()

    # Step 3: Simulate user requesting metric
    # Save configural fit results first
    configural_fits = None
    if hasattr(session, "advanced_results") and session.advanced_results:
        mg_res = session.advanced_results.get("multigroup")
        if mg_res:
            configural_fits = mg_res.fit_stats

    result2 = None
    metric_ok = False
    comparison_shown = False
    try:
        result2 = fp.handle(session, "metric")
        metric_ok = "metric" in result2.lower() if result2 else False
    except Exception as e:
        metric_ok = False

    # Check for ΔCFI/ΔRMSEA comparison
    if result2:
        comparison_shown = ("dCFI" in result2 or "dRMSEA" in result2 or
                           "delta" in result2.lower() or "comparison" in result2.lower() or
                           "ΔCFI" in result2 or "ΔRMSEA" in result2)

    if starts_configural and has_mg_state and current_level == "configural" and prompts_next:
        status = "PASS"
        detail = (f"Starts with configural: {starts_configural}. "
                  f"State machine level: {current_level}. "
                  f"Prompts for next level: {prompts_next}. "
                  f"Waits for user: {waits_for_user}. "
                  f"Metric step works: {metric_ok}. "
                  f"Comparison shown: {comparison_shown}")
    elif starts_configural and prompts_next:
        status = "PARTIAL"
        detail = (f"Starts configural and prompts, but state machine incomplete. "
                  f"Level: {current_level}. Metric: {metric_ok}")
    else:
        status = "FAIL"
        detail = (f"Does not start with configural or does not prompt progressively. "
                  f"configural: {starts_configural}, prompts: {prompts_next}, "
                  f"level: {current_level}")

    print(f"  First call starts configural: {starts_configural}")
    print(f"  State machine current_level: {current_level}")
    print(f"  Prompts for metric/scalar: {prompts_next}")
    print(f"  Waits for user command: {waits_for_user}")
    print(f"  Metric step works: {metric_ok}")
    print(f"  Comparison (dCFI/dRMSEA) shown: {comparison_shown}")
    if result1:
        print(f"  First response snippet: {result1[:200].encode('ascii', 'replace').decode()}...")
    if result2:
        print(f"  Metric response snippet: {result2[:200].encode('ascii', 'replace').decode()}...")
    print(f"  sem-analyzer behavior: {status}")
    print(f"  Details: {detail}")
    print()

    return status, detail


def main():
    print()
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  sem-analyzer vs LLM Failure Patterns — Evaluation Suite   ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()

    results = {}

    results["Task 1: Underidentified"] = task1_underidentified()
    results["Task 2: Wrong Measurement"] = task2_wrong_measurement()
    results["Task 3: Circular Paths"] = task3_circular_paths()
    results["Task 4: Bootstrap CI"] = task4_mediation_bootstrap()
    results["Task 5: Progressive Invariance"] = task5_progressive_invariance()

    # Summary table
    print()
    print(SEPARATOR)
    print("=== Comparison: sem-analyzer vs Raw LLM ===")
    print()
    print("| Task | LLM Error Risk | sem-analyzer Handles? |")
    print("|------|---------------|----------------------|")

    llm_risks = {
        "Task 1: Underidentified": "Yes — silent underid",
        "Task 2: Wrong Measurement": "Yes — silent accept",
        "Task 3: Circular Paths": "Yes — silent cycle",
        "Task 4: Bootstrap CI": "Yes — wrong SE method",
        "Task 5: Progressive Invariance": "Yes — all at once",
    }

    pass_count = 0
    partial_count = 0
    fail_count = 0
    for task, (status, detail) in results.items():
        risk = llm_risks[task]
        print(f"| {task} | {risk} | {status} |")
        if status == "PASS":
            pass_count += 1
        elif status == "PARTIAL":
            partial_count += 1
        else:
            fail_count += 1

    print()
    print(f"Summary: {pass_count} PASS, {partial_count} PARTIAL, {fail_count} FAIL out of 5 tasks")
    print()

    if pass_count == 5:
        print("sem-analyzer correctly handles all 5 common LLM failure patterns.")
    elif pass_count + partial_count == 5:
        print("sem-analyzer partially handles most patterns; some areas need improvement.")
    else:
        print("sem-analyzer has gaps in handling some LLM failure patterns.")

    print()
    return results


if __name__ == "__main__":
    main()
