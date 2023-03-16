# Data structure in the Mainz work package

1) **Table design in EXCEL for collecting biographic data**

| factoid_ID | pers_ID | event_date | event_after-date | event_before-date | event_start | event_end | event_type | pers_name | pers_title | pers_function | place_name | inst_name | rel_pers | alternative_names | source_quotations | additional_info | comment | source | source_site | info_dump |
|------------|---------|------------|------------------|-------------------|-------------|-----------|------------|-----------|------------|---------------|------------|-----------|----------|-------------------|-------------------|-----------------|---------|--------|-------------|-----------|

2) **Structure of tables for the different data sources**

a) "Erfurt" data (2022-11-11, last updated on February 2nd, 2023):

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
- Weitere Belegstellen (column not in initial data model)
- StaatskalenderID (column not in initial data model)
- Import-ID (column not in initial data model)

**5987 rows of data!**

![grafik](https://user-images.githubusercontent.com/38257338/225733762-9faab624-8943-43de-a476-6c3ca914b177.png)

b) "Jahns" data (2023-02-22, last updated February 22nd, 2023):

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

This spreadsheet has an additional tab with REL_PERS information to be included in final person list!

c) **1756er Staatskalender META FINAL** (last updated January 27th, 2023):

This spreadsheet contains 5 tabs of biographic data. In some of the tabs, the "inst_name" column is named "H".
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

Due to the large number of data rows per sheet and the redundant nature of the entries (functions enumerated per year), a vertical consolidation should be performed prior to a horizontal mapping of entities.

![grafik](https://user-images.githubusercontent.com/38257338/225738740-4763cfa5-c418-4c58-aafe-efd0336d0a27.png)

3) **Ontology tables**

For an overview of named entities in the Mainz work package and our data mapping, cf. the [ontology lists](https://github.com/ieg-dhr/DigiKAR/tree/main/OntologyFiles).

