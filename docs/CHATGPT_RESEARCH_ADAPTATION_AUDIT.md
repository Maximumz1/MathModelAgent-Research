# ChatGPT / Codex Engineering Research Adaptation Audit

Branch: `chatgpt-research-adaptation`

## Executive summary

The repository has a strong reusable core, especially the staged workflow, reproducibility contract, separation between data-driven figures and conceptual diagrams, and final consistency checks. However, the current skills are optimized for mathematical-modeling competitions and a Claude/local-shell style tool environment.

For engineering research, the safest migration strategy is **additive**:

- keep the original `skills/` unchanged as an upstream reference;
- build a new `research-skills/` layer for experimental engineering research;
- avoid rewriting the legacy backend/frontend unless the standalone MathModelAgent application itself is needed;
- keep outputs traceable to raw data, code, intermediate artifacts, figures, and manuscript claims.

## Compatibility matrix

| Component | Decision | Reason | Research adaptation |
|---|---|---|---|
| `skills/1start-mathmodel` | ADAPT | Good controller pattern, but asks competition-specific preferences and assumes Claude-style tools | Replace with research controller, project stage, data source, output target, validation gates |
| `skills/2analysis-modeling` | SPLIT + ADAPT | Strong ambiguity checking and model formulation, but mixes problem analysis, data audit, and modeling | Split into problem definition, experimental/data audit, physical/statistical modeling |
| `skills/3coding-visual` | KEEP + EXTEND | Strong reproducibility and result-record discipline | Add provenance, unit checks, calibration metrics, uncertainty, data-leakage checks, environment capture |
| `skills/4drawio` | OPTIONAL ADAPT | Useful for method/system diagrams, but CLI/export assumptions are environment-specific | Keep diagram role; allow DrawIO, Mermaid, Graphviz, image tools, or manual export depending on environment |
| `skills/5writing` | REPLACE FOR RESEARCH | Mostly competition-template logic | Replace with journal-aware manuscript writing and explicit evidence/claim traceability |
| `skills/6verity` | KEEP + REWORK | Best reusable component; strong numerical/text/figure/PDF consistency gates | Add citation audit, claim-to-evidence checks, uncertainty/reporting checks, journal compliance |
| `skills/doctor` | LOCAL-ONLY | Useful for a local Codex/Claude shell, not a browser-native ChatGPT workflow | Keep as optional local environment checker |
| `skills/typst-author` | KEEP AS UTILITY | General-purpose Typst support | Use only when Typst output is explicitly selected |
| `skills/mathmodel-figure-templates` | KEEP WITH GUARDRAILS | Useful scientific plotting patterns | Never present simulated template data as experimental results; replace with traceable user data |
| `skills/_references/math_modeling_norms.md` | MINE + FORK | Contains solid generic modeling safeguards but is competition-oriented | Create a separate engineering-research norms reference |
| Legacy `backend/` + `frontend/` | LEAVE UNCHANGED | Standalone application architecture is separate from ChatGPT browser/Codex skill use | Revisit only if deploying the original app |

## Tool compatibility findings

The original skills declare tools such as:

`Bash, Read, Write, Edit, Grep, Glob, Agent, WebSearch, WebFetch, AskUserQuestion`

These names are harness-specific and should not be assumed to exist unchanged in ChatGPT browser, Codex, or other agents.

The research layer should therefore:

1. describe **capabilities** rather than depend on one tool name;
2. use the tools available in the active environment;
3. never silently install dependencies;
4. ask for user confirmation before destructive or external write actions;
5. preserve a reproducible artifact trail even when a tool is unavailable.

## Architecture findings

### Strong patterns worth preserving

1. **Controller + downstream stages**
   - clear ownership of outputs;
   - prevents writing before analysis is stable.

2. **Artifact contracts**
   - analysis report;
   - result report;
   - code;
   - figures;
   - verification report.

3. **Numerical traceability**
   - manuscript values should come from recorded results rather than be re-estimated during writing.

