# Data retrieval from several CSV/EXCEL tables

## Simple analysis

Simple analysis of table columns with identical labels from several EXCEL files: [XLSX_analysing-multiple-files.py](https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_analysing-multiple-files.py)

### Use cases

- identifying chonologies in data sets
- data comparison
- data cleanign and data normalisation

_Sample output for the above-mentioned script:_

<!--@include: ../XLSX_multiple-files_sample-output.md-->

## Script for identifying biographic events

Script for identifying biographic events per person and sorting them by event-value and date [XLSX_select-and-sort-events.py (1st version)](https://github.com/ieg-dhr/DigiKAR/blob/main/XLSX_select-and-sort-events.py)

<<< ../XLSX_select-and-sort-events.py

### Use cases

- experimental reconstruction of biographic chronologies in cases where a lot of events have no or vague dating
- calculation of possible event time frames based on previous or following events
- merging identical events / adjusting event time frames based on information from different sources

The current sorting is four-fold and starts with the event classification. This can be adjusted in the code.

```{python}
res_sorted = res_df.sort_values(
    by =[
        'event_value',
        'event_after_date',
        'event_start',
        'event_before_date',
    ])
```

## Relationship tracer

<<< ../XLSX_relationship-tracer.py

### User cases

- consolidating genealogical information from `rel_pers` column in factoid lists
- reconstruction of sibling relations based on known parent-child-connections
- reconstruction of implict grandparent-grandchild relations

## Advanced script to query several columns across several spreadsheets based on user input

<<< ../XLSX_multiple-conditions_OR.py

- Files from directory `DigiKAR_DATEN\\Python\\InputLists` are read to a single dataframe.
- User can select search criteria for person name, date, institution, person title, function and related person. Several keywords per field are accepted.
- User can decide whether to search for exact dates, a date range or "before" and "after" dates.
- Script handles time input first and writes matches to new data frame, then conditions for remaining fields are applied. Current version of script apply OR operator to the fields. In final GUI version, user will be able to select both AND or OR operations.
- Results are written to new file. User is free to assign file name via script input.
- Time management handles `YYYY` as well as `YYYY-MM` and `YYYY-MM-DD` inputs. Searching for dates before and after input date, the `before` and `after` columns in the original spreadsheet are consider alongside start and end dates.

### Use cases

- sample for creating more complex Boolean queries across several spreadsheets
- adjustable to different spreadsheet formats
- experimenting with data parsing and potential problems arising from early modern data
