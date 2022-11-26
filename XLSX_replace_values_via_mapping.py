# Script for replacing cell values in XSLX based on mapping
# get new words from CSV file and replace old words
# written by Monika Barget in November 2022

import xlsxwriter
import csv
import pandas as pd
from pandas import DataFrame
import numpy as np
import pdftotext
import os
from collections import defaultdict

CSV_FILE='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\InputLists\\event_mapping.csv' # sample file containing original keywords and mapping to final index words

with open(CSV_FILE, encoding="utf-8", errors="ignore") as f:
    data = pd.read_csv(f, sep=";")
    events_old=data['event_name'].values
    events_new=data['event_type'].values
    func_new=data['pers_function'].values
    
# open input files as dataframe and replace / add values

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
        
# replace event types in EVENT column
            
    for e_old in events_old:
        print(type(e_old))
        try:
            e_new=data.loc[data['event_name'] == e_old, 'event_type'].values[0]
            print(e_new)
            f['event_name'] = f['event_name'].replace(e_old, e_new)
            
        except KeyError:
            print("Key Error")
            continue
                    
# write all results to new EXCEL file

    workbook='C:\\Users\\###\\Profs_mapped.xlsx'
    writer = pd.ExcelWriter(workbook, engine='xlsxwriter') # create a Pandas Excel writer using XlsxWriter as the engine.
    f.to_excel(writer, sheet_name='Mapped') # Convert the dataframe to an XlsxWriter Excel object.
    writer.save() # Close the Pandas Excel writer and output the Excel file.
                   
# iterate through all XLSX files in directoy        

if __name__ == '__main__':
    filenames = "C:\\Users\\###\\ProfEvents_MAPPING"
    extract_information(filenames)
    print("Done.") 
