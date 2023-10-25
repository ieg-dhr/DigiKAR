# Data services for (historical) geodata

<p align="justify">This page presents a few German and international services that provide and / or accept (historical) geodata and can be useful for making project data more accessible and interoperable.

## World Historical Gazetteer (WHG)

<p align="justify">The World Historical Gazetteer welcomes the contribution of new spatial data in two formats. While one format is ideal for smaller projects and less complex data,
the more detailed JSON-based <em>Linked Places-Format</em> allows the modelling of different <a href="﻿https://github.com/LinkedPasts/linked-places-format">"relations"</a>﻿ between places. Both formats are used to describe attestations of places in a standard way, primarily for linking gazetteer datasets. 
The <code>relationType</code> property must be de-referenceable to an existing vocabulary or ontology. E.g., in the Getty Vocabulary Ontology, <code>broaderPartitive</code> relations are used to represent item parents in an administrative hierarchy. <code>tgn3317_member_of</code> and <code>tgn3318_member_is</code> relations can be used to represent political unions, empires, and regions.</p>

<p align="justify">The complete documentation is available on <a href="https://github.com/WorldHistoricalGazetteer/whgazetteer">GitHub</a>.

<p align="justify">[ADD TEXT HOW WE USE THIS RESOURCE IN DIGIKAR]</p>

## GOV

<p align="justify">The <a href="http://www.gov.genealogy.net/search/index">Historic Gazetteer GOV</a> (Geschichtliches Ortsverzeichnis), contributes to the exact identification of places, a critical aspect of genealogy and historical research. Unfortunately, not all researchers and history enthusiasts can devote time to this complicated process, which is why the GOV project was established, with the primary objective of assisting historians and genealogists in effectively managing place references while providing them with up-to-date resources. Over time, GOV aspires to offer a comprehensive resource with unified access to diverse location-based information. This includes geographical coordinates or map positioning of a place, various properties associated with a place (e.g. postal codes and town codes), historical data on foreign or former place names, and past affiliations (whether administrative, legal, or related to religious institutions). GOV's extensive database encompasses a wide range of entities, including churches, church districts, towns, districts, regions, and more, all internally referred to as "GOV objects." As of November 2014, GOV had cataloged approximately one million entries.</p>

<p align="justify">[ADD TEXT HOW WE USE THIS RESOURCE IN DIGIKAR]</p>

## HOV

<p align="justify"></p>


<p align="justify">[ADD TEXT HOW WE USE THIS RESOURCE IN DIGIKAR]</p>

## RepSax

<p align="justify">The <a href="https://repsax.isgv.de/">Repertorium Saxonicum</a> offers a glimpse into the rural world of the 16th century. This online database portrays the social, economic, and constitutional conditions of over 1,800 spatial entities within the Electorate of Saxony. It relies on a valuable resource known as the "Amtserbbücher" (official hereditary books). These records provide information about various aspects of these places, such as the number of land-owning farmers in a village and the taxes they paid. They also document who served as the judge in the village and the community's obligations in times of war, including participation in military campaigns. Therefore, the Repertorium Saxonicum is a rich source for understanding the historical context of life in 16th-century rural Saxony.</p>

<p align="justify">[ADD TEXT HOW WE USE THIS RESOURCE IN DIGIKAR]</p>

## Germania Sacra

<p align="justify"><a href="http://personendatenbank.germania-sacra.de/">Germania Sacra</a> is an Online-Portal that permits users to search a constantly growing databases of clerics and monasteries, convents and collegiate churches of the Holy Roman Empire. The focus is on biographical data and the history of institutions. The Germania Sacra team also contribute data to <a href="https://www.wikidata.org/wiki/Wikidata:Main_Page">Wikidata</a>. Moreover, the database entries are linked to the project’s many monographs. Digitised versions of these publications are freely available.</p>

<p align="justify">[ADD TEXT HOW WE USE THIS RESOURCE IN DIGIKAR]</p>

## Data services provided by the German federal states (e.g. LAGIS and LeoBW)

<p align="justify">The different federal states in Germany also maintain their own data services, many of which include historical spatial data. Examples are the <a href="https://www.lagis-hessen.de/en">Hessian Regional History Information System (LAGIS)</a> and the <a href="">Regional History Information System Baden-Württemberg (LEO-BW)</a>. LEO-BW provides a comprehensive exploration of southwestern Germany, offering insights into the region, its inhabitants, culture, and history. The information in LEO-BW is categorized into sections covering People, Places, Objects, Themes, and Highlights. For all locations in Baden-Württemberg, LEO-BW offers fundamental spatial information along with visual materials. Additionally, LEO-BW encompasses a wide range of objects from archival materials to photographs, maps, posters, and videos. LEO-BW shares similar functionality and objectives with LAGIS and similar federal services.</p>

<p align="justify">[ADD TEXT HOW WE USE THIS RESOURCE IN DIGIKAR]</p>

## Wikidata

<p align="justify"><a href="https://www.wikidata.org/wiki/Wikidata:Main_Page">Wikidata</a> is a Linked Open Data project that also includes spatial data from various sources (see entry on Germania Sacra above). Wikidata can easily be queried via its own SPARQL service, but its data are often very fragmented. Spatial information on the Holy Roman Empire, for instance, cannot be systematically harvested via Wikidata alone, and future research efforts will be needed to improve the Wikidata database. For a critical analysis of Wikidata as a spatial data source, see Jan Macura's Czech-language thesis <a href="https://zenodo.org/records/55381">Comparison of Wikidata and DBpedia projects as spatial data sources</a>.</p>

<p align="justify">[ADD TEXT HOW WE USE THIS RESOURCE IN DIGIKAR]</p>

# Geonames

<p align="justify">Geonames is one of the most commonly used Gazetteers and also offers a geocoding API. Similar to the the Getty Thesaurus of Geographic Names, Geonames offers "some level of data curation, nominally global coverage, but limited explicit information with respect to data quality". (Elise Acheson, Stefano De Sabbata, Ross S. Purves, <a href="https://doi.org/10.1016/j.compenvurbsys.2017.03.007">A quantitative analysis of global gazetteers: Patterns of coverage for common feature types</a>, in: Computers, Environment and Urban Systems, Volume 64, 2017, p. 309-320, ISSN 0198-9715.</p>

<p align="justify">In the DigiKAR project, we mainly use Geonames for geocoding place names in comparison with the Google API. Geocoding results for historical place names often require manual correction. For more information, visit the tutorial <a href="https://monikabarget.github.io/GeoHumTutorials/Tutorial_geocodingGEONAMES">Geocoding with the Geonames API in Python</a>.</p>
