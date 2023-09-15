# Data collection in DigiKAR

Humanities projects, especially historians, work with large amounts of data from various sources that often need more structure. Ingesting these data into an easy-to-use database that permits complex queries or visualisations is often unattainable. The blog post addresses this challenge and presents workflows in which relational or graph databases are optional end-products rather than the starting points of the research process. The DigiKAR geohumanities project, which analyses spatial relations in Electoral Mainz and Electoral Saxony of the early modern period, uses a combination of spreadsheets, scripts, and sample databases. 

## Data structure in work package 3 "Electoral Mainz"

In work package 3, which analyses biographic mobility in Electoral Mainz, the basis for data collection is EXCEL spreadsheets that follow our project-specific factoid model. This event-oriented approach to data is modelled on the factoid approach developed at King’s College London. This means that we gather agency-related events (e.g. “grand tour”) and general life events (e.g. “birth” and “death”) as stated in different sources. Uncertainty or vagueness of the information is captured in a comments column, where we also add important source quotations:

**Table design in EXCEL for collecting biographic data**

| factoid_ID | pers_ID | event_date | event_after-date | event_before-date | event_start | event_end | event_type | pers_name | pers_title | pers_function | place_name | inst_name | rel_pers | alternative_names | source_quotations | additional_info | comment | source | source_site | info_dump |

## Analytical lenses in the "Electoral Mainz" work package

To get a better idea of the different types of ecclesiastical, academic, and political agents active in Electoral Mainz between the 16th and 18th centuries, our historians have manually collected biographic data relating to the Mainz government in the Eastern German exclave of Erfurt, Mainz officials represented at imperial institutions such as Reichstag (Imperial Diet), Reichshofrat and Reichskammergericht, and the organisation of the electoral court in Mainz itself. In addition, we have used XML data (harvested via API) and OCR technology to semi-automatically gather information on professors and students active at the early modern university of Mainz. 

The following lists give an overview of the data structure in each of these lenses and indicate the latest updates:

a) **"Erfurt" data (2022-11-11, last updated on February 2nd, 2023)**:

- factoid_ID	
- IsSubject	
- Reise (sic!)
- pers_ID	
- pers_name	
- alternative_names	
- event_after-date	
- event_before-date	
- event_start	
- event_end	
- event_date	
- pers_title	
- pers_function	
- place_name	
- inst_name	
- rel_pers	
- source_quotations	
- additional_info	
- comment	source	
- source_site	
- info_dump	
- Weitere Belegstellen (column not in the initial data model)
- StaatskalenderID (column not in the initial data model)
- Import-ID (column not in the initial data model)

**5987 rows of data!**

**Not all persons in this data set have been documented!**

![grafik](https://user-images.githubusercontent.com/38257338/225733762-9faab624-8943-43de-a476-6c3ca914b177.png)

b) **"Jahns" data (2023-02-22, last updated February 22nd, 2023)**:

- factoid_ID	
- pers_ID	
- pers_name	
- alternative_names	
- event_type	
- pers_function	
- place_name	
- inst_name	
- rel_pers	
- source_quotations	
- additional_info	
- comment	
- info_dump	
- source	
- source_site

![grafik](https://user-images.githubusercontent.com/38257338/225735037-eaf683e1-9478-4ff0-a301-0284be5f0bdd.png)

**2081 rows of data!**

This spreadsheet has an additional tab with REL_PERS information to be included in final person list. However, this list still needs to be completed.

c) **1756er Staatskalender META FINAL** (last updated January 27th, 2023):

This spreadsheet contains five tabs of biographic data. The "inst_name" column is erroneously named "H" in some tabs.
This has been changed in the copy for data consolidation.

The columns in this spreadsheet are:

- factoid_ID
- pers_ID
- alternative_names	
- event_start	
- pers_title		
- pers_function	
- place_name		
- inst_name (or "H"?)	
- source	
- pers_name_org (not in original data model!)
- pers_name	
- source_quotations	
- comment	
- source_site	
- Hilfsspalte (not in original data model!)
- additional_info	
- Recherchehinweise	(not in original data model!)
- ID_Factoid-List (not in original data model!)

*Overview of the individual tabs in the Staatskalender spreadsheet:*

- FS0 = 4457 entries
- FS1 = 4910 entries
- FS2 = 5051 entries
- FS3 = 6602 entries
- FS4 = 6540 entries

Due to the large number of data rows per sheet and the redundant nature of the entries (functions enumerated per year), a vertical consolidation should be performed before a horizontal mapping of entities.

*Important information to add to consolidated Staatskalender files:*

- add exact name of data source
- add missing person IDs (based on all existing person data)
- carefully analyse cases where middle names might be missing (issue of person disambiguation)
- watch out for entities that are currently NOT captured in the ontology lists (links below)

The 1755 Staatskalender data will not be used in the current project phase.

![grafik](https://user-images.githubusercontent.com/38257338/225738740-4763cfa5-c418-4c58-aafe-efd0336d0a27.png)

d) **Professors' and students' biographies based on Gutenberg API and Universitätsmatrikel (OCR)**:

The data structure matches the initially defined model. API and OCR data combined, there are **9013 rows of entries**.
After the reconstruction of additional events, 2412 rows were added. This combined data frame has **11428 entries**.

The merging of duplicate events reduces that number to **9323**.

![grafik](https://user-images.githubusercontent.com/38257338/225738740-4763cfa5-c418-4c58-aafe-efd0336d0a27.png)

Since spring 2023, the focus has been **cleaning and consolidating** the hitherto collected data with Open Refine and Python Scripts. To normalise the entities as far as possible while respecting uncertainty and historical development, we have decided to work with **ontology tables** that non-hierarchically list the vocabulary we use. For an overview of named entities in the Mainz work package and our data mapping, cf. the [ontology lists](https://github.com/ieg-dhr/DigiKAR/tree/main/OntologyFiles). Classifications and evaluations of the entities are not included in the data but are flexibly added via vocabulary mappings based on specific research questions. Examples can be found in the XXXX directory.
