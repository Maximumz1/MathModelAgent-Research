# Domain Profile — Relative Humidity Calibration and Reference Systems

Use this profile together with the core research skills when the project involves RH chambers, saturated salts, glycerol–water mixtures, humidity reference generation, or sensor calibration.

## Primary risks

RH experiments are especially vulnerable to:

- temperature mismatch between solution/bath, headspace, DUT, and reference sensor;
- thermal gradients;
- insufficient equilibration time;
- chamber leakage;
- sensor self-heating or placement differences;
- slow adsorption/desorption dynamics;
- hysteresis;
- sample preparation differences;
- intervention/history effects;
- treating a terminal value as equilibrium without a stability test.

## Required metadata

Record when available:

- formulation/reference method;
- composition or preparation method;
- container/chamber geometry;
- headspace volume;
- reference sensor model and serial/ID;
- DUT model/ID;
- sensor positions;
- bath/setpoint temperature;
- measured bath temperature;
- measured headspace temperature;
- ambient temperature/RH;
- start/end time;
- sampling interval;
- interventions;
- disturbances;
- whether the solution/sample is fresh or reused.

## Temperature rule

Never assume a controller setpoint equals the actual RH-generating temperature.

Keep separate variables for:

- controller setpoint;
- measured bath/solution temperature;
- measured headspace/reference-sensor temperature;
- ambient temperature.

Comparisons should be temperature-matched when the expected RH is temperature-sensitive.

## Stability / quasi-steady rule

A candidate stable window should define:

- minimum duration;
- RH slope criterion;
- RH variability criterion;
- temperature slope/variability criterion;
- maximum allowed data gap;
- distance from the most recent intervention.

Do not call a window "equilibrium" unless the experimental method and duration justify that stronger term. "Quasi-steady" is safer when the system still has unresolved slow dynamics.

## Repeatability rule

For repeated runs compare:

- stable-window mean;
- stable-window SD;
- slope;
- actual headspace temperature;
- preparation state;
- elapsed time;
- intervention history.

A repeat is not directly comparable merely because the setpoint is the same.

## Reference comparison

When comparing against literature/reference RH:

- use the correct formulation/composition;
- use temperature-appropriate reference values;
- state interpolation method if used;
- state reference uncertainty;
- separate sensor error from reference-generation uncertainty.

## Recommended outputs

### Time-series
- RH vs time;
- temperature vs time;
- intervention markers;
- highlighted candidate stable windows.

### Stable-window table
| Run | Window | RH mean | RH SD | RH slope | T mean | T SD | T slope | Status |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |

### Repeatability table
| Run A | Run B | ΔRH | ΔT | Matched? | Interpretation |
| --- | --- | ---: | ---: | --- | --- |

## Evidence language

Prefer:

- "The run reached a quasi-steady window under the stated criteria."
- "The repeated runs agree within X %RH at matched temperature."

Avoid without sufficient evidence:

- "true equilibrium";
- "exact reference RH";
- "temperature has no effect";
- "repeatability is proven" from a single repeat.

## Uncertainty contributors

Consider:

- reference-sensor accuracy;
- reference method uncertainty;
- temperature mismatch;
- within-window variability;
- between-run variability;
- composition/preparation uncertainty;
- chamber leakage/gradient;
- long-term drift.
