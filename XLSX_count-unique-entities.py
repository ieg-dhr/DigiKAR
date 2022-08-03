# Script to count related entities in several EXCEL files

# written for the DigiKAR geohumanities project by Monika Barget

# USE CASES: find and count unique entities in specific columns of several EXCEL files

import pandas as pd
import numpy as np
import os
from eldar import Query # for future implementation of BOOLEAN QUERIES
from collections import Counter
import xlsxwriter

# Paths of locally synchronised EXCEL files for DigiKAR project
# all project members can adjust paths according to their own file structure

filenames="C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\InputLists"

# obligatory columns in valid factoid list

column_names = ["factoid_ID",
                "pers_ID",
                "pers_name",
                "alternative_names",
                "event_type",
                "event_after-date",
                "event_before-date",
                "event_start",
                "event_end",
                "event_date",
                "pers_title",
                "pers_function",
                "place_name",
                "inst_name",
                "rel_pers",
                "source_quotations",
                "additional_info",
                "comment",
                "info_dump",
                "source",
                "source_site"]

### read all excel files in directory as one data frame

frame_list=[]
for item in os.listdir(filenames):
    file = os.path.join(filenames, item)
    df = pd.read_excel(file, sheet_name='FactoidList', index_col=None, dtype=str) # axis=1, sort=False
    df = df.fillna("@") # replace empty fields for string
    frame_list.append(df)

f = pd.concat(frame_list, axis=0, ignore_index=False, sort=False)
    
### read factoids from PERS_NAME

pers_f=(f[['pers_name']]) # retrieve data from selected column
pers_list=pers_f.values.tolist() # convert data frame to sorted list
pers_list_flat=[item for sublist in pers_list for item in sublist] # flatten list
pers_unique=pers_f.drop_duplicates() # remove duplicates
pers_unique_list=pers_unique.values.tolist() # write unique values to list
    
print("\n\nYour factoid list contains", len(pers_f), "PERSON NAMES.") # count data in selected column

pers_list_new=[]
for i in [item for sublist in pers_unique_list for item in sublist]: # count person occurrences
    #print("\n", i, " / ", "Häufigkeit:", pers_list_flat.count(i), "\n") # print name and occurrences
    pers_list_new.append([i, pers_list_flat.count(i)])
    
### read factoids from PERS_TITLE

pers_t=(f[['pers_title']]) # retrieve data from selected column
title_list=pers_t.values.tolist() # convert data frame to sorted list
title_list_flat=[item for sublist in title_list for item in sublist] # flatten list
title_unique=pers_t.drop_duplicates() # remove duplicates
title_unique_list=title_unique.values.tolist() # write unique values to list
    
print("\n\nYour factoid list contains", len(pers_t), "PERSON TITLES.") # count data in selected column

title_list_new=[]
for i in [item for sublist in title_unique_list for item in sublist]: # count person occurrences
    #print("\n", i, " / ", "Häufigkeit:", pers_list_flat.count(i), "\n") # print name and occurrences
    title_list_new.append([i, title_list_flat.count(i)])
    
### read factoids from PERS_FUNCTION

pers_func=(f[['pers_function']]) # retrieve data from selected column
func_list=pers_func.values.tolist() # convert data frame to sorted list
func_list_flat=[item for sublist in func_list for item in sublist] # flatten list
func_unique=pers_func.drop_duplicates() # remove duplicates
func_unique_list=func_unique.values.tolist() # write unique values to list
    
print("\n\nYour factoid list contains", len(pers_func), "FUNCTIONS.") # count data in selected column

func_list_new=[]
for i in [item for sublist in func_unique_list for item in sublist]: # count person occurrences
    #print("\n", i, " / ", "Häufigkeit:", pers_list_flat.count(i), "\n") # print name and occurrences
    func_list_new.append([i, func_list_flat.count(i)])
    
### read factoids from PLACE_NAME

place_name=(f[['place_name']]) # retrieve data from selected column
place_list=place_name.values.tolist() # convert data frame to sorted list
place_list_flat=[item for sublist in place_list for item in sublist] # flatten list
place_unique=place_name.drop_duplicates() # remove duplicates
place_unique_list=place_unique.values.tolist() # write unique values to list
    
print("\n\nYour factoid list contains", len(place_name), "PLACE NAMES.") # count data in selected column

place_list_new=[]
for i in [item for sublist in place_unique_list for item in sublist]: # count person occurrences
    #print("\n", i, " / ", "Häufigkeit:", place_list_flat.count(i), "\n") # print name and occurrences
    place_list_new.append([i, place_list_flat.count(i)])

    
### read factoids from INST_NAME

inst_name=(f[['inst_name']]) # retrieve data from selected column
inst_list=inst_name.values.tolist() # convert data frame to sorted list
inst_list_flat=[item for sublist in inst_list for item in sublist] # flatten list
inst_unique=inst_name.drop_duplicates() # remove duplicates
inst_unique_list=inst_unique.values.tolist() # write unique values to list
    
print("\n\nYour factoid list contains", len(inst_name), "INSTITUTIONS.") # count data in selected column

inst_list_new=[]
for i in [item for sublist in inst_unique_list for item in sublist]: # count person occurrences
    #print("\n", i, " / ", "Häufigkeit:", inst_list_flat.count(i), "\n") # print name and occurrences
    inst_list_new.append([i, inst_list_flat.count(i)])
    
### Write all results to new EXCEL file

with xlsxwriter.Workbook('C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\Results\\NewEntities.xlsx') as workbook:  #generate file xlsx
    worksheet1 = workbook.add_worksheet("PERSONS")
    for row_num, data in enumerate(pers_list_new):
        try:
            worksheet1.write_row(row_num, 0, data)
        except:
            pass
        
    worksheet2 = workbook.add_worksheet("TITLES")
    for row_num, data in enumerate(title_list_new):
        try:
            worksheet2.write_row(row_num, 0, data)
        except:
            pass
        
    worksheet3 = workbook.add_worksheet("FUNCTIONS")
    for row_num, data in enumerate(func_list_new):
        try:
            worksheet3.write_row(row_num, 0, data)
        except:
            pass
        
    worksheet4 = workbook.add_worksheet("PLACES")
    for row_num, data in enumerate(place_list_new):
        try:
            worksheet4.write_row(row_num, 0, data)
        except:
            pass

    worksheet5 = workbook.add_worksheet("INSTITUTIONS")
    for row_num, data in enumerate(inst_list_new):
        try:
            worksheet5.write_row(row_num, 0, data)
        except:
            pass
    
print("Done.") 
