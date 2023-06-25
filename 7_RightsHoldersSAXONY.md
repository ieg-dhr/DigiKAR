## Rights holders in Saxony - challenges of the data structure

Im Rahmen der Normalisierung der HOV- und RepSax-Datenbankeinträge stießen wir u.a. auf eine uneinheitliche Erfassung der Rechteinhaber bei der Grundherrschaft. Dies betraf besonders Rittergüter.
In ["Bürgerliche Rittergüter : sozialer Wandel und politische Reform in Kursachsen (1680 - 1844)"](https://digi20.digitale-sammlungen.de/de/fs1/object/display/bsb00056061_00147.html) heißt es:
Auch "bürgerlichen Gruppen [gelangten] in den Besitz der Rittergüter gelangten", was im Sinne einer Abbildung des sozialen Wandels eine Kategorienbildung aufgrund der Tätigkeiten und Funktionen/Rollen von Personen
sinnvoll erscheinen lässt.

Jedenfalls müssten wir doch versuchen Visualisierungsansätze an diesen Stellen von Verbindungsmöglichkeiten der Geodaten mit den biographischen Daten zu finden, 
um eben Phänomene von z.B. sozialem Wandel zu veranschaulichen und ggf. räumliche Muster dadurch zu entdecken etc.

In und unter Tab. 23 findet man die folgenden "sozialen Gruppen bürgerlicher Rittergutsbesitzer": 'Amtsträger', 'Gebildete', 'Kaufleute', 'Militärs', 'Landwirte'

(Landesherrliche) Amtsträger wie folgt beschrieben: 
"sowohl die Hof- und Justitienrätc, Kammerräte, Akzisräte und Stiftsräte der Landesbehörden als auch die Amtsschösser, 
Amtsrentverwalter und Amtmänner der Lokalverwaltung"

Mit der folgenden Stelle aus oben bereits zitiertem Buch (Seite 41-42) lassen sich z.B. viele der uneinheitlichen Einträge in den HOV- und RepSax-Daten erklären: 

"Der aktuelle Inhaber eines Rittergutes wurde im sächsischen Lehnrecht *nicht* als individueller Eigentümer betrachtet. 
Der Besitz stand vielmehr einem sozialen Verband zu. Dabei handelte sich entweder um ein Geschlecht, d.h. in der Hauptsache um die Kontinuität in der Vater-Sohn Abfolge,
oder um die Gruppe aus Vasall und Mitbelehnten, die möglicherweise eine »familia« im älteren vormodernen Sinn des Wortes bildete." (Flügel (2000. 54)"

Deshalb steht in den vorhandenen Datenbanken manchmal eine individuelle Person (als Anghöriger eines Geschlechts), aber manchmal eben auch nur bzw. explizit das Geschlecht.

Bsp. im RepSax: "von Taupaddel" vs. "Heinrich von Taupaddel" -- ersteres ist eine Instanz der Klasse 'Geschlecht', letzteres eine Instanz der Klasse 'Person'

Ganz grundlegend gibt es unabhängig von einer genauen Klassifikation das Problem, dass die Angaben nicht einheitlich sind.
**(Problem bei Datenaufbereitung und -integration/-normalisierung)**

In Sachen Projektmanagement wäre es wohl gut, wenn diese Dinge als Issues im GitLab bearbeitet werden. 
Auch wenn wir die einzigen sind, die das nutzen bzw. da reinschauen.
Ach ja, beim HOV hat man dann wohl in einer Art Vereinfachung einfach sowas wie "Rittergut Schleinitz" eingetragen.

**Je nach Kontext der Forschungsfrage, erfolgt eine andere perspektivische Einordnung?**

Wenn nicht immer die gleiche Flughöhe im selben Datenbankfeld genutzt wird, muss man den Daten mehrere mögliche Klassen zuordnen und die genaue Zuordnung zunächst offen
lassen, oder die Daten so strukturieren, dass die verschiedenen Klassen leicht erkennbar werden.
Beide Lösungen muss man entsprechend bei einer Datenabfrage berücksichtigen.
Beispielsweise kann man in den Daten zwischen Vorname und Nachname unterscheiden und damit Person und Geschlecht trennen.

Für die eigene Datenerfassung stellt sich dann nur die Frage,  ob er für die Info ein Feld, oder zwei Felder in der Datenbank machen will.
Wenn ein Feld für unterschiedlich granulare Informationen verwendet wird, ist diese Schreibweise möglich:

**"von Taupaddel, Heinrich"**

Die Anfgabe vor dem Komma verweist dann zugleich auf das Geschlecht als höherrangige Kategorie.
Dann ist analog zu AP3 klar, dass nach dem Komma eine Verfeinerung der ersten Angabe kommt. Hier bedeutet Verfeinerung: Person als Repräsentant des Geschlechts
