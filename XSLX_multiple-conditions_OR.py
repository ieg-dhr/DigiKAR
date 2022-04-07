# Script to compare data from several EXCEL files

# written for the DigiKAR geohumanities project by Monika Barget,
# with kind support by https://stackoverflow.com/users/8479387/tlentali

# USE CASES: flexibly matching conditions across EXCEL columns

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
    df = pd.read_excel(file, sheet_name='FactoidList', axis=1, ignore_index=False, sort=False)
    frame_list.append(df)

f = pd.concat(frame_list, axis=0, ignore_index=False, sort=False)
    
# read factoids from data frame

pers_f=(f[['pers_name']]) # retrieve data from selected column
pers_list=pers_f.values.tolist() # convert data frame to sorted list
pers_list_flat=[item for sublist in pers_list for item in sublist] # flatten list
pers_unique=pers_f.drop_duplicates() # remove duplicates
pers_unique_list=pers_unique.values.tolist() # write unique values to list
    
print("\n\nYour factoid list contains", len(pers_f), "entries.") # count data in selected column

#for i in [item for sublist in pers_unique_list for item in sublist]: # count person occurrences
    #print("\n", i, " / ", "Häufigkeit:", pers_list_flat.count(i), "\n") # print name and occurrences
    
### STEP 2: LET USER SELECT SEARCH CRITERIA

# queried names
print("Enter person names, separated by commas, or @.")
q_name=input()
# queried year  
print("Date(s):")
ex_year=input() 
# select type of time processing
print("No date selected (0), exact dates (1), data range (2), BEFORE date (3) or AFTER date (4)?")
z=input() 
# queried institution
print("Enter institutions, separated by commas, or @:")
q_inst=input() 
# queried title
print("Enter person titles, separated by commas, or @:")
q_title=input() 
# queried function
print("Enter person functions, separated by commas, or @:")
q_func=input() 
# queried related person
print("Enter related persons, separated by commas, or @:")
q_rel=input() 

# separate entries if lists of search terms have been submitted
qn=q_name.split(", ")
exy=ex_year.split(", ")
qi=q_inst.split(", ") 
qt=q_title.split(", ") 
qf=q_func.split(", ") 
qr=q_rel.split(", ")

in_lists=[[qn], [qi], [qt], [qf], [qr]]

# handling data input with different frequences from YYYY to YYYY-MM-DD

try:
    if len(exy[1]) & len(exy[0]) == 4:
        d1=pd.Period(exy[0], freq="Y") # convert input to Period with year frequence
        end_date=int(exy[1])+1 # add one year to expand end range
        d2=pd.Period(str(end_date), freq="Y") # convert input to Period with year frequence
    elif len(exy[1]) & len(exy[0]) == 7:
        d1=pd.Period(exy[0], freq="M") # convert input to Period with month frequence
        d2=pd.Period(exy[1], freq="M") # convert input to Period with month frequence
    elif len(exy[1]) & len(exy[0]) == 10:
        d1=pd.Period(exy[0], freq="D") # convert input to Period with day frequence
        d2=pd.Period(exy[1], freq="D") # convert input to Period with day frequence
    else:
        d1=pd.Period(exy[0], freq="D") # convert input to Period with day frequence
        d2=pd.Period(exy[1], freq="D") # convert input to Period with day frequence
    
except IndexError:
    pass
except ValueError:
    pass


### STEP 3: RUN QUERY BASED ON TIME CONDITIONS

## CASE 0: NO TIME SELECTED

if z=="0": # no dates 
    if "@" in qn and "@" in qi and "@" in qt and "@" in qf and "@" in qr:
        print("No search criteria selected!")
        
    else:
        
# define possible conditions and choices

        condlist = [(f['pers_name'].str.contains('|'.join(qn)) ^ f['pers_name'].isin(qn)),
                    f['inst_name'].isin(qi),
                    f['pers_title'].isin(qt),
                    f['pers_function'].isin(qf),
                    (f['rel_pers'].str.contains('|'.join(qr)) ^ f['rel_pers'].isin(qr)),]

        choicelist = [f['pers_name'], 
                      f['inst_name'], 
                      f['pers_title'],
                      f['pers_function'],
                      f['rel_pers']]

        output = np.select(condlist, choicelist)
        rows=np.where(output)
        new_array=f.to_numpy()
        result_array=new_array[rows]
        print(result_array)
        
