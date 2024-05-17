## Code for data collection, data cleaning and data analysis

In DigiKAR, we have also experimented with Python code for data collection, data cleaning and data analysis, especially in our Mainz workpackage. The [pandas](https://pandas.pydata.org/) package in Python is widely used for working with two-dimensional [dataframes](https://www.databricks.com/glossary/what-are-dataframes) and helped us read, manipulate and write EXCEL and CSV files. We have also worked with packages for XML, HTML, JSON and [geocoding](https://monikabarget.github.io/GeoHumTutorials/).

:::info
Scripts and their use cases are explained in the workflow section below.
:::

## Editing and running code in different environments

Some of the [Jupyter Notebook](https://jupyter.org/) files (ending in `.ipynb`) in our repository were initially created for [Google Colab](https://colab.google/) and need to be adjusted when used in other environments. In the DigiKAR project, Google Colab was initially used for collaborative code editing because we did not have access to an institutional research software infrastructure. Ideally, code should be hosted in non-commercial environments, such as university-hosted computing infrastructures for data science.

![screenshot google colab](https://github.com/ieg-dhr/DigiKAR/assets/38257338/72173520-9cf1-4dc7-be6e-4f8b25ee97b8)

To make the Colab notebooks work for you, please carry out the following steps:

1. Put the notebook on your own Google Drive, ideally in a folder whose name contains "Colab" so that you can easily identify it later.
2. Open the notebook and adjust the directory path according to your own file location. You may also change the paths of the input and output data in the script, depending on your own prefered folder structure. Make sure that all folders you name in the script also exist on Google Drive before you execute the script.
3. Select "open with" and connect to the Google Colab app. If you have not used Google Colab before, select the "connect more apps" option and find Colab there.
4. Make sure to give Colab all the necessary permissions to run the script and read / write files. If you do not want Colab to access a private Google Drive, you may want to create a new Google account exclusively for research purposes.                                                   |
