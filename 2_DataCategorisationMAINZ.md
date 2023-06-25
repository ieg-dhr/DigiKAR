## Data categorisation Mainz

# 1) Data categorisation in Metaphacts

In Metaphacts, higher-level categories can be defined as skos:Collections.

- [Classification system for biographical events](http://95.217.189.117:10214/resource/?uri=http%3A%2F%2Fdigikar.eu%2Fvocabulary%2Fevent)

- [Classification for persons' roles / functions](http://95.217.189.117:10214/resource/?uri=http%3A%2F%2Fdigikar.eu%2Fvocabulary%2Ffunction)

In die Collection (Kategorie) werden natürlich immer nur die Überbegriffe eingängt, da die Suche ja dann einfach auf die jeweiligen Unterbegriffe ausgeweitet wird.

Die Begriffe für die Ereignisse und Funktionen habe ich alle es dem letzten Excel-Datensatz der Professoren-Daten gezogen und (nicht unbedingt durchgehend fehlerfrei) die hierarchischen Zusammenhänge aus den Komma-separierten Einträgen erstellt.

# 2) Data categorisation via Python

Another way to categorise data is to define clusters and hierarchies in Python dictionaries or simple CSV tables whose information can then be "appended" to the basic factoid structure of our data.
The items can thus be assigned to different higher-level categories, depending on the research questions and theoretical contexts in which the data are being analysed.

For examples of data categorisation in Python, please view the separate folder in this repository.

# 3) Categories relevant for data analysis in WP3

- Geistliche Ämter -> Klöster und Stifte
- Geistliche Ämter -> Bistümer und Pfarrein
- Lehrtätigkeit (an Unis, aber auch seminaren und Kollegien)
- Politische Ämter (Verwalter, Gesandte, Regierungsbeamte)
- Medizinische Tätigkeiten (Leibarzt, Stadtarzt, Armenarzt etc.)
- Juristische Tätigkeiten (RKG, "Syndikus" (?), Richter an Hofgerichten etc.)
- Sonstiges (Künstler???)
(= 7 Hauptkategorien für Trivial Pursuit Modell oder Atom Modell)
