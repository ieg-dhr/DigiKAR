# Reading biographic data from UB Mainz Gutenberg Biographics XML files

# API link to files: http://gutenberg-biographics.ub.uni-mainz.de/api/items/persons/ccc318f9-f22b-478f-9211-748aafb5bdfe

# written for the DigiKAR project by Monika Barget in May 2022

from bs4 import BeautifulSoup
import os
from os.path import dirname, join

# Define directory for locally stored XML files

directory=("C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\API_Professoren")

# Iterate through all XML files in directory

results=[]
for infile in os.listdir(directory):
    filename=join(directory, infile)
    indata=open(filename,"r", encoding="utf-8", errors="ignore") 
    contents = indata.read()
    soup = BeautifulSoup(contents,'xml')
    
# get item ID

    idno = soup.find_all('idno')
    for i in idno[0]:
        source_id=i.get_text()
        print("Source:", source_id)
        
# get roleName
    roleNames = soup.find_all('roleName')
    for r in roleNames:
        roleName=r.get_text()
        print("Title:", roleName)

# get foreName
    foreNames = soup.find_all('forename')
    for f in foreNames:
        foreName=f.get_text()
        print("First name:", foreName)
        
# get surname
    surNames = soup.find_all('surname')
    for s in surNames:
        surName=s.get_text()
        print("Family name:", surName)
        
# iterate through all events

    AllEvents = soup.find_all('event')
    print("\n No. of events found:", len(AllEvents), "\n")
    for n in range(0, 10):
        event=soup.findAll('event')[n]
        print("EVENT no.", n, ":")
        
    # get data from event tag

        try:
            role = event.get('role')
        except KeyError:
            role = "none"
        print("Person role:", role)
        try:
            startDate = event.get('from')
        except KeyError:
            startDate = "none"
        print("Start date:", startDate)
        try:
            endDate = event.get('to')
        except KeyError:
            endDate = "none"
        print("End date:", endDate)
 
    # read event data from all bs4.element.Tag

        try:
            label = event.find('label')
            label_t=label.get_text()
        except (KeyError, AttributeError):
            label_t = "none"
        print("Event type:", label_t)
        try:
            orgName = event.find('orgName')
            orgName_t=orgName.get_text()
        except (KeyError, AttributeError):
            orgName_t = "none"
        print("Institution:", orgName_t)
        try:
            affiliation = event.find('affiliation')
            affiliation_t=affiliation.get_text()
        except (KeyError, AttributeError):
            affiliation_t = "none"
        print("Affiliation:", affiliation_t)
        try:
            relPers = event.find('persName')
            relPers_t=relPers.get_text()
        except (KeyError, AttributeError):
            relPers_t = "none"
        print("Related Person:", relPers_t, "\n")
    
print("done")
