# Utilising Germania Sacra Data in JSON Format

## Background and provided data

In DigiKAR, we have obtained permission to integrate data from [Germania Sacra] for research purposes. We were especially interested in data on early modern monasteries and historical figures such as bishops active in Mainz.
The data were provided in JSON and CSV formats, but the CSV files proved impossible to parse to our own factoid format.

Monasteries Data:

   - The JSON file for monasteries parsed successfully.
   - Data integration can proceed by categorizing information into the Mainz places list and the Mainz institutions list.
   - Identification of necessary IDs is ongoing to ensure consistency.

Persons Data:

    - The CSV dumps for persons were unusable due to excessive merged information, posing significant challenges for data extraction and manipulation.
    - The 22MB JSON dump provided by the Germania Sacra team caused technical problems, including constant decoding errors in Python, suggesting potential file corruption.
    -  An online tool successfully opened the 22 MB JSON dump but revealed problematic nesting structures.

## Extracting the JSON data

A smaller JSON dump specifically for bishops active in Mainz was downloaded directly from Germania Sacra. While this file parsed correctly, it still required restructuring to be useful in a tabular format.
The initial parsed JSON file included an “offices” column with event information embedded in a dictionary, which needed to be read to individual factoid columns. The “notePerson” column also contains crucial information such as educational trajectories, which are often accompanied by specific places and dates. The events in this column, however, vary in structure: some are dictionaries, while those with only dates are simple lists of strings. These inconsistencies in the data structure proved challenging for the data integration in our own project. There is no guarantee of extracting all “notePerson” information cleanly and expert review is needed.

### Current Solutions and Recommendations

- BishopsMainz-fromJSON.xlsx: This file includes the raw JSON data parsed into a dataframe without additional manipulation, retaining the “offices” column as a dictionary.
- BishopsMainz_OFFICES_separated.xlsx: This file has been partially manipulated to separate the “offices” column into individual columns for person title and person office.

### FINAL SCRIPT NEEDS TO BE EMBEDDED

### Next Steps

- Ingo works on improving the extraction script.
    - Sven should review the manipulated data to determine its consistency and completeness.
    - It is recommended that Germania Sacra be contacted to discuss the challenges faced and possibly request a more specific data dump focusing on the early modern period.
