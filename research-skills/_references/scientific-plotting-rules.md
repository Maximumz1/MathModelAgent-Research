# Generic Scientific Plotting Rules

Status: ACTIVE shared reference for the Engineering Research Agent

Purpose: provide one cross-project plotting contract so a user can make short natural-language requests such as “plot X vs Y”, “plot these two datasets”, “plot the latest data from Drive”, or “make this manuscript-ready” without creating a new plotting skill for every project.

This file defines plotting behavior only. It is **not** a numerical source of truth and must not duplicate changing project values.

## 1. Core operating principle

Interpret a plotting request using three pieces of information when available:

`WHAT TO PLOT + WHICH DATA + PURPOSE/OUTPUT LEVEL`

Examples:

- “plot voltage vs temperature from this file”
- “plot R1 against R2 using the latest data in Drive”
- “plot capacitance vs RH with uncertainty, manuscript style”
- “plot NAV of these two ETFs for one year”
- “plot PID temperature response and show overshoot/settling time”

The user does **not** need to name this plotting reference or a preset.

## 2. Natural-language trigger rule

Treat verbs/phrases such as the following as plotting intent when the surrounding request is technical, scientific, analytical, or quantitative:

- plot / replot / redraw;
- graph / chart;
- “พลอต”, “พล็อต”, “พลอตกราฟ”, “ทำกราฟ”, “วาดกราฟ”;
- compare visually;
- show residuals;
- show uncertainty/error bars;
- make a manuscript/publication figure.

When plotting intent is detected, route through `06-scientific-visualization` and apply this reference before project/domain-specific rules.

## 3. Cross-project grounding rule

Before plotting, determine where the current numerical authority lives.

Use the highest relevant source available in the active project/context:

1. raw measurements / original source data;
2. traceable reproducible analysis outputs;
3. FROZEN/finalized project results where the project uses such a lifecycle;
4. current authoritative project owner/registry;
5. user-provided file in the current conversation;
6. live connected source explicitly requested by the user, such as Google Drive;
7. verified external public source when the user asks for current/literature/external data;
8. chat memory only as navigation/context, not as numerical authority when a better source exists.

If the project defines a stricter source hierarchy, the project rule overrides this generic order.

### Project-context behavior

If the user says:

- “in this project”;
- “use the project data”;
- “use the latest source”;
- “look in the linked Drive”;
- “from the current analysis/freeze”;

then first identify the current project's canonical owner/source-routing documents before selecting values.

Do not assume that a remembered value is still current.

## 4. Source-resolution algorithm

For each plot request:

1. identify variables/series requested;
2. identify the intended dataset(s), run(s), asset(s), specimen(s), or time range;
3. determine whether values are measured, computed, model-predicted, literature-derived, simulated, or illustrative;
4. locate the current authoritative data source;
5. verify units, labels, timestamps/indices, and dataset identity;
6. inspect for obvious gaps, duplicated rows, unmatched conditions, or invalid comparisons when relevant;
7. select a plot form that answers the research question;
8. generate the figure from traceable data;
9. preserve enough provenance to reproduce the plot.

Ask a clarifying question only when an ambiguity would materially change the data or scientific interpretation and cannot be resolved from current project sources.

## 5. No-duplication rule

Do not copy changing project numerical values into this file or into domain plotting profiles merely for convenience.

A plotting profile may store:

- source locations/IDs;
- semantic roles;
- plotting conventions;
- known interpretation boundaries;
- required validation rules;
- figure presets.

It should not become a second editable database of project results.

## 6. Plot-selection rules

Choose the simplest chart that directly answers the question.

### Time-series
Use when x is time or ordered elapsed duration.

Typical uses:
- sensor trajectories;
- market/NAV series;
- heater response;
- drift/stability;
- intervention analysis.

Preserve temporal order and show gaps rather than silently connecting missing intervals when the gaps matter.

### XY scatter / response curve
Use for relationships between two measured/computed numeric variables.

Typical uses:
- capacitance vs RH;
- voltage vs temperature;
- composition vs RH;
- concentration vs response;
- predicted vs measured.

Do not connect points as a continuous experimental trajectory unless ordering/continuity is meaningful.

