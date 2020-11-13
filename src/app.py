import numpy as np
from recurrence_plot import RecurrencePlot as rp
import csv
import os
csvData=[]

time = np.arange(0, 180 , 0.3)
amplitude = np.round(np.sin(time), 5)
path = os.path.dirname(os.path.realpath(__file__))

with open(path + "/assets/dow-jones.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        csvData.append(float(row[4]))
        if (len(csvData)>=1000): break

dow = rp(10 , 3, csvData, 1)
# dow.draw_diagram()