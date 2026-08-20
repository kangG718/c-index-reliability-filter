# Reproducibility artifacts

Generated model and cache files are intentionally not committed yet. After the final training run, this directory will be populated according to manifest.json.

Expected files include trained GBM, RF and MLP models; the MLP scaler and architecture metadata; feature-column order; finalDf_cache.pkl; and XAI ranking caches.

Large binary artifacts should be stored with Git LFS or attached to a versioned GitHub Release.
