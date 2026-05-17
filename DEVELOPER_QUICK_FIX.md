# SEM-Analyzer Skill: 开发者快速修复指南

**基于**： sociology researcher user-testing report (`SEM_ANALYZER_USER_TEST_REPORT.md`)
**日期**：2026-05-17
**技能路径**：`C:\Users\zjian\.opencode\skills\sem-workflow\`

---

## 1. 问题概述

社会学研究者使用 `npx opencode` 调用 `sem-workflow` skill 进行 SEM 分析，发现**核心分析流程在模型拟合后完全崩溃**，无法得到任何结果。

**根本原因**：3个严重 bug in `agent.py` + 1个关键功能缺失。

---

## 2. 快速复现步骤

```bash
# 1. 进入项目目录
cd "C:\Users\zjian\.opencode\skills\sem-workflow"

# 2. 运行测试脚本（会失败）
# 测试脚本位置：C:\Users\zjian\autoresearch_knowledge_map\test_sem_workflow.py

# 3. 预期失败点：
#    - Test 5: interpret_fit() 崩溃 (ValueError: Series truth ambiguous)
#    - Test 6: explain_parameters() 崩溃 (TypeError: '<' between str and float)
#    - 后续所有测试依赖失败
```

---

## 3. 关键 Bugs 和修复

### Bug #1: `interpret_fit()` 的 DataFrame 提取错误

**位置**：`agent.py` 第 340-343 行（方法 `interpret_fit`）

**错误代码**：
```python
rmsea = stats.get("RMSEA", 1.0)  # stats 是 DataFrame，get() 返回 Series
if rmsea < 0.05:  # 引发 ValueError: Series truth ambiguous
```

**原因**：`semopy.calc_stats()` 返回的 `stats` 是 DataFrame（单行多列），`stats.get(key)` 返回的是包含该列的 Series，不是标量。

**修复**：从 Series 提取标量值，并处理字符串格式的 p-value。

```python
def interpret_fit(self) -> Dict:
    # ... [前面不变]
    stats = self.fit_stats
    
    def _get_scalar(key, default):
        val = stats.get(key, default)
        if isinstance(val, (pd.Series, pd.DataFrame)):
            if isinstance(val, pd.DataFrame):
                if key in val.columns:
                    val = val[key].iloc[0]
                elif key in val.index:
                    val_series = val.loc[key]
                    val = val_series.iloc[0] if hasattr(val_series, 'iloc') else val_series
                else:
                    val = default
            else:  # Series
                val = val.iloc[0] if len(val) > 0 else default
        # 处理 string like "<0.001"
        if isinstance(val, str):
            if val.startswith('<'):
                try: return float(val[1:])
                except: return 0.001
            if val.startswith('>'):
                try: return float(val[1:])
                except: return 0.999
            try: return float(val)
            except: return default
        return float(val) if val is not None else default

    rmsea = _get_scalar("RMSEA", 1.0)
    cfi = _get_scalar("CFI", 0.0)
    tli = _get_scalar("TLI", 0.0)
    srmr = _get_scalar("SRMR", 0.1)
    
    # ... [后面不变]
```

**影响**：修复后，`interpret_fit()` 可正常返回拟合解释。

---

### Bug #2: `explain_parameters()` p-value 类型错误

**位置**：`agent.py` 第 436 行附近（在 `explain_parameters` 循环中）

**错误代码**：
```python
"significant": row["p-value"] < 0.05,
```

**问题**：`row["p-value"]` 可能是字符串（如 `"<0.001"` 或 `"0.000"`），导致 `TypeError: '<' not supported between instances of 'str' and 'float'`。

**原因**：`semopy` 对于非常小的 p 值返回格式化字符串。

**修复**：复用上面的 `_get_scalar` 或独立的 `_to_float` 转换。

```python
def _to_float(self, val, default=0.0):
    if isinstance(val, (int, float)):
        return float(val)
    if isinstance(val, str):
        val_str = val.strip()
        if val_str.startswith('<') or val_str.startswith('>'):
            # 对于 "<0.001"，解析为 0.001 的阈值或返回 0.0005
            try: return float(val_str[1:])
            except: return 0.001 if val_str.startswith('<') else 0.999
        try: return float(val_str)
        except: return default
    return default
```

然后在循环中使用：
```python
p_value = self._to_float(row["p-value"])
significant = p_value < 0.05
```

**影响**：修复后，才能正确判断参数显著性。

---

### Bug #3: `explain_parameters()` 参数分类逻辑错误

**位置**：`agent.py` 第 419-449 行（原始版本）

**错误代码**：
```python
# 原始逻辑
if rval in self.theory.get("latent_variables", {}):
    # 认为是测量模型
else:
    # 认为是结构模型
