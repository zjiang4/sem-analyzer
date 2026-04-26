#!/usr/bin/env python3
"""
Non-statistical researcher UX test:
Simulate what a psychology/education researcher with NO SEM background would do.
Check: helpfulness, clarity, correctness, edge cases.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import pandas as pd
import traceback

np.random.seed(42)
PASS = 0
FAIL = 0
ISSUES = []

def test(name, condition, detail=""):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"  PASS: {name}")
    else:
        FAIL += 1
        print(f"  FAIL: {name}")
        ISSUES.append((name, detail))

def make_session():
    class S:
        pass
    s = S()
    s.data = None
    s.state = "initial"
    s.variables = {}
    s.decision_log = []
    s.hypotheses = []
    s.available_columns = []
    s.clarification_step = 0
    s.remaining_vars = None
    s.remaining_classification = {}
    s.suggested_paths = None
    s.draft = None
    s.results = None
    s.advanced_results = {}
    s.history = []
    s.textbook_retriever = None
    s.advanced_fitter = None
    s.missing_handling = "FIML"
    s.data_path = None
    s.multigroup_results = None
    s.bayesian_result = None
    s.mixture_result = None
    s.dsem_result = None
    s.multilevel_result = None
    s.imputed_datasets = None
    def add_history(k, v):
        s.history.append((k, v))
    s.add_history = add_history
    return s

def make_survey_data(n=300):
    np.random.seed(42)
    satisfaction = np.random.randn(n)
    engagement = np.random.randn(n)
    data = pd.DataFrame({
        "student_id": range(1, n + 1),
        "gender": np.random.choice(["M", "F"], n),
        "sat1": 0.7 * satisfaction + 0.3 * np.random.randn(n),
        "sat2": 0.8 * satisfaction + 0.2 * np.random.randn(n),
        "sat3": 0.6 * satisfaction + 0.4 * np.random.randn(n),
        "eng1": 0.7 * engagement + 0.3 * np.random.randn(n),
        "eng2": 0.8 * engagement + 0.2 * np.random.randn(n),
        "eng3": 0.6 * engagement + 0.4 * np.random.randn(n),
        "grade": 0.4 * satisfaction + 0.3 * engagement + 0.3 * np.random.randn(n),
    })
    return data

print("=" * 70)
print("A. DATA LOADING & FIRST IMPRESSION")
print("=" * 70)

from core.data_loader import DataLoader
from core.data_validator import DataValidator

data = make_survey_data()

print("\n--- Validator checks ---")
validator = DataValidator()
ok, warnings = validator.validate(data)
test("Survey data passes validation", ok, str(warnings))
test("No constant column warnings", all("Constant" not in w for w in warnings))
test("Has non-numeric warning for gender", any("Non-numeric" in w for w in warnings))

print("\n--- Variable type detection ---")
types = validator.detect_variable_types(data)
test("student_id detected as ID", types.get("student_id") == "id", str(types))
test("gender detected as categorical", types.get("gender") == "categorical")
test("sat1 detected as continuous", types.get("sat1") == "continuous")
test("grade detected as continuous", types.get("grade") == "continuous")

# Issue: student_id is numeric but should be categorical (it's an ID)
test("Variable detection handles ID columns", types.get("student_id") != "continuous",
     f"student_id detected as {types.get('student_id')} - should be categorical/ID")

print("\n--- Validator with tiny dataset ---")
tiny = data.head(5)
ok_tiny, warn_tiny = validator.validate(tiny)
test("Tiny dataset gets sample size warning", any("small" in w.lower() or "N=" in w for w in warn_tiny), str(warn_tiny))

print("\n--- Validator with heavy missing ---")
miss_data = data.copy()
miss_data.iloc[:100, 3] = np.nan  # 33% missing on sat2 (column index 3)
ok_miss, warn_miss = validator.validate(miss_data)
test("Heavy missing gets warning", any("sat2" in w and "missing" in w.lower() for w in warn_miss), str(warn_miss))

print("\n--- Data loader file not found ---")
loader = DataLoader()
try:
    loader.load("nonexistent_file.csv")
    test("Loader handles missing file", False, "No exception raised")
except Exception as e:
    test("Loader handles missing file gracefully", True, str(e))
    test("Error message is human-readable", "file" in str(e).lower() or "not found" in str(e).lower() or "error" in str(e).lower(),
         str(e))

# =========================================================================
print("\n" + "=" * 70)
print("B. CLARIFIER: 8-STEP GUIDED FLOW (non-statistical user)")
print("=" * 70)

from interaction.clarifier import Clarifier
clarifier = Clarifier()
session = make_session()
session.data = data

print("\n--- Step 0: Start clarification ---")
response0 = clarifier.start_clarification(session)
test("Shows data dimensions", "300 rows" in response0, response0[:100])
test("Shows variable names", "sat1" in response0 and "grade" in response0)
test("Asks for dependent variable", "dependent" in response0.lower() or "outcome" in response0.lower())
test("Provides example", "example" in response0.lower() or "e.g." in response0.lower())
test("No jargon in first message", "endogenous" not in response0.lower() and "latent" not in response0.split("Q1")[0].lower())

print("\n--- Step 0: User types a valid variable ---")
response1 = clarifier.handle_clarification(session, "grade")
test("Accepts 'grade' as dependent", "grade" in response1.lower() or "grade" in response1, response1[:150])
test("Asks for independent variables", "independent" in response1.lower() or "predictor" in response1.lower())
test("Shows remaining variables", "sat1" in response1)

print("\n--- Step 0: User types invalid variable ---")
session2 = make_session()
session2.data = data
clarifier.start_clarification(session2)
resp_invalid = clarifier.handle_clarification(session2, "happiness")
test("Rejects unrecognized variable", "not recognized" in resp_invalid.lower() or "please choose" in resp_invalid.lower(),
     resp_invalid[:200])
test("Offers help with available vars", "sat1" in resp_invalid or "grade" in resp_invalid)

print("\n--- Step 1: User lists independent variables ---")
response2 = clarifier.handle_clarification(session, "satisfaction, engagement")
test("Accepts variable list", "satisfaction" in response2 and "engagement" in response2, response2[:200])
test("Explains latent vs observed", "latent" in response2.lower() and "observed" in response2.lower())
test("Provides format example", "satisfaction: latent" in response2 or "variable_name:" in response2)

print("\n--- Step 2: User classifies variables ---")
response3 = clarifier.handle_clarification(session, "satisfaction: latent\nengagement: latent")
test("Accepts classification", "complete" in response3.lower() or "Q4" in response3 or "indicator" in response3.lower(),
     response3[:200])
test("Asks for indicators of latent vars", "indicator" in response3.lower() or "item" in response3.lower() or "sat" in response3)

print("\n--- Step 3: User defines latent indicators ---")
response4 = clarifier.handle_clarification(session, "satisfaction: sat1, sat2, sat3\nengagement: eng1, eng2, eng3")
test("Accepts indicator definitions", "satisfaction" in response4 and "engagement" in response4, response4[:200])
test("Shows remaining unused variables", "gender" in response4 or "student_id" in response4 or "remaining" in response4.lower())

print("\n--- Remaining vars: User classifies ---")
response5 = clarifier.handle_clarification(session, "gender: covariate\nstudent_id: covariate")
# This should advance to step 4 (hypothesis/paths)
test("Advances past classification", "structural" in response5.lower() or "path" in response5.lower() or "→" in response5 or "->" in response5,
     response5[:300])

print("\n--- Step 4: Confirm paths ---")
response6 = clarifier.handle_clarification(session, "confirm")
test("Accepts path confirmation", "missing" in response6.lower() or "sample" in response6.lower() or "FIML" in response6,
     response6[:300])

print("\n--- Step 5: Choose missing data method ---")
response7 = clarifier.handle_clarification(session, "1")
test("Accepts FIML choice", "draft" in str(session.__dict__) or session.clarification_step == 7 or "confirm" in response7.lower(),
     response7[:300])

# =========================================================================
print("\n" + "=" * 70)
print("C. MODEL CONFIRMATION")
print("=" * 70)

from interaction.model_confirm import ModelConfirm
confirm = ModelConfirm()

print("\n--- Show model summary ---")
try:
    if session.draft is not None:
        resp_confirm = confirm.show_and_confirm(session, "")
        test("Shows model summary", len(resp_confirm) > 50, resp_confirm[:200])
        test("Shows latent variables", "satisfaction" in resp_confirm and "engagement" in resp_confirm)
        test("Shows paths", "→" in resp_confirm or "->" in resp_confirm or "grade" in resp_confirm)
    else:
        test("Shows model summary", False, "Draft is None - clarification did not complete properly")
except Exception as e:
    test("Model confirmation works", False, str(e))
    traceback.print_exc()

# =========================================================================
print("\n" + "=" * 70)
print("D. FOLLOWUP: OUTPUT READABILITY (non-statistical user)")
print("=" * 70)

from interaction.followup_processor import FollowupProcessor
fp = FollowupProcessor()

# Simulate a fitted model in session
session_fit = make_session()
session_fit.data = data
session_fit.state = "model_confirmed"

syntax = "satisfaction =~ sat1 + sat2 + sat3\nengagement =~ eng1 + eng2 + eng3\ngrade ~ satisfaction + engagement"
try:
    import semopy
    model = semopy.Model(syntax)
    model.fit(data)
    stats = semopy.calc_stats(model)
    params = model.inspect()

    class FakeDraft:
        pass
    session_fit.draft = FakeDraft()
    session_fit.draft.latent = {"satisfaction": {"items": ["sat1", "sat2", "sat3"]}, "engagement": {"items": ["eng1", "eng2", "eng3"]}}
    session_fit.draft.latent_vars = session_fit.draft.latent
    session_fit.draft.observed = []
    session_fit.draft.covariates = []
    session_fit.draft.paths = [("satisfaction", "grade"), ("engagement", "grade")]
    session_fit.draft.group_var = None
    session_fit.draft.cluster_var = None
    session_fit.variables = {"latent_indicators": {"satisfaction": ["sat1", "sat2", "sat3"], "engagement": ["eng1", "eng2", "eng3"]}}
    session_fit.results = {"model_string": syntax, "model": model}
    session_fit.results["fit_indices"] = {
        "chi2": float(stats.iloc[0]["chi2"]),
        "df": float(stats.iloc[0]["DoF"]),
        "p_value": float(stats.iloc[0]["chi2 p-value"]),
        "cfi": float(stats.iloc[0]["CFI"]),
        "rmsea": float(stats.iloc[0]["RMSEA"]),
    }
    session_fit.advanced_results = {}
except Exception as e:
    print(f"  WARNING: Could not fit model for followup tests: {e}")

# --- Test reliability output ---
print("\n--- Reliability output ---")
try:
    resp_rel = fp.handle(session_fit, "reliability")
    test("Reliability returns readable text", len(resp_rel) > 50, resp_rel[:300])
    test("Reliability mentions Cronbach", "cronbach" in resp_rel.lower() or "alpha" in resp_rel.lower(), resp_rel[:300])
    test("Reliability mentions AVE or CR", "ave" in resp_rel.lower() or "composite" in resp_rel.lower() or "variance" in resp_rel.lower())
    test("Reliability has per-factor breakdown", "satisfaction" in resp_rel.lower() and "engagement" in resp_rel.lower())
except Exception as e:
    test("Reliability output", False, str(e))

# --- Test estimator suggestion ---
print("\n--- Estimator suggestion ---")
from core.sem_utils import suggest_estimator
est = suggest_estimator(data)
test("Estimator recommendation has reason", "reason" in est and len(est["reason"]) > 20, str(est))
test("Reason is in plain English", "sample" in est["reason"].lower() or "data" in est["reason"].lower() or "missing" in est["reason"].lower())

# --- Test missing data output ---
print("\n--- Missing data analysis output ---")
try:
    resp_miss = fp.handle(session_fit, "analyze missing data")
    test("Missing data output readable", len(resp_miss) > 30, resp_miss[:200])
    test("Missing data mentions strategy", "strategy" in resp_miss.lower() or "recommend" in resp_miss.lower())
except Exception as e:
    test("Missing data analysis", False, str(e))

# =========================================================================
print("\n" + "=" * 70)
print("E. EDGE CASES A NON-EXPERT WOULD HIT")
print("=" * 70)

print("\n--- User says just 'help' ---")
resp_help = fp.handle(session_fit, "help")
test("'help' doesn't crash", isinstance(resp_help, str), resp_help[:200])

print("\n--- User says nonsense ---")
resp_nonsense = fp.handle(session_fit, "asdfghjkl random text")
test("Nonsense doesn't crash", isinstance(resp_nonsense, str))

print("\n--- User tries to fit without data ---")
empty_session = make_session()
empty_session.data = None
empty_session.draft = None
try:
    resp_empty = fp.handle(empty_session, "fit")
    test("No-data session handled gracefully", "no data" in resp_empty.lower() or "no model" in resp_empty.lower())
except Exception as e:
    test("No-data session handled gracefully", False, str(e))

print("\n--- User uploads data with special column names ---")
special_data = pd.DataFrame({
    "Var 1": np.random.randn(100),
    "Var-2": np.random.randn(100),
    "Var_3": np.random.randn(100),
    "结果": np.random.randn(100),
})
ok_special, warn_special = validator.validate(special_data)
test("Special chars in column names don't crash validator", isinstance(ok_special, bool), str(warn_special))

print("\n--- Single column data ---")
single_col = pd.DataFrame({"x": np.random.randn(100)})
ok_single, warn_single = validator.validate(single_col)
test("Single column validated", isinstance(ok_single, bool))
test("Single column gets too-few-columns warning", any("column" in w.lower() for w in warn_single), str(warn_single))

print("\n--- All-missing column ---")
all_miss = data.copy()
all_miss["empty_col"] = np.nan
ok_am, warn_am = validator.validate(all_miss)
test("All-missing column detected", any("empty_col" in w for w in warn_am), str(warn_am))

# =========================================================================
print("\n" + "=" * 70)
print("F. DATA VALIDATOR IMPROVEMENTS NEEDED")
print("=" * 70)

print("\n--- Check: Does validator warn about ID-like columns? ---")
test("Validator warns about ID columns", any("student_id" in w or "id" in w.lower() for w in warnings),
     f"Warnings: {warnings}")
# This is likely a FAIL - validator doesn't detect ID columns

print("\n--- Check: Does validator warn about highly correlated variables? ---")
corr_matrix = data.select_dtypes(include=[np.number]).corr()
high_corr_pairs = []
for i in range(len(corr_matrix.columns)):
    for j in range(i+1, len(corr_matrix.columns)):
        if abs(corr_matrix.iloc[i, j]) > 0.9:
            high_corr_pairs.append((corr_matrix.columns[i], corr_matrix.columns[j], corr_matrix.iloc[i, j]))
test("No multicollinearity warning needed for this data", len(high_corr_pairs) == 0,
     f"High corr pairs: {high_corr_pairs}")

print("\n--- Check: Does validator suggest sample size adequacy? ---")
tiny_for_size = data.head(20)
_, warn_tiny_size = validator.validate(tiny_for_size)
test("Validator has sample size check", any("small" in w.lower() or "N=" in w for w in warn_tiny_size),
     f"Warnings for N=20: {warn_tiny_size}")

# =========================================================================
print("\n" + "=" * 70)
print("G. REPORT FORMATTER READABILITY")
print("=" * 70)

from interaction.report_formatter import ReportFormatter
rf = ReportFormatter()

print("\n--- Format fit statistics via report ---")
try:
    report = rf.generate(session_fit, format='md')
    test("Report generates markdown", len(report) > 100, report[:200])
    test("Report contains CFI", "CFI" in report)
    test("Report contains RMSEA", "RMSEA" in report)
    test("Report contains model definition", "satisfaction" in report)
except Exception as e:
    test("Report formatting", False, str(e))
    traceback.print_exc()

# =========================================================================
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"PASSED: {PASS}")
print(f"FAILED: {FAIL}")
print()
if ISSUES:
    print("ISSUES TO FIX:")
    for name, detail in ISSUES:
        print(f"  - {name}: {detail[:120]}")
else:
    print("ALL TESTS PASSED!")
