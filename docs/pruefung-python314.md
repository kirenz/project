# Prüfung der Projektvorlage mit Python 3.14

Stand: 07.11.2026. Ausschließlich lokal, kein Push oder Deployment.

Python 3.14.9, pandas 2.3.3, NumPy 2.5.4, Altair 6.3.0; vollständige Paketauflösung in uv.lock. uv sync --locked und projektlokale Kernelregistrierung erfolgreich.

Alle vier Projekt-Notebooks wurden mit nbformat validiert und in temporären Kopien über den tatsächlichen data-analytics-Kernel ausgeführt. Die Codezellen sind leere Arbeitsbereiche. Dieser Lauf prüft das ausführbare Notebookgerüst, nicht eine später ausgefüllte Analyse.

Ein unabhängiges temporäres Prüfnotebook testete im selben Kernel Python-Version, pandas-/NumPy-/Altair-Imports, Excel-Schreiben und -Lesen mit openpyxl, lineare Regression mit RMSE-Gegenprüfung, Altair-Spezifikation und Matplotlib-Grafik. Alle Prüfungen bestanden. Altair 5.5 scheiterte zunächst unter Python 3.14 beim Import; Altair 6.3.0 behebt den Konflikt.

Der automatisierte Vergleich mit dem vorigen Stand bestätigt: sämtliche Zellen, Aufgabenstellungen und leeren Codefelder bleiben unverändert. Keine gespeicherten Ausgaben oder Ausführungszähler. Nur Notebook-Metadaten und die Einrichtung wurden angepasst. Es wurden keine fachlichen Projektlösungen ergänzt.

Die Anleitung ist für macOS und Windows PowerShell formuliert. Praktische Kerneltests liefen auf macOS; Windows wurde nicht ausgeführt.
