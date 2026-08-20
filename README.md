# C-index Reliability Filter

A model-agnostic framework that uses agreement between multiple XAI feature rankings as a reliability signal for filtering financial trading predictions.

## Current research position

The current evidence is exploratory. Across GBM, MLP, and Random Forest, the selected C-index filters improved pooled per-trade Sharpe and maximum drawdown relative to the unfiltered strategy, including 5bp and 10bp cost scenarios. However, the filters did not exceed the 95th percentile of count-matched random selection, and block-permutation max-stat corrections were not statistically significant. The framework is therefore presented as a reliability-filter candidate, not as proven performance improvement.

## Repository structure

- notebooks/main: current STEP=2 main experiment with corrected Sharpe logic.
- notebooks/evaluation: transaction-cost, statistical-test, and benchmark analyses.
- notebooks/archive: original, STEP=10, and earlier STEP=2 notebooks.
- artifacts: model, preprocessing, feature-order, XAI, and cache contract. Artifacts will be added after the final training run.
- scripts: reproducibility comparison utility.
- results/figures: generated figures used in reports and presentations.
- docs/reports: PDF and Word research reports.
- docs/presentations: project slide decks.
- docs/feedback: advisor feedback retained for research traceability.

## Recommended reading order

1. Run or inspect notebooks/main/C_Index(step2,_sharpe_logic_changed).ipynb.
2. Use notebooks/evaluation/C_Index(step2,_transaction_cost).ipynb for cost robustness and block-resampling tests.
3. Use notebooks/evaluation/C_Index(step2,_benchmark_filters).ipynb for confidence and random count-matched benchmarks.
4. Treat notebooks/archive as traceability material rather than final results.

## Reproduction modes

Quick reproduction will load finalized model and XAI/cache artifacts and rerun filtering, performance evaluation, and statistical tests. Full reproduction will rebuild data, retrain all models, recompute XAI rankings, calculate C-index values, and rerun evaluation. The quick path is not available until the final model artifacts and finalDf_cache.pkl are generated and published.

## Artifact requirements

A reproducible release must include the three trained models, MLP architecture metadata and scaler, ordered feature list, training configuration, data and code hashes, finalDf_cache.pkl, and the XAI ranking caches. Large binaries should be distributed with Git LFS or a versioned GitHub Release rather than ordinary commits.

## Main experimental settings

- Assets: SPY, TLT, GLD.
- Period: 2012-01 through 2025-12.
- Operational evaluation period: 2023-12-26 through 2025-12-26.
- Models: LightGBM, Random Forest, and PyTorch MLP.
- XAI methods: Permutation Importance and SHAP.
- Rolling window: W=60; main sampling step: STEP=2.
- Filter quantiles: 0.2, 0.3, 0.4, and 0.5.
- Primary reporting: pooled per-trade Sharpe together with Trade Count.

## Status

The repository currently preserves the completed experimental notebooks and research outputs. Model checkpoints and caches are pending a final controlled training run.
