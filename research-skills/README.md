# Engineering Research Skills

This directory is the ChatGPT/Codex-oriented research adaptation layer for MathModelAgent.

The original `skills/` directory is intentionally left unchanged so it can remain an upstream reference for mathematical-modeling competitions.

## Goals

- support experimental engineering research rather than competition-only workflows;
- preserve raw-data provenance and numerical traceability;
- separate observation, computation, inference, interpretation, and hypothesis;
- support physical models, statistical models, and optional ML models;
- make figures and manuscript claims reproducible;
- verify uncertainty, repeatability, references, and manuscript consistency before finalization.

## Core workflow

```text
00-research-controller
  -> 01-problem-definition
  -> 02-experimental-data-audit
  -> 03-physical-statistical-modeling
  -> 04-computational-analysis
  -> 05-validation-uncertainty
  -> 06-scientific-visualization
  -> 07-manuscript-writing
  -> 08-research-verification
```

All nine core workflow skills are now present on the research-adaptation branch.

## Supporting content

```text
_references/
  engineering_research_norms.md

domain-profiles/
  rh-calibration-reference.md
  idc-capacitive-sensor.md

skills.sh.json
```

The domain profiles extend the general workflow without replacing the core evidence and validation rules.

## Portability rule

Skills in this directory should describe required **capabilities and outputs**, not assume that a specific harness tool name (for example `Bash`, `Read`, `WebSearch`, or `AskUserQuestion`) exists.

Use whatever tools are actually available in the active environment, while preserving the stated evidence and output contracts.

## Safety rule

Do not overwrite raw data, original manuscripts, firmware, or experimental records unless the user explicitly asks for that mutation. Prefer derived files, new branches, versioned outputs, and minimal-diff edits.

## Recommended pilot

Before merging into `main`, test the workflow on one real experimental dataset.

See:

`docs/RESEARCH_SKILLS_TEST_PLAN.md`

The pilot should verify that the workflow can:

- preserve raw-data integrity;
- detect metadata/numerical inconsistencies;
- separate setpoints from measured conditions;
- prevent unsupported equilibrium or repeatability claims;
- reproduce quantitative results;
- keep manuscript claims traceable to validated evidence.

## Relationship to original MathModelAgent

`skills/` remains the competition-oriented upstream layer.

`research-skills/` is the engineering-research layer.

Do not delete or rewrite the original skills until the research workflow has been tested on real data and the migration decision is reviewed.
