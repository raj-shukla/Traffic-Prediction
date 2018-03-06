import numpy as np
import readData

days = readData.days
flow = np.array(readData.flow)
flowList = np.array(readData.flowList)
time = np.array(readData.time)
postMile = np.array(readData.postMile)

fPM = 61.06
fTime = '12:00'
timeSlot = 24*12
points = 136
flowAtPoint = np.empty((0, timeSlot))
flowAtTime = np.empty((0, 136 ))
#print (flowAtPoint)

indexT = np.where(postMile == fPM)
indexD = np.where(time == fTime)
#print (postMile)
print (time)
print(indexD)
print("#############")
print (indexT)
tmpArray = np.array([])
for i in range (0, days):
    for j, val in np.ndenumerate(indexT):
	#print(flow[i])
	#print(val)
        tmpArray= np.append(tmpArray, flow[i][val])
    flowAtPoint = np.append(flowAtPoint, [tmpArray], axis=0)
    tmpArray = np.array([])

tmpArray = np.array([])
for i in range (0, days):
    for j, val in np.ndenumerate(indexD):
	#print(flow[i])
	#print(val)
        tmpArray= np.append(tmpArray, flow[i][val])
    flowAtTime = np.append(flowAtTime, [tmpArray], axis=0)
    tmpArray = np.array([])

'''
for i in range (0, days):
    for j, val in enumerate(flowList[i]):
        if (float(flowList[i][j][1]) == fPM):
            tmpArray= np.append(tmpArray, int(flowList[i][j][5]))
    flowAtPoint = np.append(flowAtPoint, [tmpArray], axis=0)
    tmpArray = np.empty((0, 1))
'''
print (np.shape(flowAtPoint))

pCoeffT = np.empty([0, days-1])
print(pCoeffT)
print(np.shape(pCoeffT))
#print(np.corrcoef(flowAtPoint[0], flowAtPoint[1]))
for i in range(0, days -1):
	#print(flowAtPoint[30])
	#print(flowAtPoint[i])
	#print(np.shape(np.corrcoef(flowAtPoint[30], flowAtPoint[i])))
	pCoeffT = np.append(pCoeffT, np.corrcoef(flowAtPoint[30], flowAtPoint[i])[0][1])

pCoeffD = np.empty([0, days-1])
for i in range(0, days -1):
	#print(flowAtPoint[30])
	#print(flowAtPoint[i])
	#print(np.shape(np.corrcoef(flowAtPoint[30], flowAtPoint[i])))
	pCoeffD = np.append(pCoeffD, np.corrcoef(flowAtTime[30], flowAtTime[i])[0][1])


print(pCoeffT)
print(pCoeffD)