## CASE 1: SEARCHING FOR EXACT DATES
        
elif z=="1": # get exact dates 
    print("Searching for dates:", exy)
    df_list=[]
    for x in exy:
        if len(x) == 4:
            date_searched=pd.Period(x, freq="Y") # convert input to Period with year frequence
            for n in range(0, len(pers_f)):
                try:
                    if date_searched == pd.Period(f['event_start'].iloc[n], freq="Y"):
                        date_found=pd.Period(f['event_start'].iloc[n])
                        f_match=f.iloc[[n]]
                        df_list.append(f_match)
                    else:
                        #print("Outside time frame.") # optional for data cleaning
                        continue
                except ValueError:
                    #print(ValueError.args, ":", f['event_start'].iloc[n]) # optional for data cleaning
                    pass
            
        elif len(x) == 7:
            date_searched=pd.Period(x, freq="M") # convert input to Period with month frequence
            for n in range(0, len(pers_f)):
                try:
                    if date_searched == pd.Period(f['event_start'].iloc[n], freq="M"):
                        date_found=pd.Period(f['event_start'].iloc[n])
                        f_match=f.iloc[[n]]
                        df_list.append(f_match)
                    else:
                        #print("Outside time frame.") # optional for data cleaning
                        continue
                except ValueError:
                    #print(ValueError.args, ":", f['event_start'].iloc[n]) # optional for data cleaning
                    pass
        
        elif len(x) == 10:  
            date_searched=pd.Period(x, freq="D") # convert input to Period with day frequence
            for n in range(0, len(pers_f)):
                try:
                    if date_searched == pd.Period(f['event_start'].iloc[n], freq="D"):
                        date_found=pd.Period(f['event_start'].iloc[n])
                        f_match=f.iloc[[n]]
                        df_list.append(f_match)
                    else:
                        #print("Outside time frame.") # optional for data cleaning
                        continue
                except ValueError:
                    #print(ValueError.args, ":", f['event_start'].iloc[n]) # optional for data cleaning
                    pass
    
    
    f_new = pd.concat([df_list], axis=1, ignore_index=False, sort=False)
        
    try:
        
# define possible conditions and choices

        condlist = [f_new['pers_name'].str.contains(str(qn)) ^ f_new['pers_name'].str.contains('|'.join(qn)) ^ f_new['pers_name'].isin(qn), 
                                f_new['inst_name'].isin(qi), 
                                f_new['pers_title'].isin(qt),
                                f_new['pers_function'].isin(qf),
                                f_new['rel_pers'].str.contains('|'.join(qr)) ^ f_new['rel_pers'].isin(qr)]

        choicelist = [f_new['pers_name'],
                                f_new['inst_name'], 
                                f_new['pers_title'],
                                f_new['pers_function'],
                                f_new['rel_pers']]

        output = np.select(condlist, choicelist)
        rows=np.where(output)
        new_array=f_new.to_numpy()
        result_array=new_array[rows]
        
    except ValueError:
        #print(ValueError.args, ":", f['event_start'].iloc[n])
        pass
    
## CASE 2: SEARCHING FOR DATE RANGE

elif z=="2": # get date range
    print("Searching for date range between", d1, "and", d2, "!") 
    for n in range(0, len(pers_f)):
        f_new=pd.DataFrame(columns=column_names)
        try:
            df_list=[]
            if d1 <= pd.Period(f['event_start'].iloc[n], freq="Y") <= d2:
                date_found=pd.Period(f['event_start'].iloc[n])
                f_match=f.iloc[[n]]
                df_list.append(f_match)
            else:
                #print("Outside time frame.")
                continue
        except ValueError:
            #print(ValueError.args, ":", f['event_start'].iloc[n])
            pass
    
   
    f_new = pd.concat(df_list, axis=1, ignore_index=False, sort=False)

