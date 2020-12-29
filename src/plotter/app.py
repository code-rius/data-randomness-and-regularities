import numpy as np
from recurrence_plot import RecurrencePlot as rp
import csv
import os
import json
csvData=[]

time = np.arange(0, 180 , 0.3)
amplitude = np.round(np.sin(time), 5)
path = os.path.dirname(os.path.realpath(__file__))

with open(path + "/assets/DJI.csv") as csvfile:
    csvfile.readline()   # skip the first line of headers
    reader = csv.reader(csvfile)
    for row in reader:
        csvData.append(float(row[4]))
        if (len(csvData)>=720): break

dow = rp(3 , 2, csvData, 1)

dow.draw_diagram()