#!/usr/bin/env python3
"""Read-only audit of a Phase-5-format results ZIP. No new backtest or trade."""
import argparse
import hashlib
import io
import json
import sys
import zipfile

import numpy as np
import pandas as pd

REQUIRED = {
    "prices": "01_frozen_phase4_adjusted_close.csv",
    "folds": "02_fold_boundaries.csv",
    "weights": "03_training_weights.csv",
    "metrics": "04_all_fold_metrics.csv",
    "nav": "05_daily_nav_drawdown.csv",
    "metadata": "14_run_metadata.json",
}

def audit(path):
    with zipfile.ZipFile(path) as bundle:
        def raw(filename):
            matches = [n for n in bundle.namelist() if n == filename or n.endswith("/" + filename)]
            if len(matches) != 1:
                raise ValueError(f"Expected one {filename}, got {len(matches)}")
            return bundle.read(matches[0])
        content = {k: raw(v) for k, v in REQUIRED.items()}
    metadata = json.loads(content["metadata"].decode("utf-8"))
    frames = {k: pd.read_csv(io.BytesIO(v)) for k, v in content.items() if k != "metadata"}
    checks = []
    def check(label, success, detail=""):
        checks.append({"check": label, "result": "PASS" if bool(success) else "FAIL", "detail": str(detail)})
    price_sha = hashlib.sha256(content["prices"]).hexdigest()
    check("source_sha256", price_sha == metadata.get("input_sha256"), price_sha)
    prices = frames["prices"]
    tickers = metadata.get("tickers", [])
    check("ticker_identity", bool(tickers) and all(t in prices for t in tickers))
    check("price_rows", len(prices) == int(metadata.get("price_rows", -1)))
    price_dates = pd.to_datetime(prices["Date"], errors="coerce")
    check("price_chronology", price_dates.notna().all() and price_dates.is_unique and price_dates.is_monotonic_increasing)
    px = prices[tickers].to_numpy(dtype=float)
    check("price_validity", np.isfinite(px).all() and (px > 0).all())
    fold = frames["folds"]
    ends = pd.to_datetime(fold["train_end"], errors="coerce")
    starts = pd.to_datetime(fold["test_start"], errors="coerce")
    check("fold_count", len(fold) == int(metadata.get("completed_folds", -1)))
    check("fold_no_leakage", ends.notna().all() and starts.notna().all() and (ends < starts).all())
    check("fold_training_rows", (fold["train_rows"] == int(metadata.get("train_days", -1))).all())
    check("fold_testing_rows", (fold["test_rows"] == int(metadata.get("test_days", -1))).all())
    weights = frames["weights"]
    w = weights[tickers].to_numpy(dtype=float)
    check("weight_finite_longonly", np.isfinite(w).all() and (w >= -1e-8).all() and (w <= 1 + 1e-8).all())
    check("weight_sum", np.allclose(w.sum(axis=1), 1.0, atol=1e-7))
    cap = float(metadata.get("cap_weight", 0.60))
    capped = weights.loc[weights["strategy"].str.contains("capped", case=False, na=False), tickers]
    check("weight_cap", not capped.empty and (capped.max(axis=1) <= cap + 1e-7).all())
    metric = frames["metrics"]
    nav = frames["nav"]
    key = ["fold", "strategy", "cost_rate"]
    check("metric_keys_unique", not metric.duplicated(key).any())
    check("nav_keys_unique", not nav.duplicated(key + ["date"]).any())
    errors = []
    dd_errors = []
    missing = 0
    nav_ok = True
    for (f, strategy, cost), group in nav.groupby(key, sort=False):
        group = group.sort_values("date")
        series = group["NAV"].to_numpy(dtype=float)
        nav_ok &= bool(np.isfinite(series).all() and (series > 0).all())
        observed = metric.loc[(metric["fold"] == f) & (metric["strategy"] == strategy) & np.isclose(metric["cost_rate"], cost, atol=1e-12)]
        if len(observed) != 1:
            missing += 1
            continue
        drawn = (series / np.maximum(1.0, np.maximum.accumulate(series)) - 1.0) * 100
        errors.extend([
            abs((series[-1] - 1.0) * 100 - float(observed.iloc[0]["total_return_pct"])),
            abs(float(drawn.min()) - float(observed.iloc[0]["max_drawdown_pct"]))
        ])
        dd_errors.extend(np.abs(drawn - group["drawdown_pct"].to_numpy(dtype=float)))
    check("nav_positive", nav_ok)
    check("nav_metric_keys", missing == 0 and len(errors) == len(metric) * 2)
    check("nav_recomputed", len(errors) > 0 and max(errors) < 2e-5)
    check("drawdown_recomputed", len(dd_errors) > 0 and max(dd_errors) < 2e-5)
    return {"status": "PASS" if all(c["result"] == "PASS" for c in checks) else "FAIL",
            "scope": "Phase-5-format historical export arithmetic only; not evidence of forecasting performance",
            "source_sha256": price_sha, "metric_groups": len(errors) // 2, "checks": checks}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("zip_path")
    parser.add_argument("--output", default="phase5_audit.json")
    args = parser.parse_args()
    try:
        result = audit(args.zip_path)
    except (ValueError, KeyError, OSError, zipfile.BadZipFile) as e:
        print(f"Audit BLOCKED: {e}", file=sys.stderr)
        sys.exit(2)
    with open(args.output, "w", encoding="utf-8") as out:
        json.dump(result, out, indent=2, ensure_ascii=False)
    print(result["status"], len(result["checks"]), "checks", result["metric_groups"], "metric groups")
    sys.exit(0 if result["status"] == "PASS" else 1)
