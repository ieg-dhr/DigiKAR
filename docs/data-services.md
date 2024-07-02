# Data services for (historical) geodata

This page presents a few German and international services that provide and / or accept (historical) geodata and can be useful for making project data more accessible and interoperable.

## World Historical Gazetteer (WHG)

The World Historical Gazetteer welcomes the contribution of new spatial data in two formats. While one format is ideal for smaller projects and less complex data, the more detailed JSON-based _Linked Places-Format_ allows the modelling of different ["relations"](https://github.com/LinkedPasts/linked-places-format) between places. Both formats are used to describe attestations of places in a standard way, primarily for linking gazetteer datasets.
The `relationType` property must be de-referenceable to an existing vocabulary or ontology. E.g., in the Getty Vocabulary Ontology, `broaderPartitive` relations are used to represent item parents in an administrative hierarchy. `tgn3317_member_of` and `tgn3318_member_is` relations can be used to represent political unions, empires, and regions.

The complete documentation is available on [GitHub](https://github.com/WorldHistoricalGazetteer/whgazetteer).

::: info
This part of the documentation is still missing. It should explain how we use the WHG in the DigiKAR project.
:::

## GOV

The [Historic Gazetteer GOV](http://www.gov.genealogy.net/search/index) (Geschichtliches Ortsverzeichnis), contributes to the exact identification of places, a critical aspect of genealogy and historical research. Unfortunately, not all researchers and history enthusiasts can devote time to this complicated process, which is why the GOV project was established, with the primary objective of assisting historians and genealogists in effectively managing place references while providing them with up-to-date resources. Over time, GOV aspires to offer a comprehensive resource with unified access to diverse location-based information. This includes geographical coordinates or map positioning of a place, various properties associated with a place (e.g. postal codes and town codes), historical data on foreign or former place names, and past affiliations (whether administrative, legal, or related to religious institutions). GOV's extensive database encompasses a wide range of entities, including churches, church districts, towns, districts, regions, and more, all internally referred to as "GOV objects." As of November 2014, GOV had cataloged approximately one million entries.

::: info
This part of the documentation is still missing. It should explain how we use the GOV in the DigiKAR project.
:::

## Historical Gazetteer of Saxony (HOV)

The [Historical Gazetteer of Saxony](https://hov.isgv.de/) (Historisches Ortsverzeichnis von Sachsen, HOV) lists almost all settlements, which have been documented for the territory of the modern federal state of Saxony since the Middle Ages. The individual HOV articles present a short spatial "biography" for each place and mention the historical and topographical development of villages and towns in Saxony.

::: info
This part of the documentation is still missing. It should explain how we use the HOV in the DigiKAR project.
:::

## Repertorium Saxonicum (RepSax)

The [Repertorium Saxonicum (RepSax)](https://repsax.isgv.de/) offers a glimpse into the rural world of the 16th century. This online database portrays the social, economic, and constitutional conditions of over 1,800 spatial entities within the Electorate of Saxony. It relies on a valuable resource known as the "Amtserbbücher" (official hereditary books). These records provide information about various aspects of these places, such as the number of land-owning farmers in a village and the taxes they paid. They also document who served as the judge in the village and the community's obligations in times of war, including participation in military campaigns. Therefore, the Repertorium Saxonicum is a rich source for understanding the historical context of life in 16th-century rural Saxony.

::: info
This part of the documentation is still missing. It should explain how we use the RepSax in the DigiKAR project.
:::

## Germania Sacra

[Germania Sacra](http://personendatenbank.germania-sacra.de/) is an Online-Portal that permits users to search a constantly growing databases of clerics and monasteries, convents and collegiate churches of the Holy Roman Empire. The focus is on biographical data and the history of institutions. The Germania Sacra team also contribute data to [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page). Moreover, the database entries are linked to the project’s many monographs. Digitised versions of these publications are freely available.

::: info
This part of the documentation is still missing. It should explain how we use Germania Sacra in the DigiKAR project.
:::

## Data services provided by the German federal states (e.g. LAGIS and LeoBW)

The different federal states in Germany also maintain their own data services, many of which include historical spatial data. Examples are the [Hessian Regional History Information System (LAGIS)](https://www.lagis-hessen.de/en) and the [Regional History Information System Baden-Württemberg (LEO-BW)](). LEO-BW provides a comprehensive exploration of southwestern Germany, offering insights into the region, its inhabitants, culture, and history. The information in LEO-BW is categorized into sections covering People, Places, Objects, Themes, and Highlights. For all locations in Baden-Württemberg, LEO-BW offers fundamental spatial information along with visual materials. Additionally, LEO-BW encompasses a wide range of objects from archival materials to photographs, maps, posters, and videos. LEO-BW shares similar functionality and objectives with LAGIS and similar federal services.

Unfortunately, information provided by these services is mainly stored as narrative text in content management systems for web deployment, not in consistently structured databases. Therefore, we could only use data from these services for individual data checks, not for automated data enrichment.

## Wikidata

[Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page) is a Linked Open Data project that also includes spatial data from various sources (see entry on Germania Sacra above). Wikidata can easily be queried via its own SPARQL service, but its data are often very fragmented. Spatial information on the Holy Roman Empire, for instance, cannot be systematically harvested via Wikidata alone, and future research efforts will be needed to improve the Wikidata database. For a critical analysis of Wikidata as a spatial data source, see Jan Macura's Czech-language thesis [Comparison of Wikidata and DBpedia projects as spatial data sources](https://zenodo.org/records/55381).

Although spatial data in Wikidata are not complete, we have experimented with place information and tried linking spatial attributes from Wikidata with our own data sets. A more consistent contribution of research results to Wikidata could considerably improve the data quality for future research projects.

## Geonames

Geonames is one of the most commonly used Gazetteers and also offers a geocoding API. Similar to the Getty Thesaurus of Geographic Names, Geonames offers "some level of data curation, nominally global coverage, but limited explicit information with respect to data quality". (Elise Acheson, Stefano De Sabbata, Ross S. Purves, [A quantitative analysis of global gazetteers: Patterns of coverage for common feature types](https://doi.org/10.1016/j.compenvurbsys.2017.03.007), in: Computers, Environment and Urban Systems, Volume 64, 2017, p. 309-320, ISSN 0198-9715.

In the DigiKAR project, we mainly use Geonames for geocoding place names in comparison with the Google API. Geocoding results for historical place names often require manual correction. For more information, visit the tutorial [Geocoding with the Geonames API in Python](https://monikabarget.github.io/GeoHumTutorials/Tutorial_geocodingGEONAMES).

Authors / contacts: Ingo Frank (IOS Regensburg), Jakob Listabarth (IfL Leibzig), Monika Barget (IEG Mainz, FASoS Maastricht)
