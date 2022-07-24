# Reading biographic data from UB Mainz Gutenberg Biographics XML files

# API link to files: http://gutenberg-biographics.ub.uni-mainz.de/api/items/persons/ccc318f9-f22b-478f-9211-748aafb5bdfe

# written for the DigiKAR project by Monika Barget in May 2022

from bs4 import BeautifulSoup
import os
from os.path import dirname, join
import xlsxwriter
import re

# Define directory for locally stored XML files

directory=("C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\API_Professoren")

# Define list of places to match in API data

places_DigiKAR=[
    'Aachen',
'Abderode',
'Alach',
'Algesheim',
'Altdorf',
'Alzey',
'Amorbach',
'Arnstadt',
'Aschaffenburg',
'Attendorn (Westfalen)',
'Auerstedt',
'Azmannsdorf',
'Bad Lippspringe',
'Bad Mergentheim',
'Bad Wimpfen',
'Basel',
'Beilstein (Landkreis Cochem-Zell)',
'Bennweiler (heute:Bennwihr)',
'Bensheim',
'Beringhausen in Westfalen',
'Berlin',
'Blankenhain',
'Bochum',
'Bonau bei Teuchern',
'Bonn',
'Breslau (heute: Wrocław)',
'Buchtorp',
'Bürstadt',
'Buttstädt',
'Dänemark',
'Darmstadt',
'Dieburg (Hessen)',
'Dresden',
'Duderstadt',
'Düsseldorf',
'Ehingen',
'Eichsfeld',
'Eisenach',
'Elleben',
'Eltville am Rhein',
'Elvershausen',
'Erfuft',
'Erfurt',
'Essen',
'Esslingen am Neckar',
'Europa',
'Frankfurt am Main',
'Frankfurt an der Oder',
'Frankreich',
'Freiburg im Breisgau',
'Friedberg',
'Fulda',
'Gau-Algesheim',
'Gehren',
'Geisenheim',
'Georgenthal',
'Gerolzhofen',
'Gieboldehausen',
'Gmünd (Niederösterreich)',
'Goch',
'Gotha',
'Göttingen',
'Graz',
'Großbartloff',
'Großmölsen bei Erfurt',
'Großostheim',
'Großvargula',
'Gut Geschwende',
'Hadamar',
'Hamburg',
'Hameln',
'Hamm',
'Hammelburg',
'Hannover',
'Harburg',
'Heidelberg',
'Heiligenstadt',
'Heiligenstadt auf dem Eichsfelde',
'Heiligenstadt, Eichsfeld (heute: Heilbad Heiligenstadt)',
'Herdringen',
'Herzogenbusch (’s-Hertogenbosch)',
'Hessen',
'Hildesheim',
'Hoch-Weisel (Butzbach)',
'Hofheim (Unterfranken)',
'Holzweiler (Erkelenz)',
'Horsens (Dänemark)',
'Ichtershausen',
'Idstein',
'Ingolstadt',
'Jena',
'Johannisberg (Rheingau)',
'Kaiserswerth (Düsseldorf)',
'Kassel',
'Kirchworbis',
'Kirchworbis auf dem Eichsfelde',
'Kitzingen',
'Koblenz',
'Köln',
'Konstanz',
'Langensalza',
'Leinefelde (Eichsfeld)',
'Leipzig',
'Lohr am Main',
'London',
'Lorch',
'Lyon',
'Mainz',
'Mainz-Hechtsheim',
'Mannheim',
'Marburg',
'Mayen',
'Meiningen (Thüringen)',
'Meiringen (Schweiz)',
'Meisenbach am Main',
'Melsungen',
'Meschede',
'Mittweida',
'Mittweide',
'Montabaur',
'Mühlberg',
'Mühlhausen',
'München',
'Münstermaifeld',
'Münzenberg',
'Naumburg',
'Naumburg (Saale)',
'Neubamberg',
'Neuhausen (auf den Fildern)',
'Neuss',
'Neuworbis',
'Niederlande',
'Niedernhausen',
'Nürnberg',
'Ohrdruf',
'Oldendorf an der Weser',
'Olm',
'Orb',
'Paris',
'Polen',
'Posen',
'Prag',
'Regensburg',
'Reiffenstein',
'Saarburg',
'Schleiz',
'Schlossvippach',
'Schneeberg im Erzgebirge',
'Sömmerda',
'Sontra',
'Speyer',
'Stadt Worbis auf dem Eichsfelde',
'Stadtworbis',
'Stadtworbis auf dem Eichsfelde',
'Stockholm',
'Tambach im Thüringer Walde',
'Tonndorf',
'Torgau',
'Treffurt',
'Trier',
'Upsala',
'Vippach',
'Vippachedelhausen',
'Vlotho',
'Wandersleben',
'Weimar',
'Weißensee',
'Wendehausen bei Treffurt',
'Wetzlar',
'Wien',
'Worbis',
'Worms',
'Würzburg',
'Zeitz']

# Define list of lists for all results

result_list=[]

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
        #print("Source:", source_id)
        
# get roleName
    roleNames = soup.find_all('roleName')
    for r in roleNames:
        roleName=r.get_text()
        #print("Title:", roleName)

# get foreName
    foreNames = soup.find_all('forename')
    for f in foreNames:
        foreName=f.get_text()
        #print("First name:", foreName)
        
# get addName
    addNames = soup.find_all('addName')
    for a in addNames:
        addName=a.get_text()
        print("Middle name:", addName)        
        
