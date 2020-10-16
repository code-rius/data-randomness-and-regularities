import numpy as np
import recurrence_plot as rp
import csv

csvData=[]

time = np.arange(0, 180 , 0.3)
amplitude = np.round(np.sin(time), 5)

with open("dow-jones.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        csvData.append(float(row[4]))
        if (len(csvData)>=1000): break

r = (max(csvData) - min(csvData))*0.20

rp.generate_recurrence_plot(3, 1, r, csvData, False)
# rp.generate_recurrence_diagram(3, 2, 0.55, amplitude)

"""
    TODO: 
        1. r calibration
        2. Performance improvement (Use Maximum formula)

"""