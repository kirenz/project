# Geschäftsprozess und BPMN-Skizze

Arbeitsblatt. Die BPMN-Skizze ist ein verbindlicher Bestandteil des Projekts. Sie beschreibt einen selbst gewählten Geschäftsprozess, nicht den Aufbau des Python-Codes. Ein realistischer Ablauf genügt, beispielsweise Nachfrageplanung oder die Einschätzung von Bearbeitungszeiten. Ein realer Prozess oder Daten aus einem Unternehmen sind keine Voraussetzung.

## Mögliche Schrittfolge

1. Startereignis: Eine fachliche Frage und eine Entscheidungssituation liegen vor.
2. Aufgabe einer Person: Datenherkunft, Nutzungsrechte und Eignung prüfen.
3. Exklusives Gateway „Daten geeignet?“: „nein“ führt zur Klärung oder zum Ende, „ja“ zur Analyse.
4. Aufgabe des Systems: festgelegte Datenprüfung und Regressionsanalyse ausführen.
5. Aufgabe einer Person: Baseline, Fehler und Grenzen bewerten.
6. Exklusives Gateway „Ergebnis tragfähig?“: „nein“ führt zur dokumentierten Überarbeitung oder Nichtnutzung, „ja“ zur begründeten Empfehlung.
7. Endereignis: freigegebene Empfehlung oder dokumentierte Nichtnutzung.

Im BPMN-Modell Start- und Endereignis, Aufgaben und Gateways verwenden, die Wege beschriften und Mensch und System durch Lanes unterscheiden. Die bearbeitbare Quelle und eine exportierte Grafik in diesem Ordner ablegen. Ein Rückweg zur Überarbeitung erlaubt nicht, das Modell wiederholt an den Testdaten nachzujustieren.

## Regression im Prozess

Für den Schritt, den die Regression unterstützt, festhalten:

- Eingaben: Welche Angaben sind zum Zeitpunkt der Vorhersage bekannt?
- Ergebnis: Welche Größe wird in welcher Einheit vorhergesagt?
- Übergabe: Wer prüft das Ergebnis, und welche Entscheidung trifft diese Person?

## Fester Ablauf, KI-Schritt oder Agent

Drei Varianten abwägen und die Wahl aus dem Prozess begründen:

1. Fester Ablauf: Regressionspipeline und feste Regeln.
2. KI als fester Prozessschritt: ein klar begrenzter Schritt, etwa die Erläuterung eines geprüften Ergebnisses.
3. Agent: wählt abhängig von Zwischenergebnissen zwischen freigegebenen Werkzeugen.

Für jede Variante benennen: Nutzen, zusätzliche Risiken und die Stelle, an der ein Mensch entscheidet. Der begründete Verzicht auf einen Agenten ist ein vollständiges Ergebnis. Eine Umsetzung bleibt freiwillig, siehe `optional-adk.md`.