# get surname
    surNames = soup.find_all('surname')
    for s in surNames:
        surName=s.get_text()
        #print("Family name:", surName)
                
# get birth
    try:
        birth_list=[]
        birth = soup.find('birth')
        #print(birth)
        try:
            place = birth.find('placeName')
            place_t=place.get_text()
            date = birth.find('date')
            date_t=date.get_text()
            print(place_t, date_t)
        except:
            place = "none"
            date = birth.find('date')
            date_t=date.get_text()
            
        birthDate = birth.get("when")
        print(birthDate)
        
        if int(birthDate[:4]) <=1800:
            birth_list=(foreName, addName, surName, roleName, "child", place_t, birthDate, birthDate, "birth", "none", "none", "none", date_t, source_id)
            result_list.append(birth_list)
        elif int(birthDate[:4]) >=1800:
            continue
        else:
            birth_list=(foreName, addName, surName, roleName, "child", place_t, "no date", "no date", "birth", "none", "none", "none", date_t, source_id)
            result_list.append(birth_list)

    except:
        pass
    
# get death
    try:
        death_list=[]
        death = soup.find('death')
        try:
            place = death.find('placeName')
            place_t=place.get_text()
            date = death.find('date')
            date_t=date.get_text()
            print(place_t, date_t)
        except:
            place = "none"
            date = death.find('date')
            date_t=date.get_text()
            
        deathDate = death.get("when")
        #print(deathDate)
        
        if int(birthDate[:4]) <=1870:
            death_list=(foreName, addName, surName, roleName, "deceased", place_t, deathDate, deathDate, "death", "none", "none", "none", date_t, source_id)
            result_list.append(death_list)
        elif int(birthDate[:4]) >=1870:
            continue
        else:
            birth_list=(foreName, addName, surName, roleName, "deceased", place_t, "no date", "no date", "birth", "none", "none", "none", date_t, source_id)
            result_list.append(birth_list)
    except:
        pass

# iterate through all other events

    AllEvents = soup.find_all('event')
    print("\n No. of events found:", len(AllEvents), "\n")
    for n in range(0, len(AllEvents)):
        result=[]
        event=soup.findAll('event')[n]
        #print("EVENT no.", n, ":")
        
    # get data from event tag

        try:
            role = event.get('role')
        except KeyError:
            role = "none"
        #print("Person role:", role)
        try:
            startDate = event.get('from')
        except KeyError:
            startDate = "none"
        #print("Start date:", startDate)
        try:
            endDate = event.get('to')
        except KeyError:
            endDate = "none"
        #print("End date:", endDate)
 
    # read event data from all bs4.element.Tag

        try:
            label = event.find('label')
            label_t=label.get_text()
        except (KeyError, AttributeError):
            label_t = "none"
        #print("Event type:", label_t)
        try:
            orgName = event.find('orgName')
            orgName_t=orgName.get_text()
        except (KeyError, AttributeError):
            orgName_t = "none"
        #print("Institution:", orgName_t)
        try:
            affiliation = event.find('affiliation')
            affiliation_t=affiliation.get_text()
        except (KeyError, AttributeError):
            affiliation_t = "none"
        #print("Affiliation:", affiliation_t)
        try:
            relPers = event.find('persName')
            relPers_t=relPers.get_text()
        except (KeyError, AttributeError):
            relPers_t = "none"
        #print("Related Person:", relPers_t, "\n")
        
        try:
            note = event.find('note')
            note_t=note.get_text()
            note_tokens=re.split("[, \-!?:\n(]+", note_t)
            print(note_tokens)
            for p in places_DigiKAR:
                if p in note_tokens:
                    place_n=p
                    #print(place_n)
                elif "Universität" and "Mainz" in note_tokens:
                    place_n="Universität Mainz"
                    #print(place_n)
                elif "Mainzer" in note_tokens:
                    place_n="Kurfürstliches Schloss Mainz"
                    #print(place_n)
                elif "Dom" and "Mainz" in note_tokens:
                    place_n="Dom Mainz"
                    #print(place_n)
                else:
                    place_n="no place"
            
        except (KeyError, AttributeError):
            note_t = "no note"
        #print("Note:", note_t, "\n", type(note_t))
        
        try:
            if int(startDate[:4]) >= 1850:
                pass
            elif str(startDate[6:10]) == "01:01":
                result=(foreName, addName, surName, roleName, role, place_n, str(startDate[:4]), str(endDate[:4]), label_t, orgName_t, affiliation_t, relPers_t, note_t, source_id)
            else:
                result=(foreName, addName, surName, roleName, role, place_n, startDate, endDate, label_t, orgName_t, affiliation_t, relPers_t, note_t, source_id)

            result_list.append(result)
        except ValueError:
            result=(foreName, addName, surName, roleName, role, place_n, startDate, endDate, label_t, orgName_t, affiliation_t, relPers_t, note_t, source_id)
            result_list.append(result)
               
# write events to EXCEL 

with xlsxwriter.Workbook('C:\\Users\\mobarget\\Documents\\Seafile\\DigiKAR_DATEN\\Python\\Results\\ProfEvents_v10.xlsx') as workbook:
    sheet = workbook.add_worksheet()
    row = 0
    col = 0

    for line in result_list:
        for item in line:
            sheet.write(row, col, item)
            col += 1
        row += 1
        col = 0
    workbook.close()
    
print("done")
        
