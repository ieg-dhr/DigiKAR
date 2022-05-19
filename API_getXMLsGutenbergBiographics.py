# Script to scrape XML files from Gutenberg Biographics API
# written for the DigiKAR geohumanities project by Monika Barget in May 2022

import requests
import urllib.request
import os
from bs4 import BeautifulSoup
import bs4.builder._lxml
from xml.etree.ElementTree import XML, fromstring

# URL to be called

gutenberg_url="http://gutenberg-biographics.ub.uni-mainz.de/api/items/persons/"

# function to extract html document from given url
# as suggested on https://www.geeksforgeeks.org/beautifulsoup-scraping-link-from-html/

def getHTMLdocument(url):
      
    # request for HTML document of given url
    response1 = requests.get(url)
      
    # response will be provided in JSON format
    return response1.text

# Navigate to the application home page

html_document = getHTMLdocument(gutenberg_url)
soup = BeautifulSoup(html_document, 'xml')

# Find links for all XML files

links = soup.find_all('resource')

# create counter to number files

counter=0
no_links=len(links)

# traverse list and get individual XML URLs

for lnk in links:
    index=links.index(lnk)
    counter=+index
    print(counter)
    print(lnk)
    l = lnk.get("href")
    print(l) 
    
# use new URL to access individual XML files

    response2 = requests.get(l)
    outfile=response2.text
    #print(outfile)
    #print(type(outfile)) returns XML as string
    
# save each XML files to local drive

    with open(os.path.join("C:\\Users\\mobarget\\Downloads\\ProfAPI", str(counter) + '.xml'), 'w', encoding="utf-8") as f:
        f.write(outfile)
        print("File no.", counter, "downloaded!")
                    
print("Done")
