<h2>Data replacement based on ontology lists</h2>

<a href="https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_replace_values_via_mapping.py">XLSX_replace_values_via_mapping.py</a>

<h3>Use cases</h3>

<ul>
  <li>Replace cell values in XSLX based on mapping in a separate CSV file</li>
  <li>Adding additional cell values in selected cases</li>
  <li> Data cleaning and normalisation</li>
</ul>

<h3>Example for data mapping</h3>

|event_name               |event_type       |
|-------------------------|-----------------|
|Akademische Laufbahn     |Funktionsausübung|
|Aufnahme in eine Fakultät|Rezeption        |
|Auslandsaufenthalt       |Reise            |
|Berufliche Tätigkeit     |Funktionsausübung|
|Berufung                 |Vokation         |

<p align="justify">In this example, "event_name" is the term in the input file that is to be replaced. The new term is in "event_type". 
  This relationship between the data is represented in two columns of the CSV file. The script reads the CSV file into a dataframe and analyses one item in "event_name" after the other.</p>

