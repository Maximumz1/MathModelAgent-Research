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

All nine core workflow skills are present on the research-adaptation branch.

## Supporting content

```text
_references/
  engineering_research_norms.md
  scientific-plotting-rules.md

domain-profiles/
  rh-calibration-reference.md
  idc-capacitive-sensor.md
  gly-literature-plotting-profile.md

skills.sh.json
```

## Cross-project plotting

`scientific-plotting-rules.md` is the generic plotting contract used across projects.

The user should normally be able to make short natural-language requests such as:

- `plot X vs Y from this file`
- `พลอตกราฟสองชุดนี้เทียบกัน`
- `ใช้ข้อมูลล่าสุดใน Drive`
- `ทำ residual ให้ด้วย`
- `ใส่ uncertainty`
- `ทำแบบใช้ใน manuscript`

The controller routes these requests through `06-scientific-visualization`, resolves the current project/source hierarchy, and then loads a domain profile only when domain-specific rules are needed.

Generic plotting rules define **how to plot and how to ground the data**. They do not store project numerical results.

## Domain profiles

Domain profiles extend the general workflow without replacing core evidence and validation rules.

`gly-literature-plotting-profile.md` is the specialized routing/profile file for glycerol composition–RH literature comparisons. It points the agent back to current canonical project owners, FROZEN analysis, and the current Drive literature source-data package before plotting, so it does not become a duplicate numerical authority.

Create additional domain profiles only when a project has reusable semantics or constraints that cannot be safely inferred from the generic plotting rules. Do not create one merely for every new graph.

## Portability rule

Skills in this directory should describe required **capabilities and outputs**, not assume that a specific harness tool name (for example `Bash`, `Read`, `WebSearch`, or `AskUserQuestion`) exists.

Use whatever tools are actually available in the active environment, while preserving the stated evidence and output contracts.

## Safety rule

Do not overwrite raw data, original manuscripts, firmware, or experimental records unless the user explicitly asks for that mutation. Prefer derived files, new branches, versioned outputs, and minimal-diff edits.

## Recommended pilot

Before merging into `main`, test the workflow on real datasets from more than one project/domain.

See:

`docs/RESEARCH_SKILLS_TEST_PLAN.md`

The pilot should verify that the workflow can:

- preserve raw-data integrity;
- detect metadata/numerical inconsistencies;
- separate setpoints from measured conditions;
- prevent unsupported equilibrium or repeatability claims;
- reproduce quantitative results;
- keep manuscript claims traceable to validated evidence;
- route short natural-language plotting requests correctly across different projects.

## Relationship to original MathModelAgent

`skills/` remains the competition-oriented upstream layer.

`research-skills/` is the engineering-research layer.

Do not delete or rewrite the original skills until the research workflow has been tested on real data and the migration decision is reviewed.
