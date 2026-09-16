---
name: 06-scientific-visualization
description: "Creates publication-ready, traceable engineering figures from validated result artifacts and separates data-driven plots from conceptual diagrams. Requires source-data provenance for every quantitative figure."
---

# Scientific Visualization

Read `../_references/engineering_research_norms.md`.

The goal is evidence communication, not decoration.

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

## Publication requirements

Unless a target journal states otherwise:

- readable axis labels and units;
- legible fonts at final print size;
- no unnecessary title inside the plot;
- use captions for interpretation context;
- vector PDF/SVG when practical;
- high-resolution PNG when raster is required;
- uncertainty shown when important;
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
- encode uncertainty ambiguously.

## Time-series figures

When applicable, include:

- intervention markers;
- stable-window shading;
- temperature alongside RH only when readable and justified;
- gaps rather than silently connecting missing intervals;
- elapsed time or timestamp consistently.

## Calibration figures

Consider:

- raw points;
- fitted curve;
- confidence or prediction band where justified;
- residual panel as a separate figure or companion output;
- reference uncertainty;
- operating range.

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
