---
name: 05-validation-uncertainty
description: "Validates engineering results using residuals, repeatability, reproducibility, bias, drift, robustness, sensitivity, confidence intervals, and uncertainty budgets. Prevents premature equilibrium, calibration, or performance claims."
---

# Validation and Uncertainty

Read `../_references/engineering_research_norms.md`.

This stage decides how strong the evidence is. It should be independent of the desire for a particular conclusion.

## Required output

Create or update:

- `reports/VALIDATION_UNCERTAINTY_REPORT.md`

Optional machine-readable outputs should be saved under `results/`.

## Step 1: Define the claim being validated

Examples:

- calibration accuracy;
- repeatability;
- equilibrium or quasi-steady state;
- temperature effect;
- sensor agreement;
- predictive generalization;
- control stability;
- model parameter reliability.

Each claim must have a validation test.

## Step 2: Residual diagnostics

Where a fitted model exists, examine:

- mean residual / bias;
- residual SD;
- residual vs fitted;
- residual vs time;
- residual vs temperature or other confounders;
- heteroscedasticity;
- autocorrelation;
- outliers;
- nonlinearity.

Do not report only aggregate error metrics.

## Step 3: Repeatability and reproducibility

Distinguish:

- within-run stability;
- repeated run under nominally same conditions;
- between-day;
- between-device;
- between-operator/setup;
- reused vs fresh sample where relevant.

Use matched conditions when possible.

Report both central difference and dispersion.

## Step 4: Stability / quasi-steady assessment

For time-series experiments, define the window rule explicitly.

Possible criteria include:

- absolute slope below a threshold;
- SD below a threshold;
- temperature stability;
- no intervention within the window;
- minimum duration;
- no major data gap.

Thresholds must come from a standard, prior method, user requirement, or be labeled provisional.

Do not call the final recorded point an equilibrium merely because it is the last point.

## Step 5: Bias and reference comparison

When a reference exists, compute as appropriate:

- signed bias;
- absolute error;
- relative error;
- RMSE/MAE;
- Bland–Altman statistics;
- regression agreement;
- confidence intervals.

State reference uncertainty and limitations.

## Step 6: Uncertainty

Build an uncertainty budget when the study supports it.

Possible contributors:

- reference instrument;
- repeatability;
- resolution;
- temperature mismatch;
- calibration coefficient uncertainty;
- drift;
- fitting uncertainty;
- sample preparation;
- timing/interpolation.

Distinguish Type A and Type B components when applying a metrology framework.

If a formal uncertainty budget is not justified, provide a transparent uncertainty discussion rather than a false precision calculation.

## Step 7: Sensitivity and robustness

Test conclusions against reasonable changes in:

- stable-window boundaries;
- exclusion rules;
- polynomial order;
- preprocessing choices;
- random seed;
- parameter initialization;
- temperature matching tolerance;
- model class.

A robust conclusion should not depend on one arbitrary analysis choice.

## Step 8: Model comparison

Compare candidate models on the same data partitions and preprocessing.

Recommended comparison dimensions:

| Model | Validation error | Bias | Residual structure | Parameter stability | Physical plausibility | Complexity |
| --- | ---: | ---: | --- | --- | --- | --- |

Do not declare a model superior solely on in-sample fit.

## Step 9: Evidence strength

Classify each important conclusion:

- supported;
- preliminary;
- inconclusive;
- contradicted;
- requires additional matched experiment.

Avoid converting this into an arbitrary numerical score.

## Recommended report structure

```markdown
# Validation and Uncertainty Report

## Claims under validation
## Residual diagnostics
## Repeatability / reproducibility
## Stability-window validation
## Reference comparison and bias
## Uncertainty assessment
## Sensitivity / robustness
## Model comparison
## Evidence-strength summary
## Limitations
## Required follow-up experiments
```

## Hard-stop conditions

Do not finalize a strong claim when:

- repeatability failed;
- reference conditions were not matched;
- terminal drift remains substantial;
- residuals show unmodeled structure;
- a major uncertainty source dominates but is ignored;
- the conclusion disappears under a reasonable analysis variant.
