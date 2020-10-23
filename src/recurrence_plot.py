from PIL import Image
import matplotlib.pyplot as plot
import numpy as np
from scipy import signal

class RecurrencePlot:

    def __init__(self, D: int, d: int, data: list, target: float = 15,downSample: bool = False, downSampleTarget: int = 720):
        self.D = D
        self.d = d
        self.data = data
        self.target = target
        self.downSample = downSample
        self.downSampleTarget = downSampleTarget
        self.N = len(data)
        self.M = self.N-(D-1)*d
        self.r = (max(data) - min(data))*target/100
        self.r = max(data)
        # self.find_r()
        self.calculate_recurrences()


    def find_r(self):
        # r_max = (max(self.data) - min(self.data))*self.target/100


        return 0


    def calculate_recurrences(self):
        similarities = []
        sygnalStates = []

        # Generate data pairs, tripplets, quadruplets ... depending on D
        for i in range(0, self.M):
            state = []

            for j in range(0, self.D):
                state.append(self.data[i+(j*self.d)])

            sygnalStates.append(state)

        # Generate data similarities array
        for i in range(0, self.M):
            for j in range(i, self.M):
                #TODO: Parametrized and moved to a function
                vectorDifference = np.subtract(
                    sygnalStates[i], sygnalStates[j])

                vectorDistance = np.linalg.norm(vectorDifference)

                if (vectorDistance <= self.r):
                    similarities.append([i, j])

        self.similarities = similarities


    def draw_diagram(self):
        drawArray = self.similarities

        # Fill in the missing data triangle
        print(len(self.similarities))
        print(len(self.similarities)*2)

        for i in range(0, len(self.similarities)):
            drawArray.append([drawArray[i][1], drawArray[i][0]])

        print(len(drawArray))
        # Create a black image
        img = Image.new('RGB', (self.M, self.M), "white")
        pixels = img.load()

        # Fill in whites for where similarities where found
        for i in drawArray:
            pixels[i[0], self.M-i[1]-1] = (0, 0, 0)
        img.show()


    def get_pixel_percentage(self):
        # Calculate percentage of similarities
        percentage = (len(self.similarities)-self.M)/((self.M)*(self.M)-self.M)*200
        print("N:\t", self.N, "\nM:\t", self.M, "\nD:\t", self.D, "\nd:\t", self.d, "\nr:\t", self.M,)
        print("Percentage:\t", percentage)
        return percentage


    def do_downsample(data: list, target: int = 720) -> list:
        if(len(data) <= target):
            return data
        else:
            return list(signal.resample(data, target))
