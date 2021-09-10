# script to read all data from selected column in CSV

import csv
import pandas as pd
import numpy as np

CSV_FILE='<your path>.csv'

with open(CSV_FILE, encoding="utf-8") as f:
    data = pd.read_csv(f, sep=",")
    data_by_col=(data[['Place']]) # retrieve data from selected column, in this case "place"
    print(data_by_col) # print data from selected column
