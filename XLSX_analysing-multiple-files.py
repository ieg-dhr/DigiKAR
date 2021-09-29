# Script to compare data from several EXCEL files

# written for the DigiKAR geohumanities project in September 2021 by Monika Barget

import csv
import pandas as pd
import numpy as np

# Paths of locally synchronised EXCEL files for DigiKAR project
# all project members can adjust paths according to their own file structure

events='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\MainzLists\\EventList.xlsx'
institutions='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\MainzLists\\InstitutionList.xlsx'
people='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\MainzLists\\PeopleList.xlsx'
places='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\MainzLists\\PlaceList.xlsx'
roles='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\MainzLists\\RoleList.xlsx'
sources='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\MainzLists\\SouceList.xlsx'
titles='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\MainzLists\\TitleList.xlsx'
factoids='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\MainzLists\\FactoidList.xlsx'

# read factoid file

f = pd.read_excel(factoids)
pers_name_f=(f[['pers_name']]) # retrieve data from selected column
    
print("\n\nDie Factoid-Liste enthält derzeit", len(pers_name_f), "Einträge.") # count data in selected column
print("\n\nDie Namen der erfassten Personen sind:\n", pers_name_f) # print data from selected column
    
f_dates=f[f.start=="0000-00-00"] # find entries that do not have a start date yet
# IMPORTANT: use special "date" function for more complex chronological comparisons!!
   
print("\n\nDiese erfassten Ereignisse haben bislang kein Startdatum:\n", f_dates)

# read person list

p=pd.read_excel(people)
pers_name_p=(p[['pers_name']]) 

print("\n\nDies sind die ersten 9 Personen in der Personen-Datei:\n", pers_name_p[:10]) # print first 9 person names in table column "pers_name"

# find person names that are BOTH in factoid list AND people list

people_known=[]
count=0
for x in pers_name_f: 
    count+=1
    y=pers_name_f.at[count, 'pers_name'] # read person names from factoid file
    try:
        pers_name_p[pers_name_p.eq(y).any(1)] # check if name is also in person file
        people_known.append(y) # collect names found in both EXCEL files
    except:
        print("Keine Namensübereinstimmung!")
    
    print("\n\nDiese Personen sind in der Factoid-Tabelle und in der Personen-Tabelle erfasst:\n", people_known)
    
# read place list

pl=pd.read_excel(places)
place_name_pl=(pl[['place_name']])
town_name_pl=(pl[['town_name']])

# get most frequent place name from factoid list

place_name_f=(f[['place_name']])
freq_place=place_name_f.place_name.mode()
print("\n\nDies ist der am häufigsten genannte Ortsname der Factoid-Datei:\n", freq_place)

# get info for most frequent place from place list

s=freq_place.values[0]
try:
    q=pl[place_name_pl.eq(s).any(1)] # check if place is also in place file
    print("\n\nZum gesuchten Ereignis-Ort gibt es folgende Informationen aus der Orts-Datei:\n", q.iloc[:,[2,3]])
except:
    print("Keine Namensübereinstimmung!")
    
with open('C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\MainzLists\\SomeData.csv','a', encoding="utf-8") as output:
    writer = csv.writer(output, dialect='excel')
    writer.writerows(q.iloc[:,[2]].values) # write place info to new table
    
print("Done.")
