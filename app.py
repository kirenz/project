"""Lokale Oberfläche für den festen Analyseablauf. Keine Uploads an KI-Dienste, keine automatische Entscheidung."""
import streamlit as st

from analytics_project.analysis import DEMO_TARGET, analyze, demo_data

st.set_page_config(page_title="Regression nachvollziehen", layout="centered")
st.title("Regression nachvollziehen")
st.warning("Lehrbeispiel mit synthetischen Serviceanfragen. Die Daten sind erfunden und kein Projektdatensatz.")
st.write(
    "Ein fester Ablauf sagt die Bearbeitungsdauer einer Serviceanfrage in Stunden vorher. "
    "Er vergleicht eine Mittelwert-Baseline mit einer Ridge-Regression. "
    "Die Testdaten werden nicht für die Modellwahl verwendet."
)
with st.expander("Daten und Grenzen"):
    st.dataframe(demo_data().head())
    st.write(
        f"600 erfundene Anfragen, Zielvariable `{DEMO_TARGET}`. Verwendet werden nur Angaben, "
        "die beim Eingang einer Anfrage bekannt sind. Die Kennung `anfrage_id` ist kein Prädiktor. "
        "Variablen und Erzeugung: `data/beispiel/QUELLEN.md`."
    )
if st.button("Analyse starten", type="primary"):
    try:
        st.session_state["result"] = analyze(demo_data())
    except ValueError as error:
        st.error(str(error))
if "result" in st.session_state:
    result = st.session_state["result"]
    st.subheader("Ergebnis auf zurückgehaltenen Testdaten")
    st.dataframe(result.metrics, hide_index=True)
    st.caption(
        f"Training: {result.train_rows} Anfragen, Test: {result.test_rows} Anfragen. MAE und RMSE in Stunden. "
        f"Alpha per 5-facher Kreuzvalidierung nur im Training gewählt: {result.selected_alpha}."
    )
    st.scatter_chart(result.predictions, x="actual", y="Ridge",
                     x_label="Beobachtete Dauer (Stunden)", y_label="Vorhergesagte Dauer (Stunden)")
    st.download_button("Kennzahlen herunterladen", result.metrics.to_csv(index=False), "metrics.csv", "text/csv")
    st.info(
        "Menschliche Prüfung: Die Vorhersage ist eine Einschätzung. Das Serviceteam ordnet die Fehlergröße "
        "fachlich ein und entscheidet über die Bearbeitung."
    )
