import numpy as np
import recurrence_plot as rp
import csv

csvData=[]

time = np.arange(0, 180 , 0.3)
amplitude = np.round(np.sin(time), 5)

with open("dow-jones.csv") as csvfile:
    # change contents to floats
    reader = csv.reader(csvfile)
    for row in reader:  # each row is a list
        csvData.append(float(row[4]))
        if (len(csvData)>1000):
            break

print(max(csvData))
print(min(csvData))

# print(max(csvData) - min(csvData))
r = (max(amplitude) - min(amplitude))*0.15

print(r)
# rp.generate_recurrence_diagram(2, 1, r, csvData)
rp.generate_recurrence_diagram(3, 2, 0.55, amplitude)
