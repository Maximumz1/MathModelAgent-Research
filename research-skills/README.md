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

## Initial workflow

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

The first implementation phase provides the controller, problem-definition, data-audit, and shared engineering-research norms. Later phases should add computation, validation, manuscript, and final verification skills.

## Portability rule

Skills in this directory should describe required **capabilities and outputs**, not assume that a specific harness tool name (for example `Bash`, `Read`, `WebSearch`, or `AskUserQuestion`) exists.

Use whatever tools are actually available in the active environment, while preserving the stated evidence and output contracts.

## Safety rule

Do not overwrite raw data, original manuscripts, firmware, or experimental records unless the user explicitly asks for that mutation. Prefer derived files, new branches, versioned outputs, and minimal-diff edits.
