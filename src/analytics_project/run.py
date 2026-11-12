"""Aufruf: uv run --locked python -m analytics_project.run [--csv DATEI --target SPALTE --id-columns SPALTE ...]."""
import argparse
import json
from pathlib import Path

import pandas as pd

from .analysis import DEMO_ID_COLUMNS, DEMO_TARGET, analyze, demo_data


def main():
    parser = argparse.ArgumentParser(description="Baseline und Ridge-Regression auf zurückgehaltenen Testdaten vergleichen.")
    parser.add_argument("--csv", type=Path, help="Eigene CSV-Datei. Ohne Angabe laufen die synthetischen Beispieldaten.")
    parser.add_argument("--target", help="Name der numerischen Zielspalte.")
    parser.add_argument("--id-columns", nargs="*", default=[], help="Kennungsspalten, die nicht als Prädiktor dienen.")
    parser.add_argument("--output", type=Path, default=Path("outputs"))
    args = parser.parse_args()
    if args.csv:
        if not args.target:
            parser.error("--target ist bei einer eigenen CSV-Datei erforderlich.")
        data, target, id_columns = pd.read_csv(args.csv), args.target, tuple(args.id_columns)
        source = str(args.csv)
    else:
        data, target, id_columns = demo_data(), DEMO_TARGET, DEMO_ID_COLUMNS
        source = "synthetische Serviceanfragen (Lehrbeispiel)"
    try:
        result = analyze(data, target, id_columns)
    except ValueError as error:
        parser.exit(2, f"Datenprüfung fehlgeschlagen: {error}\n")
    args.output.mkdir(parents=True, exist_ok=True)
    result.metrics.to_csv(args.output / "metrics.csv", index=False)
    result.predictions.to_csv(args.output / "predictions.csv", index=False)
    summary = {"source": source, "target": target, "id_columns": list(id_columns), "seed": 42,
               "quality": result.quality, "train_rows": result.train_rows,
               "test_rows": result.test_rows, "selected_alpha": result.selected_alpha}
    (args.output / "run.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(result.metrics.to_string(index=False))


if __name__ == "__main__":
    main()
