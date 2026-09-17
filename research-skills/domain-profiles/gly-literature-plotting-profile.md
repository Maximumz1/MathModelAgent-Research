# Domain Profile — GLY Literature Comparison Plotting

Status: ACTIVE helper profile for the Engineering Research Agent

Purpose: provide a reproducible routing and plotting contract for glycerol–water composition/RH literature-comparison figures without creating a second numerical source of truth.

## Authority boundary

This file is **not** the numerical authority for project RH values, uncertainty values, formulation composition, or literature data.

Use the current source-of-truth hierarchy:

1. raw measurements / physical preparation records;
2. traceable reproducible analysis outputs and FROZEN packages;
3. dated experimental/intervention records;
4. primary literature / standards;
5. canonical project owner documents;
6. this plotting profile only as routing/instruction context.

Never copy a changing project value into this profile merely for convenience.

## Canonical project owners to read before manuscript-facing plotting

- `GLY_Master_and_Registry.md` — current GLY campaign/formulation owner.
- `GLY_Analysis_Rules.md` — operational-stability, matched-temperature and terminology rules.
- `Publication_and_Claim_Registry.md` — P-GLY-01 scope and claim boundaries.
- `Data_Governance_and_Lifecycle.md` — RAW/QC/ANALYZED/FROZEN/MANUSCRIPT lifecycle and provenance requirements.
- `Known_Corrections_Register.md` — never-recur corrections.

For publication-level work, use the relevant current FROZEN P-GLY-01 package rather than copying manuscript numbers from chat, screenshots, dashboards, or this profile.

## Current Drive literature-comparison package

Primary folder context:

- In-paper folder: `1rXs3QFx-8p0jgZo5G2VM_MLWsL65BE8X`

Current plot artifact:

- `Composition_RH_Literature_Comparison.png`
- Drive file ID: `1GSY9i2QLiPmy0knuQiILRSFfu5d6iOX6`

Traceable source-data artifact:

- `Composition_RH_Literature_Comparison_SourceData.csv`
- Drive file ID: `1908Mk1DpA5qSc4ycDe41mQwW6_Ak7IRP`

Literature-package notes:

- `README_Literature_Comparison.txt`
- Drive file ID: `1hFc00xLO66clEa0y8B2xoDyMZndEeWLe`

When replotting, fetch the current CSV and README from Drive rather than digitizing the PNG if the CSV remains available.

## Literature curve roles

The literature-comparison package currently distinguishes the following sources/roles:

### Braun–Forney

- empirical literature relation derived from Braun data and presented/used by Forney;
- approximately 24 °C context;
- historical empirical comparison curve;
- do not call it the apparatus assigned RH.

### Zhang et al.

- water-activity values/model at 20 °C in the current package;
- plotted as `RH = 100 × a_w`;
- current source package uses interpolation for the composition grid;
- useful as a temperature-near comparison for the present ~20–22 °C project states;
- verify the exact primary-paper/table/model citation before manuscript submission.

### Hook & Mayer

- Raoult-law-based guideline in the current package;
- contextual/approximate guideline rather than an equivalent empirical reference curve;
- does not represent a full temperature-dependent glycerol equilibrium model;
- normally keep secondary to Braun–Forney and Zhang in a manuscript-facing comparison.

## Critical interpretation rules

1. `nominal literature RH ≠ measured operational RH ≠ validated assigned RH`.
2. Do not force project measurements to equal any one literature relation.
3. Do not present the three literature curves as equivalent measurements.
4. Preserve temperature context in the legend/caption.
5. A difference between project RH and one literature curve is not automatically sensor error or apparatus error.
6. If the project point temperature differs materially from the literature temperature, state that limitation.
7. For project repeatability or assigned-state conclusions, use the frozen GLY analysis rules; do not infer them from this comparison plot alone.

## Plot routing

When the user requests a GLY composition/RH plot or says phrases such as:

- “พลอต composition vs RH”
- “plot literature comparison”
- “plot กราฟ glycerol literature”
- “เปรียบเทียบ measured RH กับ literature”
- “ทำ residual เทียบ Forney/Zhang”

use this profile together with `06-scientific-visualization`.

### Step 1 — Determine plot purpose

Classify the request as one of:

- exploratory/internal;
- manuscript main figure;
- manuscript supplementary figure;
- residual/diagnostic figure;
- literature-model comparison only.

### Step 2 — Re-ground current data

For a manuscript-facing plot:

