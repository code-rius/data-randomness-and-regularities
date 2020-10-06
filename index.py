import matplotlib.pyplot as plot
import numpy as np

# Constant
r = 0.1
counter = 0
counterSimilar = 0

# Data arrays
yi = []
similarities = []
similaritiesX = []
similaritiesY = []

time = np.arange(0, 20 , 0.4)
amplitude = np.round(np.sin(time), 5)

# Arrange data values into pairs
for i in range(0, len(amplitude)-1):
    yi.append([amplitude[i], amplitude[i+1]])

# Iterate to find similar pairs
for i in range(0, len(yi)-1):
    for j in range(0, len(yi)-1):
        if (i < j):
            idata1 = yi[i][0]
            jdata1 = yi[j][0]
            idata2 = yi[i][1]
            jdata2 = yi[j][1]

            isFirstSimilar = abs(idata1 - jdata1) <= r
            isSecondSimilar = abs(idata2 - jdata2) <= r

            if(isFirstSimilar and isSecondSimilar):
                similarities.append([i, j])
                similaritiesX.append(i)
                similaritiesY.append(j)

                counterSimilar+=1
            counter+=1
        j+=1
    i+=1

print("Number of data entries:\t" + str(len(amplitude)))
print("Number of data pairs:\t" + str(len(yi)))
print("Number of iterations:\t" + str(counter))
print("Number of matches:\t" + str(counterSimilar))
print("\nSimilar pairs:\t" + str(similarities))
print("\nSimilarty pisitions X:\t" + str(similaritiesX))
print("\nSimilarty pisitions Y:\t" + str(similaritiesY))
