# Engineering Research Skills — Test Plan

Branch: `chatgpt-research-adaptation`

## Goal

Validate the new `research-skills/` workflow on a real engineering dataset before merging or modifying the original competition skills.

## Test strategy

Use one completed or nearly completed experimental project with:

- identifiable raw time-series data;
- known intervention markers;
- a reference sensor/instrument;
- at least one repeated condition;
- enough duration to test stable-window logic.

An RH reference/calibration run is a good first candidate because it exercises provenance, time-series audit, thermal matching, stability, repeatability, and uncertainty.

## Test stages

### T1 — Controller

Expected:
- research objective identified;
- current evidence state classified;
- research plan and todo generated;
- no raw files modified.

### T2 — Problem definition

Expected:
- variables and units identified;
- confounders listed;
- hypotheses separated from established results;
- acceptance criteria either sourced or marked provisional.

### T3 — Data audit

Expected:
- row count and timestamp range;
- cadence/gap analysis;
- intervention/disturbance timeline;
- candidate exclusions with reasons;
- raw data preserved.

### T4 — Modeling

Expected:
- physical constraints stated first;
- simple baseline defined;
- candidate model(s) justified;
- validation split avoids leakage.

### T5 — Computation

Expected:
- reproducible code;
- machine-readable result artifacts;
- no silent manual corrections;
- deviations from plan recorded.

### T6 — Validation / uncertainty

Expected:
- stable-window logic explicit;
- residuals checked;
- repeatability compared at matched conditions;
- uncertainty sources stated;
- evidence strength assigned without inflating claims.

### T7 — Figures

Expected:
- each quantitative figure has source data/script;
- intervention markers visible when relevant;
- no simulated template data misrepresented as experiment.

### T8 — Manuscript

Expected:
- numbers trace to result artifacts;
- Results and Discussion separated;
- hypotheses remain labeled;
- references verified.

### T9 — Final verification

Expected:
- claim-to-evidence audit;
- numerical consistency across text/table/figure;
- reference validation;
- final artifact integrity;
- PASS only if no blocking issue remains.

## Acceptance criteria for the skill framework

The framework passes the pilot when:

1. it does not overwrite raw data;
2. it detects at least one deliberately inserted metadata inconsistency or numeric mismatch;
3. it can reproduce the main quantitative results from recorded inputs;
4. it distinguishes setpoint from measured condition;
5. it prevents an unsupported equilibrium/repeatability claim;
6. final manuscript numbers match validated result artifacts;
7. the workflow remains usable without relying on Claude-specific tool names.

## After pilot

If the pilot passes:

- merge the research layer or open a pull request for review;
- add domain profiles for additional projects;
- consider a local environment doctor for Codex/CLI use;
- consider automated verification scripts only after the manual rules are stable.
