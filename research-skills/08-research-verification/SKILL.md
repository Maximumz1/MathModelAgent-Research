---
name: 08-research-verification
description: "Final engineering-research audit. Checks provenance, claims, numbers, figures, uncertainty, references, manuscript consistency, reproducibility, journal compliance, and final artifact integrity before submission or release."
---

# Research Verification

Read `../_references/engineering_research_norms.md`.

This is the final gate. It does not redesign the study merely to obtain a PASS.

## Required output

Create or update:

- `reports/VERIFY_REPORT.md`

## Verification domains

### 1. Provenance

Check:

- raw inputs identifiable;
- processed data trace back to raw data;
- experiment/session IDs consistent;
- sensor/reference identity recorded;
- major disturbances/interventions documented;
- analysis code points to the correct data.

### 2. Units and metadata

Check:

- units consistent;
- temperature scale explicit;
- elapsed time vs wall-clock distinguished;
- sampling cadence documented;
- setpoint vs measured condition not conflated;
- sensor model names consistent.

### 3. Numerical consistency

Cross-check key values among:

- result artifacts;
- reports;
- tables;
- figure annotations;
- manuscript text;
- abstract;
- conclusions.

Use the same rounding convention.

A conflict is a FAIL until reconciled.

### 4. Claim-to-evidence audit

For each major claim verify:

- evidence class;
- source artifact;
- validation status;
- limitation;
- citation if required.

Flag:
- hypothesis presented as result;
- correlation presented as causation;
- unmatched-condition comparison presented as direct repeatability;
- model output presented as measured data.

### 5. Validation and uncertainty

Check:

- residual diagnostics considered;
- repeatability assessed where claimed;
- uncertainty reported at an appropriate level;
- reference uncertainty not ignored;
- stable/equilibrium claims use explicit criteria;
- robustness checks support the conclusion.

### 6. Figures and tables

Check:

- all referenced files exist;
- captions match contents;
- units and legends correct;
- quantitative figures have traceable sources;
- exclusions/interventions are not hidden;
- no simulated template is presented as measured data.

### 7. References

Check:

- references are real;
- cited claim is actually supported;
- metadata is consistent;
- no placeholder citation remains;
- standards/datasheets use authoritative sources where possible.

If web or literature-search capability is unavailable, record that reference verification was limited rather than claiming it was completed.

### 8. Reproducibility

Check whether another researcher could determine:

- input data;
- preprocessing;
- code entry point;
- model parameters;
- package/environment requirements;
- random seeds where relevant;
- output artifacts.

Full one-click reproduction is ideal but not always required. State what was actually tested.

### 9. Manuscript/journal compliance

If a target journal exists, check current requirements for:

- article structure;
- abstract;
- word count;
- figures/tables;
- reference format;
- declarations;
- data availability;
- supplementary files.

Do not use stale remembered requirements when current verification is possible.

### 10. Final artifact integrity

For PDF/DOCX/LaTeX/Typst outputs, check as tools permit:

- file opens/compiles;
- pages are non-empty;
- tables do not overflow;
- equations and symbols render;
- figures are legible;
- cross-references resolve;
- no internal workflow notes leak into the manuscript.

## PASS / WARN / FAIL

### FAIL examples

- numerical contradiction;
- fabricated/unverifiable citation;
- missing source for a major claim;
- missing raw-data provenance for a central result;
- unresolved unit error;
- failed repeatability while claiming repeatability;
- figure does not represent the stated data;
- manuscript promotes a hypothesis to established result;
- final document cannot be opened/compiled when the needed tool is available.

### WARN examples

- limited external citation verification due to unavailable tools;
- secondary figure not referenced;
- incomplete environment snapshot;
- minor formatting issue;
- uncertainty discussion is qualitative but transparently justified.

## Report template

```markdown
# Research Verification Report

## Overall status
PASS / WARN / FAIL

## Scope of verification

## Provenance
## Units and metadata
## Numerical consistency
## Claim-to-evidence audit
## Validation and uncertainty
## Figures and tables
## References
## Reproducibility
## Journal compliance
## Final artifact integrity

## Blocking issues
## Non-blocking warnings
## Recommended next action
```

Only write PASS when no blocking issue remains.
