import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import csv, os

path = os.path.dirname(os.path.realpath(__file__))
dowData = []
dowLabels = [] #list(range(0, 1000))

with open(path + "/assets/DJI1990.csv") as csvfile:
    csvfile.readline()   # skip the first line of headers
    reader = csv.reader(csvfile)
    for row in reader:
        dowData.append(float(row[5]))
        dowLabels.append(pd.to_datetime(row[0]))
        # if (len(dowData) >= 30):
        #     break 

# afont = {'family':'monospace'}

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) # Use "2020-01-01" instead of "2020"
ax.plot(dowLabels, dowData)  # Plot data on the axes.
fig.autofmt_xdate()
ax.set_title("Dow Jones Induastrial Average adjusted for infaltion\n(1990-09-01 to 2020-08-30)")
ax.set_xlabel("Date")
ax.set_ylabel("Price (USD)")
ax.grid()

plt.show()
