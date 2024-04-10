# Data categorisation Mainz

## Overall challenges

A major challenge in the Mainz work package, which collected data from different sources, was the **normalisation of event descriptions and the modelling of their relationships**. Studies, for example, were initially recorded with or without known start and end dates as continuous event, but also as university enrolments. An enrolment is, of course, a punctual event that triggers a longer study process, for which only the start date is known. To make the biographical information collected more uniform and easier to query, it was thus necessary to reconstruct process events from punctual events if possible and to merge successive punctual events into longer continuous events, e.g. if information came from annual calendars. For this purpose, a "consolidation" script was written in Python and run on all our collected data sets.

## Data categorisation in Metaphacts

In order to query and cluster data from the Mainz work package, we experimented with the proprietary [Metaphacts](https://metaphacts.com/) system, which "supports collaborative knowledge modeling and knowledge generation". In Metaphacts, higher-level categories for collected data can be defined as `skos:Collections`. As an example, Ingo Frank (IOS Regensburg) has taken all our terms for `events` and `functions` which we collected for the early modern professors active in Mainz and created hierarchical relationships from the comma-separated entries:

- [Classification system for biographical events](http://95.217.189.117:10214/resource/?uri=http%3A%2F%2Fdigikar.eu%2Fvocabulary%2Fevent)
- [Classification for persons' roles / functions](http://95.217.189.117:10214/resource/?uri=http%3A%2F%2Fdigikar.eu%2Fvocabulary%2Ffunction)

Only the superordinate terms are included in the collection (category) as the search is then simply extended to the respective sub-terms.

## Data categorisation via Python

Another way to categorise data is to define clusters and hierarchies in Python dictionaries or simple CSV tables whose information can then be appended to the basic factoid structure of our data. Mapping data to existing spreadsheets is very easy in Python as the pandas package allows a flexible manipulation of tabular data as so-called dataframes. Each item in a selected spreadsheet column can thus be assigned to different higher-level categories, depending on the research questions and theoretical contexts in which the data are being analysed. For examples of data categorisation in Python, please view the separate [Data Categorisation](https://github.com/ieg-dhr/DigiKAR/tree/main/Data%20Categorisation) folder in this GitHub repository.

## Categories relevant for data analysis in WP3

- Ecclesiastical offices in general (all functions carried out in monasteries and diocesan administrations)
- Clerical offices (requiring holy orders, e.g. priestly functions in dioceses and parishes)
- Teaching (at universities, but also in seminaries and colleges)
- Political offices (e.g. as administrators, envoys, or government officials)
- Medical activities (e.g. as personal physicians to aristocrats, city physicians, physicians for the poor, or army physicians)
- Legal activities (e.g. as lawyers or judges)
- Military service (e.g. as soldiers, army engineers, or army physicians)

Some of the activities in these categories naturally overlap. For visualisation purposes, however, it is necessary to operate with seven to ten categories in each network graph or map, especially when categories ought to be highlighted in different colours.
