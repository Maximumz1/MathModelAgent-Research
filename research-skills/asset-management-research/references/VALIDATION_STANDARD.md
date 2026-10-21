# Portfolio Validation Contract

## Source
Freeze actual input price bytes and SHA-256, ticker order, trading calendar, currency, adjusted/raw close policy, acquisition time, start/end range, missing sessions and transformation log.

## Train/Test discipline
Predefine nonoverlapping chronological train/test folds. Train-end must precede Test-start. Never estimate weights on Test; never use a same-day close signal and claim gains from the close movement already passed. Previously inspected folds are historical exploratory evidence, not untouched future tests.

## Optimizer
Check weights are numeric, finite, long-only where specified, sum to 1, satisfy all caps and match ticker order. Check solver convergence and 100% single-asset allocations. Compare with equally feasible simpler baselines and matching risk-free assumptions.

## Simulator
Document entry day and fill reference, first exposed return, initial purchase cost, rebalance timing, transaction notional, fee calculation, slippage, annualization and monthly/weekly calendar rules. Rebalance at close *after* marking that day's portfolio movement if using close-to-close return data.

## Comparative reporting
Require Equal Weight, buy-and-hold benchmark and fixed-weight baselines. Report total return, CAGR, volatility, Sharpe, max drawdown, turnover and cost by fold, paired fold deltas, worst fold and sensitivity. Watch for FX, distribution omission and benchmark mismatch.

## Verification gates
(1) SHA-256 input matches metadata. (2) Price rows and dates valid. (3) Fold chronology valid. (4) Strategy/fold/cost/date keys unique. (5) Weights valid and capped as stated. (6) NAV positive/finite. (7) Total return = (last NAV - pre-fee initial principal 1)*100. (8) Drawdown computed from cumulative peak including initial principal. (9) Tables match figures and source IDs. (10) Cautious evidence label.

Audit PASS is not a forecast or approval for automated trading.

Historical Phase 1–5 status as of 2026-10-21: toolkit numerical functions and seven retrospective VOO/QQQM/SCHD folds were exercised. A 60% cap improved average returns in the inspected sample but did not improve every fold; strategy outperformance is **not established**. Do not hard-code sample returns in evergreen prompts.