# define possible conditions and choices

    if "#" in qn and "#" in qi and "#" in qt and "#" in qf and "#" in qr:
        result_df=f_new
    else:
        condlist = [(f_new['pers_name'].str.contains('|'.join(qn)) ^ f_new['pers_name'].isin(qn)),
                    f_new['inst_name'].isin(qi), 
                    f_new['pers_title'].isin(qt),
                    f_new['pers_function'].isin(qf),
                    f_new['rel_pers'].str.contains('|'.join(qr)) ^ f_new['rel_pers'].isin(qr)]

        choicelist = [f_new['pers_name'],
                    f_new['inst_name'], 
                    f_new['pers_title'],
                    f_new['pers_function'],
                    f_new['rel_pers']]

        output = np.select(condlist, choicelist)
        rows=np.where(output)
        new_array=f_new.to_numpy()
        result_array=new_array[rows]


## CASE 3: SEARCHING FOR DATES BEFORE      

elif z=="3": #get dates before
    print("Searching for dates before", pd.Period(exy[0], freq="D"), "!")
    nf=pd.DataFrame(columns=column_names)
    for n in range(0, len(pers_f)):
        try: 
            if pd.Period(f['event_start'].iloc[n], freq="D") <= pd.Period(exy[0], freq="D"):
                nf=nf.append(f.iloc[n], ignore_index=False, sort=False)
            elif pd.Period(f['event_before-date'].iloc[n], freq="D") <= pd.Period(exy[0], freq="D"):
                nf=nf.append(f.iloc[[n]], ignore_index=False, sort=False)
            else:
                continue
        except ValueError:
            pass
    # define possible conditions and choices
    if "@" in qn and "@" in qi and "@" in qt and "@" in qf and "@" in qr:
        result_df1=nf
    else:
        condlist = [(nf['pers_name'].str.contains('|'.join(qn)) ^ nf['pers_name'].isin(qn)), 
                    nf['inst_name'].isin(qi), 
                    nf['pers_title'].isin(qt),
                    nf['pers_function'].isin(qf),
                    nf['rel_pers'].str.contains('|'.join(qr)) ^ nf['rel_pers'].isin(qr)]

        choicelist = [nf['pers_name'],
                    nf['inst_name'], 
                    nf['pers_title'],
                    nf['pers_function'],
                    nf['rel_pers']]

        output = np.select(condlist, choicelist)
        rows=np.where(output)
        new_array=nf.to_numpy()
        result_array=new_array[rows]
        
## CASE 4: SEARCHING FOR DATES AFTER        

elif z=="4": # get dates after
    print("Searching for dates after", pd.Period(exy[0], freq="D"), "!")
    nf=pd.DataFrame(columns=column_names)
    for n in range(0, len(pers_f)):
        try: 
            if pd.Period(f['event_start'].iloc[n], freq="D") >= pd.Period(exy[0], freq="D"):
                nf=nf.append(f.iloc[[n]], ignore_index=False, sort=False)
            elif pd.Period(f['event_after-date'].iloc[n], freq="D") >= pd.Period(exy[0], freq="D"):
                nf=nf.append(f.iloc[[n]], ignore_index=False, sort=False)
            else:
                continue
        except ValueError:
            pass
        # define possible conditions and choices
        if "@" in qn and "@" in qi and "@" in qt and "@" in qf and "@" in qr:
             result_df1=nf
        else:
            condlist = [(nf['pers_name'].str.contains('|'.join(qn)) ^ nf['pers_name'].isin(qn)), 
                    nf['inst_name'].isin(qi), 
                    nf['pers_title'].isin(qt),
                    nf['pers_function'].isin(qf),
                    nf['rel_pers'].str.contains('|'.join(qr)) ^ nf['rel_pers'].isin(qr)]
            
            choicelist = [nf['pers_name'],
                      nf['inst_name'], 
                      nf['pers_title'],
                      nf['pers_function'],
                      nf['rel_pers']]

            output = np.select(condlist, choicelist)
            rows=np.where(output)
            new_array=nf.to_numpy()
            result_array=new_array[rows]
            
else:
    print("INVALID TIME OPERATOR!")
            
### STEP 4: convert result array into a dataframe

try:
    result_df2 = pd.DataFrame(result_array)
    result_df=pd.concat([result_df1, result_df2], axis=1, ignore_index=False, sort=False)
    
    print("Elements found: ", result_df[6]) # only show names
  
    # save to xlsx file

    resultpath='C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\Results'
    res_filename=input("Enter your file name: ")
    res_file=os.path.join(resultpath, res_filename + ".xlsx")

    result_df.to_excel(res_file, index=True)
    
    print("Done.") 
    
except NameError as er:
    print(er.args)
    print("No results retrieved! Try again.")
