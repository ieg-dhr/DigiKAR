<h2>Ersetzen von Daten basierend auf Ontologielisten</h2>

<a href="https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_replace_values_via_mapping.py">XLSX_replace_values_via_mapping.py"</a>

<h3>Anwendungsfälle</h3>

<ul>
  <li>Ersetzen von Zellwerten in XSLX basierend auf Mapping in einer separaten CSV Datei</li>
  <li>Ergänzen von Zellwerten in ausgewählten Fällen</li>
  <li>Datenbereinigung und Normalisierung</li>
</ul>

<h3>Beispiel für Datenmapping</h3>

|event_name               |event_type       |
|-------------------------|-----------------|
|Akademische Laufbahn     |Funktionsausübung|
|Aufnahme in eine Fakultät|Rezeption        |
|Auslandsaufenthalt       |Reise            |
|Berufliche Tätigkeit     |Funktionsausübung|
|Berufung                 |Vokation         |

<p>In diesem Beispiel steht "event_name" für die Bezeichnung in der Eingabedatei, die ersetzt werden soll. Die neue Bezeichnung steht in "event_type".
Diese Beziehung zwischen den Daten wird in zwei Spalten einer CSV-Datei dargestellt, die das Skript Eintrag für Eintrag auswertet.</p>

