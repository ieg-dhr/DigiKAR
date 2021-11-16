# Script to extract modern (German) place names from the Geonames DE.txt file

import re # to handle regular expressions 
import nltk # NLP package
import string

# path of input file

infile="C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\GeonamesDumps\\DE.txt"

# define output list for all identified place names

places_list=[]
most_common=[]
count=-1
exclude_list=["RSTN", "DE", "MRSH", "PPLX", "STM", "CNL", "A", "H", "NL", "P", "CH"]

# open and read file

with open(infile, 'r', encoding="utf-8") as file1:
    text=file1.readlines()
    for line in text:
        count+=1
        #print(line)
        one_place=[]
        tokens=nltk.word_tokenize(line) # tokenize event string  
        num_tokens=len(tokens)
        #print(num_tokens)
        for t in tokens[1:(num_tokens-13)]:
            if not t.isdigit():
                if t in exclude_list:
                    continue
                else:
                    one_place.append(t)
                    no_duplicates=list(set(one_place))
            else: 
                continue
        #print("These are variants of one place without duplicates:", no_duplicates)
        places_list.append(no_duplicates)

#print("These are all places as nested list:")
for p in places_list:
    #print(p)
    most_common.append(p[0])
    
print("These are the", count, "modern (German) places in the Geonames DE.txt file:",)
for m in most_common:
    print(m)
    
        