```

**问题**：这个逻辑完全错误！

**为什么错**：
- `semopy` 的 `model.inspect()` 输出中：
  - `=~` 操作：`lval` = observed indicator, `rval` = latent factor
  - `~` 操作：`lval` = outcome, `rval` = predictor
- 在原始 code 中：
  - 测量模型：`rval` 是 latent → 正确（因为 rval 在 theory 的 latent_variables 中）
  - 结构模型：`rval` 是 **predictor**，可能也是 latent（在 latent_variables 中！）

**结果**：结构路径（如 `organizational_loyalty ~ work_engagement`）被错误归类为测量模型，因为 `work_engagement` 在 `latent_variables` 中！

**正确逻辑**：使用 `row["op"]`（操作符）区分：

```python
for idx, row in self.parameter_estimates.iterrows():
    lval = row["lval"]
    rval = row["rval"]
    op = row["op"]
    estimate = self._to_float(row["Estimate"])
    p_value = self._to_float(row["p-value"])

    if op == "=~":
        # 测量模型：factor =~ indicator
        factor = rval
        indicator = lval
        if indicator not in explanation["measurement_model"]:
            explanation["measurement_model"][indicator] = []
        explanation["measurement_model"][indicator].append({
            "factor": factor,
            "estimate": estimate,
            "p_value": p_value,
            "significant": p_value < 0.05,
        })
        # check loading quality...

    elif op == "~":
        # 结构模型：outcome ~ predictors
        outcome = lval
        predictor = rval
        if outcome not in explanation["structural_model"]:
            explanation["structural_model"][outcome] = []
        explanation["structural_model"][outcome].append({
            "from": predictor,
            "to": outcome,
            "estimate": estimate,
            "p_value": p_value,
            "significant": p_value < 0.05,
            "effect_size": self._interpret_effect_size(estimate),
        })
```

**影响**：修复后，测量模型和结构模型的参数才能正确分类和解释。

---

### Bug #4: `get_theory_from_user()` 空实现

**位置**：`agent.py` 第 118-127 行

**现状**：方法名"interactive"但实际上返回空字典，用户无法输入理论。

**问题**：这是设计缺陷。在 opencode 的 agent 框架中，agent 的方法调用是**非交互式**的（通过函数参数传值），不是传统的 `input()` 命令行交互。

**解决方案 options**：

#### Option A: 简化为参数驱动（推荐）
不实现真正的 `input()`，而是让 `interactive_workflow()` 接受一个 `theory` 参数：

```python
def interactive_workflow(self, filepath: str, theory: Dict = None):
    # ...
    if theory is None:
        # 使用一个简单的默认理论用于演示
        print("WARNING: No theory provided. Using demo theory.")
        theory = self._get_demo_theory()
    else:
        self.theory = theory
```

#### Option B: 实现为生成器/yield 模式（需要 opencode 框架支持）
返回问题的列表，让框架收集用户回答。

**建议**：因为 `sem-workflow` skill 是集成到 opencode 而非独立运行，**应遵循 opencode 的 agent pattern**：

- Agent 的方法应接收明确的参数（如 `theory` dict）
- 交互式收集应该由 opencode 的主循环处理，不是 skill 内部处理

因此，**不修复此方法，而是在 `interactive_workflow` 中添加 `theory` 参数**：

```python
def interactive_workflow(self, filepath: str, theory: Dict):
    """
    Args:
        filepath: CSV data path
        theory: {
            "latent_variables": {"factor1": ["x1","x2","x3"], ...},
            "structural_paths": [{"outcome": "y", "predictors": ["x1","x2"]}, ...],
            "covariances": [{"var1":"e1", "var2":"e2"}, ...]
        }
    """
    self.theory = theory
    # ... 继续流程
```

---

## 4. 修复验证脚本

运行以下命令验证修复：

```bash
# 1. 应用所有修复到 agent.py
# （根据上述修复内容手动编辑）

# 2. 运行测试脚本
python "C:\Users\zjian\autoresearch_knowledge_map\test_sem_workflow.py"

# 3. 预期通过所有测试
# 应看到：
# [OK] Test 1: Data Loading and Exploration
# [OK] Test 2: Theory Validation
# [OK] Test 3: Model Building
# [OK] Test 4: Model Fitting
# [OK] Test 5: Model Diagnostics
# [OK] Test 6: Parameter Explanation
# [OK] Test 7: Report Generation
# ...
# Total: 10/10 tests passed (100.0%)
# ✓ ALL TESTS PASSED
```

---

## 5. 其他重要修复和建议（非阻塞但重要）

### 5.1 修复 `generate_report()` 对 `interpret_fit` 的调用

`generate_report()` 中调用 `fit_interp = self.interpret_fit()` 会再次触发 fit_stats 提取，建议：

```python
def generate_report(self, output_file: str = None) -> str:
    # ...
    fit_interp = self.interpret_fit()  # 确保 fit_stats 已计算
    # 或者直接使用已有的 fit_interp if cached
    # ...
