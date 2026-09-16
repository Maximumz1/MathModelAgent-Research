---
name: 00-research-controller
description: "Controller for experimental engineering research. Defines research scope, evidence state, workflow stages, artifact contracts, risk controls, and the next analysis step without assuming competition templates or a specific tool harness."
---

# Engineering Research Controller

This skill starts or resumes an engineering research workflow.

It coordinates downstream research skills but does not replace their detailed work.

Read `../_references/engineering_research_norms.md` when making methodological decisions.

## Core principles

1. Preserve raw data and original artifacts.
2. Prefer minimal-diff edits and versioned outputs.
3. Separate observed facts, computed results, model-dependent inference, literature interpretation, and hypotheses.
4. Do not draft strong manuscript claims before data/model validation.
5. Do not assume a specific tool name exists. Use capabilities available in the active environment.
6. Do not silently install software or mutate external systems.

## Determine the research state

Ask only questions that materially change the workflow and only when the answer cannot be inferred from available files or context.

Determine:

- research objective or question;
- current project stage;
- available data/files;
- measurement/reference system;
- known disturbances or interventions;
- desired output;
- target journal/template if manuscript work is requested;
- whether the task is exploratory, confirmatory, calibration, validation, optimization, or prediction.

## Required planning artifacts

Create or update, when file-writing is available:

- `research_plan.md`
- `research_todo.md`

If file-writing is unavailable, present the same information in the response rather than pretending files were created.

## Recommended workflow

```text
1. Problem definition                 -> 01-problem-definition
2. Experimental/data audit            -> 02-experimental-data-audit
3. Physical/statistical modeling      -> 03-physical-statistical-modeling
4. Computational analysis             -> 04-computational-analysis
5. Validation and uncertainty         -> 05-validation-uncertainty
6. Scientific visualization           -> 06-scientific-visualization
7. Manuscript writing                 -> 07-manuscript-writing
8. Research verification              -> 08-research-verification
```

Not every task requires every stage. Skip a stage only with an explicit reason.

## research_plan.md structure

```markdown
# Research Plan

## Objective
...

## Current evidence state
- Observed:
- Computed:
- Model-dependent:
- Literature-supported:
- Hypotheses / future work:

## Inputs
- Raw data:
- Metadata:
- Reference instrument:
- Code:
- Prior reports:

## Known disturbances / constraints
...

## Workflow
| Stage | Purpose | Input | Output | Status |
| --- | --- | --- | --- | --- |

## Validation gates
...

## Risks
...
```

## research_todo.md structure

```markdown
# Research Todo

- [ ] 1. Define research question and acceptance criteria
- [ ] 2. Audit raw data and metadata
- [ ] 3. Select/model physical and statistical relationships
- [ ] 4. Run reproducible computation
- [ ] 5. Validate uncertainty, repeatability, and robustness
- [ ] 6. Generate traceable scientific figures
- [ ] 7. Draft manuscript from verified evidence
- [ ] 8. Perform final research verification
```

## Recommended project structure

This is a logical structure, not a command to move user files.

```text
project/
├── research_plan.md
├── research_todo.md
├── metadata/
├── data/
│   ├── raw/
│   └── processed/
├── code/
├── results/
├── figures/
├── reports/
└── manuscript/
```

## Stop conditions

Pause downstream claims and mark the risk when:

- raw data cannot be identified;
- units are ambiguous;
- reference sensor/instrument identity is unknown where it materially affects conclusions;
- intervention timing is uncertain;
- substantial missing data are unexplained;
- compared conditions are not sufficiently matched;
- a result conflicts with physical constraints;
- a manuscript claim cannot be traced to evidence.

Do not fill these gaps by guessing.
