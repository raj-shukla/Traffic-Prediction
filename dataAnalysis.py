import numpy as np
import readData
import matplotlib.pyplot as plt


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


#print (flow[16])
#print(np.size(flow[16]))

'''
for i in range(0, len(flow[15])):
	if (flowList[15][i][0] != flowList[16][i][0]):
		print (i)
		print(flowList[15][i][0])
		print(flowList[16][i][0])
'''

indexT = np.where(postMile == fPM)
tmpArray = np.array([])
for i in range (0, days):
    for j, val in np.ndenumerate(indexT):
	print(i)
	print(np.size(flow[i]))
        tmpArray= np.append(tmpArray, flow[i][val])
    flowAtPoint = np.append(flowAtPoint, [tmpArray], axis=0)
    tmpArray = np.array([])


tmpArray = np.array([])
for i in range (0, points):
    if (postMile[i] == 57.75 or postMile[i] == 57.6 or postMile[i] == 57.45 or postMile[i] == 57.3 or postMile[i] == 56.59):
	continue	
    indexD = np.where(postMile == postMile[i])
    for j, val in np.ndenumerate(indexD):
        tmpArray= np.append(tmpArray, flow[15][val])
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


pCoeffT = np.empty([0, days-1])
print(pCoeffT)
print(np.shape(pCoeffT))
for i in range(0, days -1):
	pCoeffT = np.append(pCoeffT, np.corrcoef(flowAtPoint[30], flowAtPoint[i])[0][1])

pCoeffD = np.empty([0, points-1])
print (np.size(flowAtTime, 0))
for i in range(0, np.size(flowAtTime, 0) -1):
	pCoeffD = np.append(pCoeffD, np.corrcoef(flowAtTime[100], flowAtTime[i])[0][1])


print(pCoeffT)
print(pCoeffD)

plt.figure(1)
plt.plot(pCoeffT)
plt.xlabel("Days")
plt.ylabel("Correlation between traffic between different \n days at a single point in different times")
plt.show()

plt.figure(2)
plt.plot(pCoeffD)
plt.xlabel("Points")
plt.ylabel("Correlation between traffic between different \n points in  a singleday at different times")
plt.show()
