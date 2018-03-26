import numpy as np
import readData
import predictionData

days = readData.days
flow = np.array(readData.flow)
flowList = np.array(readData.flowList)
postMile = np.array(readData.postMile)



data = predictionData.inputArray
Y = predictionData.outputArray  
n = np.array([5, 10, 1])
L = np.size(n) - 1


W = []
b = []
A = []
Z = []
dZ = []
dW = []
db = []
dA = []

for i  in range (0, L+1):
    A.append([])
    Z.append([])
    dZ.append([])
    dW.append([])
    db.append([])
    dA.append([])


#data = np.array([[.35, .69, .23, .38, .52], [.3, .7, .2, .4, .5], [.33, .72, .23, .41, .48], [.31, .71, .19, .39, .45], [.29, .68, .18, .42, .55]])



A[0] = data
Z[0] = data
#Y = [[.3, .7, .2, .4, .5]]



def InitializeWeight(layers, structure):
    initialWeight = [] 
    initialBias = []
    for l in range(0, layers):
        tmpMatrix1 = (np.random.randn(n[l+1], n[l]))*0.01
	tmpMatrix2 = (np.zeros((n[l+1], 1)))
        initialWeight.append(tmpMatrix1)
	initialBias.append(tmpMatrix2) 
    initialWeight.insert(0, None)
    initialBias.insert(0, None)
    return [initialWeight, initialBias]
    
def FindError(Output):
    #print(Y)
    #print(1 - np.asarray(Y))
    #error = -np.asarray(Y)*np.log (A[L]) - (1-np.asarray(Y))*np.log(1 - A[L])
    error = np.sqrt((Y - A[L])*(Y-A[L]))
	
    #print(np.size(Y))
    #print(np.size(A[L]))
    #print(Y)
    #print(A[L])
    meanError = np.mean(error)
    return meanError
    

def ForwardPropagation(W, A, data):
    for l in range(1, L + 1):
        Z[l] = np.dot(W[l], A[l-1]) + b[l]
        #print(-Z[l])
        A[l] = 1/(1+ np.exp(-Z[l]))
        print("################################################")
	#A[l] = Z[l]
	#A[l][A[l] < 0] = 0
	#A[l] = np.maximum(0.01*Z[l], Z[l])
	print(Z[l])
        print(A[l])

def BackPropagation(W, A, data, alpha):
    m = np.shape(data)[1]
    for l in range(L, 0, -1):
        if (l == L):
            dZ[l] = A[l] - Y
	    #print(dZ[l])
        else :
            dTerm = 1/(1+ np.exp(-Z[l]))
            dZ[l] = dA[l]* (dTerm*(1-dTerm))
	    #dZ[l] = dA[l]
	    #dZ[l][dZ[l] < 0] = 0.01
	    #dZ[l][dZ[l] > 0] = 1
        dW[l] = (np.dot(dZ[l], A[l-1].T))/m
        #print(dZ[l])
	db[l] = (np.sum(dZ[l], axis=1, keepdims= True))/m
        dA[l-1] = np.dot(W[l].T, dZ[l])
        W[l] = W[l] - alpha*dW[l]
	b[l] = b[l] - alpha*db[l]
	print("#############")
	print(l)
        print(dZ[l])
        print(A[l-1])
        print(W[l].T)
        print(dA[l])
	print(alpha)
	print(alpha*dW[l])
    #print(W)

networkParam = InitializeWeight(L, n)
W = networkParam[0]
b = networkParam[1]
print (W)
#print (b)
alpha = 1.2
for i in range(0, 1):
    for i in range(0, 10000):
        #print(data[:, i:i+5])
        #ForwardPropagation(W, A, data[:, i:i+5])
        ForwardPropagation(W, A, data)
        cost = FindError(A)
        #print("######################")
        #print (cost)
        BackPropagation(W, A, data, alpha)
        alpha = alpha*1
print (W)


prediction = ForwardPropagation(W, A, data)
predictionError = FindError(A)

#print (A[L])
#print(predictionError)
