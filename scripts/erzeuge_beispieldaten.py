"""Erzeugt den synthetischen Beispieldatensatz der Vorlage.

Aufruf im Projektordner: uv run --locked python scripts/erzeuge_beispieldaten.py

Die Daten sind erfunden. Sie beschreiben keine realen Anfragen, Personen oder Unternehmen.
Der feste Seed sorgt dafür, dass jeder Lauf dieselbe Datei erzeugt.
"""
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 2627
ZEILEN = 600
ZIEL = Path(__file__).resolve().parents[1] / "data" / "beispiel" / "serviceanfragen-synthetisch.csv"

# Zuschläge in Stunden, frei gewählt für das Lehrbeispiel.
FEHLERTYP = {"Bedienung": 0.0, "Software": 1.5, "Verschleiss": 3.0, "Elektronik": 5.0}
PRODUKTGRUPPE = {"Haushalt": 0.0, "Garten": 0.8, "Gewerbe": 2.5}
EINGANGSKANAL = {"Portal": 0.0, "E-Mail": 0.6, "Telefon": 1.2}


def erzeuge(seed=SEED, zeilen=ZEILEN):
    rng = np.random.default_rng(seed)
    fehlertyp = rng.choice(list(FEHLERTYP), zeilen, p=[0.35, 0.25, 0.25, 0.15])
    produktgruppe = rng.choice(list(PRODUKTGRUPPE), zeilen, p=[0.5, 0.3, 0.2])
    eingangskanal = rng.choice(list(EINGANGSKANAL), zeilen, p=[0.45, 0.35, 0.20])
    produktalter = rng.integers(1, 121, zeilen)
    garantie = np.where(produktalter <= 24, "ja", "nein")
    fruehere_anfragen = rng.poisson(1.2, zeilen)
    beschreibung = rng.integers(40, 1201, zeilen)
    anhang = rng.choice(["ja", "nein"], zeilen, p=[0.4, 0.6])

    dauer = (
        2.0
        + pd.Series(fehlertyp).map(FEHLERTYP).to_numpy()
        + pd.Series(produktgruppe).map(PRODUKTGRUPPE).to_numpy()
        + pd.Series(eingangskanal).map(EINGANGSKANAL).to_numpy()
        + 0.025 * produktalter
        + 0.5 * fruehere_anfragen
        - 0.7 * (anhang == "ja")
        + rng.normal(0, 1.6, zeilen)
    )
    daten = pd.DataFrame({
        "anfrage_id": [f"A{nummer:04d}" for nummer in range(1, zeilen + 1)],
        "produktgruppe": produktgruppe,
        "eingangskanal": eingangskanal,
        "fehlertyp": fehlertyp,
        "produktalter_monate": produktalter.astype(float),
        "garantie": garantie,
        "fruehere_anfragen": fruehere_anfragen,
        "beschreibung_zeichen": beschreibung,
        "anhang_vorhanden": anhang,
        "bearbeitungsdauer_stunden": np.round(np.clip(dauer, 0.3, None), 1),
    })
    # Einige fehlende Angaben, wie sie in erfassten Daten vorkommen.
    daten.loc[rng.choice(zeilen, 18, replace=False), "produktalter_monate"] = np.nan
    daten.loc[rng.choice(zeilen, 12, replace=False), "eingangskanal"] = np.nan
    return daten


if __name__ == "__main__":
    ZIEL.parent.mkdir(parents=True, exist_ok=True)
    erzeuge().to_csv(ZIEL, index=False)
    print(f"{ZEILEN} Zeilen nach {ZIEL} geschrieben.")
