**1) Datenabruf aus mehreren CSV-/EXCEL-Tabellen / data retrieval from several CSV/EXCEL tables**

a) *Einfache Abfrage gleichnamiger Tabellenspalten aus mehreren EXCEL-Dateien / simple analysis of table columns with identical labels from several EXCEL files:*

<a href="https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_analysing-multiple-files.py">XLSX_analysing-multiple-files.py</a> 

**Use cases:**

- Identifikation von Zeitverläufen in Datensätzen / identifying chonologies in data sets
- Datenvergleich / data comparison 
- Datenbereinigung und Datennormalisierung / data cleanign and data normalisation

* Output-Beispiel für das obige Skript / sample output for the above-mentioned script:*

<a href="https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_multiple-files_sample-output.md">XLSX_multiple-files_sample-output.md</a> 

b) *Skript für die Identifikation biographischer Ereignisse pro Person und ihre Sortierung nach Ereignis-Wert und Zeit / script for identifying biographic events per person and sorting them by event-value and date:* 

<a href="https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_select-and-sort-events.py">XLSX_select-and-sort-events.py</a> 

**Use case:**

- experimentelle Rekonstruktion biographischer Abfolgen in Fällen, in denen viele Lebensereignissen keine oder nur vage Datierungen haben / experimental reconstruction of biographic chronologies in cases where a lot of events have no or vague dating
- Errechnung möglicher Ereigniszeiträume auf Basis vorausgehender oder nachfolgender Ereignisse / calculation of possible event time frames based on previous or following events

Die derzeitige Sortierung der Daten im Skript ist vier-stufig und beginnt mit der Ereignisklassifikation. Dies kann entsprechend im Code geändert werden. / The current sorting is four-fold and starts with the event classification. This can be adjusted in the code.

```res_sorted=res_df.sort_values(by =['event_value','event_after-date','event_start','event_before-date',])``` 

c) *Erweitertes Script zur Abfrage mehrerer Tabellenspalten aus mehreren EXCEL Dateien / advanced script to query several columns across several spreadsheets based on user input:* https://github.com/ieg-dhr/DigiKAR/blob/main/XSLX_multiple-conditions_OR.py

- Aus dem Standard-Ordner DigiKAR_DATEN\\Python\\InputLists werden alle dort abgelegten EXCEL-Dateien (in Factoid-Struktur) in einen gemeinsamen Dataframe gelesen. / Files from directory DigiKAR_DATEN\\Python\\InputLists are read to a single dataframe.

- User kann für Personenname, Datum, Institution, Titel, Funktion und "related person" (Erweiterung auf andere Spalten jederzeit möglich) einen oder mehrere Suchbegriffe / Zeitangaben mit Komma getrennt eingeben. / User can select search criteria for person name, date, institution, person title, function and related person. Several keywords per field are accepted.

- User kann wählen, ob nach konkreten Daten, Zeitraum oder "before" / "after" gesucht wird. / User can decide whether to search for exact dates, a date range or "before" and "after" dates.

- Skript analysiert zuerst die Zeit und erstellt aus allen Matches im passenden Zeitraum einen neuen Dateframe, auf den via "numpy condition list" die übrigen Bedingungen angewandt werden. Je nach Condition-List-Operator werden die Bedingungen für die einzelnen Zellen mit "UND" oder mit "ODER" verbunden. Das Skript auf GITHUB behandelt nur "ODER". Im GUI soll es dann eine Auswahlmöglichkeit geben. / Script handles time input first and writes matches to new data frame, then conditions for remaining fields are applied. Current version of script apply OR operator to the fields. In final GUI version, user will be able to select both AND or OR operations.

- Ergebnisse werden in eine neue Datei geschrieben, deren Name der User frei wählen kann und die auf DigiKAR_DATEN\\Python\\Results abgelegt wird. / Results are written to new file. User is free to assign file name via script input.

- Das Zeit-Management verarbeitet sowohl "YYYY" als auch "YYYY-MM" und "YYYY-MM-DD" Eingaben verarbeitet, und das Skript berücksichtigt z.B. bei der Suche nach "before" und "after" auch die entsprechenden "before" und "after" Spalten. / Time management handles "YYYY" as well as "YYYY-MM" and "YYYY-MM-DD" inputs. Searching for dates before and after input date, the "before" and "after" columns in the original spreadsheet are consider alongside start and end dates.


