# Geohumanities Tutorials

In a separate Github repository, Monika Barget shares [code and tutorials](https://monikabarget.github.io/GeoHumTutorials/) for geocoding historical spatial data with the Google and Geonames APIs. Some of the scripts also include embedded mapping functionalisties to create static or interactive visualisations on the fly.

## Geocoding Historical Place Names Using Python and the proprietary Open Cage API

- [Geocoding with the OpenCage API and plotting on a static map](https://github.com/ieg-dhr/DigiKAR/JupyterNotebooks_DigiKAR/Geocode-Plot_OpenCage.ipynb)

**Description:** This notebook uses the proprietary OpenCage API for geocoding and plots the geographic data. The OpenCage API requires a subscription to be fully functional.

## Geocoding Historical Place Names Using Python and the Google API

- [Geocoding with Google API and plotting on interactive map](https://github.com/ieg-dhr/DigiKAR/JupyterNotebooks_DigiKAR/Geocode_Plot_GoogleAPI_interactiveMAP.ipynb)

**Description:** Applying the Google API, this notebook performs geocoding of an EXCEL file and plots an interactive map of the data provided.
  
- [Geocoding with Google API and plotting on interactive map (data from work package 3)](https://github.com/ieg-dhr/DigiKAR/JupyterNotebooks_DigiKAR/Geocode_Plot_GoogleAPI_interactiveMAP_AP3.ipynb)

**Description:** An updated version of the Google API geocoding and interactive mapping notebook, adjusting the format of the input data to the requirements of the DigiKAR workpackage 3.

## Geocoding Historical Place Names Using Python and the Geonames API

- [Geocoding with the Geonames API and plotting on static map](https://github.com/ieg-dhr/DigiKAR/JupyterNotebooks_DigiKAR/Geocode-Plot_Geonames.ipynb)

**Description:** This notebook demonstrates how to use the Geonames API for geocoding and plotting geographic data. Based on the input data, the notebook plots a static map.
  
- [Geocoding with Geonames API and plotting on interactive map](https://github.com/ieg-dhr/DigiKAR/JupyterNotebooks_DigiKAR/Geocode-Plot_Geonames_interactiveMAP.ipynb)

**Description:** This notebook extends the basic geocoding functionality provided in the script above to plot an interactive map, allowing users a quick interactive exploration of the geocoded data.

-[Geocode data with Geonames API, checking different feature classes](https://github.com/ieg-dhr/DigiKAR/JupyterNotebooks_DigiKAR/Geocode-Plot_Geonames_complexInput.ipynb)
 
**Description:** This notebook is an advanced version of the Geocode-Plot_Geonames notebook and checks several feature classes in the Geonames API to find geodata for places that are ignored when only one of the feature classes is queried. This version of the script is especially recommended when working with less common place names, e.g. smaller towns and special places such as castles.

- [Check file with geocoded data to add known geodata for identical places and write rows with missing geodata to a new file](https://github.com/ieg-dhr/DigiKAR/JupyterNotebooks_DigiKAR/Geocode_extract-rows-without-geodata.ipynb)
 
**Description:** This notebook focuses on identifying and extracting rows from a dataset that lack geodata. In the first step, it checks if geodata for a given place name are already listed in other rows of the file. Where no geodata are available, the row is copied to a new file. This script is useful for cleaning and reviewing data.

The following *video tutorial* demonstrates in more detail how to use Python and the Geonames API to link historical place names with geodata and to plot a map for basic data explorations:

[VIDEO]https://youtu.be/56JKd1b0M7Q?si=61MjDKkTVPdtxyI7

The script performs the following tasks:
1. **Install Packages**: Install any required packages that are not part of the standard Python distribution.
2. **Import Libraries**: Import Pandas and Geocoder to read the Excel sheet and interact with Geonames.
3. **Read Excel Data**: Load the Excel sheet containing place names into a Pandas DataFrame.
4. **Geocode Place Names**: Use the Geonames API to find latitude and longitude for each place name.
5. **Save and Plot Results**: Write the results to an output file and plot the geocoded data on a simple map.

Please keep in mind that historical place names may appear in different languages including Latin or use old spellings. This makes it difficult to map old names to their modern equivalents, and feature classes in Geonames have to be chosen accordingly. Although the automated geocoding of historical place names is never perfect and needs careful review, this process can save significant time, especially when dealing with thousands of place names. In the video, Google Colab is used to run the script, but Python can also be installed and executed locally on a computer.

Several Python packages are necessary for the demonstrated script:
- **Geocoder**: To interact with the Geonames API.
- **Pandas**: For handling tabular data.
- **Basemap**: For creating visual maps.

To prepare your data, follow these steps:
1. Extract place names from historical sources and collect them in a structured format, e.g. in a CSV file.
2. Map these names to their modern equivalents.
3. Use an Excel sheet to list the place names for geocoding in the place_name column if you want to reuse our script without larger edits.

Based on more complex spatial information in the DigiKAR data, we have also written an advanced geocoding script that considers several possible exceptions when dealing with historical geodata:

- [Geocoding complex input with the Geonames API](https://github.com/ieg-dhr/DigiKAR/blob/main/JupyterNotebooks_DigiKAR/Geocode-Plot_Geonames_complexInput.ipynb)

This script helps you handle different naming conventions and potential ambiguities as it does not only search for the exact place names in Geonames but also looks for broader regions if necessary.
One section of the script ensures that places are correctly located within Europe. What still needs to be checked manually, however, are cases where place names might refer to multiple locations (e.g., "Roby" could be in both the UK and Poland). It is important to validate computer-generated results against historical records.

The following *German video tuturial (with subtitles)* shows how the script checks both the full place name and the region information for matches in Geonames: [VIDEO](https://youtu.be/m_p8-0L26bw?si=zujgCttxnXvH2zJ0)
