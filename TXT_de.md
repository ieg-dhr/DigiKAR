**2) Extrahieren strukturierter Informationen aus TXT Dateien**

a) [TXT_replaceWORDwithREGEX.py](https://github.com/ieg-dhr/DigiKAR/blob/main/TXT_replaceWORDwithREGEX.py) 

- Trennzeichen nach "regular expression" in Text einfügen
- Vorbereitung des Texts für Aufteilung in einzelne Abschnitte

b) [TXT_splitUPPERCASE.py](https://github.com/ieg-dhr/DigiKAR/blob/main/TXT_splitUPPERCASE.py)

- Identifizierung von Personeneinträgen durch Großschreibung der Namen

c) [UniversityRecordsMainz_identifyPLACEofORIGIN.py](https://github.com/ieg-dhr/DigiKAR/blob/main/UniversityRecordsMainz_identifyPLACEofORIGIN.py)

- Identifizierung der Herkunftsorte aufgrund der Tokenposition im Text
- Beispielergebnis des Skripts für die Mainzer Universitätsmatrikel:
[UniversityRecordsMainz_output_place-names.txt](https://github.com/ieg-dhr/DigiKAR/blob/main/UniversityRecordsMainz_output_place-names.txt)

d) [TransferPROFData](https://github.com/ieg-dhr/DigiKAR/blob/main/JupyterNotebooks_DigiKAR/TransferPROFData.ipynb)

- Übertragung der semi-strukturierten Textdaten, die via OCR aus den mit Schreibmaschine erstellten Mainzer Universitätsmatrikeln extrahiert wurden
- Aufteilen der Information in Name, Information und Quellenangabe
- Weitere Verfeinerung der Eintrage durch Abgleichen der "Information" mit Ontologielisten
- Identifikation von Ereignisbezeichnungen, Titeln, Funktionen, Ortsnamen und Daten

<hr>

<img src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Kurmainzische_Wappentafel_1750.jpg" alt="drawing" width="150" style="padding:10px" align="left"/>
<p><strong></strong>Der folgende Blogpost beschreibt die Verwendung einiger oben genannter Skripte im Arbeitspaket "Kurmainz":<br>
<a href="https://insulae.hypotheses.org/333">Monika Barget, "Disambiguating people and places in dirty historical data," in INSULAE, last updated 26/10/2021</a>

<hr>
