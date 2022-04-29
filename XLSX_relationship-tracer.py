# Script to trace relationships between people coded in factoid lists

# written for the DigiKAR geohumanities project by Monika Barget,

# USE CASES: analysing explicit relationships mentioned in rel_pers to reconstruct implicit / hidden connections

import csv
import pandas as pd
import numpy as np
import os
from collections import Counter
 
### STEP 1: READ DATA FROM SEVERAL EXCEL FILES IN FACTOID FORMAT

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

# read all excel files in directory as one data frame

frame_list=[]
for item in os.listdir(filenames):
    file = os.path.join(filenames, item)
    df = pd.read_excel(file, sheet_name='FactoidList', axis=1, ignore_index=False, sort=False, encoding="utf-8")
    frame_list.append(df)

f = pd.concat(frame_list, axis=0, ignore_index=False, sort=False)
    
# read factoids from data frame

pers_f=(f[['pers_name']]) # retrieve data from selected column
pers_list=pers_f.values.tolist() # convert data frame to sorted list
pers_list_flat=[item for sublist in pers_list for item in sublist] # flatten list
pers_unique=pers_f.drop_duplicates() # remove duplicates
pers_unique_list=pers_unique.values.tolist() # write unique values to list

### STEP 2: DEFINE RELATIONSHIP MARKERS TO BE QUERIED

name_list=[]

qr=["Ehefrau: ", 
    "Ehemann: ", 
    "Vater: ", 
    "Mutter: ", 
    "Tochter: ",
    "Sohn: ",
    "Bruder: ", 
    "Schwester: ", 
    "Schwiegermutter: ", 
    "Schwiegervater: ", 
    "Schwiegertochter: ", 
    "Schwiegersohn: ",
    "Schwager: ", 
    "Schwägerin: ",
    "Großmutter: ", 
    "Großvater: ",
    "GVm: ",
    "GVv: ",
    "GMm: ",
    "GMv: ",
    "Cousin: ",
    "Cousine: ",
    "Adoptivvater: ",
    "Tante: ",
    "Onkel: ",
    "Patin: ",
    "Pate: "]

### STEP 3: GET UNIQUE NAMES AND THEIR FREQUENCIES
    
print("\n\nYour factoid list contains", len(pers_f), "entries.") # count data in selected column

for i in [item for sublist in pers_unique_list for item in sublist]: # count person occurrences
    print("\n", i, " / ", "Häufigkeit:", pers_list_flat.count(i), "\n") # print name and occurrences

### STEP 2: ITERATE THROUGH UNIQUE PERSONS TO FIND RLEATIONSHIPS

    df_new=f.loc[f['pers_name'] == i]
    print("There are", len(df_new), " entries associated with this name.")
    try:
        condlist = [df_new['rel_pers'].notnull()]
        choicelist = [df_new['rel_pers']]

        output_list = np.select(condlist, choicelist).tolist()
        unique_out_set = set(output_list) # convert to set to remove duplicates
        unique_out_list = list(unique_out_set)
        #print(unique_out_list)
        #print(len(unique_out_list))
        for u in unique_out_list:
            if u == 0:
                continue
            else:
                try:
                    results=u.split("/")
                except:
                    results=u
                for r in results:
                    print(r)
                    #print(type(r))
                    if "$" in r:
                        pers_inf=r.split("$", 1)
                        print("COMPLETE PERSON:", pers_inf)
                        person=pers_inf[0]
                        info=pers_inf[1]
                    else:
                        person=r
                        info=("none")
                    print("PERSON:", person, "INFO:", info)    
                    try:
                        pers_res=person.split(":", 1)
                        function=pers_res[0]
                        name_ident=pers_res[1]
                    except:
                        pers_res=person
                        function="unknown"
                        name_ident=pers_res[0]
                    if "#" in name_ident:
                        name=name_ident.split("#")[0]
                        ident=name_ident.split("#")[1]
                    else:
                        name=name_ident
                        ident=("none")

                    name_list.append([i, function, name, ident, info])

    except AttributeError:
        pass
        
### STEP 3: SAVE TO NEW FILE

print(name_list)
print(len(name_list))

df = pd.DataFrame(name_list)

resultpath='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\Results'
res_filename=input("Enter your file name: ")
res_file=os.path.join(resultpath, res_filename + ".xlsx")

df.to_excel(res_file, index=True)
    
print("Done.")
