## Rights holders in Saxony - challenges of the data structure

In the course of normalising the HOV and RepSax database entries, we came across, among other things, an inconsistent recording of the rights holders, especially concerning the so-called **"Grundherrschaft"** in the manorial system. Right holders are sometimes indicated as individuals, but the family seat is mentioned in other cases. 

In **RepSax**, for instance, we find the variants "von Taupaddel" and "Heinrich von Taupaddel" - the former being an instance of the class 'family', the latter an instance of the class 'person'. In **HOV**, editors often entered non-person entities like "Rittergut Schleinitz" for data simplification.

It can be difficult to discern if rights were held by a person or by someone representing a specific hereditary line. This is complicated because groups exercising power became more diverse during the early modern period. In the study ["Bürgerliche Rittergüter : sozialer Wandel und politische Reform in Kursachsen (1680 - 1844)"](https://digi20.digitale-sammlungen.de/de/fs1/object/display/bsb00056061_00147.html), the author states that "bourgeois groups [also] came into possession of the manors", which, in the sense of depicting social change, might require a more detailed categorisation of right holders, based on the activities and functions/roles of persons.

Pages 41-42 explain: 

"Der aktuelle Inhaber eines Rittergutes wurde im sächsischen Lehnrecht *nicht* als individueller Eigentümer betrachtet. Der Besitz stand vielmehr einem sozialen Verband zu. Dabei handelte sich entweder um ein Geschlecht, d.h. in der Hauptsache um die Kontinuität in der Vater-Sohn Abfolge, oder um die Gruppe aus Vasall und Mitbelehnten, die möglicherweise eine »familia« im älteren vormodernen Sinn des Wortes bildete. (Flügel (2000. 54)"

"The current owner of a knight's estate was not considered an individual owner in Saxon feudal law. Rather, the property belonged to a social association. This was either a gender, i.e. mainly continuity in father-son succession, or the group of a vassal and fellow vassal, possibly forming a 'familia' in the older pre-modern sense. (Flügel (2000. 54)"

The current diversity of data leads to problems with data preparation and integration into a database structure. Ideally, each database field should contain a single type of data. Assigning several possible classes to data in one data column can cause issues with the long-term interoperability and reusability of the data. It is a challenge to structure diverse data in a way that makes different ontological classes immediately transparent. If one database field is used for differently granular information, this notation is possible:

**"von Taupaddel, Heinrich"** (individual person)
**"von Taupaddel"** (family / group)
**"Schleinitz, Rittergut"** (non-person entity)

Capturing only the information before the comma would allow a clear affiliation with the manorial family as a higher-ranking category in all three cases. Analogous to data modelling in WP3, it is clear that after the comma comes a refinement of the first specification. Here, refinement means a *person as a family representative*. Additional data enrichment may be needed depending on the research question's context.

Concerning the territorial administration, we find a similar diversity of agents. The category **"(landesherrliche) Amtsträger"** can include:
- Hof- und Justitienräte,
- Kammerräte,
- Akzisräte (affiliated with "Landesbehörden")
- Stiftsräte (affiliated with "Landesbehörden")
- Amtsschösser
- Amtsrentverwalter
- Amtmänner (of the local administration)
