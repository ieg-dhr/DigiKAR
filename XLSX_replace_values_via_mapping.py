# Script for replacing cell values in XLSX based on mapping
# get new words from several CSV files and replace old words in XLSX files
# written for the DigiKAR project by Monika Barget in November 2022

import xlsxwriter
import csv
import pandas as pd
from pandas import DataFrame
import numpy as np
import os

# define files containing ontological mapping

event_ontology='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\InputLists\\event_ontology.csv' 
title_ontology='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\InputLists\\title_ontology.csv' 
function_ontology='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\InputLists\\function_ontology.csv'
place_ontology='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\InputLists\\place_ontology.csv' 

# open ontology files

with open(event_ontology, encoding="utf-8", errors="ignore") as f_event:
    data_e = pd.read_csv(f_event, sep=";")
    events_old=data_e['event_old'].values
    events_new=data_e['event_type'].values
    func_new=data_e['pers_function'].values
    
#with open(title_ontology, encoding="utf-8", errors="ignore") as f_title: # MAPPING NOT COMPLETE
    #data_t = pd.read_csv(f_title, sep=";")
    #title_old=data_t['title_old'].values
    #events_new=data_t['per_title'].values

#with open(function_ontology, encoding="utf-8", errors="ignore") as f_function: # MAPPING NOT COMPLETE
    #data_f = pd.read_csv(f_function, sep=";")
    #function_old=data_f['function_old'].values
    #function_new=data_f['pers_function'].values
    
with open(place_ontology, encoding="utf-8", errors="ignore") as f_place:
    data_p = pd.read_csv(f_place, sep=";")
    places_old=data_p['place_old'].values
    places_new=data_p['place_new'].values
    
# function to process data

def extract_information(filenames):
        
# read all excel files in directory as one data frame

    frame_list=[]
    for item in os.listdir(filenames):
        file = os.path.join(filenames, item)
        print(file)
        df = pd.read_excel(file, sheet_name='FactoidList', index_col=None, dtype=str) # axis=1, sort=False
        df = df.fillna("@") # replace empty fields for string
        frame_list.append(df)

    f = pd.concat(frame_list, axis=0, ignore_index=False, sort=False)
        
# replace words in EVENT column & check if corresponding function needs to be updated
            
    for e_old in events_old:
        print(type(e_old))
        try:
            e_new=data_e.loc[data_e['event_old'] == e_old, 'event_type'].values[0]
            print(e_new)
            f['event_name'] = f['event_name'].replace(e_old, e_new)
            
# check if event results in a specific function and add it if necessary

            f_rel=data_e.loc[data_e['title_old'] == e_old, 'pers_function'].values[0]
            
            if f_rel==True:
                f['title_old'] = f['title_old'].replace(e_old, e_new)
            else:
                print("No function found.")
                continue
            
        except KeyError:
            print("Key Error")
            continue
            
# find "hidden" places rows and add values to PLACE column
            
    for p in places_new:
        print(p)
        try:
            p_add=f[f["place_new"].map(lambda place_new: p in place_new) & f["inst_name"].map(lambda inst_name: p in inst_name)]
            print(p_add)
            
# Still raises ValueError: Columns must be same length as key
# Code will be fixed ASAP

            f['place_name'] =(f['place_name'].map(str) + "/" + p_add)
            
        except KeyError:
            print("Key Error")
            continue
            
        print(f)
                
# write all results to new EXCEL file

    workbook='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\Results\\ProfEvents_FINAL\\Profs_mapped.xlsx'
    writer = pd.ExcelWriter(workbook, engine='xlsxwriter') # create a Pandas Excel writer using XlsxWriter as the engine.
    f.to_excel(writer, sheet_name='Mapped2') # Convert the dataframe to an XlsxWriter Excel object.
    writer.save() # Close the Pandas Excel writer and output the Excel file.
                   
# MAIN FUNCTION: iterate through all XLSX files in directoy        

if __name__ == '__main__':
    filenames = "C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\Results\\ProfEvents_MAPPING"
    extract_information(filenames)
    print("Done.") 
    
# ADDITIONAL OPTIONS to be added when all ontology lists are in place:

'''            
# replace words in TITLE column
            
    for t_old in title_old:
        print(t_old)
        try:
            t_new=data.loc[data['title_old'] == t_old, 'pers_title'].values[0]
            print(e_new)
            f['title_old'] = f['title_old'].replace(t_old, t_new)                
            
        except KeyError:
            print("Key Error")
            continue
            
# replace words in FUNCTION column
            
    for f_old in function_old:
        print(f_old)
        try:
            f_new=data_f.loc[data_f['event_name'] == f_old, 'event_type'].values[0]
            print(f_new)
            f['event_name'] = f['event_name'].replace(f_old, f_new)
            
        except KeyError:
            print("Key Error")
            continue
            
        print(f)
'''
