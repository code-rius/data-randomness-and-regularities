import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy import signal as sg
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
        # Declaring file paths
        source_file = src_dir + '/' + file1
        dest_file = src_dir + '/' + file2_dir + file2_name

        # print('Source file path:\t', source_file,
            # '\nDestination file path:\t', dest_file)

        shutil.move(source_file, dest_file)
        # print(os.listdir(src_dir + file2_dir))
    else:
        print("create_new_file: file not found")


def generate_and_save_graph(data_labels, data_values, file_name, dirname, title="Generated data"):
    fig, ax = plt.subplots()  # Create a figure containing a single axes.

    ax.plot(data_labels, data_values)  # Plot data on the axes.
    ax.set_title(title)
    ax.set_xlabel("Data item number")
    ax.set_ylabel("Data item value")
    ax.grid()

    plt.savefig(dirname + file_name)
    # plt.show()


def generate_data_with_trend(lower_bound, upper_bound, \
            batch_number, batch_size, rate_up, exponent):

    # Declare variables
    data = []
    dataLabels = []
    counter = 0

    # Loop a total of 720 times
    for _ in range(batch_number):
        for _ in range(batch_size):
            counter += 1
            newVal = random.randrange(lower_bound, upper_bound)

            data.append(newVal)
            dataLabels.append(counter)

        rate_up = rate_up * exponent
        lower_bound = round(lower_bound + rate_up)
        upper_bound = round(upper_bound + rate_up)

    return (dataLabels, data)


def generate_trend_assets(N):
    graph_dir = 'jupyter/rp-data/trend/'
    lower_bound = 0
    upper_bound = 60
    batch_number = 33
    batch_size = 22
    rate_up = 5
    exponent = 1.01
    exponent_increment = round((exponent - 1)/N*2, 10)
    print(exponent_increment)

    for i in range(N):
        t_rate_up = round(rate_up + random.uniform(-2,2), 2)
        data = generate_data_with_trend(lower_bound, upper_bound, \
                                        batch_number, batch_size, \
                                        t_rate_up, exponent)

        graph_fileName = 'trend_graph_' + str(i) + '.png'
        generate_and_save_graph(
            data[0], data[1], graph_fileName, graph_dir)

        dow=rp(4,2,data[1] , 1 , 17.5 ,3)
        dow.draw_diagram()
        create_new_file('plotpic.png', 'rp_graph_' +
                        str(i) + '.png', graph_dir)

        exponent -= exponent_increment


############################################
# Generating trend data
############################################
# Generate trend data

############################################
# Generating periodic data
############################################
def generate_periodic_assets(N):
    graph_dir = 'ml-data/periodic/'
    freq = 2
    amp = 2
    time_start = 0
    time_stop = 1
    duty1 = 0.3
    duty2 = 0.5

    for i in range(N):
        # RP Variables
        D = random.randint(2, 5)
        d = random.randint(2, 4)

        size = 720 + (D-1)*d

        t_freq = freq + round(random.uniform(0, 1.5),4)
        t_amp = amp + round(random.uniform(0, 1.5), 4)
        t_time_start = time_start #+ round(random.uniform(-0.5, 0.5), 2)
        t_time_stop = time_stop + round(random.uniform(0, 7), 2)
        t_duty1 = duty1 + round(random.uniform(-0.15, 0.55), 3)
        t_duty2 = duty2 + round(random.uniform(-0.35, 0.35), 3)

        time = np.linspace(t_time_start, t_time_stop, size)

        signal1 = t_amp*np.sin(2*np.pi*t_freq*time)
        signal2 = t_amp*sg.square(2*np.pi*t_freq*time, duty=t_duty1)
        signal3 = t_amp*sg.sawtooth(2*np.pi*t_freq*time, width=t_duty2)

        signal1_fileName = 'periodic_graph_' + str(i*3) + '.png'
        signal2_fileName = 'periodic_graph_' + str(i*3+1) + '.png'
        signal3_fileName = 'periodic_graph_' + str(i*3+2) + '.png'

        generate_and_save_graph(range(0, size), signal1,
                                signal1_fileName, graph_dir)
        generate_and_save_graph(range(0, size), signal2,
                                signal2_fileName, graph_dir)
        generate_and_save_graph(range(0, size), signal3,
                                signal3_fileName, graph_dir)

        ### Generating RP 

        dow1 = rp(D, d, signal1, 1, 17.5, 2.5)
        dow1.draw_diagram()
        create_new_file('plotpic.png', 'rp_graph_' +
                        str(i*3) + '.png', graph_dir)

        dow2 = rp(D, d, signal2, 1, 17.5, 2.5)
        dow2.draw_diagram()
        create_new_file('plotpic.png', 'rp_graph_' +
                        str(i*3+1) + '.png', graph_dir)
        dow3 = rp(D, d, signal3, 1, 17.5, 2.5)
        dow3.draw_diagram()
        create_new_file('plotpic.png', 'rp_graph_' +
                        str(i*3+2) + '.png', graph_dir)


def generate_chaotic_assets(N):
    graph_dir = 'ml-data/chaotic/'

    for i in range(N):
        data = []
        # RP Variables
        D = random.randint(2, 5)
        d = random.randint(2, 4)

        size = 720 + (D-1)*d

        for _ in range(size):
            data.append(random.randint(0,random.randint(50,1500)))
        
        graph_fileName = 'chaos_graph_' + str(i) + '.png'

        generate_and_save_graph(range(0, size), data,
                                graph_fileName, graph_dir)

        dow1 = rp(D, d, data, 1, 17.5, 2.5)
        dow1.draw_diagram()
        create_new_file('plotpic.png', 'rp_graph_' +
                        str(i) + '.png', graph_dir)

generate_trend_assets(1000)
# generate_periodic_assets(334)
# generate_chaotic_assets(1000)
