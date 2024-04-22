# Managing space

:::info
This part of the documentation is still lacking information. It should give a brief summary of how we manage the concept of space in the DigiKAR project.
:::

The dataset contains place_geonames_id, place_geonames_latitude, place_geonames_longitude, place_name and place_name_variants. This enables the dataset to capture the uncertainty concerning place names and geolocation.

The column place_name provides the name of the places we derived either from secondary sources and literature or by interpreting the name of the place given in the primary sources.

The original place name given by primary sources or alternative place names found in secondary sources and literature can be found in the place_name_variants column.

Using the varchar data type for these columns allows for flexibility in representing uncertain or ambiguous place information. It accommodates various formats of place names or textual descriptions of dates, which is common in historical or fuzzy datasets.

The place_name is also used to generate the geolocation by using the Geonames API. Thus, we derive the coordinates and the Geonames ID of the place.

Overall, focusing on event-related place columns allows us to handle spatial uncertainty per archival factoid but may not be the ideal solution for all projects.

## Challenges of deriving place names

Abstract: Deriving modern place names from the information given in primary/secondary sources, literature, or other non georeferenced datasets can prove challenging. Place names still developed and varied greatly in the early modern period. Thus, one must use Gazetteers and traditional tools (e.g. Graesse: Orbis Latinus). However, identifying modern places with the information given mostly has to rely on different levels of uncertainty.

In our case, the origin of the place names is derived from the three sources used:
1) Mainly from the university registers (automatically recorded "source edition")
2) Partly also professor data (partly manually and partly automatically recorded secondary literature)
3) Partly from secondary literature on the RKG by Jahns (secondary literature)
Initially, the place names were automatically recorded from the respective sources and collated and compiled in an alphabetically sorted Excel list. 
Advantage: Similar spellings of a place name are often close to each other and are therefore easily recognisable and sometimes helpful for a person
Disadvantage: Additional information such as specifications of the place name was not recorded. Such information must be queried and taken into account during manual comparison.
An initially planned georeferencing of the place names recorded from the sources by Google and Geonames without further processing steps was not satisfactory, as only a few place names were recognised and even these were often implausibly located. Even the attempt to convert the source names into modern place names using ChatGPT was hardly successful, as ChatGPT lacks the necessary context. The following tedious manual assignment of a modern place name, recognisable for Google and Geonames, to the names in the sources is therefore necessary.
On the one hand, this requires a basic familiarity with early modern place name forms and the expected geographical area. Gazetteers.net can be helpful in resolving old spellings, as can the lagis database for places in Hesse. Otherwise, it is advisable to consult the registers of other (south-west German) universities, as students' names of origin often can be found there. It is also helpful to research possible places and old spellings in geographical lexicons of the 18th century. The Orbis Latinus can be useful for Latin place names, although it often does not cover smaller places and Latinised German place names (e.g. Asperavallis). In addition to the use of regional and local history literature, there is also the search in archive portals. If the assignment of the historical to a modern name form remained doubtful, this was labelled with the note "fraglich".
The frequent similarity of German place names is already problematic in the resolution of old or Latinised forms of names, and then also in the clear assignment to modern places. The safest and at the same time laborious and rarely successful way is to research the individual persons, assigned to the respective place name: Is there other evidence in the secondary literature or sources for the person or their family that can be clearly assigned to the place or a geographically close one? If this does not lead to a result, probabilities must be used: Does one of the possible places recommend itself, due to its local history or location in or near the archbishopric? What was the approximate size of the places in the early modern period? What was the denominational character of the place? If a place was clearly recommended above all others on the basis of these criteria, it was accepted. If the criteria did not clearly point to a place, a probable option was selected, and this was noted with the remark "unsicher"; if necessary, an equivalent alternative was given.
Even if the stated criteria and approach seem obvious and justified on the basis of previous research, especially on the Catholic University of Mainz, and the Catholic imperial chamber judges, apart from the usual uncertainties of historical research, it leads to a further problem: The assumption of places as more probable, if they were located in or near the archbishopric and were Catholic can possibly distort the results of the study in the direction of the previous research opinion as part of a self-fulfilling prophecy.
Once this time-consuming process of manually assigning the place names selected from the (secondary) sources to modern place names had been completed, the place ontology was automatically georeferenced on the basis of the latter. In our case, this was done using the Geonames API on the one hand and Google's API on the other. This resulted in the following problems, especially for Geonames:
1. Place names were not recognised due to typos or superfluous spaces.
2. Place names were not recognised because the respective specification was not stored. For example, Geonames cannot recognise Bischofsheim near Groß-Gerau, if the more common names Mainz-Bischofsheim or Bischofsheim, Mainspitze are used.
If orthographic errors and unassignable specifications of place names have been corrected manually, all places can be georeferenced. However, the assignment of the selected modern German place name to the object georeferenced by the API is often incorrect:
1. in particular, it can be seen that the APIs generally favour places located on the American continents over the (Central) European ones meant in our case. This must be corrected with additional geographical information. For example, a "Europe" is added to the place names for the query by the API.
2 However, as this step does not limit all georeferences to the expected area, further outliers in the visualisation of all georeferenced points must be identified manually and corrected using additional information (assignment to modern states and administrative units).
3. Although almost all points are located in the expected (Central) European area, a manual check of each individual georeferencing would hardly be feasible. For this reason, the two geo-references from Geonames and Google have now been automatically compared and, in the event of statistically relevant deviations, the modern name form has been re-examined and further specified.


## Cotrolling Geocoding results

After geocoding the derived modern place names with the API it is necessary to controll the results, since typically some of the places are matched with other places of the same name. This requires additional troubleshooting by hand or script.

## Places as virtual / relational spaces

Many places in AP3 denote connections that are not necessarily physical; see places of nobilitation. Many offices and titles awarded in the early modern period could be held by absent persons.

## Differentiating between places and territories

Some sources contain research speculations on which places within a country or region a person visited, e.g. "Österreich / Wien". Other regions which people visited are cultural regions whose borders or extensions can hardly be defined, e.g. "Wetterau" / "Wetteraviensis". Such places are identified by an entry in the place_type column.



## Dealing with spatial uncertainty in DigiKAR


