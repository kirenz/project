# Regeln für Coding-Agenten

Im Projekt übernimmt der Agent Analyseschritte. Das Team prüft jedes Ergebnis fachlich und verantwortet die Schlussfolgerungen.

- `data/raw/` unverändert lassen. Aufbereitete Daten unter `data/interim/` oder `data/processed/` speichern und den Aufbereitungsschritt im Notebook nachvollziehbar halten.
- Nur den beauftragten Analyseschritt bearbeiten. Vorhandene Ergebnisse und Texte des Teams erhalten.
- Beobachtungseinheit, Auswahl, Zähler, Nenner und Einheiten ausdrücklich prüfen.
- Code mit der vorhandenen uv-Umgebung ausführen. Neue Pakete nach Rückfrage mit `uv add` ergänzen, sodass `pyproject.toml` und `uv.lock` zusammen geändert werden.
- Pfade relativ zum Notebook angeben, etwa `../data/raw/`.
- Berechnete Ergebnisse von Annahmen trennen. Fehlende Werte als fehlend erhalten.
- Korrelation und Kausalität sowie Modellanpassung und Vorhersagequalität getrennt darstellen.
- Geänderte Dateien und Prüfergebnisse am Ende berichten, damit das Team sie gegenrechnen kann.
- Zugangsdaten und vertrauliche Daten bleiben außerhalb des Repositorys. Daten nur auf ausdrücklichen Auftrag hochladen oder veröffentlichen.
