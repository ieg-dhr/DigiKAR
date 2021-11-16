# Script to read places of origin from the semi-structured transcripts of early modern university records from Mainz
# provided in PDF format and read to TXT
# delimiters such as #PERSON and #SOURCE were introduced to identify individual entries

import re # to handle regular expressions 
import nltk # NLP package

# path of input file

infile="C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Universitätsmatrikeln\\#####.txt"

# define output list for all identified place names

origin_list=[]
person_list=[]
result_list
count=-1

# open and read file

with open(infile, 'r', encoding="utf-8") as file1:
    text=file1.read() 
    
# split on hashtag to extract entries for each person
    persons=text.split("#PERSON")
    for p in persons:
        count+=1
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
            
# find places of origin            
        try:
            origin=first_tokens[:2] # place of origin is most likely first TWO tokens in first event
            origin_list.append(origin) # write all presumed places to one list to clean manually
        except:
            pass
                            
# output result

for o in origin_list:
    print(o) # write each entry to new row

        
