
<h1>Data visualisation in DigiKAR</h1>

<h2>Goals and challenges</h2>
<p align="justify">
The <a href="https://digikar.eu/">DigiKAR geo-humanities project</a> (<strong>Digital Map Lap Holy Roman Empire</strong>) is an interdisciplinary and international project led by the Institute of European History in Mainz and funded by the German Leibniz Association from 2021 to 2024. It questions established visual representations of a historical space whose legal and political complexity is only insufficiently captured through polygons and line-oriented maps with narrow thematic foci. As a fractured yet interwoven territory, the Holy Roman Empire and its individual, often overlapping or contested regions require multi-modal and multi-perspective visualizations. By proto-typically tracing human, material, and ideational border-crossings and competing spatial conceptions, the project addresses the central challenges of both traditional imperial historiography and digital historical research.
</p>

<p align="justify">One primary focus of DigiKAR is to understand data visualisations as both explorational and educational tools. Our approach to (geo)visualisations is marked by the following four statements:</p>
<ul>
<li>Visualisations (in the plural), not ONE visualisation!</li>
<li>Visualisations not at the end of a project, but throughout!</li>
<li>Visualisations not only by "experts," but also by students!</li>
<li>Visualisations on various levels of complexity!</li>
</ul>
<p align="justify">
Bringing together interdisciplinary researchers as well as heritage professionals and students, the DigiKAR project uses maps for high-level data evaluation, data cleaning, a critical reflection on our own research biases, and as tools to highlight developments and alternative views of our data. At a later stage, more elaborate visualizations as tools of science communication will follow.
</p>
<img class="wp-image-638 alignleft" src="https://insulae.hypotheses.org/files/2022/08/5-300x169.jpg" alt="slide with map" width="351" height="198" align="left" target="_blank" style="padding: 10px;" />
<p align="justify">
The image gives an example of a static map created for DigiKAR: In this map, lines are connecting early modern migrants' places of birth with places where birth or apprenticeship letters were issued. These letters are the early modern versions of passports and other certificates. The spatial data behind this map came from early modern manuscript records kept at the City Archives in Mainz, Germany.
</p>

<p align="justify">
Some metadata had already been digitized, other data were collected by a team of MA students who transcribed letters from scratch. The visualization displayed here was created by MA student Maximilian Michel and helped us understand the often impressive distances across which early modern agents would relocate for private or professional reasons.
</p>

<h3>Visualisation as storytelling</h3>
<img class="wp-image-633 alignleft" src="https://insulae.hypotheses.org/files/2022/08/3-300x169.jpg" alt="slide with map" width="344" height="194" align="left" target="_blank" style="padding: 10px;" />
<p align="justify">
Overall, we view visualizations as a storytelling device on two levels.
On the one hand, maps help us to tell history from different perspectives and to make "gaps" and ambiguities visible.
On the other hand, visualizations tell the story of our research process and make (changing) research questions transparent.
</p>

<p align="justify">
The slide on the left gives an example of the narrative embedding of visualizations in our project.
The DigiKAR pilot project "<a href="https://teaching-dhlab.pages.gitlab.rlp.net/geburtsbriefemainz/home/">Early modern birth letters from Mainz</a>", which we completed in August 2021, combines a digital edition of multi-lingual text sources, different maps, and academic content. A second mapping experiment, carried out with MA students of history in 2022, covers the <a href="https://clerical-mobility.ieg-mainz.de/">professional biographies of high-ranking clerics in the Prince-Archbishopric of Mainz</a>.
</p>
<p align="justify">
<img class="wp-image-640 alignleft" src="https://insulae.hypotheses.org/files/2022/08/6-300x169.jpg" alt="slide with map" width="346" height="195" align="left" target="_blank" style="padding: 10px;" />
<p align="justify">
All in all, the process of creating visualizations such as maps for historical research projects is like an iceberg. The visual output is only the uppermost part. Also, historians cannot rely on just one tool or methodology. Sources must constantly be analyzed in comparison with others, including sources of entirely different genres. This also requires seeing abstract structures in text and reading historic maps as narratives. Visualizations we create are hardly ever final but reflect work in progress. This is why the DigiKAR project shares data tables, scripts and exemplary visualizations on GITHUB where they can be easily updated and versioned. At the same time, we want our data to be inter-operable and open for re-use, which is why we apply established data models whenever possible. Beyond the specific research questions of the DigiKAR project, we intend our data modelling and visualization efforts to serve as samples for similar humanities projects. As explained in this presentation, our maps are not primarily research output but flexible tools of exploration. Moreover, experienced historians, as well as students and interns, benefit from making maps themselves as it challenges them to name uncertainties and ambiguities in their research data.
</p>

<h3>What data are being visualised in DigiKAR?</h3>

The data that we visualise in DigiKAR is -- similar to many other historical projects -- highly fragmented and come from various sources. 
First of all, we work with spatial data extracted from textual (narrative) early modern sources (both in the form of archival manuscripts and printed books). 
Secondly, we work with spatial data extracted from early modern maps (using OCR technology for identifying place names). 
Thirdly, we are re-using historical spatial data originally gathered by historians in previous decades (some of which have already been digitised and made available via APIs).

<strong>The workflow in our project includes 6 main steps:</strong>
<ul>
 	<li>semi-automated data collection in spreadsheets (using Python for web-scraping)</li>
 	<li>semi-automated data normalisation and data cleaning</li>
 	<li>geocoding with Google and Open Street Map APIs (incl. manual corrections)</li>
 	<li>preliminary, experimental geo-visualisations in QGIS</li>
 	<li>import of consolidated data into <a href="https://metaphacts.com/">Metaphacts</a> (graph database) and/or a relational GIS database</li>
 	<li>advanced data queries and advanced visualisations created by the cartography team at <a href="https://leibniz-ifl.de/">IfL Leipzig</a></li>
</ul>

<h3>(Automated) geocoding</h3>

<p align="justify">[Link Monika's blogpost here!]</p>

<h3>What do we consider "base maps"?</h3>

<p align="justify">The DigiKAR team have given a lot of thought to the basemaps used for the sample visualisations. While modern maps including infrastructures and major settlements generally offer users the best spatial orientation, those maps raise
many problems from a historiographical perspective. Our final decision is to work with a simple geographical map on which we project some of the most important early modern cities as the standard base map. We deliberately avoid topographic maps that include additional geological information on heights and distances.
Other maps are then used as optional backgrounds, including georeferenced versions of research maps of the Holy Roman Empire and its territories.</p>

<h3>Interpolating "territories" as Voronoi polygones</h3>

<p align="justify">[ADD TEXT]</p>

<h3>Further information</h3>
<p align="justify">
If you want to find out more about DigiKAR, you are welcome to visit <a href="https://digikar.eu/">our website</a>. Questions can be addressed to <a href="mailto:digikar@ieg-mainz.de">digikar@ieg-mainz.de</a>. Project manager Constanze Buyken will be happy to respond.
You are also welcome to download the full conference presentation containing the displayed slides: <a href="https://insulae.hypotheses.org/files/2022/08/Blog_VisualizationAsExploration.pdf">Blog_VisualizationAsExploration</a>
</p>
