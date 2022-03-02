# Script to compare data from several EXCEL files

# written for the DigiKAR geohumanities project in September 2021 by Monika Barget,
# with kind support by https://stackoverflow.com/users/8479387/tlentali

# USE CASES: flexibly matching "OR" conditions across EXCEL columns, 
# including sub-string matching for person names

import csv
import pandas as pd
import numpy as np
from collections import Counter

# Paths of locally synchronised EXCEL files for DigiKAR project
# all project members can adjust paths according to their own file structure

events='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\EventList_0.0.1.xlsx'
institutions='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\InstitutionList_0.0.1.xlsx'
people='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\PeopleList_0.0.1.xlsx'
places='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\PlaceList_0.0.1.xlsx'
roles='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\FunctionList_0.0.1.xlsx'
titles='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\TitleList_0.0.1.xlsx'
factoids='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\FactoidList_Erfassung_Jahns_TEST.xlsx'

# read factoid file

f=pd.read_excel(factoids)
pers_f=(f[['pers_name']]) # retrieve data from selected column
pers_list=pers_f.values.tolist() # convert data frame to sorted list
pers_list_flat=[item for sublist in pers_list for item in sublist] # flatten list
pers_unique=pers_f.drop_duplicates() # remove duplicates
pers_unique_list=pers_unique.values.tolist() # write unique values to list
    
print("\n\nYour fatoid list contains", len(pers_f), "entries.") # count data in selected column

#for i in [item for sublist in pers_unique_list for item in sublist]: # items # sorting not possible if float and string are mixed in file
    #print("\n", i, " / ", "Häufigkeit:", pers_list_flat.count(i), "\n") # print name and occurrences
    
# let user select 
# queried names
print("Enter person names, separated by commas, or press ENTER.")
q_name=input()
# queried year  
print("Date(s):")
ex_year=input() 
# select type of time processing
print("No date selected (0), exact dates (1), data range (2), A QUO date (3) or ANTE QUEM date (4)?")
z=input() 
# queried institution
print("Enter institutions, separated by commas, or press ENTER:")
q_inst=input() 
# queried title
print("Enter person titles, separated by commas, or press ENTER:")
q_title=input() 
# queried function
print("Enter person functions, separated by commas, or press ENTER:")
q_func=input() 
# queried related person
print("Enter related persons, separated by commas, or or press ENTER:")
q_rel=input() 

# separate entries if lists have been submitted
qn=q_name.split(",")
exy=ex_year.split(",")
qi=q_inst.split(",") 
qt=q_title.split(",") 
qf=q_func.split(",") 
qr=q_rel.split(",")

# adjust query according to time conditions

try:
    if z=="0": # no dates 
        try:
# define possible conditions

            condlist = [(f['pers_name'].str.contains('|'.join(qn)) ^ f['pers_name'].isin(qn)), 
                f['event_start'].isin(exy),
                f['inst_name'].isin(qi), 
                f['pers_title'].isin(qt),
                f['pers_function'].isin(qf),
                f['rel_pers'].str.contains('|'.join(qr)) ^ f['rel_pers'].isin(qr)]
            
        except:
            print("No match found!")
    
    elif z=="1": # get exact dates 
        try:
# define possible conditions

            condlist = [(f['pers_name'].str.contains('|'.join(qn)) ^ f['pers_name'].isin(qn)), 
                f['event_start'].isin(exy),
                f['inst_name'].isin(qi), 
                f['pers_title'].isin(qt),
                f['pers_function'].isin(qf),
                f['rel_pers'].str.contains('|'.join(qr)) ^ f['rel_pers'].isin(qr)]
            
        except:
            print("No match found!")
            
    elif z=="2": # get date range
        print("Searching for date range between", exy[0], "and", exy[1], "!") 
        try:
# define possible conditions

            condlist = [(f['pers_name'].str.contains('|'.join(qn)) ^ f['pers_name'].isin(qn)), 
                pd.to_datetime(exy[0]) <= pd.to_datetime(f['event_start'].values) <= pd.to_datetime(exy[1]),
                f['inst_name'].isin(qi), 
                f['pers_title'].isin(qt),
                f['pers_function'].isin(qf),
                f['rel_pers'].str.contains('|'.join(qr)) ^ f['rel_pers'].isin(qr)]
            
        except:
            print("No match found!")
         
    elif z=="3": #get dates before
        print("Searching for dates before", exy[0], "!")
        try:
# define possible conditions

            condlist = [(f['pers_name'].str.contains('|'.join(qn)) ^ f['pers_name'].isin(qn)), 
                pd.to_datetime(f['event_start'].values) <= pd.to_datetime(exy[0]),
                f['inst_name'].isin(qi), 
                f['pers_title'].isin(qt),
                f['pers_function'].isin(qf),
                f['rel_pers'].str.contains('|'.join(qr)) ^ f['rel_pers'].isin(qr)]
            
        except:
            print("No match found!")
            
    elif z=="4": # get dates after
        print("Searching for dates after", exy[1], "!")
        try:
            
# define possible conditions

            condlist = [(f['pers_name'].split(" ").isin(qn) ^ f['pers_name'].isin(qn)), 
                pd.to_datetime(f['event_start'].values) >= pd.to_datetime(exy[0]),
                f['inst_name'].isin(qi), 
                f['pers_title'].isin(qt),
                f['pers_function'].isin(qf),
                f['rel_pers'].str.contains('|'.join(qr)) ^ f['rel_pers'].isin(qr)]
            
        except:
            print("No match found!")
            
except: # no valid selection
    print("No valid selection!")
    
# define full range of choices

choicelist = [f['pers_name'], 
            f['event_start'],
            f['inst_name'], 
            f['pers_title'],
            f['pers_function'],
            f['rel_pers']]
            
# apply conditions 

output = np.select(condlist, choicelist, default=0)
new_array=f.to_numpy()
rows=np.where(output)
result_array=new_array[rows]
print("Elements meeting required conditions:", result_array)

# convert your result array into a dataframe

result_df = pd.DataFrame(result_array)

# save to xlsx file

filepath='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\SelectedData.xlsx'

result_df.to_excel(filepath, index=False)

print("Done.")  
