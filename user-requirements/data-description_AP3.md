## Mobilität und multiple Zugehörigkeiten von Funktionsträgern

{:.justified}
Die Fallstudie Kurmainz zeigt beispielhaft, wie Mobilität und multiple Zugehörigkeiten von Personen (in diesem Fall: Funktionsträgern) aus diversen Daten modelliert werden können. Datenmodellierung ist eine strukturierte Aufbereitung von Daten in maschinenlesbare Form, die eine automatisierte Abfrage und Visualisierung der Daten (z.B. über Datenbankabfragen mit [SQL](https://en.wikipedia.org/wiki/SQL) oder [SPARQL](https://en.wikipedia.org/wiki/SPARQL) erlaubt.

### Sinn und Zweck der Datenmodellierung in historischen Projekten

{:.justified}
Idealerweise beginnt Datenmodellierung bereits mit der ersten Erfassung von Metadaten und setzt sich dann im gesamten Projekt fort. Im DigiKAR Projekt, das interdisziplinär angelegt ist und Forschende an verschiedenen Standorten verbindet, ist kontinuierliche und kollaborative Datenmodellierung auch Teil der Verständigung im Projekt. Damit verbunden ist auch die Zielsetzung, die Daten klar zu beschreiben und anderen Projekten zur Nachnutzung zur Verfügung zu stellen.

{:.justified}
Außerdem ist Datenmodellierung nicht nur dann notwendig, wenn im Projekt eine Datenbank mit graphischem Interface (d.h. Benutzeroberfläche) gebaut werden soll. Auch für Datenabfragen allein mit Excel-Filtern oder Skripten (z.B. in Python) ist die Strukturierung und (teilweise) Normalisierung von Daten notwendig. In historischen Projekten ist dies oft eine besondere Herausforderungen, da nur wenige Daten bereits seriell vorliegen und viele Quellen nicht digitalisiert wurden.

### Fallstudie Kurmainz: Quellentypen und Möglichkeiten ihrer strukturierten Auswertung

Zur Analyse (biographischer) Mobilität in Kurmainz haben wir die folgenden Quellentypen ausgewertet, die auch für andere frühneuzeitliche Projekte relevant sein können:

- handschriftliche Archivquellen
- semi-strukturierte Zusammenfassungen von Quellen (mit Schreibmaschine geschriebene Universitätsmatrikeln)
- in XML strukturierte biographische Daten (Professoren-API der JGU)
- gedruckte Quellen (Staatskalender)

![img data overview](../assets/DataOverview.png){:width="50%" }

Für die Extraktion und Aufbereitung relevanter Daten aus diesen Quellen sind verschiedene Strategien erforderlich, die wir u.a. in den folgenden Beiträgen beschrieben haben:

- [Reading historical maps with optical character recognition (OCR)](https://insulae.hypotheses.org/485)
- [Disambiguating people and places in dirty historical data](https://insulae.hypotheses.org/333)
- siehe Jupyter-Notebooks und Code-Beschreibungen in diesem Github Repositirum
- ???

Die folgende Graphik fasst die Herangehensweise zusammen:

![img data extraction](../assets/DataExtraction.png){:width="50%"}

### Vor- und Nachteile des Tabellenmodells zur Datenerfassung im DigiKAR Arbeitspaket Kurmainz

{:.justified}
Um diese Daten für die computergestützte Aufbereitung verfügbar zu machen, haben wir uns in DigiKAR für eine Strukturierung in Tabellenformat entschieden. Eine Tabelle erlaubt bereits, Daten zueinander in klare Beziehungen zu setzen. Alternativ wäre eine Strukturierung in einem Triple-Format (vgl. [Turtle Syntax](https://en.wikipedia.org/wiki/Turtle_(syntax)) möglich gewesen, aber wir haben uns besonders im Arbeitspaket Kurmainz bewusst für ein ereignisorientiertes Tabellenmodell entschieden, dessen Spalten die folgenden Überschriften haben:

| factoid_ID | pers_ID | event_date | event_after-date | event_before-date | event_start | event_end | event_type | pers_name | pers_title | pers_function | place_name | inst_name | rel_pers | alternative_names | source_quotations | additional_info | comment | source | source_site | info_dump |
|------------|---------|------------|------------------|-------------------|-------------|-----------|------------|-----------|------------|---------------|------------|-----------|----------|-------------------|-------------------|-----------------|---------|--------|-------------|-----------|
| | | | | | | | | | | | | | | | | | | | | |

{:.justified}
Dieses Tabellenmodell folgt dem sog. [Factoid-Ansatz](https://www.kcl.ac.uk/factoid-prosopography/ontology) und hat folgende Eigenschaften:

- hohe Quellennähe
- Redundanz (dieselben Ereignisse können abhängig von der Quellenlage mehrmals erfasst werden)
- vergleichweise wenige Tabellenspalten, dafür aber viele Zeilen (sh. Redundanz der Ereignisse)
- Ereignisorientierung
- Datenunsicherheit wird für alle Factoide als hoch angenommen und nur in wenigen Fällen zusätzlich ausgewiesen

Das Problem, Unsicherheiten nicht vollständig erfassen zu können, wurde durch die folgenden Ansätze gelöst:

- Teils Klammern und Fragezeichen als bewusste Ergänzung hinter Orten (zur Dokumentation der Konventionen sh. [Ontologie Master Datei mit ausführlichen Kommentaren von Florian Stabel](https://github.com/ieg-dhr/DigiKAR/tree/main/OntologyFiles){:target="_blank"})
- viele Quellentypen (z.B. die Universitätsmatrikeln, die selbst eine sekundäre Quelle sind) werden generell als unsicher behandelt
- Hierarchie der Vertrauenswürdigkeit: höchste Qualität wird eigener Erfassung aus Primärquellen zugeschrieben
- Datenkonflikte werden durch bewusste Mehrfachnennung von Ereignissen abgebildet

{:.justified}
Die Aufbereitung der Daten erfolgte in AP3 ausschließlich via Excel und Python, um nicht von (kommerzieller) Datenbanksoftware abhängig zu sein und in allen Phasen des Projekts Roh-Daten zu generieren, die andere Projekte ebenfalls ohne Datenbanken nachnützen können (sog. *No DB Modell*):

![img no DB](../assets/NoDB.png){:width="30%" style="float:left; padding:10px"}

{:.justified}
Herausforderungen der Datenorganisation besonders in geisteswissenschaftlichen Projekten, die sich oft den Aufbau und Erhalt einer Datenbank nicht leisten können, hat Monika Barget in einem [Beitrag für den Mosa Historia Blog der Geschichtsfakultät Maastricht](https://fasos-research.nl/mosahistoria/blog/) in englischer Sprache näher erklärt. In AP3 Kurmainz haben die erfassenden Historiker*innen vor allem Filter in Excel genutzt, um während der Erfassung Daten sortieren und selektieren zu können. In AP2 wurde hingegen stärker über die Erstellung einer Eingabemaske nachgedacht und zeitweilig mit den Datentabellen in QGIS gearbeitet.
  
### Konkrete Schritte der Ontologie-Entwicklung (Best Practices)

{:.justified}
Um die in EXCEL grundständig geordneten Daten komplex (d.h. über mehrere Spalten hinweg) abfragen zu können, ist über die Entwicklung eines Eingabeformats hinaus auch die Entwicklung eines kontrollierten Vokabulars und eine Hierarchisierung bzw. logische Zuordnung von Begriffen zueinander notwendig. Diese Zuordnung von Begriffen übernehmen sogenannte Ontologien, von denen CIDOC-CRM eine der in den Geisteswissenschaften geläufigsten ist. Viele Begriffe, die für die Arbeit mit historischen Ortsdaten wichtig sind, sind bereits in CIDOC-CRM angelegt, weshalb diese Ontologie eine Basis bildet, die projektbezogen erweitert werden kann. Die Ontologie legt z.B. bereits fest, wie sich akademische Titel aufeinander beziehen: bevor man Professor wird, muss man promovieren etc.

{:.justified}
In der speziellen Arbeit in AP3 haben wir uns sowohl an CIDOC-CRM orientiert, als auch einige eigene Entscheidungen getroffen, um die Daten möglichst schlank und flexibel zu beschreiben. Entscheidungen haben wir in den sog. Ontologie-Listen des AP3 festgehalten. Dies sind Tabellen, die alle in den QUellen vorhandenen Originalbegriffe zunächst einer Kategorie Person, Ort, Institution, FUnktion oder Titel zuordnen und dann festlegen, auf welche normalisierte Bezeichnung diese Begriffe "gemappt" werden sollen. Es wurde auch in einer separaten Spalte dokumentiert, weshalb diese Entscheidungen getroffen wurden.

{:.justified}
Das Anlegen von Ontologie-Listen dieser Art ist einerseits eine wichtige Dokumentation für die Transparenz des Forschungsprojekts, anderseits können diese Listen auch konkret zur Datenbereinigung von neu erfassten Daten dienen (vgl. dazu auch Video XXXXX).

Der aktuellste Stand der Ontologie-Listen für das Arbeitspaket Kurmainz in DigiKAR wurde hier auch GITHUB geteilt:

[Ontology Files](https://github.com/ieg-dhr/DigiKAR/tree/main/OntologyFiles){:target="_blank"}
                                                                                 
### Empfehlungen für Historiker*innen für die grundlegende Datenerfassung ohne Datenbank

{:.callout.todo}
Text
                                                                                 
### Empfehlungen für die Arbeitsteilung zwischen Historiker*innen und Informationswissenschaftler*innen bzw. DB-Entwickler*innen

{:.callout.todo}
Tipps dazu, welche Modellierung auf der Erfassungsseite passieren sollte, und was aber die Abfrage geregelt werden kann, wenn es eine relationale DB und / oder eine Graph DB gibt.

- "activity" Unterklassen für Ereignisse nur seitens der Abfragen?
- Hierarchien von Institutionen nicht in den eigenen Daten modellieren, sondern über sekundäre Daten bei den Abfragen einbeziehen?
- Personen-Daten sekundär über GND und andere Normdaten "anreichern", ohne dies in den eigenen Daten zu modellieren?
- Zugehörigkeiten von Orten zu Pfarreien z.B. nicht explizit modellieren, sondern u.a. aber geographische Nähe abfragen?
- ???
                                         
### Kritik verschiedener Datenbankmodelle für das Arbeiten mit historischen Ortsdaten

Insgesamt haben wir uns kritisch mit Datenbankmodellen befasst…

![img DB review](../assets/DBReview.png){:width="50%"}