4. **Separation of figure types**
   - data-driven plots are generated from code/results;
   - conceptual diagrams are handled separately.

5. **Verification as an independent final gate**
   - text placeholders;
   - missing images;
   - inconsistent numbers;
   - compile failures;
   - visual PDF errors.

### Competition-specific assumptions that should be removed

- “Problem 1 / Problem 2 / Problem 3” as the main organizing principle;
- competition type as a top-level preference;
- mandatory competition paper templates;
- default competition-style sections and summary sheets;
- ranking/evaluation methods being over-represented relative to measurement science;
- assumption that the final deliverable is always a competition paper.

## Engineering research requirements to add

The research layer should explicitly support:

### Experimental traceability
- raw-data identity and source;
- sensor/device IDs;
- firmware/software versions;
- sampling interval and timestamps;
- calibration/reference instrument;
- environmental conditions;
- exclusions and intervention markers;
- units and coordinate conventions.

### Measurement science
- accuracy vs precision;
- repeatability and reproducibility;
- bias;
- hysteresis;
- drift;
- response time;
- residual analysis;
- uncertainty budget;
- confidence intervals;
- temperature/environment matching.

### Model validation
- physical plausibility before goodness-of-fit;
- train/validation/test separation where applicable;
- time-aware validation for time-series data;
- cross-validation only when statistically valid;
- comparison against baselines;
- residual diagnostics;
- sensitivity and robustness;
- explicit extrapolation limits.

### Research claim control
Every important manuscript claim should be classifiable as one of:
- directly observed;
- computed from data;
- model-dependent inference;
- literature-supported interpretation;
- hypothesis/future work.

Do not promote a hypothesis to a result without evidence.

## Proposed research workflow

```text
00-research-controller
        |
        v
01-problem-definition
        |
        v
02-experimental-data-audit
        |
        +--> data quality / metadata / units / interventions
        |
        v
03-physical-statistical-modeling
        |
        +--> physical model
        +--> statistical model
        +--> optional ML model
        |
        v
04-computational-analysis
        |
        v
05-validation-uncertainty
        |
        +--> residuals / repeatability / robustness
        +--> uncertainty / confidence intervals
        |
        v
06-scientific-visualization
        |
        v
07-manuscript-writing
        |
        v
08-research-verification
```

A later version may split the modeling stage into independent physical, statistical, and ML skills when the workload justifies it.

## Recommended output structure

```text
project/
├── research_plan.md
├── research_todo.md
├── metadata/
│   └── experiment_manifest.md
├── data/
│   ├── raw/
│   └── processed/
├── code/
├── results/
├── figures/
├── reports/
│   ├── PROBLEM_DEFINITION_REPORT.md
│   ├── DATA_AUDIT_REPORT.md
│   ├── MODELING_REPORT.md
│   ├── RESULTS_REPORT.md
│   ├── VALIDATION_UNCERTAINTY_REPORT.md
│   └── VERIFY_REPORT.md
└── manuscript/
```

This is a recommended logical structure, not a requirement to physically move user data.

## Migration phases

### Phase 1 — Safe parallel layer
- create `research-skills/`;
- leave `skills/` untouched;
- create research controller and engineering norms;
- define artifact contracts.

### Phase 2 — Analysis and computation
- create problem-definition skill;
- create experimental/data-audit skill;
- adapt computational analysis from `3coding-visual`;
- add validation/uncertainty skill.

### Phase 3 — Manuscript and verification
- journal profile / manuscript skill;
- figure and claim traceability;
- citation and numerical consistency gates;
- compile/visual checks where tools exist.

### Phase 4 — Domain profiles
Optional profiles for:
- humidity calibration and reference systems;
- capacitive/IDC sensors;
- thermal/PID systems;
- embedded/IoT systems;
- TinyML;
- quantitative finance/econophysics.

## Immediate recommendation

Do **not** modify the original six competition skills yet.

Create the new research layer on this branch, test it on one real dataset/workflow, then decide which generic improvements should be backported or shared with the original skills.
