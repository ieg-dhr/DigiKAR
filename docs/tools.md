# Tools used or recommended by the DigiKAR project

Different tools and the appropriate underlying database technologies are needed in the various phases of the research data life cycle (see the phases of the historical information life cycle presented in the report [Past, present and future of histortical information science](http://library.oapen.org/handle/20.500.12657/34839): _creation_, _enrichment_, _editing_, _retrieval_, _analysis_, _presentation_.) in order to support the phases from data creation to querying the enriched, edited and interlinked data for various visualization purposes (incl. e.g. explorative analysis). in general, a selection of tools for DigiKAR has to be used in the following tasks.

1. create data: create data by extracting information from historical sources; reusing existing datasets
2. enrichment: enrich data (enhancement, normalization), add information from authority files (e.g. gazetteers), georeference entries
3. editing: record linkage (records/factoids providing historical information about persons, but also about places), filling gaps in the database (e.g. place-based information about political or ecclessiastical affiliations; e.g. reconstruction of family relations)
4. retrieval: query data as basis for analysis and presentation -- for example querying the necessary place-based information to construct Thiessen polygons as an experimental approach to estimate the borders of political or ecclessiastical administrative areas and their presentation via interactive visualization tools
5. analysis: see example in 4.
6. presentation: see example in 4.

## Tools for data queries

Major requirement: information retrieval for visualization.

Phases in the research data life cycle: retrieval and analysis.

- [PracticalSPARQL for integrating SPARQL-queries in Jupyter Notebooks:](https://github.com/hassanhajj910/practicalsparql)
  PracticalSPARQL is a package that facilitates the integration of SPARQL queries directly into Jupyter Notebooks. It simplifies querying RDF data, making it easier to work with knowledge graphs. Queries are stored in individual files within a 'queries' folder.
- [ChatGPT promt engineering for the Digital Humanities:](https://chpollin.github.io/GM-DH/)
  ChatGPT is a language model that is now also used in the Digital Humanities, e.g. for data cleaning. For this purpose, humanities scholars need a better understanding of prompt engineering, which is why AI experts as well as humanities researchers experimenting with AI now offer specialised workshops.

## Tools for data visualization

Major requirement: explorative analysis and information visualization.

Phases in the research data life cycle: analysis and presentation.

- [Gicait for geospatial analysis with Python:](https://github.com/gicait/python-for-geospatial-data-analysis) Gicait offers tools and training sessions covering the fundamentals of Python programming for geospatial data analysis.
- [Visualization workflows for geodata:](http://www.informatik.uni-leipzig.de/bsv/homepage/de/people/dr-stefan-j%C3%A4nicke)
  Stefan Jänicke provides suggested workflows for data visualisation.
- [Challenges of interdisciplinarity:](http://www.informatik.uni-leipzig.de/~stjaenicke/balancing.pdf)
  Stefan Jänicke's document discusses the research challenges related to interdisciplinarity.
- [Building elaborate visualizations with Vega-Lite:](https://vega.github.io/vega-lite/examples/)
  Vega-Lite is a high-level grammar for statistical graphics, akin to ggplot or Tableau. It generates complete Vega specifications [EXPLAIN], supporting various visualization types and interactive data exploration. This includes rule-based geovisualisations. One example is this
  [map of line segments connecting SEA to every Airport Reachable via Direct Flights](https://vega.github.io/vega-lite/examples/geo_rule.html).
  [Quantity aggregation](https://vega.github.io/vega-lite/tutorials/getting_started.html#data-transformation-aggregation) [EXPLAIN] is also possible in Vega-Lite
- [Streamgraphs](https://en.wikipedia.org/wiki/Streamgraph) might be a visualization option for displaying the number of events per place and period in the Mainz work package. Streamgraphs depict data as a series of flowing, ribbon-like layers, with each layer representing a different category or variable. The thickness of a layer corresponds to the value of that category at a given point in time. Streamgraphs are particularly effective for illustrating changes in multivariate data. Streamgraphs enable viewers to grasp temporal patterns, trends, and the relative contributions of various categories within the data at first glance. Tools like "D3.js" and "Streamgraph" in "Vega-Lite" help create streamgraphs.
- [SPARQLing Unicorn for explorative visualizations in QGIS](https://github.com/sparqlunicorn/sparqlunicornGoesGIS)
  SPARQLing Unicorn is a plugin for QGIS that enables explorative visualizations through flexible SPARQL queries. It directly adds a GeoJSON layer from SPARQL endpoint queries. For the integration of SPARQLing Unicorn with QGIS, consult the [Doxygen Documentation](https://sparqlunicorn.github.io/sparqlunicornGoesGIS/). You can download the plug-in [here](https://plugins.qgis.org/plugins/sparqlunicorn/).

- [D3](https://d3js.org/) is an open-source JavaScript library for data visualization, in particular for interactive web visualization.
  In contrast to other data popular visualization popular libraries (like _vega_ or _vega-lite_) it follows a low level approach, making it a very flexible tool.
  It is used for the more complex symbology for work package "Electoral Saxony".
- [maplibre GL JS](https://github.com/maplibre/maplibre-gl-js) is an open-source library for publishing web maps.
  It enables the use of vector tiles.
  Because of its GPU-accelerated rendering it is more performant than traditional map libraries such as _leaflet_.

## Databases

Major requirement: data entry and enrichment, information integration and information retrieval.

Phases in the research data life cycle:

- creation
- enrichment
- editing
- and retrieval.

### Overview

::: info
Integrate tool review table (e.g., as file download and image) and briefly describe why different database tools needed to be tested in DigiKAR. Not all tools have to be described in detail as we can refer to the comments in the review table.
:::

Proposal for tool review table using specific aspects (data import, data export, data validation, use cases, etc.):

|                       | Geovistory       | Omeka S          | ResearchSpace  | Metaphacts     | CSV + Python                                              | Access           | MySQL            | Nodegoat         | PostGIS + QGIS   |
| --------------------- | ---------------- | ---------------- | -------------- | -------------- | --------------------------------------------------------- | ---------------- | ---------------- | ---------------- | ---------------- |
| Data Import           | CSV              | CSV              | RDF, CSV       | RDF, CSV       | CSV                                                       | CSV              | CSV              | CSV              | CSV              |
| Data Entry/Editing    |                  |                  | Semantic Forms | Semantic Forms |                                                           | GUI              |                  |                  |                  |
| Data Export           |                  |                  |                |                |                                                           |                  |                  |                  |                  |
| Database Model        | relational model | relational model | RDF            | RDF            | Python pandas DataFrame (data structure for tabular data) | relational model | relational model | relational model | relational model |
| Data Validation       |                  |                  | SPIN           | SPARQL         |                                                           |                  |                  |                  |                  |
| Information Retrieval |                  | API              | SPARQL         | SPARQL         | pandas                                                    | SQL              | SQL              |                  | SQL              |
| Data Exploration      |                  |                  |                |                |                                                           |                  |                  |                  |                  |
| Use Cases             |                  |                  |                |                |                                                           |                  |                  |                  |                  |

### Details

- [PostgreSQL](https://www.postgresql.org/) with [PostGIS](https://postgis.net/), an open-source, spatial database extension. PostGIS enables PostgreSQL databases to manage and query geospatial data effectively. It provides support for geographic objects, spatial indexing, and a wide range of functions and stored procedures for geospatial analysis (e.g. creating voronoi polygons).
- [Metaphactory](https://metaphactory.com/") is a knowledge graph platform designed for managing and exploring semantic data. It allows users to create, search, and visualize linked data and knowledge graphs, making it a popular tool for researchers and organizations dealing with complex data relationships. In addition to the proprietary Metaphactory platform, the tool is available as ResearchSpace for those who can host their own instance. ResearchSpace was specifically designed for cultural heritage and digital humanities application. While ResearchSpace has a user base in cultural heritage and digital humanities research, Metaphactory's user community is more diverse. The choice between them depends on the specific requirements and financial means of your knowledge graph project or research. ResearchSpace is focused on CIDOC CRM and its extension as core ontology and due to its origin from cultural heritage application it supports IIIF and semantic annotation -- a feature not available in the commercial Metaphactory.
- [Linked Data Reactor](http://ld-r.org/) (LD-Reactor or LD-R) is an open-source framework to develop web-based user interfaces to create, edit, search and explore linked data. Similar to ResearchSpace and Metaphactory, LD-R allows the configuration of faceted navigation systems and editing of RDF data, but in a very generic way based on its user interface components for Linked Data applications.
- [Duckdb](https://duckdb.org/) is a free and open-source _"in-process SQL OLAP database management system"_. It is optimized for analytical purposes, where querying and aggregating significant amount of data is required making a good fit to analyze data of work package "Electoral Mainz" where a large collection of individual events need to be grouped, aggregated and linked before they can be eventually visualized in a map.

*Authors / contacts: Ingo Frank (IOS Regensburg), Jakob Listabarth (IfL Leibzig), Monika Barget (IEG Mainz, FASoS Maastricht), Bertrant Duménieu (EHESS Paris)*
