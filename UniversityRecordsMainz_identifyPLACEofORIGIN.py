# Script to read places of origin from the semi-structured transcripts of early modern university records from Mainz
# provided in PDF format and read to TXT
# delimiters such as #PERSON and #SOURCE were introduced to identify individual entries

import re # to handle regular expressions 
import nltk # NLP package

# path of input file

infile="C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Universitätsmatrikeln\\students_hashtags_corr9_source-added.txt"

# define output list for all identified place names and tokens to exclude

origin_list=[]
exclude_list=["get", "erhält", "*", "+", "V", "=", "hat", "oo", "-", "phil", "theol",
              "Bittet", "bittet", "mag", "stud", ".", "Mag", "bac", "bacc", "Bacc", 
              "Dr.", "paup.", "paup", "Pfr", "log", "lic", "Lic."] # titles and biographic info not to be read as place
delimiters=[".", "/", "-"]
regexPattern='|'.join(map(re.escape, delimiters))
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
            one_token=first_tokens[0] # place of origin is most likely FIRST token in first event
            second_token=first_tokens[1] # get 2nd token
            digit1=re.split(regexPattern, one_token)[0] # handle date variants in first token
            digit2=re.split(regexPattern, second_token)[0] # handle date variants in second token
            four_tokens=first_tokens[:4] # place of origin is most likely first FOUR tokens in first event
             
# check validity of 1st token 
            
            if one_token.isdigit():
                print("EXCLUDE NUMBER:", one_token)
                continue
            if one_token in exclude_list:
                print("EXCLUDE INFO:", one_token)
                continue 
            if digit1.isdigit():
                print("EXCLUDE NUMBER:", one_token)
                continue
            else:    
                
# check validity of 2nd token
                if second_token in exclude_list:
                    print("EXCLUDE INFO:", second_token)
                    origin_list.append(one_token)
                    continue
                if second_token.isdigit():
                    print("EXCLUDE NUMBER:", second_token)
                    origin_list.append(one_token)
                    continue
                if digit2.isdigit():
                    print("EXCLUDE NUMBER:", second_token)
                    origin_list.append(one_token)
                    continue
                else:
                    origin_list.append(four_tokens)
        except:
            pass
                            
# output result

for o in origin_list:
    print(o) # write each entry to new row


        
