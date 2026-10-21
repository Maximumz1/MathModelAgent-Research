# Reproducible Research Artifact Contract

For every substantive analysis, prefer a separate UTC session folder and ZIP. Never overwrite the raw input.

Suggested contents:
- source_snapshot.csv: original prices with Date and explicit ticker columns;
- fold_boundaries.csv: fold, train_start, train_end, test_start, test_end, train_rows, test_rows;
- training_weights.csv: fold, strategy, weight per asset;
- strategy_metrics.csv: fold, strategy, cost_rate, total_return_pct, annualized_return_pct, volatility_pct, max_drawdown_pct, sharpe, turnover;
- daily_nav_drawdown.csv: fold, strategy, cost_rate, date, NAV, drawdown_pct;
- transaction_events.csv: date, action, notional, fee and NAV;
- cost_sensitivity.csv: strategy, cost_rate and compared performance;
- validation_checks.csv: test, PASS/WARN/FAIL, evidence;
- run_metadata.json: source name, exact checksum, date, tickers, price basis, annualization, currency, code/library versions, train/test bounds, cost assumptions, evidence status;
- figures/*.png and analysis_report.md with data source, units, interpretation and limitations.

Missing required data is a BLOCK; never fabricate CSVs or fill gaps silently. Private brokerage exports must stay outside public GitHub. Legacy Phase-5 exports use a different schema and must be explicitly mapped or audited by a compatible script.
