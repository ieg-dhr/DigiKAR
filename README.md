<img src="https://github.com/ieg-dhr/DigiKAR/blob/main/DigiKAR_logo-small.png" alt="drawing" width="200" style="padding=10px" align="left"/>

# DigiKAR

### Skripte zur Bearbeitung von Ortsdaten und biographischen Angaben im DigiKAR Projekt / scripts for managing spatial and biographic data in the DigiKAR project

<hr>

**1) Datenabruf aus mehreren CSV-/EXCEL-Tabellen / data retrieval from several CSV/EXCEL tables**

a) [XLSX_analysing-multiple-files.py](https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_analysing-multiple-files.py) 

b) [XLSX_multiple-files_sample-output.md](https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_multiple-files_sample-output.md)

- Identifikation von Zeitverläufen in Datensätzen / identifying chonologies in data sets
- Datenvergleich / data comparison
- Datenbereinigung und Datennormalisierung / data cleanign and data normalisation

c) Erweitertes Script zur Abfrage mehrerer Tabellenspalten aus mehreren EXCEL Dateien / advanced script to query several columns across several spreadsheets based on user input:

- Aus dem Standard-Ordner DigiKAR_DATEN\\Python\\InputLists werden alle dort abgelegten EXCEL-Dateien (in Factoid-Struktur) in einen gemeinsamen Dataframe gelesen. / Files from directory DigiKAR_DATEN\\Python\\InputLists are read to a single dataframe.

- User kann für Personenname, Datum, Institution, Titel, Funktion und "related person" (Erweiterung auf andere Spalten jederzeit möglich) einen oder mehrere Suchbegriffe / Zeitangaben mit Komma getrennt eingeben. / User can select search criteria for person name, date, institution, person title, function and related person. Several keywords per field are accepted.

- User kann wählen, ob nach konkreten Daten, Zeitraum oder "before" / "after" gesucht wird. / User can decide whether to search for exact dates, a date range or "before" and "after" dates.

- Skript analysiert zuerst die Zeit und erstellt aus allen Matches im passenden Zeitraum einen neuen Dateframe, auf den via "numpy condition list" die übrigen Bedingungen angewandt werden. Je nach Condition-List-Operator werden die Bedingungen für die einzelnen Zellen mit "UND" oder mit "ODER" verbunden. Das Skript auf GITHUB behandelt nur "ODER". Im GUI soll es dann eine Auswahlmöglichkeit geben. / Script handles time input first and writes matches to new data frame, then conditions for remaining fields are applied. Current version of script apply OR operator to the fields. In final GUI version, user will be able to select both AND or OR operations.

- Ergebnisse werden in eine neue Datei geschrieben, deren Name der User frei wählen kann und die auf DigiKAR_DATEN\\Python\\Results abgelegt wird. / Results are written to new file. User is free to assign file name via script input.

- Das Zeit-Management verarbeitet sowohl "YYYY" als auch "YYYY-MM" und "YYYY-MM-DD" Eingaben verarbeitet, und das Skript berücksichtigt z.B. bei der Suche nach "before" und "after" auch die entsprechenden "before" und "after" Spalten. / Time management handles "YYYY" as well as "YYYY-MM" and "YYYY-MM-DD" inputs. Searching for dates before and after input date, the "before" and "after" columns in the original spreadsheet are consider alongside start and end dates.

c) *Erweiterte Skripe in Bearbeitung / advanced scripts in progress:*

- "BIOGRAPHY TRACING": select person by ID, match name variants, find all life events recorded, narrow down events by time limits if necessary, put events in chronological order
- "DISAMBIGUATION": script to compare similar names of people and places and assign unique IDs (human intervention necessary), e.g. using Python's fuzzy wuzzy package.
- "SPATIAL EVOLUTION": extracts events coinciding in specific places, reconstruct political / cultural role of places through human agency

<hr>

**2) Extrahieren strukturierter Informationen aus TXT Dateien / extracting structured information from TXT files**

a) [TXT_replaceWORDwithREGEX.py](https://github.com/ieg-dhr/DigiKAR/blob/main/TXT_replaceWORDwithREGEX.py) 

- Trennzeichen nach "regular expression" in Text einfügen / adding delimiters to text based on regular expression
- Vorbereitung des Texts für Aufteilung in einzelne Abschnitte / preparing text for splitting into individual sections

b) [TXT_splitUPPERCASE.py](https://github.com/ieg-dhr/DigiKAR/blob/main/TXT_splitUPPERCASE.py)

- Identifizierung von Personeneinträgen durch Großschreibung der Namen / identifiying person entries based on uppercase characters in names

c) [UniversityRecordsMainz_identifyPLACEofORIGIN.py](https://github.com/ieg-dhr/DigiKAR/blob/main/UniversityRecordsMainz_identifyPLACEofORIGIN.py)

- Identifizierung der Herkunftsorte aufgrund der Tokenposition im Text / identifying places of origin according to token position in text
- Beispielergebnis des Skripts für die Mainzer Universitätsmatrikel / sample output of script for the Mainz university records: 

[UniversityRecordsMainz_output_place-names.txt](https://github.com/ieg-dhr/DigiKAR/blob/main/UniversityRecordsMainz_output_place-names.txt)

<img src="https://insulae.hypotheses.org/files/2021/10/INSULAE_featured-images_biographic-data-980x450.png" alt="drawing" width="250" align="left"/>

<hr>

**Ausführliche Beschreibung des Worksflows / detailed workflow description**

Der folgenden Blogpost beschreibt die Verwendung der oben genannten Skripte im Arbeitspaket "Kurmainz": / The following blog post describes the application of the above-mentioned scripts in the "Kurmainz" work package:

[Monika Barget, "Disambiguating people and places in dirty historical data," in INSULAE, last updated 26/10/2021](https://insulae.hypotheses.org/333)

<hr>

**Verantwortlich für den Inhalt / responsible for content:**

[Monika Barget](https://github.com/MonikaBarget)

*Digitale Kartenwerkstatt Altes Reich (DigiKAR) – Daten & Transfer* 

Leibniz-Institut für Europäische Geschichte (IEG) 
Alte Universitätsstraße 19 
55116 Mainz 

[DigiKAR on Twitter](https://twitter.com/digi_KAR)






