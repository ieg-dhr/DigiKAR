<h2>Remplacement de données basé sur des listes d'ontologies</h2>

<a href="https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_replace_values_via_mapping.py">XLSX_replace_values_via_mapping.py"</a>

<h3>Cas d'utilisation</h3>

<ul>
  <li>Remplacement des valeurs des cellules XSLX sur la base d'un mappage dans un fichier CSV séparé</li>
  <li>Compléter les valeurs de certaines cellules</li>
  <li>Nettoyage et normalisation des données</li>
</ul>

<h3>Exemple de mappage de données</h3>

|event_name               |event_type       |
|-------------------------|-----------------|
|Akademische Laufbahn     |Funktionsausübung|
|Aufnahme in eine Fakultät|Rezeption        |
|Auslandsaufenthalt       |Reise            |
|Berufliche Tätigkeit     |Funktionsausübung|
|Berufung                 |Vokation         |

<p align="justify">Dans cet exemple, "event_name" est le nom dans le fichier d'entrée qui doit être remplacé. Le nouveau nom se trouve dans "event_type". 
  Cette relation entre les données est représentée dans deux colonnes du fichier CSV, qui sont lues par le script.</p>
