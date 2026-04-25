# SEM Analyzer Skill

## Overview

Provides **guided Structural Equation Modeling (SEM) analysis** for applied researchers. Through natural language interaction, it helps users:

- Define latent-to-observed variable mappings
- Visually confirm model structure
- Automatically fit and interpret results
- Generate publication-ready academic reports
- Learn SEM concepts through integrated textbook guidance

## Core Features

- **Zero barrier to entry**: Users upload data and describe their hypothesis in a single sentence
- **Visual confirmation**: Each step produces a model sketch; the user must confirm before proceeding
- **Session continuity**: Supports model adjustments (add/remove paths, change indicators) with automatic refitting
- **Educational feedback**: Every step includes relevant textbook excerpts from 8 SEM reference books, plain-language explanations of fit indices, diagnostics, and modification suggestions
- **Rich output**: Markdown reports (executive summary + technical details + textbook references), ASCII path diagrams, data tables

## Built-in Textbook Knowledge

The skill ships with a pre-built index of **8 curated SEM reference works** (2,604 indexed sections). Sources are labeled generically (SEM Reference A–H) to avoid reproducing copyrighted bibliographic details. At every step of the analysis workflow, the skill retrieves and presents:

- Relevant chapter titles and generic source attribution
- Content summaries explaining the concept
- Content excerpts with practical guidance

## Installation

```bash
pip install semopy pandas numpy scipy
```

## Usage

### 8-Step Clarification Workflow

1. **Send data** (CSV/Excel file) or paste raw data text
2. **Describe research hypothesis** (e.g., "Learning satisfaction influences achievement through study engagement")
3. **Confirm latent-variable-to-indicator mappings**
4. **Confirm structural path directions**
5. **Review the full model sketch**
6. **Fit the model** (automatic ML estimation via semopy)
7. **Review results**: fit indices, coefficient table, diagnostics
8. **Generate report**: Markdown format with textbook references, ready to paste into a manuscript

### Example Dialog

```
User: I want to run a SEM analysis. [attachment: data.csv]
Skill: Data loaded (N=326). Possible latent variables detected: sat1-3 (satisfaction), se1-4 (engagement)
       Please describe your research hypothesis.

Recommended reading:
  **Model Specification** (Kline SEM)
    A properly specified model is one whose structure corresponds to the true population...

User: Learning satisfaction influences achievement through study engagement.
Skill: I have drafted the following model:
       Measurement: satisfaction =~ sat1 + sat2 + sat3; engagement =~ se1 + se2 + se3 + se4
       Structural: satisfaction -> engagement -> achievement
       Do you also need a direct path from satisfaction to achievement? [Yes/No]

Recommended reading:
  **Structural Equation Models with Latent Variables** (SEM Handbook)
    Structural models specify directional relationships among latent constructs...
...
```

## Tech Stack

- **semopy**: SEM estimation engine
- **pandas**: Data handling
- **scipy**: Bootstrap CI, JSD, KS tests
- **graphviz** (optional): Path diagram rendering
- **python-docx** (optional): Word report output

## Session Commands

All commands work without re-uploading data:

| Command | Description |
|---|---|
| `fit` | Fit or refit the current model |
| `add path X -> Y` | Add a structural path |
| `remove path X -> Y` | Remove a structural path |
| `change missing <method>` | Change missing-data handling method |
| `mediation X M Y` | Run mediation analysis with bootstrap CI |
| `growth model loadings 0 1 2` | Specify a growth model with time loadings |
| `multigroup <var>` | Run multigroup analysis (configural → metric → scalar) |
| `metric` | Test metric invariance (after configural) |
| `scalar` | Test scalar invariance (after metric) |
| `export report` | Export report (markdown) |
| `export report docx` | Export report (Word) |
| `diagram` | Display model diagram (DOT) |
| `results` | Show fit indices and parameter estimates |

## Limitations

- Continuous variables only (Likert 5/7-point scales are acceptable)
- Each latent variable requires at least 2 indicators
- Recommended sample size: N > 100 for simple models, N > 200 for complex models
- Multigroup analysis requires group variable specification
- Categorical latent variables (Mplus-style) are not supported

---

## Architecture

```
entry.py                  → SemAnalyzerSkill (routing, session management)
├── interaction/
│   ├── clarifier.py      → 8-step clarification with textbook guidance
│   ├── model_confirm.py  → Model review and confirmation
│   ├── followup_processor.py → Post-fit commands, advanced analysis
│   └── report_formatter.py   → Markdown/DOCX report generation
├── core/
│   ├── advanced_fitter.py     → BCa bootstrap, multigroup, growth
│   ├── templates.py           → Model syntax generation (CFA/mediation/multigroup/growth)
│   ├── model_draft.py         → Editable model with validation (guardrails)
│   ├── textbook_retriever_v2.py → Handbook index (pre-built JSON)
│   ├── data_validator.py      → Variable type detection
│   └── sem_fitter.py          → Basic SEM fitting
├── build_handbook_index.py    → Rebuild index from handbooks/ MD files
└── handbooks/                 → 8 SEM textbook Markdown files
    └── handbook_index.json    → Pre-built index (2604 sections, 4652 keywords)
```
