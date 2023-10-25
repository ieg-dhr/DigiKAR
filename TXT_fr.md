# 2) Extraction d'informations structurées à partir de fichiers TXT</h2>

##  <a href="https://github.com/ieg-dhr/DigiKAR/blob/main/TXT_replaceWORDwithREGEX.py">TXT_replaceWORDwithREGEX.py</a>
    <p>
        - ajout de délimiteurs au texte en fonction d'une expression régulière<br>
        - préparation du texte pour la découpe en sections individuelles
    </p>

## b) <a href="https://github.com/ieg-dhr/DigiKAR/blob/main/TXT_splitUPPERCASE.py">TXT_splitUPPERCASE.py</a>
    <p>
        - identification des entrées de personnes basée sur les majuscules dans les noms
    </p>

## c) <a href="https://github.com/ieg-dhr/DigiKAR/blob/main/UniversityRecordsMainz_identifyPLACEofORIGIN.py">UniversityRecordsMainz_identifyPLACEofORIGIN.py</a>
    <p>
        - identification des lieux d'origine en fonction de la position des tokens dans le texte<br>
        - exemple de sortie du script pour les registres de l'université de Mayence :
        <a href="https://github.com/ieg-dhr/DigiKAR/blob/main/UniversityRecordsMainz_output_place-names.txt">UniversityRecordsMainz_output_place-names.txt</a>
    </p>

## d) <a href="https://github.com/ieg-dhr/DigiKAR/blob/main/JupyterNotebooks_DigiKAR/TransferPROFData.ipynb">TransferPROFData</a>
    <p>
        - Transfert de données textuelles semi-structurées extraites via OCR des registres de l'université de Mayence (à l'origine rédigés à la machine à écrire) vers EXCEL<br>
        - Découpe des informations en colonnes "nom", "information" et "citation source"<br>
        - Affinement ultérieur des entrées en faisant correspondre les "informations" avec des listes d'ontologies<br>
        - Identification des noms d'événements, des titres, des fonctions, des noms de lieu et des dates.
    </p>

    <hr>

<img src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Kurmainzische_Wappentafel_1750.jpg" alt="drawing" width="150" style="padding:10px" align="left"/>
Le billet suivant décrit l'application de quelques scripts susmentionnés dans le paquet de travail "Kurmainz":</p>
<a href="https://insulae.hypotheses.org/333">Monika Barget, "Disambiguating people and places in dirty historical data," in INSULAE, last updated 26/10/2021</a>

<hr>
