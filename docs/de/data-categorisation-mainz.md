# Datenkategorisierung Mainz

## Allgemeine Herausforderungen

Eine große Herausforderung im Mainzer Arbeitspaket, das Daten aus verschiedenen Quellen sammelte, war die **Normalisierung von Ereignisbeschreibungen und die Modellierung ihrer Beziehungen**. Studien wurden beispielsweise zunächst mit oder ohne bekannte Start- und Enddaten als kontinuierliches Ereignis erfasst, aber auch als Universitätsimmatrikulationen. Eine Immatrikulation ist natürlich ein punktuelles Ereignis, das einen längeren Studienprozess auslöst, für den nur das Startdatum bekannt ist. Um die gesammelten biografischen Informationen einheitlicher und leichter abfragbar zu machen, war es daher notwendig, Prozesse aus punktuellen Ereignissen zu rekonstruieren, wenn möglich, und aufeinanderfolgende punktuelle Ereignisse zu längeren kontinuierlichen Ereignissen zusammenzuführen, z.B. wenn Informationen aus Jahreskalendern stammten. Zu diesem Zweck wurde ein "Konsolidierungs"-Skript in Python geschrieben und auf alle unsere gesammelten Datensätze ausgeführt.

## Datenkategorisierung in Metaphacts

Um Daten aus dem Mainzer Arbeitspaket abzufragen und zu clustern, haben wir mit dem proprietären System [Metaphacts](https://metaphacts.com/) experimentiert, das "kollaborative Wissensmodellierung und Wissensgenerierung unterstützt". In Metaphacts können höhere Kategorien für gesammelte Daten als `skos:Collections` definiert werden. Ingo Frank (IOS Regensburg) hat als Beispiel alle unsere Begriffe für `Ereignisse` und `Funktionen`, die wir für die in Mainz tätigen frühneuzeitlichen Professoren gesammelt haben, genommen und hierarchische Beziehungen aus den durch Kommas getrennten Einträgen erstellt:

- [Klassifikationssystem für biografische Ereignisse](http://95.217.189.117:10214/resource/?uri=http%3A%2F%2Fdigikar.eu%2Fvocabulary%2Fevent)
- [Klassifikation für Rollen/Funktionen von Personen](http://95.217.189.117:10214/resource/?uri=http%3A%2F%2Fdigikar.eu%2Fvocabulary%2Ffunction)

Nur die übergeordneten Begriffe sind in der Sammlung (Kategorie) enthalten, da die Suche dann einfach auf die jeweiligen Unterbegriffe ausgeweitet wird.

## Datenkategorisierung über Python

Eine andere Möglichkeit, Daten zu kategorisieren, besteht darin, Cluster und Hierarchien in Python-Wörterbüchern oder einfachen CSV-Tabellen zu definieren, deren Informationen dann an die grundlegende Faktendatenstruktur unserer Daten angehängt werden können. Das Zuordnen von Daten zu vorhandenen Tabellenkalkulationen ist in Python sehr einfach, da das pandas-Paket eine flexible Manipulation von Tabellendaten als sogenannte Dataframes ermöglicht. Jeder Eintrag in einer ausgewählten Tabellenkalkulationsspalte kann somit je nach Forschungsfragen und theoretischen Kontexten, in denen die Daten analysiert werden, verschiedenen höheren Kategorien zugewiesen werden. Beispiele für die Datenkategorisierung in Python finden Sie im separaten [Data Categorisation](https://github.com/ieg-dhr/DigiKAR/tree/main/Data%20Categorisation) Ordner in diesem GitHub-Repository.

## Kategorien, die für die Datenanalyse in WP3 relevant sind

- Kirchliche Ämter im Allgemeinen (alle Funktionen, die in Klöstern und Diözesanverwaltungen ausgeübt werden)
- Klerikale Ämter (die Weihen erfordern, z.B. priesterliche Funktionen in Diözesen und Pfarreien)
- Lehre (an Universitäten, aber auch in Seminaren und Kollegien)
- Politische Ämter (z.B. als Administratoren, Gesandte oder Regierungsbeamte)
- Medizinische Tätigkeiten (z.B. als Leibarzt für Adelige, Stadtarzt, Armenarzt oder Feldarzt)
- Juristische Tätigkeiten (z.B. als Anwälte oder Richter)
- Militärdienst (z.B. als Soldaten, Militäringenieure oder Feldärzte)

Einige der Aktivitäten in diesen Kategorien überschneiden sich natürlich. Für Visualisierungszwecke ist es jedoch notwendig, mit sieben bis zehn Kategorien in jedem Netzdiagramm oder jeder Karte zu arbeiten, insbesondere wenn Kategorien in verschiedenen Farben hervorgehoben werden sollen.
