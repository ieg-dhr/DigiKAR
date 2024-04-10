# Data Queries

## Data queries as machine-readable translations of research questions

Data queries in DigiKAR are inherently driven by historical research questions specific to our two work packages. Based on user stories and a thorough requirements analysis conducted by work package 4 "Data Modelling", Ingo Frank (IOS Regensburg) has developed sample SPARQL queries that reflect some of our research goals. A complete German-language documentation of our competency questions and user stories is available in a [separate Github repository](https://ieg-dhr.github.io/DigiKAR-Competency-Questions/).

In work package 3, which has a focus on biographies and human mobility, we are, inter alia, interested in the following aspects of our data:

- Which offices were often held in succession?
- What are the typical careers of people from place X or educated in place Y?
- What is the ratio/distribution of clerical and temporal offices?
- Which persons were involved in research, teaching, political activities, etc.?
- What are spatial hotspots of activity?
- Can we already say something about institutional or familial networks?
- In how far do our findings contradict or confirm existing qualitative research?

In the summer term of 2022, Bettina Braun (JGU Mainz), Florian Stabel (JGU Mainz), Jana Moser (IfL) and Monika Barget (IEG Mainz / Maastricht) taught an [MA seminar in the history programme](http://clerical-mobility.ieg-mainz.de/), which focused on fourteen early modern cathedral provosts from Mainz. Their professional careers and mobility patterns already gave us essential insights into Mainz's religious and political interconnections in the 17th and 18th centuries. Several clerics in the data set studied abroad, went on the grand tour or took on diplomatic missions. Moreover, many clerics serving in the Mainz cathedral chapters also served in Speyer or Cologne at some point in their careers. One example of a mobile cleric in the analysed data set is Dietrich Kaspar von Fürstenberg, who spent time in Florence and Rome as well as in Speyer, Cologne, Bohemia and several places in present-day Belgium and France. Results from the seminar included static maps and a [zoomable map of individual biographies](http://clerical-mobility.ieg-mainz.de/qgis2web_Domherren_v3/#4/51.08/2.07).

## Challenges and limitations

Naturally, we have also experienced many challenges and data-related limitations in trying to answer our research questions. A fundamental challenge in the Mainz work package was to convert early modern sources not only to machine-readable text but highly structured text (ideally coded or in table format) to analyse relationships between people, institutions, and places over a long period of time. Some of our early efforts to use OCR technology and semi-automated layout recognition failed. An example of an early modern printed source that we would have liked to use in more detail are the so called [“state calendars” (“Staatskalender”)](https://www.dilibri.de/nav/classification/1419790) annually published in the Electorate of Mainz in the 18th century. These sources contain short biographic entries on clerics and other officials working for the princely administration in the given year, including their titles. As these sources are printed in Fraktur font, testing and elaborating OCR models for this particular text type was vital in making these data machine-readable in the first place. Unfortunately, our OCR efforts with [Transkribus](https://readcoop.eu/transkribus/) were only sufficient to allow the researchers in our team a full-text search. We were not able to transfer the nested and often inconsistent layout of the Staatskalender directly to a table-format that we could use for automated data analysis and data visualisation. A more thorough analysis of the Staatskalender would require a complete digital edition with annotations.
