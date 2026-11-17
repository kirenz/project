# Freiwillige Erweiterung: Agent mit Google ADK

Die Vorlage enthält keinen Agenten und benötigt keinen API-Schlüssel. Ein Agent ist keine Voraussetzung für das Projekt.

Ein möglicher Agent erläutert bereits berechnete Kennzahlen oder wählt unter wenigen freigegebenen Analysefunktionen. Der Python-Ablauf bleibt ohne Agent ausführbar und testbar. Der Agent erfindet keine Kennzahlen, verwendet Testdaten nicht zur Modellwahl und ersetzt keine menschliche Entscheidung.

Vor einer Umsetzung festlegen:

1. Den konkreten Zusatznutzen gegenüber dem festen Ablauf.
2. Die erlaubten Werkzeuge und Eingaben.
3. Die Abbruchbedingungen und die menschliche Freigabe.
4. Einen Prüffall für den Normalfall und einen für fehlende Daten.

API-Schlüssel nur lokal als Umgebungsvariable speichern, nie im Repository. Nur freigegebene, nicht vertrauliche Daten an einen Modellanbieter senden. Die Einrichtung beschreibt das Kursmaterial [Agents mit Google ADK](https://kirenz.github.io/data-analytics-ws2627/agents.html).
