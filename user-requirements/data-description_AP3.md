**Fallstudie Kurmainz: Mobilität und multiple Zugehörigkeiten von Funktionsträgern**

Die Fallstudie Kurmainz zeigt beispielhaft, wie Mobilität und multiple Zugehörigkeiten von Personen (in diesem Fall: Funktionsträgern) aus diversen Daten modelliert werden können.
Zur Analyse (biographischer) Mobilität in Kurmainz haben wir die folgenden Quellentypen ausgewertet, die auch für andere frühneuzeitliche Projekte relevant sein können:

- handschriftliche Archivquellen
- semi-strukturierte Zusammenfassungen von Quellen (mit Schreibmaschine geschriebene Universitätsmatrikeln)
- in XML strukturierte biographische Daten (Professoren-API der JGU)
- gedruckte Quellen (Staatskalender)

<img scr="../assets/DataOverview.png" width="50%">

Für die Extraktion relevanter Daten aus diesen Quellen sind verschiedene Strategien erforderlich, die wir u.a. in den folgenden Beiträgen beschrieben haben:

(Hier Liste mit Blogposts, Papers, etc. ergänzen!)

Die folgende Graphik fasst die Herangehensweise zusammen:

(BILD EINFÜGEN)

Um diese Daten für die computergestützte Aufbereitung verfügbar zu machen, war eine Strukturierung in Tabellenformat notwendig. Alternativ wäre eine Strukturierung als TTL möglich gewesen, aber wir haben uns in AP3 bewusst für das folgende Modell entschieden:

# Data structure in the Mainz work package

1) **Table design in EXCEL for collecting biographic data**

| factoid_ID | pers_ID | event_date | event_after-date | event_before-date | event_start | event_end | event_type | pers_name | pers_title | pers_function | place_name | inst_name | rel_pers | alternative_names | source_quotations | additional_info | comment | source | source_site | info_dump |
|------------|---------|------------|------------------|-------------------|-------------|-----------|------------|-----------|------------|---------------|------------|-----------|----------|-------------------|-------------------|-----------------|---------|--------|-------------|-----------|


Dieses Tabellenmodell folgt dem Factoid-Ansatz und hat folgende Eigenschaften:

- hohe Quellennähe
- Redundanz
- vergleichweise wenige Tabellenspalten
- Ereignisorientierung
- Datenunsicherheit wird nur bedingt erfasst

Das Problem, Unsicherheiten hier nicht explizit erfassen zu können, wurde durch die folgenden Ansätze gelöst:

- Teils Klammern und Fragezeichen als bewusste Ergänzung hinter Orten
- viele Quellentypen (z.B. die Universitätsmatrikeln, die selbst eine sekundäre Quelle sind) werden generell als unsicher behandelt
- Hierarchie der Vertrauenswürdigkeit: höchste Qualität wird eigener Erfassung aus Primärquellen zugeschrieben
- Datenkonflikte werden durch bewusste Mehrfachnennung von Ereignissen abgebildet

Die Auswertung folge dann einem No DB Modell:

<img scr="./gh-pages/assets/NoDB.png" width="50%">

Auf ein graphisches Interface wurde verzichtet, da die erfassenden Historiker vor allem Filter in Excel genutzt haben. In AP2 wurde hingegen stärker über die Erstellung einer Eingabemaske nachgedacht.

Um die in EXCEL grundständig geordneten Daten allerdings komplex (d.h. über mehrere Spalten hinweg) abfragen zu können, war allerdings über die Entwicklung eines Eingabeformats hinaus auch die Entwicklung eines kontrollierten Vokabulars und eine Hierarchisierung bzw. logische Zuordnung von Begriffen zueinander notwendig. Diese Zuordnung von Begriffen übernehmen sogenannte Ontologien, von denen CIDOC-CRM eine der in den Geisteswissenschaften geläufigste ist. Viele Begriffe, die für die Arbeit mit historischen Ortsdaten wichtig sind, sind bereits in CIDOC-CRM angelegt, weshalb diese Ontologie eine Basis bildet, die projektbezogen erweitert werden kann. Die Ontologie legt z.B. bereits fest, wie sich akademische Titel aufeinander beziehen: bevor man Professor wird, muss man promovieren etc. 

In der speziellen Arbeit in AP3 haben wir uns sowohl an CIDOC-CRM orientiert, als auch einige eigene Entscheidungen getroffen, um die Daten möglichst schlank und flexibel zu beschreiben. Entscheidungen haben wir in den sog. Ontologie-Listen des AP3 festgehalten. Dies sind Tabellen, die alle in den QUellen vorhandenen Originalbegriffe zunächst einer Kategorie Person, Ort, Institution, FUnktion oder Titel zuordnen und dann festlegen, auf welche normalisierte Bezeichnung diese Begriffe "gemappt" werden sollen. Es wurde auch in einer separaten Spalte dokumentiert, weshalb diese Entscheidungen getroffen wurden.

Das Anlegen von Ontologie-Listen dieser Art ist einerseits eine wichtige Dokumentation für die Transparenz des Forschungsprojekts, anderseits können diese Listen auch konkret zur Datenbereinigung von neu erfassten Daten dienen (vgl. dazu auch Video XXXXX).

Der aktuellste Stand der Ontologie-Listen für das Arbeitspaket Kurmainz in DigiKAR wurde hier auch GITHUB geteilt:

<a href="../main/OntologyFiles">Ontology Files</a>

Insgesamt haben wir uns kritisch mit Datenbankmodellen befasst...

<img scr="./gh-pages/assets/DBReview.png" width="50%">





