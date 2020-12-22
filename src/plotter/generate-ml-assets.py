import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import csv
import os
import shutil
import random
from recurrence_plot import RecurrencePlot as rp


def create_new_file(file1, file2_name, file2_dir):
    src_dir = os.getcwd()
    print(src_dir + '/' + file1)

    if (os.path.isfile(src_dir + '/' + file1) is True):
        print("We found the file")
        # Declaring file paths
        source_file = src_dir + '/' + file1
        dest_file = src_dir + '/' + file2_dir + file2_name

        print('Source file path:\t', source_file,
            '\nDestination file path:\t', dest_file)

        shutil.move(source_file, dest_file)
        # print(os.listdir(src_dir + file2_dir))
    else:
        print("create_new_file: file not found")

############################################
# Generating trend data
############################################


# time = np.arange(0, 20, 0.03)
# amplitude = np.round(np.sin(time), 5)
# print(amplitude)


data = [1]
# exponent_rate_up = random.uniform(0,50)
# exponent_rate_down = random.uniform(0, 49)
# for i in range(0,720):
    # newVal = 
    # if (i % 2) == 0:
    #     newVal = data[-1]+exponent_rate_up
    # else:
    #     newVal = data[-1]-exponent_rate_down
    # data.append(newVal)
    # print(newVal)

# dow = rp(3, 2, data, 1, 15, 0.3)
# dow.draw_diagram()

dates = pd.date_range("2019-1-1", "2019-4-1", freq="D")


def trend(count, start_weight=1, end_weight=3):
    lin_sp = np.linspace(start_weight, end_weight, count)
    return lin_sp/sum(lin_sp)


date_trends = np.random.choice(dates, size=200000, p=trend(len(dates)))

print("Total dates", len(date_trends))

print("counts of each dates")
print(np.unique(date_trends, return_counts=True)[1])

# dow=rp(3,2,amplitude,1,75,0.3)
# dow.draw_diagram()

# create_new_file('plotpic.png', 'periodic.png', 'ml-data/')

# dowData = []
# dowLabels = []

# path = os.path.dirname(os.path.realpath(__file__))

# with open(path + "/assets/DJI1990.csv") as csvfile:
#     csvfile.readline()   # skip the first line of headers
#     reader = csv.reader(csvfile)
#     for row in reader:
#         dowData.append(float(row[5]))
#         dowLabels.append(pd.to_datetime(row[0]))
# if (len(dowData) >= 30):
#     break

# afont = {'family':'monospace'}


# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) # Use "2020-01-01" instead of "2020"
# ax.plot(dowLabels, dowData)  # Plot data on the axes.
# fig.autofmt_xdate()
# ax.set_title("Dow Jones Induastrial Average adjusted for infaltion\n(1990-09-01 to 2020-08-30)")
# ax.set_xlabel("Date")
# ax.set_ylabel("Price (USD)")
# ax.grid()

# plt.show()
