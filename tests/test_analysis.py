import numpy as np
import pytest

from analytics_project.analysis import DEMO_ID_COLUMNS, DEMO_TARGET, analyze, demo_data, validate


def test_reproducible_baseline_and_holdout():
    a, b = analyze(demo_data()), analyze(demo_data())
    assert a.train_rows + a.test_rows == 600
    assert a.test_rows == 120
    assert a.metrics.equals(b.metrics)
    assert np.isfinite(a.metrics[["MAE", "RMSE", "R2"]]).all().all()
    assert a.predictions["Baseline (Trainingsmittelwert)"].nunique() == 1


def test_numeric_and_categorical_predictors_are_used():
    quality = analyze(demo_data()).quality
    assert quality["numeric_predictors"] == 3
    assert quality["categorical_predictors"] == 5
    assert quality["missing_predictor_cells"] == 30


def test_only_numeric_predictors_work():
    data = demo_data().select_dtypes("number")
    assert analyze(data, id_columns=()).quality["categorical_predictors"] == 0


@pytest.mark.parametrize("kind", ["missing_target", "constant_target", "text_target", "infinity", "duplicate",
                                  "empty_feature", "id_as_predictor", "missing_id_column"])
def test_invalid_data_rejected(kind):
    data, id_columns = demo_data(), DEMO_ID_COLUMNS
    if kind == "missing_target": data.loc[0, DEMO_TARGET] = np.nan
    if kind == "constant_target": data[DEMO_TARGET] = 1.0
    if kind == "text_target": data[DEMO_TARGET] = "lang"
    if kind == "infinity": data.loc[0, "produktalter_monate"] = np.inf
    if kind == "duplicate": data.loc[1] = data.loc[0]
    if kind == "empty_feature": data["fehlertyp"] = np.nan
    if kind == "id_as_predictor": id_columns = ()
    if kind == "missing_id_column": id_columns = ("gibt_es_nicht",)
    with pytest.raises(ValueError):
        validate(data, DEMO_TARGET, id_columns)
