# Engineering Research Norms

This reference contains stable safeguards for experimental engineering and computational research. It is guidance, not a rigid output template.

## 1. Evidence classes

Every important statement should be distinguishable as:

1. **Observed** — directly measured or recorded.
2. **Computed** — deterministically calculated from recorded data.
3. **Model-dependent inference** — depends on a fitted or physical model.
4. **Literature-supported interpretation** — supported by cited external evidence.
5. **Hypothesis / future work** — plausible but not established by the present evidence.

Never promote a hypothesis to an experimental result without supporting evidence.

## 2. Raw-data integrity

- Preserve original raw files unchanged.
- Record filename, acquisition date/time, source instrument/device, and sampling cadence when available.
- Record firmware/software version when it can affect results.
- Record sensor/reference identity and configuration.
- Record unit conventions.
- Record exclusions, interventions, restarts, dropouts, and environmental disturbances.
- Derived data must be reproducible from raw data by documented code or transformations.

## 3. Measurement science

Distinguish:

- accuracy;
- precision;
- repeatability;
- reproducibility;
- bias;
- drift;
- hysteresis;
- resolution;
- response time;
- uncertainty.

Do not use these terms interchangeably.

Where relevant, report:
- mean;
- standard deviation;
- confidence interval;
- slope/drift;
- residual distribution;
- sample count;
- temperature/environmental state;
- reference-instrument limitations.

## 4. Experimental comparisons

A comparison is only strong when important boundary conditions are matched or explicitly adjusted for.

Examples:
- temperature-matched comparisons for RH measurements;
- same sampling interval and filtering;
- same sensor position;
- same excitation frequency for impedance/capacitance tests;
- same preprocessing for model comparisons.

If conditions differ, describe the comparison as conditional rather than directly equivalent.

## 5. Model selection

Prefer the simplest model that:
- respects known physics;
- explains the data adequately;
- generalizes under appropriate validation;
- has interpretable failure limits.

Good fit alone is insufficient.

Check:
- residuals;
- physical bounds;
- units/dimensions;
- parameter plausibility;
- extrapolation domain;
- sensitivity;
- identifiability where relevant.

## 6. Statistical modeling

- Avoid data leakage.
- Time-series validation must preserve temporal order.
- Fit scalers/encoders using training data only when ML validation is performed.
- State how missing values and outliers were handled.
- Report uncertainty around estimated parameters where meaningful.
- Prefer confidence intervals and effect sizes over a single metric when possible.

## 7. Machine learning

Use ML only when it adds value beyond a suitable baseline.

Always compare against at least one simple baseline where feasible.

Report:
- data split;
- feature set;
- preprocessing;
- hyperparameter procedure;
- evaluation metrics;
- random seed when relevant;
- validation strategy;
- known domain limitations.

Do not tune on the final test set.

## 8. Physical models

For physical or mechanistic models, state:
- variables and units;
- assumptions;
- governing equations;
- initial/boundary conditions;
- parameter sources;
- numerical solver;
- timestep/grid choices;
- convergence or stability checks when relevant.

## 9. Visualization

Every figure should answer a research question.

For data-driven figures:
- use traceable source data;
- preserve the script used to generate the figure;
- use correct units and labels;
- avoid decorative features that obscure interpretation.

For conceptual figures:
- ensure the diagram reflects the actual method;
- do not imply measured quantities where none exist.

## 10. Manuscript traceability

Numerical claims in a manuscript must trace to:
- recorded result tables;
- generated result files;
- analysis code outputs;
- or validated figures.

Do not retype or re-estimate numbers independently during manuscript drafting.

## 11. References

Use real, verifiable references.

Prefer:
- standards;
- primary research articles;
- authoritative datasheets;
- official documentation.

Do not invent citations, DOIs, journal metadata, or standard identifiers.

## 12. Verification gate

Before calling a research output final, check:
- raw-data provenance;
- units;
- preprocessing;
- statistical assumptions;
- model consistency;
- numerical values;
- figures;
- references;
- manuscript claims;
- compile/export success;
- visual integrity of the final artifact where relevant.
