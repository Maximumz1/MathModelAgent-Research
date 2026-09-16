---
name: 01-problem-definition
description: "Transforms an engineering research question into a testable, traceable analysis specification with variables, hypotheses, acceptance criteria, scope, confounders, and required outputs."
---

# Problem Definition

Read `../_references/engineering_research_norms.md`.

## Purpose

Convert a broad research goal into a specification that can be audited, modeled, computed, and validated.

## Required output

Create or update:

`reports/PROBLEM_DEFINITION_REPORT.md`

If file-writing is unavailable, provide the report content directly.

## Required sections

### 1. Research objective

State the question in operational terms.

Avoid vague goals such as "find the best model" without defining what "best" means.

### 2. Research type

Classify the task where possible:

- calibration;
- characterization;
- comparison;
- validation;
- prediction;
- classification;
- optimization;
- control;
- mechanistic modeling;
- exploratory analysis.

Multiple labels are allowed.

### 3. Variables

Define:

| Role | Variable | Symbol | Unit | Source |
| --- | --- | --- | --- | --- |
| response | ... | ... | ... | ... |
| predictor | ... | ... | ... | ... |
| control | ... | ... | ... | ... |
| confounder | ... | ... | ... | ... |

Do not invent units or sources.

### 4. Hypotheses

For each important hypothesis state:

- claim;
- mechanism/rationale;
- observable prediction;
- competing explanation;
- evidence needed to discriminate.

### 5. Scope and exclusions

State:
- operating range;
- devices/samples included;
- environmental range;
- intended inference domain;
- explicit exclusions.

### 6. Confounders

List factors that may change the apparent result.

Examples:
- temperature;
- time/history;
- sensor drift;
- chamber leakage;
- spatial gradient;
- sample preparation;
- batch-to-batch variation;
- firmware changes;
- filtering or smoothing.

### 7. Acceptance criteria

Define measurable criteria before final analysis where possible.

Examples:
- maximum RMSE;
- repeatability tolerance;
- confidence interval width;
- slope threshold for quasi-steady behavior;
- maximum bias versus a reference;
- physical residual pattern requirement.

Avoid inventing thresholds not provided by standards, literature, or the user. Label provisional thresholds as provisional.

### 8. Required outputs

Specify:
- tables;
- figures;
- model coefficients;
- uncertainty;
- validation tests;
- manuscript-ready results.

## Quality gate

The definition is incomplete if a reader cannot tell:

- what will be measured;
- what will be compared;
- under what conditions;
- what would count as supporting or contradicting the hypothesis;
- what data are required.
