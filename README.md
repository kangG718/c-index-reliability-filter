# C-index Reliability Filter

A model-agnostic framework that uses agreement between multiple XAI feature rankings as a reliability signal for filtering financial trading predictions.

## Current research position

The current evidence is model-dependent and remains exploratory. In the verified STEP=2 cache (861 rows), the selected active C-index filters improved pooled per-trade Sharpe for GBM and Random Forest across 0bp, 5bp, and 10bp cost scenarios, and exceeded the 95th percentile of count-matched random selection. Max-stat adjusted p-values were below 0.05 for GBM at 0bp/5bp and RF at 5bp/10bp, while GBM at 10bp and RF at 0bp were suggestive (adjusted p about 0.058 and 0.056). MLP did not improve and was not significant. The framework is therefore presented as a promising but non-universal reliability-filter candidate rather than proven performance improvement across models.

## Repository structure

- `notebooks/main`: current STEP=2 main experiment with corrected Sharpe logic.
- `notebooks/evaluation`: transaction-cost, statistical-test, and benchmark analyses.
- `notebooks/archive`: original, STEP=10, and earlier STEP=2 notebooks retained for traceability.
- `configs`: recorded main experiment settings.
- `artifacts`: `finalDf_cache.pkl` and compact final evaluation tables; model checkpoints are still pending.
- `results/tables`: CSV outputs from the verified current run.
- `results/figures`: generated figures from the verified current run.
- `scripts`: reproducibility utilities.

## Recommended reading order

1. Run or inspect `notebooks/main/C_Index(step2,_sharpe_logic_changed).ipynb`.
2. Use `notebooks/evaluation/C_Index(step2,_transaction_cost).ipynb` for cost robustness and block-resampling tests.
3. Use `notebooks/evaluation/C_Index(step2,_benchmark_filters).ipynb` for confidence and random count-matched benchmarks.
4. Use `results/run_manifest.json` to check the current output inventory.
5. Treat `notebooks/archive` as traceability material rather than final results.

## Reproduction modes

Quick downstream reproduction is now available: load `artifacts/finalDf_cache.pkl` and rerun the evaluation notebooks without retraining models or recomputing XAI rankings. Full reproduction still rebuilds data, retrains all models, recomputes XAI rankings, calculates C-index values, and reruns evaluation. Because trained model weights, preprocessing objects, and full XAI caches have not yet been published, full reproduction currently requires training from code.

## Artifact requirements

The published `finalDf_cache.pkl` is sufficient for transaction-cost, statistical-test, and benchmark evaluation. A complete training-level release should additionally include the three trained models, MLP architecture metadata and scaler, ordered feature list, training configuration, data and code hashes, and XAI ranking caches. Large binaries should be distributed with Git LFS or a versioned GitHub Release rather than ordinary commits.

## Main experimental settings

- Assets: SPY, TLT, GLD.
- Period: 2012-01 through 2025-12.
- Operational evaluation period: 2023-12-26 through 2025-12-26.
- Models: LightGBM, Random Forest, and PyTorch MLP.
- XAI methods: Permutation Importance and SHAP.
- Rolling window: W=60; main sampling step: STEP=2.
- Filter quantiles: 0.2, 0.3, 0.4, and 0.5.
- Primary reporting: pooled per-trade Sharpe together with Trade Count.
- Statistical test: 20-trading-day block bootstrap/permutation with max-stat multiple-testing correction.

## Status

The current evaluation notebooks, `finalDf_cache.pkl`, compact evaluation artifacts, CSV tables, figures, and run manifest are published on the `initial-organization` branch. Model weights and full training/XAI caches remain the main missing items for complete from-scratch reproduction.
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
