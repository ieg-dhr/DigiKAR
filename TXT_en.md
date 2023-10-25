**2) Extracting structured information from TXT files**

a) [TXT_replaceWORDwithREGEX.py](https://github.com/ieg-dhr/DigiKAR/blob/main/TXT_replaceWORDwithREGEX.py) 

- adding delimiters to text based on regular expression
- preparing text for splitting into individual sections

b) [TXT_splitUPPERCASE.py](https://github.com/ieg-dhr/DigiKAR/blob/main/TXT_splitUPPERCASE.py)

- identifiying person entries based on uppercase characters in names

c) [UniversityRecordsMainz_identifyPLACEofORIGIN.py](https://github.com/ieg-dhr/DigiKAR/blob/main/UniversityRecordsMainz_identifyPLACEofORIGIN.py)

- identifying places of origin according to token position in text
- sample output of script for the Mainz university records: 
[UniversityRecordsMainz_output_place-names.txt](https://github.com/ieg-dhr/DigiKAR/blob/main/UniversityRecordsMainz_output_place-names.txt)

d) [TransferPROFData](https://github.com/ieg-dhr/DigiKAR/blob/main/JupyterNotebooks_DigiKAR/TransferPROFData.ipynb)

- Transfer of semi-structured text data extracted via OCR from the Mainz university registers (originally written with a typewriter) to EXCEL
- Splitting the information into "name", "information" and "source citation" columns
- Further refinement of the entries by matching the "information" with ontology lists
- Identification of event names, titles, functions, place names and dates

<hr>

<img src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Kurmainzische_Wappentafel_1750.jpg" alt="drawing" width="150" style="padding:10px" align="left"/>
The following blog post describes the application of some of the above-mentioned scripts in the "Kurmainz" work package:<br>
<a href="https://insulae.hypotheses.org/333">Monika Barget, "Disambiguating people and places in dirty historical data," in INSULAE, last updated 26/10/2021</a>

<hr>
