---
name: asset-management-research
description: "Evidence-traceable portfolio and ETF quantitative research: risk, optimization, backtesting, walk-forward, cost/concentration checks, and CSV/JSON/ZIP audits. No trading."
version: "1.0.0"
---

# Asset Management Research Skill v1.0

**Role:** research analyst, not execution agent. Complements the current Investing Project Second Brain and the Research Agent. Does not place trades or connect to brokers.

## When to activate
Thai/US portfolio risks, correlation, allocation, Sharpe/GMV optimizers, ETF comparison, drawdown, performance, walk-forward, cost sensitivity, and CSV/JSON/ZIP export.

## Source priority
1. Current Investing Project authoritative files and current connected/user-provided raw or frozen prices, transactions and dividend documents.
2. Traceable calculations with dates, currency, price basis, data provider and frozen SHA-256.
3. The Research Agent in Maximumz1/MathModelAgent-Research branch chatgpt-research-adaptation governs **methodology only**.
4. Memory and watchlists are navigation, not evidence of actual holdings. Never fabricate quantities, NAV, payouts or purchase prices.

Read references/PROJECT_ROUTING.md, references/VALIDATION_STANDARD.md and references/ARTIFACT_CONTRACT.md as relevant.

## Workflow
1. Determine research question, asset universe, period, benchmark, base currency, goals and evidence state.
2. Audit chronological input, ticker identity, duplicate/missing sessions, adjustment policy, splits, dividends, FX and corporate actions. Freeze original data with checksum; never overwrite raw.
3. Start with equal-weight, buy-and-hold and fixed-weight baselines. Compute historical return, volatility, drawdown, covariance/correlation, capital weights, risk contributions and concentration.
4. Use the external Python asset_management_toolkit library for mathematical portfolio functions **only if separately installed and permitted**. Do not vendor/copy its source. Its repo had no explicit redistributable LICENSE in the inspected tree (2026-10-21).
5. For optimization, fit expected returns/covariance on TRAINING ONLY; check finite weights, long-only, sum-to-one, constraint feasibility, label order, solver success, extreme boundary weights. A 60% position cap is an experimental assumption, not a universal investment recommendation or necessarily built-in library feature.
6. For backtests, predeclare folds, strictly later Test windows, an executable price convention (e.g. first test close, earn only next-day return), entry cost, rebalancing costs, slippage/spread assumptions and benchmark parity. Distinguish retrospective viewed folds from untouched future tests.
7. For robustness, report per-fold return, Sharpe and maximum drawdown, paired differences, median/worst cases, cost sensitivity, concentration and solver instability; do not tune on held-out periods and then claim independent out-of-sample validation.
8. Produce structured CSV/JSON/PNG/ZIP and a concise Thai report explaining what was measured, computed, modeled or hypothesized. Mark PASS/WARN/FAIL and limitations.

## Finance-specific safeguards
- Distinguish raw Close, Adjusted Close (total-return-like proxy), fund NAV, paid cash distributions and actual after-tax investment return. Do not infer JEPQ/QQQI payouts from adjusted prices.
- Check portfolio benchmark basis, USD/THB, WHT and distribution type from authoritative records. Never hardcode a universal tax assumption.
- Risk contribution is not the same as weight; max Sharpe may select one asset.
- The prior Phase 1–5 experiments were exploratory tool validations, not proof of live returns or superior strategy performance.
- Do not silently install Python dependencies, modify canonical documents, or perform broker/account actions.

## Outputs when numerical analysis occurs
Prefer source_snapshot.csv, fold_boundaries.csv, training_weights.csv, strategy_metrics.csv, daily_nav_drawdown.csv, transaction_events.csv, cost_sensitivity.csv, validation_checks.csv, run_metadata.json, figures/*.png, analysis_report.md and a reproducible session ZIP. Do not invent files that were not generated. No CSV required for explanation-only requests.

Evidence labels: synthetic_demo, historical_exploratory, retrospective_walk_forward, independently_reproduced, forward_paper_tracked.

Audit PASS means arithmetic and provenance consistency only, not a proven market edge. Block when the original source is unknown, chronology or constraints are invalid, a look-ahead error is unresolved, or a comparison is materially unmatched.

If plotting, also follow research-skills/06-scientific-visualization/SKILL.md and research-skills/_references/scientific-plotting-rules.md. Prefer reproducible figures and explicit units.
