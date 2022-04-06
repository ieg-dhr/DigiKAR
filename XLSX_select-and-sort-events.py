# Script to select event per persons and to sort them by event values and dates

# written for the DigiKAR geohumanities project in April 2022 by Monika Barget

import csv
import pandas as pd
import numpy as np

# Paths of locally synchronised EXCEL files for DigiKAR project
# all project members can adjust paths according to their own file structure

factoids='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\FactoidList_Erfassung_Jahns_TEST.xlsx'

# classify events

#f=pd.read_excel(factoids)
#events_f=(f[['event_type']])
#search_event=events_f.drop_duplicates()
#print(search_event)

event_value_dict={"Sonstiges":0, 
                  "Geburt":1, 
                  "Taufe":2, 
                  "Primäre Bildungsstation":3, 
                  "Privatunterricht":3,
                  "Rezeption":4, 
                  "Zulassung":9, 
                  "Immatrikulation":10,
                  "Studium":11,
                  "Prüfungsverfahren":11,
                  "Graduation":12,
                  "Praktikum":13,
                  "Promotion":14,
                  "Wohnsitznahme": 20,
                  "Reise":20, 
                  "Nobilitierung":20,
                  "Aufnahme":20,
                  "Aufschwörung":20,
                  "Eheschließung":20,
                  "Funktionsausübung":20,
                  "erfolglose Bewerbung":20,
                  "Rejektion":20,
                  "Aufenthalt":20,
                  "mittelbare Nobilitierung":20,
                  "Privilegierung":20,
                  "Wappenbesserung":20,
                  "Introduktion":30, 
                  "Mitgliedschaft":30,
                  "Gesandtschaft":30, 
                  "Präsentation":30, 
                  "Vokation":39, 
                  "Ernennung":40,
                  "Amtseinführung":41,
                  "Vereidigung":41,
                  "Amtsantritt":42,
                  "Beförderung":44, 
                  "Ehrung":45, 
                  "Entlassung":50,
                  "Suspendierung":50,
                  "Absetzung":50,
                  "Resignation":50,
                  "Rücktritt":50,
                  "Pensionierung":90,
                  "Pension":91,
                  "Tod":100}

# read person list

f=pd.read_excel(factoids)
pers_name_f=(f[['pers_name']]) 
search_df=pers_name_f.drop_duplicates() # remove duplicates
search_list=search_df['pers_name'].tolist()

# count no. of entries in flattened person list

no_person=len(search_list)
print("There are", no_person, "unique person names in this data set.")

# add event values from dict to data frame

f['event_value'] = f['event_type'].map(event_value_dict)

# iterate through unique persons to get their events

for name in search_list:
    print(name)
    res_df=(f.loc[f['pers_name'] == name])
    res_sorted=res_df.sort_values(by =['event_value','event_after-date','event_start','event_before-date',])
   
 # write results to new sheets in EXCEL
    
    with pd.ExcelWriter('C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\JahnsEvents.xlsx', engine='openpyxl', mode='a') as writer:  
        res_sorted.to_excel(writer, sheet_name=name[-14:], index="True")
     
print("Done.")
