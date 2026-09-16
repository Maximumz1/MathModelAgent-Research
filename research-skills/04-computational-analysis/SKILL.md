---
name: 04-computational-analysis
description: "Implements the approved engineering analysis reproducibly. Produces code, processed data, model parameters, diagnostics, run logs, result tables, and a traceable RESULTS_REPORT without altering raw data."
---

# Computational Analysis

Read `../_references/engineering_research_norms.md`.

This stage implements the approved analysis. It does not silently change the research question or model definition.

## Required outputs

Create or update where file-writing is available:

- `code/`
- `results/`
- `reports/RESULTS_REPORT.md`

Optionally:
- `data/processed/`
- environment/dependency snapshot;
- machine-readable result files such as CSV/JSON.

Never overwrite raw data.

## Step 1: Reproducible setup

Record:

- language and version;
- package versions when material;
- random seeds;
- input file identity;
- configuration values;
- analysis timestamp;
- code entry point.

Avoid embedding secrets or credentials in the repository.

## Step 2: Data transformation

Every transformation should be reproducible and justified:

- parsing;
- unit conversion;
- filtering;
- resampling;
- smoothing;
- baseline correction;
- feature derivation;
- exclusions.

Record before/after row counts.

Do not apply undocumented manual corrections.

## Step 3: Implement incrementally

For each analysis task:

1. load inputs;
2. verify schema and units;
3. implement model;
4. run sanity checks;
5. save intermediate outputs;
6. save final metrics/parameters;
7. save diagnostics;
8. record any deviation from `MODELING_REPORT.md`.

Do not write a large untested pipeline in one pass if incremental verification is possible.

## Step 4: Numerical safeguards

Where relevant check:

- finite values;
- matrix conditioning;
- convergence status;
- solver tolerances;
- boundary hits;
- parameter bounds;
- residual magnitude;
- constraint satisfaction;
- timestep/grid sensitivity;
- reproducibility across random seeds.

A solver reporting success is not by itself proof of a valid solution.

## Step 5: Time-series safeguards

For time-indexed experimental data:

- preserve timestamp order;
- quantify gaps;
- avoid interpolation across major disturbances unless justified;
- record resampling method;
- distinguish elapsed time from wall-clock time;
- keep intervention markers.

## Step 6: Result artifacts

Prefer machine-readable artifacts for key results.

Examples:

```text
results/
  model_parameters.csv
  metrics.json
  stable_windows.csv
  exclusions.csv
  residual_summary.csv
  run_manifest.json
```

Names may differ by project.

## Step 7: RESULTS_REPORT

Recommended structure:

```markdown
# Results Report

## Reproducible environment
## Input data identity
## Preprocessing and exclusions
## Analysis execution
## Model parameters
## Primary results
## Diagnostics
## Constraint / physical sanity checks
## Deviations from modeling plan
## Machine-readable outputs
## Reproduction steps
```

All manuscript-ready numbers should be traceable to this report or a referenced result artifact.

## Evidence labeling

When reporting a result, label internally whether it is:

- observed;
- computed;
- model-dependent.

This prevents modeled values from being accidentally presented as direct measurements.

## Failure handling

If computation reveals that an assumption is invalid:

- stop promotion of the affected result;
- record the issue;
- return to the modeling stage;
- do not patch the output merely to obtain an expected conclusion.
