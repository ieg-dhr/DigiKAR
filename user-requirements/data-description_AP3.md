**Fallstudie Kurmainz: Mobilität und multiple Zugehörigkeiten von Funktionsträgern**

Die Fallstudie Kurmainz zeigt beispielhaft, wie Mobilität und multiple Zugehörigkeiten von Personen (in diesem Fall: Funktionsträgern) aus diversen Daten modelliert werden können.
Zur Analyse (biographischer) Mobilität in Kurmainz haben wir die folgenden Quellentypen ausgewertet, die auch für andere frühneuzeitliche Projekte relevant sein können:

- handschriftliche Archivquellen
- semi-strukturierte Zusammenfassungen von Quellen (mit Schreibmaschine geschriebene Universitätsmatrikeln)
- in XML strukturierte biographische Daten (Professoren-API der JGU)
- gedruckte Quellen (Staatskalender)

Für die Extraktion relevanter Daten aus diesen Quellen sind verschiedene Strategien erforderlich, die wir u.a. in den folgenden Beiträgen beschrieben haben:

(Hier Liste mit Blogposts, Papers, etc. ergänzen!)

Die folgende Graphik fasst die Herangehensweise zusammen:

Um diese Daten für die computergestützte Aufbereitung verfügbar zu machen, war eine Strukturierung in Tabellenformat notwendig. Alternativ wäre eine Strukturierung als TTL möglich gewesen, aber wir haben uns in AP3 bewusst für das folgende Modell entschieden:

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


