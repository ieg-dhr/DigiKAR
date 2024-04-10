## Ersetzen von Daten basierend auf Ontologielisten

[XLSX_replace_values_via_mapping.py](https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_replace_values_via_mapping.py)

### Anwendungsfälle

- Ersetzen von Zellwerten in EXCEL Dateien basierend auf Daten-Mapping in einer separaten CSV Datei
- Ergänzen von Zellwerten in ausgewählten Fällen
- Datenbereinigung und Normalisierung

### Beispiel für Datenmapping

|event_name               |event_type       |
|-------------------------|-----------------|
|Akademische Laufbahn     |Funktionsausübung|
|Aufnahme in eine Fakultät|Rezeption        |
|Auslandsaufenthalt       |Reise            |
|Berufliche Tätigkeit     |Funktionsausübung|
|Berufung                 |Vokation         |

In diesem Beispiel steht "event_name" für die Bezeichnung in der Eingabedatei, die ersetzt werden soll. Die neue Bezeichnung steht in "event_type".
Diese Beziehung zwischen den Daten wird in zwei Spalten einer CSV-Datei dargestellt, die das Skript Eintrag für Eintrag auswertet.
