import numpy as np
import readData
#np.set_printoptions(threshold=np.nan)


days = readData.days
flow = np.array(readData.flow)
flowList = np.array(readData.flowList)
time = np.array(readData.time)
postMile = np.array(readData.postMile)

fPM = 35.78
fTime = '12:00'
timeSlot = 24*12
points = 136
flowAtPoint = np.empty((0, timeSlot))
flowAtTime = np.empty((0, timeSlot ))
#print(np.max(flow))
#print(np.min(flow))
flow = (flow - np.min(flow))/(np.max(flow) - np.min(flow))
#print(flow - np.min(flow))


indexT = np.where(postMile == fPM)
tmpArray = np.array([])
for i in range (0, days):
    for j, val in np.ndenumerate(indexT):
        tmpArray= np.append(tmpArray, flow[i][val])
    flowAtPoint = np.append(flowAtPoint, [tmpArray], axis=0)
    tmpArray = np.array([])


#print (np.shape(flowAtPoint))

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
        #print(j)
        #print(j+nTimeSlot)
        #print(flowAtPoint[i][j:j+nTimeSlot])
        #print(flowAtPoint[i][j+nTimeSlot])

pSlotTraffic = pSlotTraffic.T
#print (pSlotTraffic)
#print (nSlotTraffic)

print (np.shape(pSlotTraffic))
print (np.shape(nSlotTraffic))

inputArray = pSlotTraffic
outputArray = np.array([nSlotTraffic])
#np.reshape(outputArray, (1, inputArray.shape[1]))
#outputArray = outputArray.tolist()

print (np.shape(inputArray))
print (np.shape(outputArray))

#print (inputArray)
print (outputArray)


