import json
import sys
from pathlib import Path
from io import StringIO

import pandas as pd


TARGET_CELLS = {
    "model_metrics": 11,
    "rf_metrics": 15,
    "mlp_metrics": 17,
    "disagreement": 24,
    "pooled_performance": 36,
    "asset_performance": 39,
}


def _read_html_tables(output):
    html = output.get("data", {}).get("text/html")
    if not html:
        return []
    html = "".join(html)
    try:
        return pd.read_html(StringIO(html))
    except ValueError:
        return []


def _normalize_df(df):
    df = df.copy()
    df.columns = [str(c) for c in df.columns]
    return df.to_csv(index=False, float_format="%.10g")


def extract_signature(path):
    nb = json.loads(Path(path).read_text(encoding="utf-8"))
    signature = {}

    for name, cell_idx in TARGET_CELLS.items():
        cell = nb["cells"][cell_idx]
        outputs = cell.get("outputs", [])

        text_parts = []
        table_parts = []

        for output in outputs:
            text = "".join(output.get("text", []))
            if text:
                # Epoch logs can include many repeated lines; keep them because they
                # are exactly what should be reproducible for seed validation.
                text_parts.append(text.strip())

            for table in _read_html_tables(output):
                table_parts.append(_normalize_df(table))

        signature[name] = {
            "text": "\n".join(text_parts),
            "tables": table_parts,
        }

    return signature


def compare(paths):
    sigs = [extract_signature(path) for path in paths]
    base = sigs[0]
    ok = True

    for i, sig in enumerate(sigs[1:], start=2):
        for section in TARGET_CELLS:
            if sig[section] != base[section]:
                ok = False
                print(f"[DIFF] run1 vs run{i}: {section}")
                if sig[section]["text"] != base[section]["text"]:
                    print("  - text output differs")
                if sig[section]["tables"] != base[section]["tables"]:
                    print("  - table output differs")

    if ok:
        print("PASS: all selected outputs are identical across runs.")
    else:
        print("FAIL: at least one selected output differs.")

    return ok


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python3 reproducibility_compare.py "
            "run1.ipynb run2.ipynb run3.ipynb"
        )
        sys.exit(2)

    sys.exit(0 if compare(sys.argv[1:]) else 1)
