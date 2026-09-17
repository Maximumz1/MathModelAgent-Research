---
name: 06-scientific-visualization
description: "Creates publication-ready, traceable engineering figures from validated result artifacts and separates data-driven plots from conceptual diagrams. Supports short natural-language plotting requests across projects and requires source-data provenance for every quantitative figure."
---

# Scientific Visualization

Read:

- `../_references/engineering_research_norms.md`
- `../_references/scientific-plotting-rules.md`

The goal is evidence communication, not decoration.

## Natural-language plotting behavior

The user does not need to name this skill explicitly.

Requests such as:

- “plot X vs Y”;
- “พลอตกราฟ X กับ Y”;
- “use the latest data from Drive”;
- “compare these two files”;
- “show residuals”;
- “add uncertainty”;
- “make it manuscript-ready”

should route here automatically when the context is quantitative/scientific.

Use the generic plotting rules to resolve:

1. what variables/series are requested;
2. which project/file/source is authoritative;
3. whether the output is exploratory or publication-facing;
4. which plot form best answers the question;
5. whether a domain profile must be loaded.

Ask a clarification only when unresolved ambiguity would materially change the selected data or scientific interpretation.

## Project and domain grounding

Before plotting project data:

- identify the current project source hierarchy/canonical owner when available;
- use live connected sources when the user explicitly asks for Drive or another connected source;
- prefer raw/traceable/FROZEN data over remembered chat values;
- use a domain profile when reusable domain-specific semantics apply;
- do not create a domain profile merely for one new figure.

## Required outputs

Create or update where supported:

- `figures/`
- `reports/FIGURE_REPORT.md`

For each quantitative figure, preserve the source data or a reproducible script path.

## Figure classes

### A. Data-driven figures

Examples:

- time series;
- calibration curves;
- residual plots;
- agreement plots;
- confidence intervals;
- stability-window plots;
- model comparison;
- sensitivity analysis;
- distributions.

These must be generated from traceable data.

### B. Conceptual figures

Examples:

- apparatus schematic;
- analysis workflow;
- signal chain;
- model architecture;
- experimental timeline.

These must reflect the actual system and must not imply measured values that were not measured.

## Figure selection rule

Every figure should answer one question.

Examples:

- Is the system stable?
- How large is the bias?
- Does temperature explain the shift?
- Is the calibration nonlinear?
- Are residuals structured?
- Does a complex model improve validation?

If the figure has no clear question, reconsider generating it.

## Exploratory vs publication-facing mode

### Exploratory

For quick requests such as “plot this” or “show me the trend”:

- prioritize transparent visualization;
- use the best current available data;
- label preliminary/exploratory sources when applicable;
- do not perform unnecessary manuscript-level verification.

### Publication-facing

If the user requests manuscript/paper/journal/final/600-dpi output:

- re-ground current authoritative/FROZEN values;
- verify literature/reference sources when included;
- include only traceable uncertainty;
- preserve plotting provenance;
- check consistency with manuscript claims and figures.

Do not silently promote an exploratory graph into a manuscript figure.

## Publication requirements

Unless a target journal states otherwise:

- readable axis labels and units;
- legible fonts at final print size;
- no unnecessary title inside the plot;
- use captions for interpretation context;
- vector PDF/SVG when practical;
- high-resolution PNG when raster is required;
- uncertainty shown when important and traceable;
- consistent variable notation across manuscript and figures;
- color choices should remain interpretable in grayscale where practical.

## Traceability table

Maintain in `FIGURE_REPORT.md`:

| Figure | Research question | Source artifact | Script | Key transformation | Manuscript section |
| --- | --- | --- | --- | --- | --- |

## Anti-misleading checks

Do not:

- truncate axes in a way that exaggerates effects without clear justification;
- mix unmatched runs without labeling;
- hide excluded data;
- smooth away meaningful dynamics;
- show a simulated template as experimental data;
- use dual y-axes unless necessary and clearly explained;
- encode uncertainty ambiguously;
- digitize an image when current source-data files are available;
- use stale remembered values when the user requested current project/Drive data.

## Time-series figures

When applicable, include:

- intervention markers;
- stable-window shading;
- related variables in aligned panels when clearer than dual axes;
- gaps rather than silently connecting missing intervals;
- elapsed time or timestamp consistently.

## Calibration / XY figures

Consider:

- raw measured points;
- fitted/model curve only when justified;
- confidence or prediction band where justified;
- residual plot as a companion output;
- reference uncertainty;
- operating/validated range.

Do not use visual smoothness or training R² alone to select a model.

## Cross-project portability

This skill is generic and should work across sensor, thermal/PID, ML, finance/market, student-lab, and other quantitative projects.

The plotting method is shared; the current project/domain determines:

- source authority;
- variable meaning;
- valid comparisons;
- uncertainty definition;
- domain-specific interpretation.

## Output report

Recommended structure:

```markdown
# Figure Report

## Figure inventory
## Data-driven figures
## Conceptual figures
## Traceability table
## Exclusions / transformations shown
## Publication-format checks
## Figures not generated and why
```
