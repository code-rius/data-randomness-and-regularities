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

r = (max(csvData) - min(csvData))*0.20

dow = rp(4 , 1, csvData)

dow.get_pixel_percentage()
dow.draw_diagram()

# rp.generate_recurrence_diagram(3, 2, 0.55, amplitude)

# print(plotdata)
"""
    TODO: 
        1. r calibration
        2. Performance improvement (Use Maximum formula)
"""