```

### 5.2 添加 `_to_float` 辅助方法

将通用的类型转换逻辑提取为类方法，避免重复：

```python
def _to_float(self, val, default=0.0):
    """Safely convert any value to float, handling special string formats."""
    if isinstance(val, (int, float)):
        return float(val)
    if isinstance(val, str):
        val_str = val.strip()
        if val_str.startswith('<'):
            try: return float(val_str[1:])
            except: return 0.001
        if val_str.startswith('>'):
            try: return float(val_str[1:])
            except: return 0.999
        try: return float(val_str)
        except: return default
    return default
```

### 5.3 修复 `generate_report()` 中访问 `fit_stats` 的方式

```python
# Current:
for idx, row in self.fit_stats.iterrows():
    report_lines.append(f"  {idx}: {row.get('Value', row.values[0]):.4f}")

# Better (use _get_scalar):
rmsea = self._get_scalar_from_fit_stats("RMSEA")
cfi = self._get_scalar_from_fit_stats("CFI")
# ... then format
```

### 5.4 集成 `DataPreparator` 到主流程

在 `interactive_workflow()` 中添加：

```python
# Step 2.5: Data quality checks
print("\nStep 2.5: Checking data quality...")
outliers = DataPreparator.detect_outliers(data, threshold=3.0)
skewness = DataPreparator.check_normality(data)
# 报告给用户
```

### 5.5 更新文档

- 更新 `SKILL.md` 说明当前**已实现**的功能 vs **规划中**的功能
- 添加 `KNOWN_ISSUES.md` 列出已知 bugs
- 添加真实的使用示例（not 伪代码）

---

## 6. 文件位置参考

| 文件 | 路径 |
|------|------|
| 原始 skill code | `C:\Users\zjian\.opencode\skills\sem-workflow\` |
| `agent.py` | `...\sem-workflow\agent.py` |
| `data_preparator.py` | `...\sem-workflow\data_preparator.py` |
| `diagnostics.py` | `...\sem-workflow\diagnostics.py` |
| `model_builder.py` | `...\sem-workflow\model_builder.py` |
| `interpreter.py` | `...\sem-workflow\interpreter.py` |
| `visualizer.py` | `...\sem-workflow\visualizer.py` |
| SKILL.md | `...\sem-workflow\SKILL.md` |
| README.md | `...\sem-workflow\README.md` |
| 用户测试报告 | `C:\Users\zjian\autoresearch_knowledge_map\SEM_ANALYZER_USER_TEST_REPORT.md` |
| 本指南 | `C:\Users\zjian\autoresearch_knowledge_map\DEVELOPER_QUICK_FIX.md` |

---

## 7. 测试数据

**测试数据集**：`C:\Users\zjian\autoresearch_knowledge_map\test_sem_data.csv`

```csv
# 生成脚本见 test_sem_workflow.py 第 9-40 行
# 结构：N=250, 3 latent factors, 4 indicators each + 3 controls
```

---

## 8. 时间估计

| 任务 | 时间 |
|------|------|
| Bug #1 (interpret_fit) | 30 分钟 |
| Bug #2 (p-value conversion) | 30 分钟 |
| Bug #3 (parameter classification) | 1 小时 |
| 集成 DataPreparator | 2-3 小时 |
| 修复 generate_report | 1 小时 |
| 测试完整流程 | 1 小时 |
| 文档更新 | 2 小时 |
| **总计** | **7-8 小时** |

---

## 9. 验证清单

修复后，运行 `test_sem_workflow.py` 并确认：

- [ ] Test 1: Data loading - PASS
- [ ] Test 2: Theory validation - PASS
- [ ] Test 3: Model building - PASS
- [ ] Test 4: Model fitting - PASS
- [ ] Test 5: Model diagnostics - PASS, fit interpretation correct
- [ ] Test 6: Parameter explanation - PASS, measurement vs structural correctly separated
- [ ] Test 7: Report generation - PASS, report contains all sections
- [ ] Test 8: DataPreparator - PASS, methods work (even if not integrated yet)
- [ ] Test 9: ModelBuilder - PASS
- [ ] Test 10: Edge cases - PASS, proper warnings for small N, missing vars, etc.

---

## 10. 联系方式 & 反馈

本指南基于**真实用户测试**，不是理论推测。开发者应优先修复 blocking bugs，再进行优化。

如果修复后仍有问题，请复现测试并更新 `KNOWN_ISSUES.md`。
