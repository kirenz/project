# Prüfung: Regressionsbeispiel und Streamlit-Oberfläche

Stand: 12.11.2026. Ausschließlich lokal in einer temporären Kopie, kein Push.

macOS, Python 3.14.10, uv 0.12.19. `uv sync --locked` erfolgreich. Lockversionen: pandas 2.3.3, scikit-learn 1.9.1, Streamlit 1.67.0, pytest 9.2.0.

- `uv run --locked pytest`: 12 Tests bestanden (reproduzierbare Analyse und Baseline, numerische und kategoriale Prädiktoren mit fehlenden Werten, Lauf nur mit numerischen Prädiktoren, acht ungültige Datenfälle, Start und wiederholter Lauf der Oberfläche über AppTest).
- `uv run --locked python -m analytics_project.run`: Baseline MAE 2,24 Stunden, RMSE 2,77, R² −0,01; Ridge MAE 1,25 Stunden, RMSE 1,60, R² 0,66; 480 Trainings- und 120 Testfälle, Alpha 1,0. Ergebnis auf synthetischen Daten, keine Zielvorgabe.
- Aufruf mit `--csv`, `--target` und `--id-columns` auf der Beispieldatei: dieselben Kennzahlen. Ohne `--id-columns` bricht der Lauf mit einer verständlichen Meldung zur Kennungsspalte ab.
- `scripts/erzeuge_beispieldaten.py` erzeugt bei erneutem Lauf eine identische Datei.
- `uv run --locked streamlit run app.py`: Seite im Browser geöffnet, „Analyse starten“ gewählt. Die Tabelle zeigt dieselben Kennzahlen wie der Terminallauf.
- Alle vier Notebooks mit nbformat validiert und über den projektlokalen Kernel `data-analytics` ausgeführt. Die Codezellen sind weiterhin leere Arbeitsbereiche.

Nicht geprüft: Windows, der Weg ohne uv, eine fremde CSV-Datei mit anderen Datentypen (etwa Datumsspalten).
