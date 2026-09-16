---
name: 03-physical-statistical-modeling
description: "Builds engineering models from audited data using physical reasoning first, then statistical or ML models when justified. Defines equations, parameters, assumptions, identifiability, baselines, validation strategy, and implementation contracts."
---

# Physical and Statistical Modeling

Read `../_references/engineering_research_norms.md`.

This stage consumes the problem definition and data audit. It should not invent missing variables, units, or metadata.

## Required output

Create or update:

- `reports/MODELING_REPORT.md`

If file-writing is unavailable, provide the same content directly.

## Modeling order

Prefer this order unless the research question clearly requires otherwise:

1. physical constraints and known mechanisms;
2. simple analytical/statistical baseline;
3. richer statistical model;
4. ML model only if justified by data volume, nonlinearity, or prediction goals.

A more complex model must earn its complexity by improved validation, interpretability, or practical utility.

## Step 1: Define the model target

State:

- response variable(s);
- predictor/input variables;
- operating range;
- sampling unit;
- independent experimental unit;
- intended inference domain.

For time-series or repeated-measures data, identify dependence between observations.

## Step 2: Physical model

Where applicable, define:

- governing equations;
- constitutive relationships;
- conservation laws;
- boundary/initial conditions;
- units;
- parameter meanings;
- expected sign and range of each parameter;
- simplifications and neglected mechanisms.

Perform a dimensional sanity check.

If a full physical model is not justified, state why.

## Step 3: Statistical baseline

Choose a simple baseline that can be beaten meaningfully.

Examples:

- constant/mean predictor;
- linear regression;
- low-order polynomial;
- ordinary least squares;
- first-order dynamic response;
- simple exponential model.

Avoid selecting polynomial order only by training fit.

## Step 4: Candidate models

For each candidate specify:

| Model | Purpose | Inputs | Parameters | Assumptions | Validation |
| --- | --- | --- | --- | --- | --- |

Possible classes include:

- linear / polynomial regression;
- nonlinear least squares;
- generalized linear models;
- mixed-effects models;
- time-series models;
- state-space models;
- physical parameter estimation;
- Gaussian process;
- tree ensemble;
- neural network.

Do not include methods merely to make the study look sophisticated.

## Step 5: Identifiability and collinearity

Check whether parameters can be estimated separately from available data.

Consider:

- parameter correlation;
- insufficient excitation/range;
- multicollinearity;
- redundant features;
- confounded temperature/time/history effects.

If two effects cannot be separated, report that limitation explicitly.

## Step 6: Validation design

Define before final fitting where possible:

- train/validation/test split;
- grouped split by run/device/sample;
- blocked or rolling split for time series;
- cross-validation scheme;
- baseline comparison;
- primary metric;
- secondary diagnostics.

Never randomly split highly autocorrelated time-series points across train and test unless independence is justified.

## Step 7: Model selection criteria

Use more than one criterion where appropriate:

- RMSE / MAE;
- bias;
- residual structure;
- confidence intervals;
- AIC/BIC for comparable likelihood models;
- cross-validated error;
- physical plausibility;
- parameter stability;
- extrapolation behavior;
- computational cost.

Do not choose a model on R² alone.

## Step 8: Implementation contract

End `MODELING_REPORT.md` with:

```markdown
## Computational implementation contract

| Task | Input | Method | Output | Validation | Failure condition |
| --- | --- | --- | --- | --- | --- |
```

This table becomes the interface to `04-computational-analysis`.

## Recommended report structure

```markdown
# Modeling Report

## Modeling objective
## Variables and units
## Physical constraints/mechanism
## Baseline model
## Candidate models
## Assumptions
## Identifiability and confounders
## Validation design
## Selection criteria
## Extrapolation limits
## Computational implementation contract
```

## Quality gate

Do not proceed as if the model is final when:

- units are unresolved;
- key parameters are not identifiable;
- validation would leak information;
- a compared model uses different preprocessing;
- parameter values violate known physical limits;
- the model requires extrapolation beyond the measured domain without explicit warning.
