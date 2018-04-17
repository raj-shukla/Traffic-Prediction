import numpy as np
import readData
#np.set_printoptions(threshold=np.nan)


days = readData.days
flow = np.array(readData.flow)
flowList = np.array(readData.flowList)
time = np.array(readData.time)
postMile = np.array(readData.postMile)

flow = (flow - np.min(flow))/(np.max(flow) - np.min(flow))
flowArray = []

for i, val in enumerate(flow):
    flowArray.append(np.array(flow[i].reshape(24*12, 136)))

flowArray = np.asarray(flowArray)

#print(flowArray[0][25][78])
#print (np.shape(flowArray))
#print(type(flowArray))

inputArray = []
outputArray = []
timeSlot = 24*12
points = 136
fPM = 2.43
m = 5
q =  3
pTmp = 5
p = (pTmp - 1)/2
col = np.where(postMile == fPM)[0][0]
#print (col)
k = col
tmpMatrix = np.array([])
for i in range(0, days):
    for j in range (m, timeSlot):
        tmpMatrix = np.append(tmpMatrix, flowArray[i, j-q:j, k - p:k + p +1])
        #print(flowArray[i][j-q:j])
        #print(flowArray[i, j - m: j - q, k])
        #print (tmpMatrix)
        tmpMatrix = np.append(tmpMatrix, flowArray[i, j - m: j - q, k])
        #print(tmpMatrix)
        #print([flowArray[i, j, k]])
        inputArray.append(tmpMatrix)
        outputArray.append([flowArray[i, j, k]])
        tmpMatrix = np.array([])

#print ("##################")
inputArray = np.array(inputArray).T
outputArray = np.array(outputArray).T
#print(np.shape(inputArray))
#print(np.shape(outputArray))
#print (inputArray)
         

'''
fPM = 35.78
fTime = '12:00'
timeSlot = 24*12
points = 136
flowAtPoint = np.empty((0, timeSlot))
flowAtTime = np.empty((0, timeSlot ))
#print(np.max(flow))


indexT = np.where(postMile == fPM)
tmpArray = np.array([])
for i in range (0, days):
    for j, val in np.ndenumerate(indexT):
        tmpArray= np.append(tmpArray, flow[i][val])
    flowAtPoint = np.append(flowAtPoint, [tmpArray], axis=0)
    tmpArray = np.array([])



inputArray = []
outputArray = []
nTimeSlot = 5
pSlotTraffic = np.empty((0, nTimeSlot))
nSlotTraffic = np.array([])
for i in range(0, days):
    for j in range(0, timeSlot + 1):
        if (j + nTimeSlot + 1 >=timeSlot + 1):
            break
        pSlotTraffic = np.append(pSlotTraffic, [flowAtPoint[i][j:j+nTimeSlot]], axis=0)
        nSlotTraffic = np.append(nSlotTraffic, flowAtPoint[i][j+nTimeSlot])

pSlotTraffic = pSlotTraffic.T

print (np.shape(pSlotTraffic))
print (np.shape(nSlotTraffic))

inputArray = pSlotTraffic
outputArray = np.array([nSlotTraffic])

print (np.shape(inputArray))
print (np.shape(outputArray))

print (outputArray)
'''


