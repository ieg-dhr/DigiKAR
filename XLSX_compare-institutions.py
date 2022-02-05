# Script to compare data from several EXCEL files

# written for the DigiKAR geohumanities project in September 2021 by Monika Barget

# USE CASES: counting institutions names mentioned in factoid list, matching institutions to ontology list, matching institutions and places

import csv
import pandas as pd
import numpy as np
from collections import Counter

# Paths of locally synchronised EXCEL files for DigiKAR project
# all project members can adjust paths according to their own file structure

events='C:\\Users\\###\\EventList_0.0.1.xlsx'
institutions='C:\\###\\InstitutionList_0.0.1.xlsx'
people='C:\\Users\\###\\PeopleList_0.0.1.xlsx'
places='C:\\Users\\###\\PlaceList_0.0.1.xlsx'
roles='C:\\Users\\###\\FunctionList_0.0.1.xlsx'
titles='C:\\Users\\###\\TitleList_0.0.1.xlsx'
factoids='C:\\Users\\###\\FactoidList_1756er_Staatskalender_Master.xlsx'

# read factoid file

f=pd.read_excel(factoids)
inst_f=(f[['inst_name']]) # retrieve data from selected column
inst_list=inst_f.values.tolist() # convert data frame to list
inst_list_flat=[item for sublist in inst_list for item in sublist] # flatten list
inst_unique=inst_f.drop_duplicates() # remove duplicates
inst_unique_list=inst_unique.values.tolist() # write unique values to list
    
print("\n\nDie Factoid-Liste enthält derzeit", len(inst_f), "Institutioneneinträge.") # count data in selected column
print("\n\nDie Namen der erfassten INSTITUTIONEN sind:\n")
for i in [item for sublist in inst_unique_list for item in sublist]: # items # sorting not possible if float and string are mixed in file
    print(i, "\n")
    print("Häufigkeit:", inst_list_flat.count(i), "\n") # print occurrences per institution

# read institution list

i=pd.read_excel(institutions)
inst_i=(i[['inst_name']])

# find institutions that are BOTH in factoid list AND institutions list

inst_known=[] # define result list of institutions in both files
count=0
for x in inst_unique_list: 
    try:
        inst_i[inst_i.eq(x).any(1)] # check if institution name is already in ontology list for institutions
        inst_known.append(x) # add institutions found in both EXCEL files to result list
    except:
        print("Nur in Factoid Datei:", x) # print institutions only found in factoid file
    
print("\n\nDiese Institutionen sind in der Factoid-Tabelle und in der Institutionen-Tabelle erfasst:\n", inst_known) # print result list
    
# count occurence of place names in factoid list

place_name_f=(f[['place_name']])
place_series=place_name_f.squeeze() # turn DF into SERIES for counting

print("\n\nOrtsnamen und ihre Häufigkeit:\n", place_series.value_counts(ascending=True)) # return frequency of places

freq_place=place_name_f.place_name.mode(dropna=True) # find most frequent item in row of place names
print("\n\nDies ist der am häufigsten genannte Ortsname der Factoid-Datei:\n", freq_place)

# get places associated with institutions

inst_place_f=(f[['inst_name', 'place_name']]) # get institution names and place names from factoid list
inst_place_list=inst_place_f.values.tolist() # convert df into list
inst_place_flat=[item for sublist in inst_place_list for item in sublist] # flatten list
print("\n\nBeziehung zwischen Institutionen und Orten:\n")

for p1, p2 in zip(inst_place_flat[::2], inst_place_flat[1::2]): # zip list to print items in pairs
    print("\n", p1, " IN ", p2) # print institution next to place name

print("Done")
