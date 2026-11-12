"""Fester Analyseablauf der Vorlage: Daten prüfen, aufteilen, Baseline und Regression vergleichen.

Der Ablauf braucht keine externen Dienste. Die Beispieldaten sind synthetisch
(siehe data/beispiel/QUELLEN.md) und kein Projektdatensatz.
"""
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error
from sklearn.model_selection import GridSearchCV, KFold, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

DEMO_PATH = Path(__file__).resolve().parents[2] / "data" / "beispiel" / "serviceanfragen-synthetisch.csv"
DEMO_TARGET = "bearbeitungsdauer_stunden"
DEMO_ID_COLUMNS = ("anfrage_id",)
MAX_CATEGORIES = 20


@dataclass
class Result:
    metrics: pd.DataFrame
    predictions: pd.DataFrame
    quality: dict
    selected_alpha: float
    train_rows: int
    test_rows: int


def demo_data():
    """Synthetische Serviceanfragen. Lehrbeispiel, kein Projektdatensatz."""
    return pd.read_csv(DEMO_PATH)


def split_columns(data, target, id_columns=()):
    """Teilt die Prädiktoren in numerische und kategoriale Spalten."""
    predictors = data.drop(columns=[target, *id_columns])
    numeric = [c for c in predictors if pd.api.types.is_numeric_dtype(predictors[c])]
    categorical = [c for c in predictors if c not in numeric]
    return numeric, categorical


def validate(data, target, id_columns=()):
    """Prüft die Daten vor der Analyse und meldet Probleme als ValueError."""
    if data.columns.duplicated().any():
        raise ValueError("Spaltennamen müssen eindeutig sein.")
    if target not in data:
        raise ValueError("Zielspalte fehlt.")
    missing_ids = [c for c in id_columns if c not in data]
    if missing_ids:
        raise ValueError(f"Kennungsspalte fehlt: {', '.join(missing_ids)}.")
    if len(data) < 30:
        raise ValueError("Mindestens 30 Zeilen für diesen technischen Ablauf erforderlich. Die Projektvorgaben verlangen mehr.")
    if data.duplicated().any():
        raise ValueError("Identische Zeilen gefunden. Duplikate und Beobachtungseinheit vor dem Split fachlich klären.")
    if not pd.api.types.is_numeric_dtype(data[target]):
        raise ValueError("Die Zielspalte muss numerisch sein.")
    if data[target].isna().any() or data[target].nunique() < 2:
        raise ValueError("Zielwerte müssen vollständig und veränderlich sein.")

    numeric, categorical = split_columns(data, target, id_columns)
    if not numeric and not categorical:
        raise ValueError("Mindestens ein Prädiktor erforderlich.")
    numeric_values = data[[target, *numeric]].to_numpy(dtype=float)
    if np.isinf(numeric_values).any():
        raise ValueError("Unendliche Werte sind nicht zulässig.")
    predictors = data[[*numeric, *categorical]]
    if predictors.isna().all().any():
        raise ValueError("Keine vollständig leeren Prädiktoren.")
    for column in categorical:
        if data[column].nunique() > MAX_CATEGORIES:
            raise ValueError(
                f"Spalte '{column}' hat mehr als {MAX_CATEGORIES} Ausprägungen. "
                "Kennungen als Kennungsspalte angeben; Freitext und feine Kategorien fachlich zusammenfassen."
            )
    return {"rows": len(data), "numeric_predictors": len(numeric),
            "categorical_predictors": len(categorical),
            "missing_predictor_cells": int(predictors.isna().sum().sum())}


def build_pipeline(numeric, categorical):
    """Aufbereitung und Modell in einer Pipeline: Alle Schritte lernen nur aus den Trainingsdaten."""
    numeric_steps = Pipeline([("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())])
    categorical_steps = Pipeline([("impute", SimpleImputer(strategy="most_frequent")),
                                  ("encode", OneHotEncoder(handle_unknown="ignore"))])
    preparation = ColumnTransformer([("numeric", numeric_steps, numeric),
                                     ("categorical", categorical_steps, categorical)])
    return Pipeline([("prepare", preparation), ("ridge", Ridge())])


def analyze(data, target=DEMO_TARGET, id_columns=DEMO_ID_COLUMNS, seed=42):
    quality = validate(data, target, id_columns)
    numeric, categorical = split_columns(data, target, id_columns)
    X, y = data[[*numeric, *categorical]], data[target]
    # Zufälliger Split: nur für unabhängige Beobachtungen ohne Zeitbezug geeignet.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)
    if X_train.isna().all().any():
        raise ValueError("Ein Prädiktor ist im Trainingssatz vollständig leer.")
    # Alpha wird per Kreuzvalidierung nur im Training gewählt. Die Testdaten bleiben unberührt.
    search = GridSearchCV(build_pipeline(numeric, categorical), {"ridge__alpha": [0.1, 1.0, 10.0, 100.0]},
                          scoring="neg_mean_absolute_error",
                          cv=KFold(5, shuffle=True, random_state=seed))
    search.fit(X_train, y_train)
    baseline = DummyRegressor(strategy="mean").fit(X_train, y_train)
    rows, predictions = [], {"actual": y_test.to_numpy()}
    for name, model in [("Baseline (Trainingsmittelwert)", baseline), ("Ridge", search)]:
        pred = model.predict(X_test)
        rows.append({"model": name, "MAE": mean_absolute_error(y_test, pred),
                     "RMSE": root_mean_squared_error(y_test, pred), "R2": r2_score(y_test, pred)})
        predictions[name] = pred
    return Result(pd.DataFrame(rows), pd.DataFrame(predictions), quality,
                  float(search.best_params_["ridge__alpha"]), len(X_train), len(X_test))
