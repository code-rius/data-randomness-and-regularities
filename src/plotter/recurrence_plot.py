import matplotlib.pyplot as plot
import numpy as np
import timeit
from scipy import signal
from PIL import Image, ImageOps


class RecurrencePlot:

    def __init__(self, D: int, d: int, data: list, compare_mode:int = 0, target: float = 17.5, deviation: float = 3, down_sample: bool = False, down_sample_target: int = 720):
        self.down_sample_target = down_sample_target
        self.compare_mode = compare_mode
        self.down_sample = down_sample
        self.target = target
        self.data = data
        self.D = D
        self.d = d
        self.deviation = deviation
        self.N = len(data)
        self.M = self.N-(D-1)*d
        self.r = self.percentage = 0
        self.calibrate_r()

    def calibrate_r(self):
        if (self.compare_mode == 0):
            r_last = (max(self.data) - min(self.data))*np.sqrt(self.D)
        elif (self.compare_mode == 1):
            r_last = (max(self.data) - min(self.data))

        self.percentage = percentage_last = 100

        counter = 0
        # Repeat until R is calibrated
        while (abs(self.percentage-self.target) > self.deviation):
            counter += 1
            t_start = timeit.default_timer()

            self.r = (self.r+r_last)/(self.percentage+percentage_last)*self.target
            self.calculate_recurrences()

            percentage_last = self.percentage
            r_last = self.r

            t_end = timeit.default_timer()

            print("R=", self.r, "\tNow %=", self.percentage,
                  "\tTime taken: ", t_end - t_start)

            if (counter > 3):
                print('No R exists to reach requested pixel percentage.')
                break

    def calculate_recurrences(self):
        similarities, sygnalStates = [], []

        # Generate data pairs, tripplets, quadruplets... D - plets
        for i in range(self.M):
            state = []

            for j in range(self.D):
                state.append(self.data[i+j*self.d])

            sygnalStates.append(state)

        # Generate data similarities array
        if (self.compare_mode == 0):
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

        elif (self.compare_mode == 1):
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

    def draw_diagram(self, filename = "plotpic.png"):
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

        # Save the image
        img.save(filename)
        
        return filename

    def get_pixel_percentage(self):
        # We must first remove a single row of of data from both sides (self.M)
        # to account for the middle diagonal line which is always present.
        # 
        # We then divide the number of similarity by the number of total pixels
        # the final image.
        #
        # Then, we multiply everything by 2 to account for the fact that
        # self.similarities only contains one half of the image.
        #
        # Finally we multiply everything by 100 to get the percentage value of
        # the ratio.
        self.percentage = (len(self.similarities)-self.M)/((self.M)*(self.M)-self.M)*2*100

    def do_down_sample(self, data: list, target: int = 720) -> list:
        if(len(data) <= target):
            return data
        else:
            return list(signal.resample(data, target))