### Line curve
Use for continuous documented model/literature relations or ordered numeric x when interpolation/model continuity is justified.

Do not turn sparse experimental points into a smooth line merely for aesthetics.

### Bar chart
Use for discrete category comparisons.

Typical uses:
- RMSE by model;
- bias by sensor;
- performance by specimen/group.

Avoid bars for dense continuous scientific relationships where scatter/line is more informative.

### Residual plot
Use whenever fit quality, bias structure, calibration error, or model disagreement is central.

A high R² does not remove the need for residual diagnostics.

### Error-bar / interval plot
Use when traceable uncertainty, SD, CI, range, or other interval estimates exist and are relevant.

Label exactly what the interval represents. Never invent error bars.

### Distribution plot
Use for repeated observations, noise, residual distributions, replicate variability, or population comparisons.

Choose histogram/ECDF/box/violin only when sample size and interpretation justify it.

### Agreement plot
Consider Bland–Altman or equivalent agreement views when comparing two measurement methods, if assumptions are appropriate.

Do not substitute simple correlation for agreement.

## 7. Comparison validity

Before placing two series on the same scientific comparison plot, determine whether important conditions are matched.

Examples:
- temperature;
- sampling interval;
- sensor/device identity;
- run state;
- frequency/mode;
- preprocessing;
- date/time period;
- currency or adjusted/unadjusted price basis;
- normalization convention.

If conditions are not matched, plot them only with explicit labeling and avoid implying direct equivalence.

## 8. Data semantics

The figure/caption should distinguish where relevant:

- measured;
- derived/computed;
- fitted;
- predicted;
- simulated;
- literature/reference;
- illustrative/example.

Never visually present simulated, interpolated, or model-generated points as raw experimental observations.

## 9. Units and transformations

Before plotting:

- identify x/y units;
- standardize compatible units when needed;
- document normalization/log transforms;
- preserve original values in traceable source data;
- avoid hidden offsets or corrections;
- do not convert units based on an assumed convention when the source is ambiguous.

If a transformation materially affects interpretation, state it in the caption/report.

## 10. Filtering, smoothing, and exclusions

Do not silently:

- delete outliers;
- smooth transients;
- interpolate across major data gaps;
- remove disturbed runs;
- crop data to improve apparent agreement;
- choose a favorable subset after seeing the outcome.

When filtering/smoothing is justified:

- preserve raw data;
- state the method/parameters;
- preferably show raw data or provide a raw-data companion view when scientific interpretation depends on the transformation.

## 11. Uncertainty and error bars

Use uncertainty only from a traceable source.

Differentiate:

- standard deviation;
- standard error;
- confidence interval;
- prediction interval;
- expanded measurement uncertainty;
- min–max/range.

Do not label all of these generically as “error”.

If uncertainty is unavailable, omit error bars and say that the figure does not include uncertainty rather than fabricating one.

## 12. Regression/model overlays

Before adding a fitted/model curve:

- identify model form;
- use the intended training/fitting subset;
- report fit range;
- avoid extrapolation beyond validated range unless explicitly requested and clearly marked;
- preserve coefficients/parameters in a result artifact;
- generate residual diagnostics when model performance is part of the claim.

Do not choose model complexity based only on visual smoothness or training R².

## 13. Multi-axis rule

Avoid dual y-axes by default.

Use them only when:

- both variables are necessary to understand one process;
- scales/units differ materially;
- the relationship would be harder to understand with aligned panels/separate plots;
- the axes are unmistakably labeled.

For manuscript figures, aligned panels often communicate more honestly than dual axes.

## 14. Axis-range rule

Do not truncate an axis to exaggerate a small effect.

A non-zero origin may be valid for scientific plots when:

- the full physical range is irrelevant;
- the selected range is clearly labeled;
- truncation does not create a misleading magnitude impression.

For bar charts, a zero baseline is normally preferred unless a strong reason exists.

## 15. Publication-facing mode

When the user requests “manuscript”, “paper”, “publication”, “journal”, “600 dpi”, “final figure”, or equivalent:

