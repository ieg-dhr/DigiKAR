# Rights and right holders in Saxony

## Historiographical incentives of studying spatial dimensions of rights in early modern Saxony

::: info
This part of the documentation is still missing. It should give a brief summary of what the Saxony work package does and why this is important.
:::

## Structuring space through complex legal affiliations

The Saxony work package in DigiKAR focuses on the structuring of early modern space through the complex legal affiliations of individual landmarks (e.g. bridges and mills), non-inhabited areas (e.g. forests), settlements and individual estates within settlements. We focus on five rights out of many, and DigiKAR generally does not pretend that we can model *the* Holy Roman Empire with all its administrative bodies. The selected cases are already challenging because abstracting from the original sources to create normalised and structured data requires careful ontological decisions. For example, finding an overarching definition of early modern **"Landesherrschaft"** is difficult. Researchers have focused on military organization, imperial taxation, and certain offices or legal instruments as key elements, but they remain contested. In our own data collection, have therefore decided ...

::: info
This part of the documentation is still missing. It should explain where the data comes from, in which formats it is available and how it is collected. Add link to "Datenverfügbarkeitsstudie"?
:::

## Handling the relationship between rights and right holders

Also, we do not try to identify whether right holders are in charge by office or by inheritance. Our focus is more pragmatically on the fact that there is a spatial expression of a particular right and that one person, community, or non-person entity (e.g. “Rittergut”) holds that right at a particular point in time. Identifying the chain of command behind the right holders is beyond the scope of our project and also not immediately necessary for visualizing the legal space.

## Challenges of divergent data structures

In the course of normalizing database entries which we could import from the historical gazetteers [HOV](https://hov.isgv.de/") and [RepSax](https://repsax.isgv.de/), we encountered, among other things, an inconsistent recording of the rights holders, especially regarding the so-called **"Grundherrschaft"** in the manorial system. Right holders are sometimes indicated as individuals, but the family seat is mentioned in other cases.

In the **Repertorium Saxonicum (RepSax)**, for instance, we find the variants "von Taupaddel" and "Heinrich von Taupaddel" - the former being an instance of the class 'family,' the latter an instance of the class 'person.' In **HOV**, editors often entered non-person entities like "Rittergut Schleinitz" for data simplification.

It can be difficult to discern if rights were held by a person or by someone representing a specific hereditary line. This is complicated because groups exercising power became more diverse during the early modern period. In the study ["Bürgerliche Rittergüter : sozialer Wandel und politische Reform in Kursachsen (1680 - 1844)"](https://digi20.digitale-sammlungen.de/de/fs1/object/display/bsb00056061_00147.html), the author states that "bourgeois groups [also] came into possession of the manors," which, in the sense of depicting social change, might require a more detailed categorization of right holders, based on the activities and functions/roles of persons.

Pages 41-42 explain:

> "The current owner of a knight's estate was not considered an individual owner in Saxon feudal law. Rather, the property belonged to a social association. This was either a family, based mainly on continuity in father-son succession, or the group around a vassal and fellow vassal, possibly forming a 'familia' in the older pre-modern sense. (Flügel (2000. 54)"

The current diversity of data in repositories that cover the early modern period leads to problems with data preparation and integration into a new database structure. Ideally, each database field should contain a single type of data. Assigning several possible classes to data in one data column can cause issues with the long-term interoperability and reusability of the data. It is a challenge to structure diverse data in a way that makes different ontological classes immediately transparent.

If one database field in our own data model is used for differently granular information, this notation is possible:

| string                    | type              |
| ------------------------- | ----------------- |
| `von Taupaddel, Heinrich` | individual person |
| `von Taupaddel`           | family or group   |
| `Schleinitz, Rittergut`   | non-person entity |

Capturing only the information before the comma would allow a clear affiliation with the manorial family as a higher-ranking category in all three cases. Analogous to data modeling in WP3, it is clear that after the comma comes a refinement of the first specification. Here, refinement means a _person as a family representative_. Additional data enrichment may be needed depending on the research question's context.

Concerning the territorial administration, we find a similar diversity of agents. The category **"(landesherrliche) Amtsträger"** can include:

- Hof- und Justitienräte
- Kammerräte
- Akzisräte (affiliated with "Landesbehörden")
- Stiftsräte (affiliated with "Landesbehörden")
- Amtsschösser
- Amtsrentverwalter
- Amtmänner (of the local administration)
