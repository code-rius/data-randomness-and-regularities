from PIL import Image
import matplotlib.pyplot as plot
import numpy as np
from scipy import signal

import timeit

class RecurrencePlot:

    def __init__(self, D: int, d: int, data: list, compareMode:int = 0, target: float = 15,downSample: bool = False, downSampleTarget: int = 720):
        self.downSampleTarget = downSampleTarget
        self.compareMode = compareMode
        self.downSample = downSample
        self.target = target
        self.data = data
        self.D = D
        self.d = d
        self.allowed_r_deviation = 1
        self.N = len(data)
        self.M = self.N-(D-1)*d
        self.r = self.percentage = 0
        self.calibrate_r()

    def calibrate_r(self):
        if (self.compareMode == 0):
            r_last = (max(self.data) - min(self.data))*np.sqrt(self.D)
        elif (self.compareMode == 1):
            r_last = (max(self.data) - min(self.data))

        self.percentage = percentage_last = 100

        # Repeat until R is calibrated
        while (abs(self.percentage-self.target) > self.allowed_r_deviation):
            t_start = timeit.default_timer()

            self.r = (self.r+r_last)/(self.percentage+percentage_last)*self.target
            self.calculate_recurrences()

            percentage_last = self.percentage
            r_last = self.r

            t_end = timeit.default_timer()

            print("R=", self.r, "\tNow %=", self.percentage,
                  "\tTime taken: ", t_end - t_start)

    def calculate_recurrences(self):
        similarities = []
        sygnalStates = []

        # Generate data pairs, tripplets, quadruplets... D - plets
        for i in range(0, self.M):
            state = []

            for j in range(0, self.D):
                state.append(self.data[i+j*self.d])

            sygnalStates.append(state)

        # Generate data similarities array
        if (self.compareMode == 0):
            # Calculate using euclidian norm
            for i in range(0, self.M):
                for j in range(i, self.M):
                    vectorDifference = []
                    
                    for k in range(0, self.D):
                        vectorDifference.append(
                            sygnalStates[i][k] - sygnalStates[j][k])

                    vectorDistance = np.linalg.norm(vectorDifference)

                    if (vectorDistance <= self.r):
                        similarities.append([i, j])

        elif (self.compareMode == 1):
            # Calculate using the maximum value
            for i in range(0, self.M):
                for j in range(i, self.M):
                    vectorDifference = []

                    for k in range(0, self.D):
                        vectorDifference.append(sygnalStates[i][k] - sygnalStates[j][k])

                    if (abs(max(vectorDifference)) <= self.r):
                        similarities.append([i, j])

        self.similarities = similarities
        self.get_pixel_percentage()

    def draw_diagram(self):
        drawArray = self.similarities

        # Fill in the missing data triangle
        for i in range(0, len(self.similarities)):
            drawArray.append([drawArray[i][1], drawArray[i][0]])

        # Create a black image
        img = Image.new('RGB', (self.M, self.M), "white")
        pixels = img.load()

        # Fill in whites for where similarities where found
        for i in drawArray:
            pixels[i[0], self.M-i[1]-1] = (0, 0, 0)
        img.show()

    def get_pixel_percentage(self):
        self.percentage = (len(self.similarities)-self.M)/((self.M)*(self.M)-self.M)*200

    def do_downsample(self, data: list, target: int = 720) -> list:
        if(len(data) <= target):
            return data
        else:
            return list(signal.resample(data, target))
