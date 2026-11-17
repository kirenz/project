# Analyseprojekt

Data Analytics · WS 2026/27

Diese Vorlage verbindet Fragestellung, Daten und reproduzierbare Analyse. Die fachlichen Anforderungen stehen in der [Projektbeschreibung des Kurses](https://kirenz.github.io/data-analytics-ws2627/project-description.html). Termine und Prüfungsmodalitäten stehen im aktuellen Moodle-Kurs.

## Eigene Arbeitskopie

1. Auf GitHub „Use this template“ und „Create a new repository“ wählen.
2. Einen eigenen Repository-Namen vergeben und die Sichtbarkeit „Private“ wählen.
3. Das eigene Repository mit GitHub Desktop oder dem vorhandenen Git-Werkzeug klonen.
4. Ein Terminal im geklonten Projektordner öffnen.

## Python-Umgebung

Die Vorlage verwendet Python 3.14 und einen projektlokalen Notebook-Kernel.

Voraussetzung: [uv ist installiert](https://github.com/kirenz/uv-setup#installing-uv). Das Terminal befindet sich im Projektordner.

1. Die festgelegte Umgebung einrichten:

```bash
uv sync --locked
```

2. Den Kernel in dieser lokalen Umgebung einrichten:

```bash
uv run --locked python -m ipykernel install --sys-prefix --name data-analytics --display-name "Python 3.14 (Data Analytics)"
```

3. Jupyter Lab starten:

```bash
uv run --locked jupyter lab
```

4. Im Notebook den Kernel „Python 3.14 (Data Analytics)“ auswählen.

Prüfkriterium: `uv run --locked python --version` zeigt Python 3.14.

Die lokale Umgebung wird in `.venv` angelegt. `pyproject.toml` und `uv.lock` gehören zum Repository; `.venv` bleibt lokal.

## Regressionsbeispiel und Streamlit-Oberfläche

Die Vorlage enthält einen kleinen lauffähigen Regressionsablauf. Er sagt die Bearbeitungsdauer einer Serviceanfrage in Stunden vorher, vergleicht eine Mittelwert-Baseline mit einer Ridge-Regression und bewertet beide auf zurückgehaltenen Testdaten. Die Beispieldaten unter `data/beispiel/` sind synthetisch, also erfunden. Variablen und Erzeugung stehen in `data/beispiel/QUELLEN.md`. Als Kursbeispiel sind sie kein Projektdatensatz.

Voraussetzung: Die Python-Umgebung ist eingerichtet. Das Terminal befindet sich im Projektordner.

1. Den Analyseablauf im Terminal starten:

```bash
uv run --locked python -m analytics_project.run
```

2. Die Kennzahlen im Terminal mit `outputs/metrics.csv` vergleichen.
3. Die Oberfläche starten:

```bash
uv run --locked streamlit run app.py
```

4. Die angezeigte lokale Adresse im Browser öffnen und „Analyse starten“ wählen.
5. Die automatischen Prüfungen ausführen:

```bash
uv run --locked pytest
```

Prüfkriterium: Terminal und Oberfläche zeigen dieselben Kennzahlen für Baseline und Ridge. Alle Tests bestehen.

Für eine eigene CSV-Datei die Zielspalte und die Kennungsspalten angeben:

```bash
uv run --locked python -m analytics_project.run --csv data/raw/meine-daten.csv --target zielspalte --id-columns kennung
```

Der Ablauf verwendet einen zufälligen Split für unabhängige Beobachtungen ohne Zeitbezug. Numerische Merkmale werden mit dem Median ergänzt und skaliert. Kategoriale Merkmale werden mit dem häufigsten Wert ergänzt und in 0/1-Spalten umgewandelt (One-Hot-Kodierung). Diese Schritte und die Wahl des Parameters Alpha lernen nur aus den Trainingsdaten. Eine Textspalte mit mehr als 20 Ausprägungen führt zu einer Fehlermeldung: Kennungen gehören zu `--id-columns`, feine Kategorien werden fachlich zusammengefasst. Das Beispiel ist ein Ausgangspunkt und ersetzt keine eigene Analyse.

## Projekt beginnen

1. In dieser README den Projekttitel, die Fragestellung und die Teammitglieder ergänzen.
2. In `references/topic-ideas.ipynb` geeignete Daten und Fragen vergleichen.
3. In `references/project-proposal.ipynb` die ausgewählte Frage und den Analyseplan beschreiben.
4. Freigegebene Originaldaten in `data/raw/` ablegen und ihre Herkunft dokumentieren.
5. In `notebooks/draft-analysis.ipynb` Datenprüfung, Exploration und Modellierung entwickeln.
6. In `docs/prozessmodell.md` den Geschäftsprozess beschreiben und die BPMN-Skizze ablegen.
7. `src/analytics_project/` und `app.py` an die eigene Analyse anpassen.
8. In `reports/report.ipynb` Ergebnisse, Prüfung und Grenzen zusammenführen.
9. Den Kernel neu starten und den Bericht vollständig ausführen.

Prüfkriterium: Der Bericht läuft mit der dokumentierten Umgebung vollständig durch. Jede Schlussfolgerung lässt sich auf Daten und Berechnungen zurückführen.

## Projektstruktur

| Pfad | Inhalt |
|---|---|
| `data/raw/` | Unveränderte, für das Projekt freigegebene Originaldaten |
| `data/external/` | Ergänzende Daten aus externen Quellen |
| `data/interim/` | Zwischenstände der Aufbereitung |
| `data/processed/` | Aufbereitete Analysedaten |
| `notebooks/` | Entwicklung und Prüfung der Analyse |
| `references/` | Fragestellung, Datenbeschreibung und Quellen |
| `src/analytics_project/` | Analyseablauf: Datenprüfung, Split, Baseline, Regression, Bewertung |
| `app.py` | Streamlit-Oberfläche für den Analyseablauf |
| `tests/` | Automatische Prüfungen für Analyse und Oberfläche |
| `data/beispiel/` | Synthetische Beispieldaten mit Variablenverzeichnis |
| `scripts/` | Erzeugung der Beispieldaten mit festem Seed |
| `docs/prozessmodell.md` | Geschäftsprozess, BPMN-Skizze und Abwägung zum KI-Einsatz |
| `docs/optional-adk.md` | Hinweise zu einer freiwilligen Agenten-Erweiterung |
| `models/` | Gespeicherte Modelle |
| `reports/` | Ergebnisbericht und Präsentation |
| `pyproject.toml`, `uv.lock` | Pakete und festgelegte Versionen |

Notebooks in Unterordnern verwenden Pfade relativ zu ihrem Speicherort, beispielsweise `../data/raw/`. Benötigte zusätzliche Pakete mit uv ergänzen und `pyproject.toml` sowie `uv.lock` gemeinsam committen.

Die vorhandene Umgebung deckt die Kursbeispiele ab. Die Eignung zusätzlicher Pakete richtet sich nach der gewählten Analyse. Quelldaten werden nicht überschrieben. Zugangsdaten und vertrauliche Daten ohne Freigabe gehören nicht in Git.

## Einsatz von Coding-Agenten

Bei zulässigem KI-Einsatz im Projekt dokumentieren, welche Schritte übernommen wurden und wie sie geprüft wurden. Ergebnisse anhand der Daten unabhängig nachrechnen. Die Regeln für den Agenten stehen in `AGENTS.md`. Das BPMN-Prozessmodell zeigt Zuständigkeiten, Übergaben und den Schritt, an dem eine Person das Ergebnis prüft.
