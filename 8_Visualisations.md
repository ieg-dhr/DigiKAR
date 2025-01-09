
# Data visualisation in DigiKAR

## Goals and challenges

{:.justified}
The [DigiKAR geo-humanities project](https://digikar.eu/) (**Digital Map Lap Holy Roman Empire**) is an interdisciplinary and international project led by the Institute of European History in Mainz and funded by the German Leibniz Association from 2021 to 2024. It questions established visual representations of a historical space whose legal and political complexity is only insufficiently captured through polygons and line-oriented maps with narrow thematic foci. As a fractured yet interwoven territory, the Holy Roman Empire and its individual, often overlapping or contested regions require multi-modal and multi-perspective visualizations. By proto-typically tracing human, material, and ideational border-crossings and competing spatial conceptions, the project addresses the central challenges of both traditional imperial historiography and digital historical research.

{:.justified}
One primary focus of DigiKAR is to understand data visualisations as both explorational and educational tools. Our approach to (geo)visualisations is marked by the following four statements:

- Visualisations (in the plural), not ONE visualisation!
- Visualisations not at the end of a project, but throughout!
- Visualisations not only by "experts," but also by students!
- Visualisations on various levels of complexity!

{:.justified}
Bringing together interdisciplinary researchers as well as heritage professionals and students, the DigiKAR project uses maps for high-level data evaluation, data cleaning, a critical reflection on our own research biases, and as tools to highlight developments and alternative views of our data. At a later stage, more elaborate visualizations as tools of science communication will follow.

![slide with map](https://insulae.hypotheses.org/files/2022/08/5-300x169.jpg){:width="351px" height="198px" style="padding: 0 1em 0 0;float:left;"}

{:.justified}
The image gives an example of a static map created for DigiKAR: In this map, lines are connecting early modern migrants' places of birth with places where birth or apprenticeship letters were issued. These letters are the early modern versions of passports and other certificates. The spatial data behind this map came from early modern manuscript records kept at the City Archives in Mainz, Germany.

{:.justified}
Some metadata had already been digitized, other data were collected by a team of MA students who transcribed letters from scratch. The visualization displayed here was created by MA student Maximilian Michel and helped us understand the often impressive distances across which early modern agents would relocate for private or professional reasons.


### Visualisation as storytelling

![slide with screenshot](https://insulae.hypotheses.org/files/2022/08/3-300x169.jpg){:width="351px" height="198px" style="padding: 0 1em 0 0;float:left;"}

{:.justified}
Overall, we view visualizations as a storytelling device on two levels.
On the one hand, maps help us to tell history from different perspectives and to make "gaps" and ambiguities visible.
On the other hand, visualizations tell the story of our research process and make (changing) research questions transparent.

{:.justified}
The slide on the left gives an example of the narrative embedding of visualizations in our project.
The DigiKAR pilot project ["Early modern birth letters from Mainz"](https://teaching-dhlab.pages.gitlab.rlp.net/geburtsbriefemainz/home/), which we completed in August 2021, combines a digital edition of multi-lingual text sources, different maps, and academic content. A second mapping experiment, carried out with MA students of history in 2022, covers the [professional biographies of high-ranking clerics in the Prince-Archbishopric of Mainz](https://clerical-mobility.ieg-mainz.de/).

![slide with experiments](https://insulae.hypotheses.org/files/2022/08/6-300x169.jpg){:width="351px" height="198px" style="padding: 0 1em 0 0;float:left;"}

{:.justified}
All in all, the process of creating visualizations such as maps for historical research projects is like an iceberg. The visual output is only the uppermost part. Also, historians cannot rely on just one tool or methodology. Sources must constantly be analyzed in comparison with others, including sources of entirely different genres. This also requires seeing abstract structures in text and reading historic maps as narratives. Visualizations we create are hardly ever final but reflect work in progress. This is why the DigiKAR project shares data tables, scripts and exemplary visualizations on GITHUB where they can be easily updated and versioned. At the same time, we want our data to be inter-operable and open for re-use, which is why we apply established data models whenever possible. Beyond the specific research questions of the DigiKAR project, we intend our data modelling and visualization efforts to serve as samples for similar humanities projects. As explained in this presentation, our maps are not primarily research output but flexible tools of exploration. Moreover, experienced historians, as well as students and interns, benefit from making maps themselves as it challenges them to name uncertainties and ambiguities in their research data.

### What data are being visualised in DigiKAR?

The data that we visualise in DigiKAR is -- similar to many other historical projects -- highly fragmented and come from various sources.
First of all, we work with spatial data extracted from textual (narrative) early modern sources (both in the form of archival manuscripts and printed books).
Secondly, we work with spatial data extracted from early modern maps (using OCR technology for identifying place names).
Thirdly, we are re-using historical spatial data originally gathered by historians in previous decades (some of which have already been digitised and made available via APIs).

** The workflow in our project includes 6 main steps:**

- semi-automated data collection in spreadsheets (using Python for web-scraping)
- semi-automated data normalisation and data cleaning
- geocoding with Google and Open Street Map APIs (incl. manual corrections)
- preliminary, experimental geo-visualisations in QGIS
- import of consolidated data into [Metaphacts](https://metaphacts.com/) (graph database) and/or a relational GIS database
- advanced data queries and advanced visualisations created by the cartography team at [IfL Leipzig](https://leibniz-ifl.de/)

### (Automated) geocoding

{:.justified}
In work package 3 "Kurmainz" within DigiKAR project, we have performed our initial geocoding of place names with the Google and Geonames API, comparing and manually correcting the results. As we had decided to focus on a settlement level rather than visualising individual institutions / estates, the results of the automated geocoding were sufficient although the exact point coordinates for modern places are now often located outside the historical centres. In most cases, the Geonames results were preferred to the Google results. Smaller places, especially those that are now part of larger administrative units, could not be found via the automated geocoding and were added by Sven Dittmar and student assistants at Mainz University. 

In work package 2 "Kursachsen", we received geodata for most spatial entities from existing data sources such as the historical gazetteers for Saxony. Therefore, no from-scratch geocoding was performed here.

:::info
For details on our geocoding process and our challenges in the Mainz work package, also consult Monika Barget's blog posts on [geocoding with the Geonames API](https://insulae.hypotheses.org/2040) and [geocoding with the Google API](https://insulae.hypotheses.org/2123).
:::

### What do we consider "base maps"?

{:.justified}
The DigiKAR team have given a lot of thought to the basemaps used for the sample visualisations. While modern maps including infrastructures and major settlements generally offer users the best spatial orientation, those maps raise
many problems from a historiographical perspective. Our final decision is to work with a simple geographical map on which we project some of the most important early modern cities as the standard base map. We deliberately avoid topographic maps that include additional geological information on heights and distances.
Other maps are then used as optional backgrounds, including georeferenced versions of research maps of the Holy Roman Empire and its territories.

### Interpolating "territories" as Voronoi polygones

{:.callout.todo}
Add Text

### Further information

{:.justified}
If you want to find out more about DigiKAR, you are welcome to visit [our website](https://digikar.eu/). Questions can be addressed to [digikar@ieg-mainz.de](mailto:digikar@ieg-mainz.de). Project manager Constanze Buyken will be happy to respond.
You are also welcome to download the [full conference presentation](https://insulae.hypotheses.org/files/2022/08/Blog_VisualizationAsExploration.pdf), containing the displayed slides.
