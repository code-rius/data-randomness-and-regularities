from PIL import Image
import matplotlib.pyplot as plot
import numpy as np

def generate_recurrence_diagram(D: int, d: int, r: float, data: list) -> list:
    N = len(data)
    M = N-(D-1)*d
    sygnalStates = []
    similarities = []

    # Generate data pairs, tripplets, quadruplets ... depending on D
    for i in range(0, M):
        state = []
        for j in range(0, D):
            state.append(data[i+(j*d)])
        sygnalStates.append(state)

    # Generate data similarities array
    for i in range(0, M-1):
        for j in range(0, M-1):
            vectorDifference = np.subtract(sygnalStates[i], sygnalStates[j])
            vectorDistance = np.linalg.norm(vectorDifference)
            if (vectorDistance <= r):
                similarities.append([i, j])

    print("N:\t", N, "\nM:\t", M, "\nD:\t", D, "\nd:\t", d, "\nr:\t", M,)
    print("Colored %:\t", len(similarities)/(M*M)*100)

    img = Image.new('RGB', (M, M), "white")  # Create a new black image
    pixels = img.load()  # Create the pixel map

    for i in similarities:
        pixels[i[0], i[1]] = (0, 0, 0)

    img.show()