# Domain Profile — IDC Capacitive Humidity Sensor

Use this profile for interdigitated-electrode (IDC) capacitive humidity sensors, dielectric coatings, frequency-response studies, and RH calibration models.

## Required sensor metadata

Record:

- sensor ID;
- electrode material;
- substrate;
- finger count;
- finger width/spacing;
- active area;
- coating material;
- measured coating thickness if actually measured;
- fabrication/batch information;
- connector/cable configuration;
- measurement instrument/front end;
- excitation frequency;
- excitation amplitude where relevant;
- temperature;
- RH reference method.

Do not convert an estimated fabrication parameter into a measured value.

## Measurement modes

Possible outputs include:

- capacitance;
- impedance magnitude/phase;
- dissipation factor;
- voltage from an analog front end;
- frequency from an oscillator/transducer.

The model must state which quantity is directly measured and which is derived.

## Frequency dependence

If multiple frequencies are tested:

- analyze each frequency separately first;
- inspect sensitivity, linearity, loss/dissipation, noise, and hysteresis;
- avoid selecting the "best" frequency solely from one metric;
- ensure the same RH/temperature states are compared.

## Calibration modeling

Start with interpretable baselines:

1. linear;
2. low-order polynomial;
3. physically motivated nonlinear model where justified.

Only add ML when cross-device/run validation shows benefit.

For polynomial models:
- avoid selecting degree by training R² alone;
- inspect residuals;
- compare validation error;
- test edge behavior;
- report usable RH range.

## Temperature compensation

If temperature changes materially:

```text
sensor_output = f(RH, T)
```

or

```text
RH = g(sensor_output, T)
```

must be validated using data that span the relevant temperature range.

Do not claim temperature compensation from a narrow temperature band.

## Device-level validation

When multiple IDC samples exist, prefer validation that separates devices:

- train on some devices / test on held-out device;
- grouped cross-validation by sensor;
- repeated calibration across days.

Randomly mixing points from the same device into both train and test can overstate generalization.

## Hysteresis and dynamics

If adsorption and desorption sweeps are available, assess them separately.

Consider:

- hysteresis loop;
- response time;
- recovery time;
- drift;
- cycle-to-cycle repeatability.

## Coating studies

For coating/material comparisons:

- compare matched geometry and test conditions;
- distinguish nominal thickness from measured thickness;
- record deposition process;
- consider pinholes/roughness/coverage only as hypotheses unless characterized.

## Recommended figures

- sensor response vs RH;
- residual vs RH;
- sensitivity derivative vs RH;
- response across frequencies;
- hysteresis adsorption/desorption;
- temperature-colored calibration plot;
- device-to-device comparison;
- response-time plot.

## Hard-stop conditions

Do not finalize a calibration model when:

- RH reference is not validated;
- temperature confounds the response;
- sensor IDs are mixed without tracking;
- frequency differs between compared runs;
- model extrapolates outside the measured RH range without warning;
- coating thickness is assumed rather than measured but presented as measured.
