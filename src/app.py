import numpy as np
from recurrence_plot import RecurrencePlot as rp
import csv

csvData=[]

time = np.arange(0, 180 , 0.3)
amplitude = np.round(np.sin(time), 5)

with open("dow-jones.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        csvData.append(float(row[4]))
        if (len(csvData)>=1000): break

dow = rp(2 , 1, csvData)
dow.draw_diagram()