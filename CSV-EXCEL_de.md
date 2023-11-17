**1) Datenabruf aus mehreren CSV-/EXCEL-Tabellen**

a) *Einfache Abfrage gleichnamiger Tabellenspalten aus mehreren EXCEL-Dateien:*

[XLSX_analysing-multiple-files.py](https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_analysing-multiple-files.py)

**Anwendungsfälle:**

- Identifikation von Zeitverläufen in Datensätzen
- Datenvergleich
- Datenbereinigung und Datennormalisierung

*Output-Beispiel für das obige Skript:*

[XLSX_multiple-files_sample-output.md](https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_multiple-files_sample-output.md)

b) *Skript für die Identifikation biographischer Ereignisse pro Person und ihre Sortierung nach Ereignis-Wert und Zeit:* 

[XLSX_select-and-sort-events.py](https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_select-and-sort-events.py)

**Anwendungsfälle:**

- experimentelle Rekonstruktion biographischer Abfolgen in Fällen, in denen viele Lebensereignissen keine oder nur vage Datierungen haben
- Errechnung möglicher Ereigniszeiträume auf Basis vorausgehender oder nachfolgender Ereignisse
- Zusammenführung identischer Ereignisse / Anpassung von Ereigniszeiträumen auf der Grundlage von Informationen aus verschiedenen Quellen

Die derzeitige Sortierung der Daten im Skript ist vier-stufig und beginnt mit der Ereignisklassifikation. Dies kann entsprechend im Code geändert werden.

```res_sorted=res_df.sort_values(by =['event_value','event_after-date','event_start','event_before-date',])``` 

c) *Relationship Tracer:*

[XSLX_relationship-tracer.py](https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_relationship-tracer.py)

**Anwendungsfälle:**

- Konsolidierung genealogischer Informationen aus der Spalte `rel_pers` in Factoid-Listen
- Rekonstruktion von Geschwisterbeziehungen basierend auf bekannten Eltern-Kind-Verbindungen
- Rekonstruktion von impliziten Großeltern-Enkel-Beziehungen

d) *Erweitertes Script zur Abfrage mehrerer Tabellenspalten aus mehreren EXCEL Dateien*

[Abfrage von ODER Bedingungen: XSLX_multiple-conditions_OR.py(https://github.com/ieg-dhr/DigiKAR/blob/main/XSLX_multiple-conditions_OR.py)

- Aus dem Standard-Ordner `DigiKAR_DATEN\\Python\\InputLists` werden alle dort abgelegten EXCEL-Dateien (in Factoid-Struktur) in einen gemeinsamen Dataframe gelesen.
- User kann für Personenname, Datum, Institution, Titel, Funktion und "related person" (Erweiterung auf andere Spalten jederzeit möglich) einen oder mehrere Suchbegriffe / Zeitangaben mit Komma getrennt eingeben.
- User kann wählen, ob nach konkreten Daten, Zeitraum oder "before" / "after" gesucht wird.
- Skript analysiert zuerst die Zeit und erstellt aus allen Matches im passenden Zeitraum einen neuen Dateframe, auf den via "numpy condition list" die übrigen Bedingungen angewandt werden. Je nach Condition-List-Operator werden die Bedingungen für die einzelnen Zellen mit "UND" oder mit "ODER" verbunden. Das Skript auf GITHUB behandelt nur "ODER". Im GUI soll es dann eine Auswahlmöglichkeit geben.
- Ergebnisse werden in eine neue Datei geschrieben, deren Name der User frei wählen kann und die auf DigiKAR_DATEN\\Python\\Results abgelegt wird.
- Das Zeit-Management verarbeitet sowohl "YYYY" als auch "YYYY-MM" und "YYYY-MM-DD" Eingaben verarbeitet, und das Skript berücksichtigt z.B. bei der Suche nach "before" und "after" auch die entsprechenden "before" und "after" Spalten.

**Anwendungsfälle:**

- Beispiel für die Erstellung komplexerer boolescher Abfragen über mehrere Tabellenkalkulationen hinweg
- Anpassung an verschiedene Tabellenformate möglich
- Experimentieren mit dem Parsen von Zeitangaben und potenziellen Problemen, die durch frühneuzeitliche Datumsangaben entstehen