# Script to read place names from geographic list (e.g. Geonames) and find them in semi-structured text
# example: student list from the early modern Mainz University records, collected and edited in the 19th and early 20th centuries

import re # to handle regular expressions 
import nltk # NLP package
import requests # to read data from website

# path of input files

infile="C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Universitätsmatrikeln\\students_hashtags_corr9_source-added.txt" # here: student list
geonames="https://raw.githubusercontent.com/ieg-dhr/DigiKAR/main/Geonames_PLACESmodernDE.txt" # list of place names to be matched

# read geonames list via URL

r=requests.get(geonames)
places=nltk.word_tokenize(r.text)
print(places[10]) # print place no. "n" in list

# define output list for all identified place names

students_places=[]
count=-1

# open and read txt file

with open(infile, 'r', encoding="utf-8") as file1:
    text=file1.read() 
    
# split on hashtag to extract entries for each person
    persons=text.split("#PERSON")
    for p in persons:
        info_ref=p.split("#SOURCE") # separate person info from source references
        info=info_ref[0] # get person info by index
        ref=info_ref[-1] # get refrences by index
        
# split on semi-colon to extract individual names
        one_pers=info.split(";")
  
# call name as first element
        name=one_pers[0]
  
# call events as second and following elements        
        try:
            events=one_pers[1:] 
            first=one_pers[1] # select first event as it most likely contains place information
            first_tokens=nltk.word_tokenize(first) # tokenize event string
        except:
            pass
            
# find places in first event           
        try:
            for f in first_tokens:
                if f in places:
                    count+=1
                    students_places.append(f) # add results to new list
                else:
                    continue
        except:
            pass
                            
# output result list of all place names found

print(count, "place names were found in student list.")
for s in students_places:
    print(s) # write each entry to new row
