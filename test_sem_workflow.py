#!/usr/bin/env python3
"""
测试脚本：测试 sem-workflow skill 的功能
作为社会学研究者（无统计/编程背景），评估该 skill 是否真的实现其声称的功能
"""

import sys
import os
import importlib.util
from pathlib import Path
import pandas as pd
import numpy as np

# 手动加载 sem-workflow 模块（目录名含连字符，需要特殊处理）
sem_workflow_dir = Path(r"C:\Users\zjian\.opencode\skills\sem-workflow")
if not sem_workflow_dir.exists():
    print(f"ERROR: sem-workflow not found at {sem_workflow_dir}")
    exit(1)

# 手动加载各个模块
def load_module(name, file_path):
    spec = importlib.util.spec_from_file_location(name, file_path)
    if spec is None:
        raise ImportError(f"Cannot load {name} from {file_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

try:
    # 创建虚拟包结构
    sys.modules['sem_workflow'] = type(sys)('sem_workflow')
    sys.modules['sem_workflow'].__path__ = [str(sem_workflow_dir)]

    # 加载各个模块
    agent_mod = load_module('sem_workflow.agent', sem_workflow_dir / 'agent.py')
    data_prep_mod = load_module('sem_workflow.data_preparator', sem_workflow_dir / 'data_preparator.py')
    model_build_mod = load_module('sem_workflow.model_builder', sem_workflow_dir / 'model_builder.py')
    diag_mod = load_module('sem_workflow.diagnostics', sem_workflow_dir / 'diagnostics.py')
    interp_mod = load_module('sem_workflow.interpreter', sem_workflow_dir / 'interpreter.py')
    vis_mod = load_module('sem_workflow.visualizer', sem_workflow_dir / 'visualizer.py')

    # 导入到当前命名空间
    SEMWorkflowAgent = agent_mod.SEMWorkflowAgent
    DataPreparator = data_prep_mod.DataPreparator
    ModelBuilder = model_build_mod.ModelBuilder
    SEMDiagnostics = diag_mod.SEMDiagnostics
    ResultInterpreter = interp_mod.ResultInterpreter
    SEMVisualizer = vis_mod.SEMVisualizer

    print("[OK] All sem_workflow modules loaded successfully")
except Exception as e:
    print(f"ERROR: Failed to load sem_workflow modules: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

# 测试数据集路径
TEST_DATA = "test_sem_data.csv"

def test_data_loading():
    """测试 1: 数据加载和探索"""
    print("\n" + "="*80)
    print("TEST 1: Data Loading and Exploration")
    print("="*80)

    agent = SEMWorkflowAgent()

    # 加载数据
    try:
        data, inspection = agent.load_data(TEST_DATA)
        print("[OK] Data loaded successfully")
        print(f"  Rows: {inspection['n_rows']}")
        print(f"  Columns: {inspection['n_cols']}")
        print(f"  Missing cells: {inspection['missing_total']} ({inspection['missing_percent']:.1f}%)")
        success = True
    except Exception as e:
        print(f"[NO] Data loading failed: {e}")
        success = False
        data = None

    # 缺失值分析
    if data is not None:
        try:
            missing_analysis = agent.assess_missing_data(data)
            print("\n[OK] Missing data analysis completed")
            print(f"  Complete cases: {missing_analysis['complete_cases']} ({missing_analysis['complete_percent']:.1f}%)")
            print(f"  Recommendation: {missing_analysis['recommendation'][:100]}...")
        except Exception as e:
            print(f"\n[NO] Missing data analysis failed: {e}")
            success = False

    return success

def test_theory_validation():
    """测试 2: 理论模型验证"""
    print("\n" + "="*80)
    print("TEST 2: Theory Validation")
    print("="*80)

    agent = SEMWorkflowAgent()
    data, _ = agent.load_data(TEST_DATA)

    # 定义一个社会学理论模型
    theory = {
        "latent_variables": {
            "job_satisfaction": ["sat1", "sat2", "sat3", "sat4"],
            "work_engagement": ["eng1", "eng2", "eng3", "eng4"],
            "organizational_loyalty": ["loy1", "loy2", "loy3", "loy4"]
        },
        "structural_paths": [
            {"outcome": "work_engagement", "predictors": ["job_satisfaction"]},
            {"outcome": "organizational_loyalty", "predictors": ["work_engagement", "job_satisfaction"]}
        ],
        "covariances": []
    }

    try:
        is_valid, issues = agent.validate_theory(theory, data)
        print("[OK] Theory validation completed")
        print(f"  Valid: {is_valid}")
        if issues:
            print(f"  Issues found: {len(issues)}")
            for issue in issues[:3]:  # 只显示前3个
                print(f"    - {issue}")
        else:
            print("  No issues found")

        # 测试参数计数
        n_params = agent._count_parameters(theory)
        print(f"  Number of parameters: {n_params}")
        print(f"  Sample size: {len(data)}")
        print(f"  N/parameters ratio: {len(data)/n_params:.1f}")

        return True
    except Exception as e:
        print(f"[NO] Theory validation failed: {e}")
        return False

def test_model_building():
    """测试 3: 模型构建"""
    print("\n" + "="*80)
    print("TEST 3: Model Building")
    print("="*80)

    agent = SEMWorkflowAgent()

    theory = {
        "latent_variables": {
            "job_satisfaction": ["sat1", "sat2", "sat3", "sat4"],
            "work_engagement": ["eng1", "eng2", "eng3", "eng4"],
            "organizational_loyalty": ["loy1", "loy2", "loy3", "loy4"]
        },
        "structural_paths": [
            {"outcome": "work_engagement", "predictors": ["job_satisfaction"]},
            {"outcome": "organizational_loyalty", "predictors": ["work_engagement"]}
        ],
        "covariances": []
    }

    try:
        model_desc = agent.build_model_description(theory)
        print("[OK] Model description built successfully")
        print("\nModel syntax:")
        print("-"*40)
        print(model_desc)
        print("-"*40)

        # 验证模型描述包含必要的部分
        checks = [
            ("Measurement model", "# Measurement model" in model_desc or "=~" in model_desc),
            ("Latent variable 1", "job_satisfaction =~" in model_desc),
            ("Latent variable 2", "work_engagement =~" in model_desc),
            ("Latent variable 3", "organizational_loyalty =~" in model_desc),
            ("Structural paths", "~" in model_desc and "work_engagement ~" in model_desc),
        ]

        print("\nModel syntax validation:")
        all_passed = True
        for name, passed in checks:
            status = "[OK]" if passed else "[NO]"
            print(f"  {status} {name}")
            if not passed:
                all_passed = False

        return all_passed
    except Exception as e:
        print(f"[NO] Model building failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_model_fitting():
    """测试 4: 模型拟合"""
    print("\n" + "="*80)
    print("TEST 4: Model Fitting")
    print("="*80)

    agent = SEMWorkflowAgent()
    data, _ = agent.load_data(TEST_DATA)

    theory = {
        "latent_variables": {
            "job_satisfaction": ["sat1", "sat2", "sat3", "sat4"],
            "work_engagement": ["eng1", "eng2", "eng3", "eng4"],
            "organizational_loyalty": ["loy1", "loy2", "loy3", "loy4"]
        },
        "structural_paths": [
            {"outcome": "work_engagement", "predictors": ["job_satisfaction"]},
            {"outcome": "organizational_loyalty", "predictors": ["work_engagement"]}
        ],
        "covariances": []
    }

    agent.theory = theory
    agent.build_model_description(theory)

    try:
        print("Attempting to fit model...")
        success, results = agent.fit_model(data, obj='MLW', solver='SLSQP')

        if success:
            print("[OK] Model fitted successfully!")
            print(f"  Optimizer: {results['solver']}")
            print(f"  Objective: {results['objective']}")
            print(f"  Results: {str(results['results'])[:100]}...")

            # 检查参数估计
            if agent.parameter_estimates is not None:
                print(f"  Parameter estimates shape: {agent.parameter_estimates.shape}")
                print(f"  Parameters with estimates: {len(agent.parameter_estimates)}")
        else:
            print("[NO] Model fitting failed")
            print(f"  Results: {results}")

        return success
    except Exception as e:
        print(f"[NO] Model fitting raised exception: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_diagnostics():
    """测试 5: 模型诊断"""
    print("\n" + "="*80)
    print("TEST 5: Model Diagnostics")
    print("="*80)

    agent = SEMWorkflowAgent()
    data, _ = agent.load_data(TEST_DATA)

    theory = {
        "latent_variables": {
            "job_satisfaction": ["sat1", "sat2", "sat3", "sat4"],
            "work_engagement": ["eng1", "eng2", "eng3", "eng4"],
            "organizational_loyalty": ["loy1", "loy2", "loy3", "loy4"]
        },
        "structural_paths": [
            {"outcome": "work_engagement", "predictors": ["job_satisfaction"]},
            {"outcome": "organizational_loyalty", "predictors": ["work_engagement"]}
        ],
        "covariances": []
    }

    agent.theory = theory
    agent.build_model_description(theory)

    try:
        success, _ = agent.fit_model(data)
        if not success:
            print("[NO] Cannot test diagnostics: model fitting failed")
            return False

        # 获取拟合指数
        fit_stats = agent.get_fit_indices()
        print("[OK] Fit indices calculated")
        print("\nFit indices:")
        for idx, row in fit_stats.iterrows():
            value = row.get('Value', row.iloc[0])
            print(f"  {idx}: {value:.4f}")

        # 解释拟合
        fit_interp = agent.interpret_fit()
        print(f"\n[OK] Fit interpretation generated")
        print(f"  Overall fit: {fit_interp['overall_fit']}")
        if fit_interp['issues']:
            print(f"  Issues: {len(fit_interp['issues'])}")
            for issue in fit_interp['issues'][:2]:
                print(f"    - {issue}")

        return True
    except Exception as e:
        print(f"[NO] Diagnostics failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_parameter_explanation():
    """测试 6: 参数解释"""
    print("\n" + "="*80)
    print("TEST 6: Parameter Explanation")
    print("="*80)

    agent = SEMWorkflowAgent()
    data, _ = agent.load_data(TEST_DATA)

    theory = {
        "latent_variables": {
            "job_satisfaction": ["sat1", "sat2", "sat3", "sat4"],
            "work_engagement": ["eng1", "eng2", "eng3", "eng4"],
            "organizational_loyalty": ["loy1", "loy2", "loy3", "loy4"]
        },
        "structural_paths": [
            {"outcome": "work_engagement", "predictors": ["job_satisfaction"]},
            {"outcome": "organizational_loyalty", "predictors": ["work_engagement"]}
        ],
        "covariances": []
    }

    agent.theory = theory
    agent.build_model_description(theory)

    try:
        success, _ = agent.fit_model(data)
        if not success:
            print("[NO] Cannot test parameter explanation: model fitting failed")
            return False

        # 解释参数
        explanation = agent.explain_parameters()
        print("[OK] Parameter explanation generated")

        if "measurement_model" in explanation:
            print(f"\nMeasurement model: {len(explanation['measurement_model'])} latent variables")
            for latent, loadings in explanation['measurement_model'].items():
                sig_count = sum(1 for l in loadings if l['significant'])
                print(f"  {latent}: {len(loadings)} indicators, {sig_count} significant")

        if "structural_model" in explanation:
            print(f"\nStructural model: {len(explanation['structural_model'])} outcome variables")
            for outcome, paths in explanation['structural_model'].items():
                for path in paths:
                    sig = "[OK]" if path['significant'] else "[NO]"
                    print(f"  {sig} {path['from']} → {path['to']}: β={path['estimate']:.3f}, {path['effect_size']} effect")

        if explanation["problematic"]:
            print(f"\n[!]  Problematic parameters: {len(explanation['problematic'])}")
            for p in explanation['problematic'][:3]:
                print(f"  - {p}")

        return True
    except Exception as e:
        print(f"[NO] Parameter explanation failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_report_generation():
    """测试 7: 报告生成"""
    print("\n" + "="*80)
    print("TEST 7: Report Generation")
    print("="*80)

    agent = SEMWorkflowAgent()
    data, _ = agent.load_data(TEST_DATA)

    theory = {
        "latent_variables": {
            "job_satisfaction": ["sat1", "sat2", "sat3", "sat4"],
            "work_engagement": ["eng1", "eng2", "eng3", "eng4"],
            "organizational_loyalty": ["loy1", "loy2", "loy3", "loy4"]
        },
        "structural_paths": [
            {"outcome": "work_engagement", "predictors": ["job_satisfaction"]},
            {"outcome": "organizational_loyalty", "predictors": ["work_engagement"]}
        ],
        "covariances": []
    }

    agent.theory = theory
    agent.build_model_description(theory)

    try:
        success, _ = agent.fit_model(data)
        if not success:
            print("[NO] Cannot generate report: model fitting failed")
            return False

        report = agent.generate_report("sem_test_report.txt")
        print("[OK] Report generated successfully")
        print(f"  Report length: {len(report)} characters")
        print(f"  Report saved to: sem_test_report.txt")

        # 检查报告关键部分
        sections = [
            "DATA SUMMARY",
            "MODEL SPECIFICATION",
            "MODEL FIT",
            "PARAMETER ESTIMATES",
            "RECOMMENDATIONS"
        ]

        print("\nReport sections check:")
        all_present = True
        for section in sections:
            present = section in report
            status = "[OK]" if present else "[NO]"
            print(f"  {status} {section}")
            if not present:
                all_present = False

        # 显示报告前几行
        print("\nReport preview (first 300 chars):")
        print("-"*40)
        print(report[:300] + "...")
        print("-"*40)

        return all_present
    except Exception as e:
        print(f"[NO] Report generation failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_data_preparator():
    """测试 8: DataPreparator 模块"""
    print("\n" + "="*80)
    print("TEST 8: DataPreparator Module")
    print("="*80)

    try:
        from sem_workflow.data_preparator import DataPreparator
        import pandas as pd

        data = pd.read_csv(TEST_DATA)

        # 测试缺失值策略建议
        strategy = DataPreparator.suggest_missing_strategy(data)
        print(f"[OK] Missing data strategy: {strategy}")

        # 测试异常值检测
        outliers = DataPreparator.detect_outliers(data, threshold=3.0)
        print(f"[OK] Outlier detection: {len(outliers)} outliers found")

        # 测试方差检查
        low_var = DataPreparator.check_variance(data, min_variance=0.1)
        print(f"[OK] Variance check: {len(low_var)} variables with low variance")

        return True
    except Exception as e:
        print(f"[NO] DataPreparator test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_model_builder_standalone():
    """测试 9: ModelBuilder 独立功能"""
    print("\n" + "="*80)
    print("TEST 9: ModelBuilder Standalone")
    print("="*80)

    try:
        from sem_workflow.model_builder import ModelBuilder

        # 测试 CFA 模型构建
        cfa_spec = {
            'job_satisfaction': ['sat1', 'sat2', 'sat3', 'sat4'],
            'work_engagement': ['eng1', 'eng2', 'eng3', 'eng4']
        }
        cfa_model = ModelBuilder.build_cfa_model(cfa_spec)
        print("[OK] CFA model built")
        print(cfa_model[:200] + "...")

        # 验证语法
        checks = [
            ("job_satisfaction =~" in cfa_model, "Factor 1 defined"),
            ("work_engagement =~" in cfa_model, "Factor 2 defined"),
            ("~~" in cfa_model, "Factor covariance included")
        ]
        print("\nCFA model validation:")
        all_passed = True
        for passed, name in checks:
            status = "[OK]" if passed else "[NO]"
            print(f"  {status} {name}")
            if not passed:
                all_passed = False

        return all_passed
    except Exception as e:
        print(f"[NO] ModelBuilder test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_edge_cases():
    """测试 10: 边界情况"""
    print("\n" + "="*80)
    print("TEST 10: Edge Cases")
    print("="*80)

    agent = SEMWorkflowAgent()

    # 测试 1: 小样本 (<200)
    print("\nEdge case 1: Small sample size")
    try:
        small_data = pd.DataFrame({
            'x1': np.random.normal(0, 1, 50),
            'x2': np.random.normal(0, 1, 50),
            'x3': np.random.normal(0, 1, 50),
            'y1': np.random.normal(0, 1, 50),
            'y2': np.random.normal(0, 1, 50),
            'y3': np.random.normal(0, 1, 50),
        })
        small_theory = {
            "latent_variables": {
                "factor1": ["x1", "x2", "x3"],
                "factor2": ["y1", "y2", "y3"]
            },
            "structural_paths": [{"outcome": "factor2", "predictors": ["factor1"]}],
            "covariances": []
        }

        is_valid, issues = agent.validate_theory(small_theory, small_data)
        print(f"  Validation: {is_valid}")
        if issues:
            print(f"  Issues detected: {issues[0][:80]}")
        print("  [OK] Small sample case handled")
    except Exception as e:
        print(f"  [NO] Small sample test failed: {e}")

    # 测试 2: 变量缺失
    print("\nEdge case 2: Missing variables in theory")
    try:
        data = pd.read_csv(TEST_DATA)
        bad_theory = {
            "latent_variables": {
                "factor1": ["x1", "x2", "nonexistent_column"]
            },
            "structural_paths": [],
            "covariances": []
        }
        is_valid, issues = agent.validate_theory(bad_theory, data)
        if not is_valid and "not found in data" in issues[0]:
            print("  [OK] Missing variable detected correctly")
        else:
            print("  [NO] Missing variable NOT detected")
    except Exception as e:
        print(f"  [NO] Missing variable test failed: {e}")

    # 测试 3: 指标数量不足 (<3)
    print("\nEdge case 3: Insufficient indicators (<3)")
    try:
        bad_theory = {
            "latent_variables": {
                "factor1": ["sat1"]  # 只有一个指标
            },
            "structural_paths": [],
            "covariances": []
        }
        is_valid, issues = agent.validate_theory(bad_theory, data)
        if not is_valid and "only 1 indicators" in issues[0].lower():
            print("  [OK] Insufficient indicators detected correctly")
        else:
            print("  [NO] Insufficient indicators NOT detected")
    except Exception as e:
        print(f"  [NO] Insufficient indicators test failed: {e}")

    return True

def main():
    print("="*80)
    print("SEM-WORKFLOW SKILL FUNCTIONALITY TEST REPORT")
    print("模拟社会学研究者视角（无统计/编程背景）")
    print("="*80)

    results = []

    # 运行所有测试
    tests = [
        ("Data Loading & Exploration", test_data_loading),
        ("Theory Validation", test_theory_validation),
        ("Model Building", test_model_building),
        ("Model Fitting", test_model_fitting),
        ("Model Diagnostics", test_diagnostics),
        ("Parameter Explanation", test_parameter_explanation),
        ("Report Generation", test_report_generation),
        ("DataPreparator Module", test_data_preparator),
        ("ModelBuilder Module", test_model_builder_standalone),
        ("Edge Cases Handling", test_edge_cases),
    ]

    for test_name, test_func in tests:
        try:
            passed = test_func()
            results.append((test_name, passed))
        except Exception as e:
            print(f"\n[NO] Test '{test_name}' crashed: {e}")
            import traceback
            traceback.print_exc()
            results.append((test_name, False))

    # 生成总结报告
    print("\n" + "="*80)
    print("TEST SUMMARY")
    print("="*80)

    passed_count = sum(1 for _, passed in results if passed)
    total_count = len(results)

    for test_name, passed in results:
        status = "[OK] PASS" if passed else "[NO] FAIL"
        print(f"{status}: {test_name}")

    print(f"\nTotal: {passed_count}/{total_count} tests passed ({passed_count/total_count*100:.1f}%)")

    if passed_count == total_count:
        print("\n[OK] ALL TESTS PASSED - The skill appears to fully implement its claimed features!")
    else:
        print(f"\n[!]  {total_count - passed_count} test(s) failed - Some features may be incomplete or buggy")

    print("\n" + "="*80)
    print("END OF TEST REPORT")
    print("="*80)

if __name__ == "__main__":
    main()
