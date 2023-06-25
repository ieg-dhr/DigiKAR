## Rights holders in Saxony - challenges of the data structure

In the course of normalising the HOV and RepSax database entries, we came across, among other things, an inconsistent recording of the rights holders, especially concerning the so-called "Grundherrschaft" in the manorial system. In the study ["Bürgerliche Rittergüter : sozialer Wandel und politische Reform in Kursachsen (1680 - 1844)"](https://digi20.digitale-sammlungen.de/de/fs1/object/display/bsb00056061_00147.html), the author states that "bourgeois groups [also] came into possession of the manors", which, in the sense of depicting social change, makes a categorisation based on the activities and functions/roles of persons seem sensible.

Moreover, we need to find visualisation approaches reflecting possible connections between geodata and the biographical data to illustrate phenomena of social change and, if necessary, to discover spatial patterns through them.

In and under table 23, one finds the following "social groups of bourgeois manor owners": 'office holders', 'educated', 'merchants', 'military', 'farmers'.

The category "(Landesherrliche) Amtsträger" can include:
- Hof- und Justitienräte,
- Kammerräte,
- Akzisräte (affiliated with "Landesbehörden")
- Stiftsräte (affiliated with "Landesbehörden")
- Amtsschösser
- Amtsrentverwalter
- Amtmänner (of the local administration)

*"sowohl die Hof- und Justitienräte, Kammerräte, Akzisräte und Stiftsräte der Landesbehörden als auch die Amtsschösser, 
Amtsrentverwalter und Amtmänner der Lokalverwaltung"*

The following passage from the book already cited above (pages 41-42) can explain many of the inconsistent entries in the HOV and RepSax data:

"Der aktuelle Inhaber eines Rittergutes wurde im sächsischen Lehnrecht *nicht* als individueller Eigentümer betrachtet. 
Der Besitz stand vielmehr einem sozialen Verband zu. Dabei handelte sich entweder um ein Geschlecht, d.h. in der Hauptsache um die Kontinuität in der Vater-Sohn Abfolge,
oder um die Gruppe aus Vasall und Mitbelehnten, die möglicherweise eine »familia« im älteren vormodernen Sinn des Wortes bildete." (Flügel (2000. 54)"

"The current owner of a knight's estate was not considered an individual owner in Saxon feudal law. Rather, the property belonged to a social association. This was either a gender, i.e. mainly continuity in father-son succession, or the group of a vassal and fellow vassal, possibly forming a 'familia' in the older pre-modern sense of the word." (Flügel (2000. 54)"

This is why the existing databases sometimes contain an individual person (as a member of one family), but sometimes only or explicitly the gender.

**Example in RepSax**: "von Taupaddel" vs. "Heinrich von Taupaddel" - the former is an instance of the class 'family', the latter an instance of the class 'person'.
In **HOV**, editors often entered non-person entities like "Rittergut Schleinitz" for data simplification.

Regardless of an exact classification, there is the problem that the data would ideally be more uniform. The current diversity of data leads to problems with data preparation and integration/normalisation. Depending on the context of the research question, a different perspective classification may be needed.

Suppose the same interpretational level is only sometimes used in the same database field. In that case, one must assign several possible classes to the data and initially leave the exact assignment open or structure the data so that the different ontological classes are easily recognisable. Both solutions must be taken into account accordingly in a data query. For example, one can distinguish between first and last names in the data and thus separate person and gender.

For additional data entry, the question is whether you want to assign one or more fields in the database. If one field is used for differently granular information, this notation is possible:

**"von Taupaddel, Heinrich"** (individual person)
**"von Taupaddel"** (family / group)
**"Schleinitz, Rittergut"** (non-person entity)

Capturing only the information before the comma would allow a clear affiliation with the manorial family as a higher-ranking category in all three cases. Analogous to data modelling in WP3, it is clear that after the comma comes a refinement of the first specification. Here, refinement means a *person as a representative of the family*.
