<h2>Rights and right holders in Saxony</h2>

<h3>Structuring space through complex legal affiliations</h3>

<a align="justify">Summary of what the Saxony work package does and why this is important...</p>

<p align="justify">Also, finding an overarching definition of early modern <strong>"Landesherrschaft"</strong> is difficult. Researchers have focused on military organization, imperial taxation, and certain offices or legal instruments as key elements, but they remain contested.</p>

<h3>Data collection</h3>

<a align="justify">From what sources and in which formats does the work package collect data?</p>

<h3>Challenges of divergent data structures</h3>

<p align="justify">In the course of normalizing the HOV and RepSax database entries, we encountered, among other things, an inconsistent recording of the rights holders, especially regarding the so-called <strong>"Grundherrschaft"</strong> in the manorial system. Right holders are sometimes indicated as individuals, but the family seat is mentioned in other cases.</p>

<p align="justify">In the <strong>Repertorium Saxonicum (RepSax)</strong>, for instance, we find the variants "von Taupaddel" and "Heinrich von Taupaddel" - the former being an instance of the class 'family,' the latter an instance of the class 'person.' In <strong>HOV</strong>, editors often entered non-person entities like "Rittergut Schleinitz" for data simplification.</p>

<p align="justify">It can be difficult to discern if rights were held by a person or by someone representing a specific hereditary line. This is complicated because groups exercising power became more diverse during the early modern period. In the study <a href="https://digi20.digitale-sammlungen.de/de/fs1/object/display/bsb00056061_00147.html">"Bürgerliche Rittergüter : sozialer Wandel und politische Reform in Kursachsen (1680 - 1844)"</a>, the author states that "bourgeois groups [also] came into possession of the manors," which, in the sense of depicting social change, might require a more detailed categorization of right holders, based on the activities and functions/roles of persons.</p>

<p>Pages 41-42 explain:</p>

<blockquote>
  <p align="justify">"The current owner of a knight's estate was not considered an individual owner in Saxon feudal law. Rather, the property belonged to a social association. This was either a family, based mainly on continuity in father-son succession, or the group around a vassal and fellow vassal, possibly forming a 'familia' in the older pre-modern sense. (Flügel (2000. 54)"</p>
</blockquote>

<p align="justify">The current diversity of data in repositories that cover the early modern period leads to problems with data preparation and integration into a new database structure. Ideally, each database field should contain a single type of data. Assigning several possible classes to data in one data column can cause issues with the long-term interoperability and reusability of the data. It is a challenge to structure diverse data in a way that makes different ontological classes immediately transparent.</p>

<p align="justify">If one database field in our own data model is used for differently granular information, this notation is possible:</p>
<blockquote>
  <p><strong>"von Taupaddel, Heinrich"</strong> (individual person)</p>
  <p><strong>"von Taupaddel"</strong> (family / group)</p>
  <p><strong>"Schleinitz, Rittergut"</strong> (non-person entity)</p>
</blockquote>

<p align="justify">Capturing only the information before the comma would allow a clear affiliation with the manorial family as a higher-ranking category in all three cases. Analogous to data modeling in WP3, it is clear that after the comma comes a refinement of the first specification. Here, refinement means a <em>person as a family representative</em>. Additional data enrichment may be needed depending on the research question's context.</p>

<p align="justify">Concerning the territorial administration, we find a similar diversity of agents. The category <strong>"(landesherrliche) Amtsträger"</strong> can include:</p>

<ul>
  <li>Hof- und Justitienräte</li>
  <li>Kammerräte</li>
  <li>Akzisräte (affiliated with "Landesbehörden")</li>
  <li>Stiftsräte (affiliated with "Landesbehörden")</li>
  <li>Amtsschösser</li>
  <li>Amtsrentverwalter</li>
  <li>Amtmänner (of the local administration)</li>
</ul>
