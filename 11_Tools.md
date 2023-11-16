<h1>Tools used or recommended by the DigiKAR project</h1>

<h2>Tools for data queries</h2>
<ul>
<li>
<a href="https://github.com/hassanhajj910/practicalsparql">PracticalSPARQL for integrating SPARQL-queries in Jupyter Notebooks:</a><br>
PracticalSPARQL is a package that facilitates the integration of SPARQL queries directly into Jupyter Notebooks. It simplifies querying RDF data, making it easier to work with knowledge graphs. Queries are stored in individual files within a 'queries' folder.
</li>
<li>
<a href="https://chpollin.github.io/GM-DH/">ChatGPT promt engineering for the Digital Humanities:</a><br>
ChatGPT is a language model that is now also used in the Digital Humanities, e.g. for data cleaning. For this purpose, humanities scholars need a better understanding of prompt engineering, which is why AI experts as well as humanities researchers experimenting with AI now offer specialised workshops.
</li>
</ul>

<h2>Tools for data visualization</h2>
<ul>
<li>
<a href="https://github.com/gicait/python-for-geospatial-data-analysis">Gicait for geospatial analysis with Python:</a><br>
Gicait offers tools and training sessions covering the fundamentals of Python programming for geospatial data analysis.
</li>
<li>
<a href="http://www.informatik.uni-leipzig.de/bsv/homepage/de/people/dr-stefan-j%C3%A4nicke">Visualization workflows for geodata:</a><br>
Stefan Jänicke provides suggested workflows for data visualisation.
</li>
<li>
<a href="http://www.informatik.uni-leipzig.de/~stjaenicke/balancing.pdf">Challenges of interdisciplinarity:</a><br>
Stefan Jänicke's document discusses the research challenges related to interdisciplinarity.
</li>
<li>
<a href="https://vega.github.io/vega-lite/examples/">Building elaborate visualizations with Vega-Lite:</a><br>
Vega-Lite is a high-level grammar for statistical graphics, akin to ggplot or Tableau. It generates complete Vega specifications [EXPLAIN], supporting various visualization types and interactive data exploration. This includes rule-based geovisualisations. One example is this
<a href="https://vega.github.io/vega-lite/examples/geo_rule.html">map of line segments connecting SEA to every Airport Reachable via Direct Flights</a>.
<a href="https://vega.github.io/vega-lite/tutorials/getting_started.html#data-transformation-aggregation">Quantity aggregation</a> [EXPLAIN] is also possible in Vega-Lite.</li>
<li>
<a href="https://en.wikipedia.org/wiki/Streamgraph">Streamgraphs</a> might be a visualization option for displaying the number of events per place and period in the Mainz work package. Streamgraphs depict data as a series of flowing, ribbon-like layers, with each layer representing a different category or variable. The thickness of a layer corresponds to the value of that category at a given point in time. Streamgraphs are particularly effective for illustrating changes in multivariate data.  Streamgraphs enable viewers to grasp temporal patterns, trends, and the relative contributions of various categories within the data at first glance. Tools like "D3.js" and "Streamgraph" in "Vega-Lite" help create streamgraphs.
</li>
<li>
<a href="https://github.com/sparqlunicorn/sparqlunicornGoesGIS">SPARQLing Unicorn for explorative visualizations in QGIS:</a><br>
SPARQLing Unicorn is a plugin for QGIS that enables explorative visualizations through flexible SPARQL queries. It directly adds a GeoJSON layer from SPARQL endpoint queries. For the integration of SPARQLing Unicorn with QGIS, consult the <a href="https://sparqlunicorn.github.io/sparqlunicornGoesGIS/">Doxygen Documentation</a>. You can download the plug-in <a href="https://plugins.qgis.org/plugins/sparqlunicorn/">here</a>.
</li>
</ul>

- [D3](https://d3js.org/) is an open-source JavaScript library for data visualization, in particular for interactive web visualization.
In contrast to other data popular visualization popular libraries (like *vega* or *vega-lite*) it follows a low level approach, making it a very flexible tool.
It is used for the more complex symbology for work package "Electoral Saxony".
- [maplibre GL JS](https://github.com/maplibre/maplibre-gl-js) is an open-source library for publishing web maps.
It enables the use of vector tiles.
Because of its GPU-accelerated rendering it is more performant than traditional map libraries such as *leaflet*.

## Databases

<p align="justify">Integrate tool review table (e.g., as file download and image) and briefly describe why different database tools needed to be tested in DigiKAR. Not all tools have to be described in detail as we can refer to the comments in the review table.</p>

- [PostgreSQL](https://www.postgresql.org/) with [PostGIS](https://postgis.net/), an open-source, spatial database extension. PostGIS enables PostgreSQL databases to manage and query geospatial data effectively. It provides support for geographic objects, spatial indexing, and a wide range of functions for geospatial analysis (e.g. creating voronoi polygons).
- [Metaphactory](https://metaphactory.com/") is a knowledge graph platform designed for managing and exploring semantic data. It allows users to create, search, and visualize linked data and knowledge graphs, making it a popular tool for researchers and organizations dealing with complex data relationships. In addition to the proprietary Metaphactory platform, the tool is available as ResearchSpace for those who can host their own instance. ResearchSpace was specifically designed for cultural heritage and digital humanities application. While ResearchSpace has a user base in research, Metaphactory's user community is more diverse. The choice between them depends on the specific requirements and financial means of your knowledge graph project or research.
- [Duckdb](https://duckdb.org/) is a free and open-source "in-process SQL OLAP database management system". It is optimized for analytical purposes, where querying and aggregating significant amount of data is required making a good fit to analyze data of work package "Electoral Mainz" where a large collection of individual events need to be grouped, aggregated and linked before they can be eventually visualized in a map.
