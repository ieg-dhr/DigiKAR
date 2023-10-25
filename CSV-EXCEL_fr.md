<h2>1) Récupération de données à partir de plusieurs tableaux CSV/EXCEL</h2>

    <h3>a) Analyse simple des colonnes d'un tableau avec des étiquettes identiques à partir de plusieurs fichiers EXCEL:</h3>
    <a href="./XLSX_analysing-multiple-files.py">XLSX_analysing-multiple-files.py</a>

    Cas d'utilisation :
    <ul>
        <li>Identification de chronologies dans des ensembles de données</li>
        <li>Comparaison de données</li>
        <li>Nettoyage et normalisation des données</li>
    </ul>

    Exemple de sortie pour le script susmentionné :
    <a href="./XLSX_multiple-files_sample-output.md">XLSX_multiple-files_sample-output.md</a>

    <h3>b) Script pour identifier les événements biographiques par personne et les trier par valeur d'événement et date:</h3>
    <a href="./XLSX_select-and-sort-events.py">1ère version : XLSX_select-and-sort-events.py</a>

    Cas d'utilisation :
    <ul>
        <li>Reconstruction expérimentale de chronologies biographiques dans les cas où beaucoup d'événements n'ont pas de datation ou une datation vague</li>
        <li>Calcul de la chronologie possible d'un événement en fonction des événements précédents ou suivants</li>
        <li>Fusion d'événements identiques / ajustement de la chronologie des événements sur la base d'informations provenant de sources différentes</li>
    </ul>

    Le tri actuel est quadruple et commence par la classification des événements. Ceci peut être ajusté dans le code:
    <code>res_sorted=res_df.sort_values(by =[ 'event_value', 'event_after-date', 'event_start', 'event_before-date',])</code>

    <h3>c) Traceur de relations:</h3>
    <a href="./XSLX_relationship-tracer.py">Version étendue : XSLX_relationship-tracer.py</a>

    Cas d'utilisateurs :
    <ul>
        <li>Consolidation des informations généalogiques de la colonne rel_pers dans les listes de factoïdes</li>
        <li>Reconstruction des relations entre frères et sœurs à partir des liens parents-enfants connus</li>
        <li>Reconstruction de relations implicites grand-parent-petit-enfant</li>
    </ul>

    <h3>d) Script avancé permettant d'interroger plusieurs colonnes sur plusieurs feuilles de calcul en fonction de la saisie de l'utilisateur:</h3>
    <a href="./XSLX_multiple-conditions_OR.py">Interrogation des conditions OR : XSLX_multiple-conditions_OR.py</a>

    Les fichiers du répertoire DigiKAR_DATEN\Python\InputLists sont lus dans un seul cadre de données.

    L'utilisateur peut sélectionner des critères de recherche pour le nom de la personne, la date, l'institution, le titre de la personne, la fonction et la personne liée. Plusieurs mots-clés par champ sont acceptés.

    L'utilisateur peut décider de rechercher des dates exactes, une plage de dates ou des dates "avant" et "après".

    Le script traite d'abord l'entrée de l'heure et écrit les correspondances dans un nouveau cadre de données, puis les conditions pour les autres champs sont appliquées. La version actuelle du script applique l'opérateur OR aux champs. Dans la version finale de l'interface graphique, l'utilisateur pourra sélectionner les deux opérations AND ou OR.

    Les résultats sont écrits dans un nouveau fichier. L'utilisateur est libre d'assigner un nom de fichier via l'entrée du script.

    La gestion du temps prend en charge les entrées "YYYY" ainsi que "YYYY-MM" et "YYYY-MM-DD". En recherchant les dates avant et après la date d'entrée, les colonnes "avant" et "après" de la feuille de calcul originale sont prises en compte avec les dates de début et de fin.

    Cas d'utilisation :
    <ul>
        <li>Exemple pour créer des requêtes booléennes plus complexes sur plusieurs feuilles de calcul</li>
        <li>Adaptation à différents formats de feuilles de calcul</li>
        <li>Expérimentation de l'analyse syntaxique des données et des problèmes potentiels posés par les données modernes anciennes</li>
    </ul>
