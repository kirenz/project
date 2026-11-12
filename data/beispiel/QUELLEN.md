# Beispieldaten: Serviceanfragen (synthetisch)

`serviceanfragen-synthetisch.csv` ist ein erfundener Datensatz für das Lehrbeispiel der Vorlage. Er beschreibt keine realen Anfragen, Personen oder Unternehmen. Aussagen über echte Serviceprozesse lassen sich daraus nicht ableiten.

- Erzeugung: `scripts/erzeuge_beispieldaten.py`, Zufallsseed 2627, erstellt am 12.11.2026.
- Umfang: 600 Zeilen, 10 Spalten. Eine Zeile entspricht einer abgeschlossenen Serviceanfrage.
- Nutzung: frei für die Arbeit in diesem Kurs. Als Kursbeispiel ist der Datensatz kein zulässiger Projektdatensatz.
- Fehlende Werte: 18 in `produktalter_monate`, 12 in `eingangskanal`. Sie sind absichtlich enthalten.

| Variable | Bedeutung | Einheit oder Ausprägungen | Rolle | Beim Eingang bekannt |
|---|---|---|---|---|
| `anfrage_id` | Kennung der Anfrage | Text | Kennung | ja |
| `produktgruppe` | Produktgruppe des Geräts | Haushalt, Garten, Gewerbe | Prädiktor | ja |
| `eingangskanal` | Kanal, über den die Anfrage einging | Portal, E-Mail, Telefon | Prädiktor | ja |
| `fehlertyp` | Gemeldeter Fehlertyp | Bedienung, Software, Verschleiss, Elektronik | Prädiktor | ja |
| `produktalter_monate` | Alter des Geräts | Monate | Prädiktor | ja |
| `garantie` | Gerät innerhalb der Garantie (bis 24 Monate) | ja, nein | Prädiktor | ja |
| `fruehere_anfragen` | Zahl früherer Anfragen zum selben Gerät | Anzahl | Prädiktor | ja |
| `beschreibung_zeichen` | Länge der Fehlerbeschreibung | Zeichen | Prädiktor | ja |
| `anhang_vorhanden` | Foto oder Dokument beigefügt | ja, nein | Prädiktor | ja |
| `bearbeitungsdauer_stunden` | Aktive Bearbeitungsdauer bis zum Abschluss | Stunden | Zielvariable | nein |

`garantie` wird aus `produktalter_monate` abgeleitet und ist damit eine zweite Darstellung desselben Merkmals. `beschreibung_zeichen` hat in den erzeugten Daten keinen Einfluss auf die Dauer. Beide Eigenschaften sind absichtlich enthalten, damit die Auswahl von Prädiktoren begründet werden muss.
