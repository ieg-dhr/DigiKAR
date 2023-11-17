## Remplacement de données basé sur des listes d'ontologies

[XLSX_replace_values_via_mapping.py](https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_replace_values_via_mapping.py)

### Cas d'utilisation

- Remplacement des valeurs des cellules XSLX sur la base d'un mappage dans un fichier CSV séparé
- Compléter les valeurs de certaines cellules
- Nettoyage et normalisation des données

### Exemple de mappage de données

|event_name               |event_type       |
|-------------------------|-----------------|
|Akademische Laufbahn     |Funktionsausübung|
|Aufnahme in eine Fakultät|Rezeption        |
|Auslandsaufenthalt       |Reise            |
|Berufliche Tätigkeit     |Funktionsausübung|
|Berufung                 |Vokation         |

{:.justified}
Dans cet exemple, "event_name" est le nom dans le fichier d'entrée qui doit être remplacé. Le nouveau nom se trouve dans "event_type".
Cette relation entre les données est représentée dans deux colonnes du fichier CSV.
Le script lit le fichier CSV dans un *dataframe* et analyse les éléments de "event_name" les uns après les autres.
