import time
import numpy as np
import matplotlib.pyplot as plt
import scipy
import predictionData
import functions

test_x = predictionData.inputData[:, 3999:4600]
test_y = predictionData.outputData[:, 4000:4600]

print(np.shape(test_y))

initial_val = test_x[:, 1]

def MovingAverage(inputArray):
    weights = np.array([1.0/21, 2.0/21, 3.0/21, 4.0/21, 5.0/21, 6.0/21])
    inputArray = np.multiply(inputArray, weights)
    return np.average(inputArray)

predict_y = [] 
inputArray = initial_val
print(inputArray)
for i in range(0, np.shape(test_y)[1]):
    print(inputArray)
    y = MovingAverage(inputArray)
    inputArray = np.append(inputArray[1:], y)
    predict_y.append(y)

cost = functions.compute_cost(predict_y, test_y)
averageError = functions.averageError(predict_y, test_y)

print(cost)
print(averageError)