1. re-ground current authoritative project values;
2. use publication/FROZEN outputs when the project defines them;
3. verify external source metadata when literature curves/data are included;
4. use clear axis labels and SI/discipline-appropriate units;
5. keep legends concise;
6. avoid unnecessary in-plot titles if the journal/caption carries the title;
7. use vector PDF/SVG when practical plus high-resolution raster when requested;
8. check final-size legibility;
9. preserve source-data/script provenance;
10. ensure figure, caption, manuscript values, and claim wording are consistent.

A visually polished figure is not manuscript-ready if its data provenance is unresolved.

## 16. Exploratory mode

When the user asks simply to “plot” or “see what it looks like” and publication use is not implied:

- prioritize rapid, transparent visualization;
- use current available data;
- clearly mark preliminary/exploratory sources;
- avoid unnecessary full manuscript verification;
- still preserve raw-data integrity and do not invent values.

Exploratory output must not silently be upgraded to manuscript evidence later. Re-ground before publication use.

## 17. Connected-source behavior

When the user explicitly says to use a connected source such as Drive:

- use the live connected source where available;
- prefer source-data CSV/XLSX/analysis outputs over digitizing a PNG;
- use README/metadata/provenance files to interpret columns/curves;
- if only an image exists, digitization may be used but must be labeled as digitized/approximate;
- do not assume the newest modified file is scientifically authoritative unless project governance says so.

## 18. Cross-project portability

This generic plotting reference applies to any project.

Examples:

### Sensor / instrumentation
“Plot capacitance vs RH for Track A with uncertainty.”

### Thermal / PID
“Plot temperature and setpoint for the latest run and mark overshoot and settling time.”

### ML
“Plot measured vs predicted plus residuals for the held-out test set.”

### Finance / markets
“Plot NAV and distributions for these two ETFs over the same period.”

### Student/lab data
“Plot voltage vs current from this Excel file and fit a linear model.”

The generic plotting rules remain the same; project/domain sources determine what the variables mean and which data are authoritative.

## 19. Domain-profile escalation

Use a domain profile only when the domain has reusable semantics or constraints that the generic rules cannot safely infer.

Examples:

- glycerol RH literature roles/temperature context;
- IDC frequency/mode/specimen semantics;
- thermal-system settling definitions;
- finance total-return/distribution conventions.

Do **not** create a new domain profile merely because one new figure is requested.

## 20. Internal routing modes

These are internal convenience categories; the user does not need to know or type them.

- `PLOT-TS` — time-series / trajectory
- `PLOT-XY` — numeric relationship / calibration
- `PLOT-CAT` — categorical comparison
- `PLOT-RESID` — residual / error structure
- `PLOT-UNC` — uncertainty/interval-focused
- `PLOT-AGREE` — method agreement
- `PLOT-MODEL` — observed vs fitted/predicted
- `PLOT-LIT` — literature/reference comparison
- `PLOT-PUB` — publication-facing rendering/check

A request may invoke more than one route, e.g. `PLOT-XY + PLOT-UNC + PLOT-PUB`.

## 21. Minimal user-command expectation

The user should normally be able to type natural commands such as:

- “plot X vs Y”;
- “plot these two files together”;
- “plot using the latest data from Drive”;
- “plot residuals too”;
- “make it suitable for the paper”;
- “use the data in this project”.

The Research Agent should infer the appropriate plotting route, project source hierarchy, and domain profile whenever the context makes them clear.

## 22. Reproducibility record

For a substantive scientific figure, preserve when practical:

- plot identifier/title;
- research question;
- source file(s)/IDs;
- source version/date or FROZEN package;
- variable/column mapping;
- units;
- exclusions/transformations;
- fitting/model details if used;
- uncertainty source;
- plotting script/version;
- generated artifact(s);
- limitations.

For manuscript-facing figures, this record is expected, not optional.

## 23. Hard-stop conditions

Do not produce a manuscript-facing quantitative figure as if final when:

- the source dataset cannot be identified;
- units are unresolved;
- project values conflict with a higher-authority source;
- a current FROZEN output is required but not located;
- uncertainty bars are requested but no traceable uncertainty exists;
- compared datasets are materially unmatched and the mismatch is hidden;
- the figure would present model/interpolated/simulated values as measurements;
- literature values cannot be traced to a verified source where publication-level citation is required.

In such cases, an exploratory figure may still be generated if useful, but it must be clearly labeled as exploratory and the missing verification must be stated.
