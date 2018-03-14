import numpy as np
import readData

days = readData.days
flow = np.array(readData.flow)
flowList = np.array(readData.flowList)
postMile = np.array(readData.postMile)

fPM = 61.06
timeSlot = 24*12
flowAtPoint = np.empty((0, timeSlot))

L = 5
n = np.array([10, 5, 4, 5, 3, 1])
print (n)

W = []
A = [[], [], [], [], [], []]
Z = [[], [], [], [], [], []]
dZ = [[], [], [], [], [], []]
data = np.array([[3, 4], [5, 2], [4, 5], [2, 7], [3, 2], [4, 2], [3, 5], [2, 1], [3, 4], [2, 6]])
m = 2
dW = [[], [], [], [], [], []]
dA = [[], [], [], [], [], []]
A[0] = data
Z[0] = data
Y = [[0.9,  0.7]]


def InitializeWeight(layers, structure):
    initialWeight = [] 
    for l in range(0, layers):
        tmpMatrix = np.random.rand(n[l+1], n[l])
        initialWeight.append(tmpMatrix)
    initialWeight.insert(0, None)
    return initialWeight

def ForwardPropagation(W, A, data):
    for l in range(1, L + 1):
        Z[l] = np.dot(W[l], A[l-1])
        A[l] = 1/(1+ np.exp(-Z[l]))

def BackPropagation(W, A, data, alpha):
    for l in range(L, 0, -1):
        print ("#######################")
        if (l == L):
            dZ[l] = A[l] - Y
        else :
            dZ[l] = dA[l]* Z[l]
        dW[l] = (np.dot(dZ[l], A[l-1].T))/m
        dA[l-1] = np.dot(W[l].T, dZ[l])

        W[l] = W[l] - alpha*dW[l]
        

W = InitializeWeight(L, n)
print (W)
ForwardPropagation(W, A, data)
BackPropagation(W, A, data, 0.9)

print (W)


