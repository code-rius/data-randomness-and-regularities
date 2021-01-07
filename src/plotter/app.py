import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import csv
import os
import shutil
import random
from scipy import signal as sg
from recurrence_plot import RecurrencePlot as rp
csvData=[]

plt.rcParams.update({'font.size': 16})

time = np.arange(0, 20, 0.05)
amplitude = np.round(np.sin(time), 10)
path = os.path.dirname(os.path.realpath(__file__))

with open(path + "/assets/DJI.csv") as csvfile:
    csvfile.readline()   # skip the first line of headers
    reader = csv.reader(csvfile)
    for row in reader:
        csvData.append(float(row[4]))
        if (len(csvData)>=720): break

dow = rp(1, 1, amplitude, 1, 17.5, 0)

dow.draw_diagram()
print(dow.r)

title = "Generated sine signal"
fig, ax = plt.subplots()  # Create a figure containing a single axes.

ax.plot(list(range(len(csvData))), csvData)  # Plot data on the axes.
ax.set_title(title)
ax.grid()

plt.savefig('plotgraph.png')
# round_to_tenths = [round(num, 6) for num in amplitude]
# print(round_to_tenths)
