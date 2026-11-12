from pathlib import Path
from streamlit.testing.v1 import AppTest

def test_app_initial_run_and_repeat():
    app = AppTest.from_file(Path(__file__).resolve().parents[1] / "app.py").run(timeout=30)
    assert not app.exception
    app.button[0].click().run(timeout=30)
    assert not app.exception
    assert len(app.dataframe) == 2
    app.button[0].click().run(timeout=30)
    assert not app.exception