- read the current GLY owner/method/publication files;
- obtain current FROZEN project values from the authoritative analysis package;
- fetch the current Drive literature-comparison CSV and README;
- verify external primary sources if the caption/reference list will be publication-ready.

For exploratory plotting, the current source-data CSV plus canonical owner values may be sufficient, but label outputs as exploratory if they are not from the current FROZEN package.

### Step 3 — Preserve traceability

For each generated figure preserve:

- source project data/FROZEN output;
- literature source-data CSV version or Drive ID;
- plotting script/version;
- generated PNG/PDF/SVG;
- plot purpose;
- claim(s) supported;
- limitations.

## Plot presets

### `GLY-LIT-1` — Full literature context

Use:

- Braun–Forney curve;
- Zhang 20 °C curve;
- Hook & Mayer guideline;
- current project measured/frozen points.

Best for:

- supplementary material;
- literature landscape;
- methodological context.

Required caption note: curves have different empirical/model status and temperature context.

### `GLY-LIT-2` — Manuscript focused

Use:

- Braun–Forney empirical relation;
- Zhang 20 °C relation/model;
- current project measured/frozen points;
- project uncertainty bars when current FROZEN `U_RH` is available and the figure purpose requires it.

Normally omit Hook & Mayer from the main figure or move it to supplementary/context.

Best for:

- main manuscript composition–RH comparison.

### `GLY-LIT-3` — Residual vs literature

At the actual project formulation compositions, compute:

- `ΔRH_BF = RH_project − RH_Braun_Forney`
- `ΔRH_Zhang = RH_project − RH_Zhang`
- optionally `ΔRH_HM = RH_project − RH_Hook_Mayer`

Best for:

- showing composition-dependent deviation;
- preventing a vague “higher/lower than literature” statement;
- Discussion/diagnostics.

Do not interpret residuals as instrument error without an uncertainty/temperature/method analysis.

### `GLY-LIT-4` — Literature-model spread

Plot literature differences without project measurements, for example:

- `RH_Zhang − RH_Braun_Forney`
- `RH_Hook_Mayer − RH_Braun_Forney`

Best for:

- showing that “literature” is not one universal curve;
- supporting discussion of model/temperature/source dependence.

### `GLY-LIT-5` — Project points + uncertainty only

Use:

- current seven-formulation FROZEN project states;
- x = CoA-corrected glycerol wt%;
- y = measured operational RH;
- y-error = current FROZEN expanded uncertainty if applicable;
- optional faint literature relation as context.

Best for:

- emphasizing the operational RH ladder rather than literature agreement.

## Style rules

For publication-facing plots:

- label x-axis explicitly as glycerol mass fraction / corrected glycerol wt%;
- label y-axis as relative humidity (%RH);
- state literature temperature in legend or caption;
- use project formulation IDs only when they improve interpretation;
- use error bars only from traceable uncertainty outputs;
- avoid decorative smoothing of project measurement points;
- literature curves may be continuous only when generated from the documented source relation/interpolation;
- avoid implying independent replication by plotting many interpolated literature grid points as experimental observations.

## Updating rule

If any of the following changes, re-ground before replotting:

- CoA purity/composition;
- FROZEN R1/representative ladder;
- operational uncertainty model;
- literature source/model/table;
- manuscript scope;
- figure source-data CSV.

Do not silently reuse an old figure when upstream evidence changes.

## Recommended response behavior

If the user says only:

> “พลอตกราฟ literature comparison ให้หน่อย”

then:

1. read this profile;
2. read the minimum relevant current canonical GLY/publication sources;
3. fetch the current literature source-data CSV/README from Drive;
4. select `GLY-LIT-2` by default for a manuscript-focused request, otherwise `GLY-LIT-1` for broad exploration;
5. state whether the project points are current FROZEN values or exploratory values;
6. generate the figure and preserve a traceable source-data table/script when practical.

If the user specifies a preset such as `GLY-LIT-3`, use that preset directly after the required grounding.

## Quick commands

Examples for future chats:

- `ใช้ Research Agent พลอต GLY-LIT-2 จากข้อมูลปัจจุบันใน source`
- `ใช้ Research Agent ทำ GLY-LIT-3 เทียบ Forney กับ Zhang`
- `อัปเดต GLY literature plot จาก FROZEN data ล่าสุด`
- `ทำ GLY-LIT-5 พร้อม U_RH จาก freeze ปัจจุบัน`

The phrase “ข้อมูลปัจจุบันใน source” means: re-read current canonical owners/FROZEN outputs and the current Drive literature source package before plotting; do not reuse stale numbers from this profile or chat memory.
