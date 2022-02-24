# Script to compare data from several EXCEL files

# written for the DigiKAR geohumanities project

import csv
import pandas as pd
import numpy as np
from collections import Counter

# Paths of locally synchronised EXCEL files for DigiKAR project
# all project members can adjust paths according to their own file structure

factoids='C:\\####\\FactoidList_Python.xlsx' # EXCEL file in DigiKAR Factoid format

# read factoid file

f=pd.read_excel(factoids)
pers_f=(f[['pers_name']]) # retrieve data from selected column
pers_list=pers_f.values.tolist() # convert data frame to sorted list
pers_list_flat=[item for sublist in pers_list for item in sublist] # flatten list
pers_unique=pers_f.drop_duplicates() # remove duplicates
pers_unique_list=pers_unique.values.tolist() # write unique values to list

# count items and print output
    
print("\n\nDie Factoid-Liste enthält derzeit", len(pers_f), "Personeneinträge.") # count data in selected column

for i in [item for sublist in pers_unique_list for item in sublist]:
    print("\n", i, " / ", "Häufigkeit:", pers_list_flat.count(i), "\n") # print names and number of occurrences
    
