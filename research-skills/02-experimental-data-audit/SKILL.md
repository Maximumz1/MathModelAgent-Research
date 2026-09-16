---
name: 02-experimental-data-audit
description: "Audits experimental engineering data before modeling: provenance, timestamps, units, missingness, interventions, sensor/reference identity, disturbances, sampling cadence, duplicates, outliers, and comparison validity."
---

# Experimental and Data Audit

Read `../_references/engineering_research_norms.md`.

Do not fit the final model before completing the audit unless the user explicitly asks for a preliminary exploratory model.

## Required outputs

Create or update:

- `reports/DATA_AUDIT_REPORT.md`
- `metadata/experiment_manifest.md` when metadata can be reconstructed reliably.

Never overwrite raw data.

## Step 1: Inventory

For each file or data source, record:

- name/path;
- format;
- size/rows/columns when available;
- timestamp range;
- variable names;
- units;
- device/source;
- raw vs processed status.

## Step 2: Provenance

Identify:

- experiment/session ID;
- acquisition start/end;
- sensor/DUT identity;
- reference instrument;
- firmware/software version if relevant;
- sampling interval;
- setpoints;
- measured environmental conditions;
- intervention markers;
- known disturbances.

Mark unknown fields as unknown rather than inferring them.

## Step 3: Structural checks

Check:

- duplicate timestamps;
- duplicate rows;
- gaps;
- unexpected cadence changes;
- non-monotonic timestamps;
- missing columns;
- unit inconsistency;
- impossible values;
- parse failures.

For time series, quantify major gaps.

## Step 4: Data-quality checks

Assess:

- missingness;
- clipping/saturation;
- spikes;
- step changes;
- drift;
- frozen/stuck values;
- suspicious repeated values;
- sensor dropouts;
- boundary effects.

Do not automatically remove anomalies. First classify whether they are:
- measurement error;
- real intervention;
- real physical transition;
- unknown.

## Step 5: Experimental-state segmentation

Where relevant, label:

- pre-run;
- startup/transient;
- stable/quasi-steady candidate;
- intervention;
- recovery;
- disturbed segment;
- shutdown.

Segmentation criteria must be stated.

## Step 6: Comparison validity

Before comparing runs or devices, check whether key conditions are matched:

- temperature;
- pressure if relevant;
- humidity;
- sensor position;
- excitation frequency;
- sample preparation;
- elapsed time;
- filtering;
- calibration state.

If not matched, label the comparison as conditional.

## Step 7: Audit report

Recommended structure:

```markdown
# Data Audit Report

## Dataset inventory
## Provenance and metadata
## Sampling and timestamp integrity
## Missing data and gaps
## Disturbances and interventions
## Unit and range checks
## Candidate exclusions
## Experimental-state segmentation
## Comparison-validity assessment
## Risks before modeling
## Approved inputs for modeling
```

## Exclusion rule

Every excluded interval or sample class should include:
- reason;
- rule;
- number of affected samples;
- whether the exclusion was decided before or after observing the target result.

Avoid outcome-driven exclusions.
