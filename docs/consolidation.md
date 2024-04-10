# Code for data consolidation

:::info
This part of the documentation is still missing. It should give a brief summary of how we consolidate data in the DigiKAR project.
:::

## Read and merge input files, normalise data

## Add geodate and person IDs

## Unify and reconstruct events

## Group and aggregate events

## Add numeric values or categorise events

1. Add event values: We enrich the data by adding event values from an external Python dictionary stored in Github.
2. Categorise events: This is a script for adding additional event categories to factoid lists created for the DigiKAR project. The script mainly uses the Pandas package in Python to read and manipulate EXCEL data as DataFrames. DataFrames are 2-dimensional data representations in rows and columns. They can be written to different file formats such as CSV, EXCEL, JSON or RDF.
3. Categorise functions: This is a script for adding function categories (e.g. teaching versus administration functions) to factoid lists created for the DigiKAR project.
4. …
5. …
