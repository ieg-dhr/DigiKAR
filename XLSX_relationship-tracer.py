# Script to trace relationships between people coded in factoid lists

# written for the DigiKAR geohumanities project by Monika Barget,

# USE CASES: analysing explicit relationships mentioned in rel_pers to reconstruct implicit / hidden connections

import csv
import pandas as pd
import numpy as np
import os
from collections import Counter
from itertools import combinations
from itertools import product
 
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
    df = pd.read_excel(file, sheet_name='FactoidList', header=0)
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

### STEP 2: GET UNIQUE NAMES AND THEIR FREQUENCIES
    
print("\n\nYour factoid list contains", len(pers_f), "entries.") # count data in selected column

for i in [item for sublist in pers_unique_list for item in sublist]: # count person occurrences
    #print("\n", i, " / ", "Häufigkeit:", pers_list_flat.count(i), "\n") # print name and occurrences

### STEP 3: ITERATE THROUGH UNIQUE PERSONS TO FIND RELATIONSHIPS

    df_new=f.loc[f['pers_name'] == i]
    #print("There are", len(df_new), " entries associated with this name.")
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
                    #print(r)
                    #print(type(r))
                    if "$" in r:
                        pers_inf=r.split("$", 1)
                        #print("COMPLETE PERSON:", pers_inf)
                        person=pers_inf[0]
                        info=pers_inf[1]
                    else:
                        person=r
                        info=("none")
                    #print("PERSON:", person, "INFO:", info)    
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
    
### STEP 4: CONVERT NAME LIST TO DF:

f2 = pd.DataFrame(name_list)
f2.columns=["i", "function", "name", "ident", "info"]
print(f2)
    
### STEP 4: RECONSTRUCT SIBLINGS:

siblings1=['Bruder', 'Schwester']
siblings2=['Sohn', 'Tochter']

df_sibling_brother=f2.loc[f2['function'] == siblings1[0]]
for brother in df_sibling_brother.iterrows():
    brother_current=brother[1].to_frame()
    brother_reversed=[brother_current.loc['name'].values, "brother", brother_current.loc['i'].values, "unknown", "no info"]
    name_list.append(brother_reversed)

df_sibling_sister=f2.loc[f2['function'] == siblings1[1]]
for sister in df_sibling_sister.iterrows():
    sister_current=sister[1].to_frame()
    sister_reversed=[sister_current.loc['name'].values, "brother", sister_current.loc['i'].values, "unknown", "no info"]
    name_list.append(sister_reversed)

for s2 in siblings2:
    df_sibling2=f2.loc[f2['function'] == s2]
    for child in df_sibling2.iterrows():
        child_current=child[1].to_frame()
        child_reversed=[child_current.loc['name'].values, "parent", child_current.loc['i'].values, "unknown", "no info"]
        name_list.append(child_reversed)
        
    parents=df_sibling2['i'].unique() # unique names of parents in dataframe
    for parent in parents: # find children per parent
        df_family = df_sibling2[df_sibling2['i'] == parent]
        siblings_in_family=df_family['name'].unique() # unique names of sibling in family
        siblings_number=len(siblings_in_family) # number of siblings in family
        siblings_res=list(combinations(siblings_in_family, 2)) # find all possible sibling pairs
        for pair in siblings_res:
            if pair[0] == pair[1]:
                continue
            else: 
                pair1=[pair[0], "sibling", pair[1], "unknown", "no info"]
                name_list.append(pair1)
                pair2=[pair[1], "sibling", pair[0], "unknown", "no info"]
                name_list.append(pair2)
            
### STEP 5: RECONSTRUCT GRANDPARENTS / GRANDCHILDREN:

grandchildren1=['Vater', 'Mutter']
grandchildren2=['Enkel', 'Enkelin']
grandchildren3=["GVm","GVv", "GMm", "GMv"]

for g1 in grandchildren1: # FIND GRANPARENTS / GRANDCHILDREN via KNOWN PARENTS
    df_grandchildren1=f2.loc[f2['function'] == g1]
    grandparents=df_grandchildren1['name'].unique() # unique names of parents = grandparents in data frame
    parents=df_grandchildren1['i'].unique() # unique names of children = parents in data frame
    for parent in parents:
        for s2 in siblings2:
            df_grandchildren4=f2.loc[f2['i'] == parent][f2['function'] == s2]
            grandchildren=df_grandchildren4['name'].unique() # unique names of grandchildren in family
            grandparents_per_parent=df_grandchildren1.loc[df_grandchildren1['i'] == parent]
            grandparents_values=grandparents_per_parent['name'].unique() # unique names of grandparents per parent
            
            grandchildren_res = list(list(zip(grandparents_values, element))
                           for element in product(grandchildren, repeat = len(grandparents_values)))
            grandchildren_flat=[x for y in grandchildren_res for x in y]
            #print(grandchildren_flat)
            # find all possible grandchild-grandparent pairs for each parent link
            for pair in grandchildren_flat:
                pair1=[pair[0], "grandparent-grandchild", pair[1], "unknown", "no info"]
                name_list.append(pair1)
                pair2=[pair[1], "grandparent-grandchild", pair[0], "unknown", "no info"]
                name_list.append(pair2)
    
for g2 in grandchildren2: # FIND GRANDPARENTS FOR KNOWN GRANDCHILDREN
    df_grandchildren2=f2.loc[f2['function'] == g2]
    for gc2 in df_grandchildren2.iterrows():
        gc_current2=gc2[1].to_frame()
        gc_reversed2=[gc_current2.loc['name'].values, "grandchild", gc_current2.loc['i'].values, "unknown", "no info"]
        name_list.append(gc_reversed2)
    

#print(df_grandchildren2)

for g3 in grandchildren3: # FIND GRANDCHILDREN FOR KNOWN GRANDPARENTS
    df_grandchildren3=f2.loc[f2['function'] == g3]
    for gc3 in df_grandchildren3.iterrows():
        gc_current3=gc3[1].to_frame()
        gc_reversed3=[gc_current3.loc['name'].values, "grandchild", gc_current3.loc['i'].values, "unknown", "no info"]
        name_list.append(gc_reversed3)
            
### STEP 5: SAVE TO NEW FILE

#print(name_list)
#print(len(name_list))

df = pd.DataFrame(name_list)

resultpath='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\Results'
res_filename=input("Enter your file name: ")
res_file=os.path.join(resultpath, res_filename + ".xlsx")

df.to_excel(res_file, index=True)
    
print("Done.") 
