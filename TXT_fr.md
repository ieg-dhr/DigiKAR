## 2) Extraction d'informations structurées à partir de fichiers TXT

### a) [TXT_replaceWORDwithREGEX.py](https://github.com/ieg-dhr/DigiKAR/blob/main/TXT_replaceWORDwithREGEX.py)

- ajout de délimiteurs au texte en fonction d'une expression régulière
- préparation du texte pour la découpe en sections individuelles

### b) [TXT_splitUPPERCASE.py](https://github.com/ieg-dhr/DigiKAR/blob/main/TXT_splitUPPERCASE.py)

- identification des entrées de personnes basée sur les majuscules dans les noms

### c) [UniversityRecordsMainz_identifyPLACEofORIGIN.py](https://github.com/ieg-dhr/DigiKAR/blob/main/UniversityRecordsMainz_identifyPLACEofORIGIN.py)

- identification des lieux d'origine en fonction de la position des tokens dans le texte
- exemple de sortie du script pour les registres de l'université de Mayence :
[UniversityRecordsMainz_output_place-names.txt](https://github.com/ieg-dhr/DigiKAR/blob/main/UniversityRecordsMainz_output_place-names.txt)

### d) [TransferPROFData](https://github.com/ieg-dhr/DigiKAR/blob/main/JupyterNotebooks_DigiKAR/TransferPROFData.ipynb)

- Transfert de données textuelles semi-structurées extraites via OCR des registres de l'université de Mayence (à l'origine rédigés à la machine à écrire) vers EXCEL
- Découpe des informations en colonnes "nom", "information" et "citation source"
- Affinement ultérieur des entrées en faisant correspondre les "informations" avec des listes d'ontologies
- Identification des noms d'événements, des titres, des fonctions, des noms de lieu et des dates

***

![drawing](https://upload.wikimedia.org/wikipedia/commons/1/1c/Kurmainzische_Wappentafel_1750.jpg){:width="150" style="padding:10px" align="left"}

Le billet suivant décrit l'application de quelques scripts susmentionnés dans le paquet de travail "Kurmainz":
[Monika Barget, "Disambiguating people and places in dirty historical data," in INSULAE, last updated 26/10/2021](https://insulae.hypotheses.org/333)

***
