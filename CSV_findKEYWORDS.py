# finding rows that contain one of several keywords in "place" column of CSV file

import csv
import pandas as pd
import numpy as np

CSV_FILE='<your path>.csv' # define input file
CSV_OUTPUT='C<your path>.csv' # define output file
searchterms=['Mainz', 'Mayntz', 'Mayence'] # define list of searchterms

with open(CSV_FILE, encoding="utf-8") as f: # open input file
    data = pd.read_csv(f, sep=",") # read input file as CSV
    for x in searchterms:
        data_selected=data[data.Place == x] # find all searchterms in the "place" column of the CSV file
        print(data_selected) # print selected data
        data_selected.to_csv(CSV_OUTPUT) # write selected data to output file
