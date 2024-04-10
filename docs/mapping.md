## Data replacement based on ontology lists

[XLSX_replace_values_via_mapping.py](https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_replace_values_via_mapping.py)

### Use cases

- Replace cell values in XSLX based on mapping in a separate CSV file
- Adding additional cell values in selected cases
- Data cleaning and normalisation

### Example for data mapping

|event_name               |event_type       |
|-------------------------|-----------------|
|Akademische Laufbahn     |Funktionsausübung|
|Aufnahme in eine Fakultät|Rezeption        |
|Auslandsaufenthalt       |Reise            |
|Berufliche Tätigkeit     |Funktionsausübung|
|Berufung                 |Vokation         |

{:.justified}
In this example, "event_name" is the term in the input file that is to be replaced. The new term is in "event_type".
This relationship between the data is represented in two columns of the CSV file.
The script reads the CSV file into a dataframe and analyses one item in "event_name" after the other.
