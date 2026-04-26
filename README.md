# sem-analyzer

An open-source AI agent skill for interactive structural equation modeling (SEM). sem-analyzer encodes the expert SEM workflow into a stateful, multi-step procedure that runs inside any skills-enabled agent runtime.

## Features

- **8-Step Clarification Workflow** — Guided model specification with validation at every step
- **Automated Inference** — Sobel mediation test (1.000 sensitivity/specificity), KS grouping detection, time-series variable recognition
- **Advanced Templates** — CFA, latent growth models, mediation with BCa bootstrap CIs, interactive multi-group invariance testing
- **Embedded Knowledge Base** — 2,600+ indexed sections from 8 SEM reference works with stage-aware retrieval
- **Architectural Guardrails** — Catches underidentification, circular paths, measurement-level violations, and incorrect inference methods
- **Report Generation** — Structured Markdown and DOCX export with fit indices, parameter estimates, and decision audit trail

## Installation

```bash
# Clone
git clone https://github.com/zjiang4/sem-analyzer.git
cd sem-analyzer

# Install dependencies (uv recommended)
uv sync

# Or with pip
pip install semopy pandas numpy scipy python-docx
```

## Quick Start

sem-analyzer runs as a **skill module** inside an AI agent. After loading the skill:

1. **Upload your CSV data** to the agent
2. The skill initiates the **8-step clarification**:
   - Outcome selection → Predictor selection → Variable classification → Indicator definition → Covariate classification → Structural paths → Missing data strategy → Confirmation
3. After confirmation, the model is **estimated automatically**
4. Request **advanced analyses** in natural language:
   - `"run a CFA"`
   - `"mediation analysis X → M → Y"`
   - `"growth model with loadings 0, 0.5, 1, 1.5"`
   - `"multi-group invariance test by gender"`
5. **Export** the report: `"export report"` or `"export report as Word"`

## Project Structure

```
sem-analyzer/
├── core/
│   ├── advanced_fitter.py      # Estimation engine, BCa bootstrap, multigroup
│   ├── model_draft.py          # Model specification data class
│   ├── sem_fitter.py           # Base SEM fitter (semopy wrapper)
│   ├── templates.py            # CFA / Growth / Mediation / Multigroup templates
│   └── textbook_retriever_v2.py # Handbook knowledge base index
├── interaction/
│   ├── clarifier.py            # 8-step clarification state machine
│   ├── followup_processor.py   # Post-confirmation command handler
│   └── report_formatter.py     # Markdown / DOCX report generation
├── utils/
│   └── state_manager.py        # Session state management
├── visualization/
│   └── dot_generator.py        # DOT graph generation
├── handbooks/                  # 8 SEM reference work markdown files
├── tests/                      # Test suite (11 unit + 39 E2E scenarios)
├── entry.py                    # Skill entry point
├── build_handbook_index.py     # Pre-builds handbook_index.json
├── handbook_index.json         # Pre-built keyword index (2,604 sections)
└── eval_inference.py           # Evaluation script for automated heuristics
```

## Supported Analysis Types

| Type | Description | Key Feature |
|------|-------------|-------------|
| **Path Model** | Basic structural regression | Default specification |
| **CFA** | Confirmatory factor analysis | First-loading-fixed identification |
| **Growth** | Latent growth curve model | User-defined time loadings |
| **Mediation** | X → M → Y indirect effects | BCa bootstrap CIs (default B=500) |
| **Multigroup** | Measurement invariance | Interactive configural → metric → scalar |

## Testing

```bash
# Unit tests (11 tests)
pytest tests/ -v

# E2E verification (39 scenarios, 12 paper claims)
python tests/test_e2e_verification.py

# Heuristic evaluation
python eval_inference.py
```

## Tech Stack

- **Estimation**: [semopy](https://github.com/yxzl/semopy) (Python SEM library)
- **Bootstrap**: NumPy-based BCa with jackknife acceleration
- **Mediation test**: Sobel (1982) product-of-coefficients via OLS
- **Knowledge base**: Pre-built inverted index (offline, no LLM needed)
- **Export**: python-docx for Word, native Markdown

## License

MIT

## Citation

If you use sem-analyzer in your research, please cite:

> sem-analyzer: A Skills-Based AI Architecture for Interactive Structural Equation Modeling.
