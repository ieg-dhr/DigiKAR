## 1) Récupération de données à partir de plusieurs tableaux CSV/EXCEL

### a) Analyse simple des colonnes d'un tableau avec des étiquettes identiques à partir de plusieurs fichiers EXCEL:

{:.justified}
[XLSX_analysing-multiple-files.py](https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_analysing-multiple-files.py)

{:.justified}
**Cas d'utilisation:**

- Identification de chronologies dans des ensembles de données
- Comparaison de données
- Nettoyage et normalisation des données

{:.justified}
Exemple de sortie pour le script susmentionné:
[XLSX_multiple-files_sample-output.md](https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_multiple-files_sample-output.md)

### b) Script pour identifier les événements biographiques par personne et les trier par valeur d'événement et date:

{:.justified}
[1ère version : XLSX_select-and-sort-events.py](https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_select-and-sort-events.py)

{:.justified}
**Cas d'utilisation:**

- Reconstruction expérimentale de chronologies biographiques dans les cas où beaucoup d'événements n'ont pas de datation ou une datation vague
- Calcul de la chronologie possible d'un événement en fonction des événements précédents ou suivants
- Fusion d'événements identiques / ajustement de la chronologie des événements sur la base d'informations provenant de sources différentes

{:.justified}
Le tri actuel est quadruple et commence par la classification des événements. Ceci peut être ajusté dans le code:
`res_sorted=res_df.sort_values(by =[ 'event_value', 'event_after-date', 'event_start', 'event_before-date',])`

### c) Traceur de relations:

{:.justified}
[Version étendue : XSLX_relationship-tracer.py](https://github.com/ieg-dhr/DigiKAR/blob/main/XSLX_relationship-tracer.py)

{:.justified}
**Cas d'utilisation:**

- Consolidation des informations généalogiques de la colonne rel_pers dans les listes de factoïdes
- Reconstruction des relations entre frères et sœurs à partir des liens parents-enfants connus
- Reconstruction de relations implicites grand-parent-petit-enfant

### d) Script avancé permettant d'interroger plusieurs colonnes sur plusieurs feuilles de calcul en fonction de la saisie de l'utilisateur:

{:.justified}
[Interrogation des conditions OR : XSLX_multiple-conditions_OR.py](https://github.com/ieg-dhr/DigiKAR/blob/main/XSLX_multiple-conditions_OR.py)

{:.justified}
Les fichiers du répertoire DigiKAR_DATEN\Python\InputLists sont lus dans un seul cadre de données. L'utilisateur peut sélectionner des critères de recherche pour le nom de la personne, la date, l'institution, le titre de la personne, la fonction et la personne liée. Plusieurs mots-clés par champ sont acceptés. L'utilisateur peut décider de rechercher des dates exactes, une plage de dates ou des dates "avant" et "après". Le script traite d'abord l'entrée de l'heure et écrit les correspondances dans un nouveau cadre de données, puis les conditions pour les autres champs sont appliquées. La version actuelle du script applique l'opérateur OR aux champs. Dans la version finale de l'interface graphique, l'utilisateur pourra sélectionner les deux opérations AND ou OR. Les résultats sont écrits dans un nouveau fichier. L'utilisateur est libre d'assigner un nom de fichier via l'entrée du script. La gestion du temps prend en charge les entrées "YYYY" ainsi que "YYYY-MM" et "YYYY-MM-DD". En recherchant les dates avant et après la date d'entrée, les colonnes "avant" et "après" de la feuille de calcul originale sont prises en compte avec les dates de début et de fin.

{:.justified}
**Cas d'utilisation:**

- Exemple pour créer des requêtes booléennes plus complexes sur plusieurs feuilles de calcul
- Adaptation à différents formats de feuilles de calcul
- Expérimentation de l'analyse syntaxique des données et des problèmes potentiels posés par les données modernes anciennes
