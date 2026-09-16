---
name: 07-manuscript-writing
description: "Drafts or revises an engineering research manuscript from validated evidence, with journal-aware structure, claim-to-evidence traceability, real references only, and strict separation between results, interpretation, and hypotheses."
---

# Manuscript Writing

Read `../_references/engineering_research_norms.md`.

This stage writes from verified evidence. It must not create missing results.

## Inputs

Prefer to read, when available:

- `PROBLEM_DEFINITION_REPORT.md`;
- `DATA_AUDIT_REPORT.md`;
- `MODELING_REPORT.md`;
- `RESULTS_REPORT.md`;
- `VALIDATION_UNCERTAINTY_REPORT.md`;
- `FIGURE_REPORT.md`;
- target-journal profile/template;
- verified literature sources.

## Required outputs

Depending on the user's request:

- manuscript draft;
- revised section(s);
- abstract;
- cover-letter content;
- response to reviewers;
- claim-evidence table.

Do not assume the user wants a full manuscript.

## Step 1: Determine target structure

Use the target journal's current author guidelines/template when provided or when fresh public lookup is appropriate.

If no journal is specified, use a conventional research structure:

```text
Title
Abstract
Keywords
1. Introduction
2. Materials and Methods
3. Results
4. Discussion
5. Conclusions
Declarations / Data availability / Conflicts as applicable
References
```

Do not force this structure onto journals with different requirements.

## Step 2: Claim-evidence control

Maintain a working table:

| Claim | Evidence class | Source result/file | Uncertainty/limitation | Citation needed? |
| --- | --- | --- | --- | --- |

Evidence classes:
- observed;
- computed;
- model-dependent;
- literature-supported;
- hypothesis/future work.

## Step 3: Results vs Discussion

### Results
Report:
- what was measured/computed;
- numerical values;
- uncertainty;
- validated trends;
- figure/table references.

Avoid speculative mechanism claims.

### Discussion
Interpret:
- physical meaning;
- comparison with literature;
- limitations;
- alternative explanations;
- implications;
- future experiments.

Clearly label speculation or working hypotheses.

## Step 4: Numerical discipline

Every manuscript number must trace to a validated artifact.

Keep:
- units;
- significant figures;
- rounding;
- sample count;
- uncertainty notation

consistent throughout text, tables, and figures.

## Step 5: References

Use only real, verifiable references.

For technical claims prefer:
- standards;
- primary papers;
- authoritative datasheets;
- official documentation.

Never invent a DOI, issue number, page range, or author list.

## Step 6: Journal fit

When a target journal exists, check:

- scope;
- article type;
- word limits;
- abstract format;
- figure/table limits;
- reference style;
- data availability requirements;
- ethics/declaration requirements;
- graphical abstract/highlights if applicable.

Separate "journal requirement" from "writing preference".

## Step 7: Research-language quality

Prefer:
- precise verbs;
- quantified statements;
- explicit subjects;
- cautious language proportional to evidence.

Avoid:
- inflated novelty claims;
- "proves" where evidence only supports;
- generic AI-like filler;
- repetitive conclusions;
- hiding limitations.

## Step 8: Manuscript output

If editing an existing manuscript, use minimal-diff editing and preserve the author's structure unless there is a clear reason to change it.

If creating from scratch, build sections from validated reports rather than directly from memory.

## Hard-stop conditions

Do not finalize a section when:

- the key number has no traceable source;
- a citation cannot be verified;
- Results and Discussion contradict validation findings;
- a hypothesis is written as an established result;
- journal requirements are unknown but presented as certain.
