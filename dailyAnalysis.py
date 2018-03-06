import numpy as np
import readData
import matplotlib.pyplot as plt

days = readData.days
flow = np.array(readData.flow)
flowList = np.array(readData.flowList)
time = np.array(readData.time)
postMile = np.array(readData.postMile)

fPM = 67.99
timeSlot = 24*12
points = 136
flowAtPoint = np.empty((0, days))



'''
indexTmp = np.where(postMile == fPM)


print (indexTmp)
for i in range(0, np.size(indexTmp)):
    if(time[indexTmp[0][i]] == fTime):
	indexT =  indexTmp[0][i]

print (indexT)
tmpArray = np.array([])
for i in range (0, days):
    flowAtPoint = np.append(flowAtPoint, flow[i][indexT])

print (flowAtPoint)
'''

def Analysis(fTime):
    indexTmp = np.where(postMile == fPM)
    for i in range(0, np.size(indexTmp)):
        if(time[indexTmp[0][i]] == fTime):
	    indexT =  indexTmp[0][i]
    tmpArray = np.array([])
    for i in range (0, days):
        tmpArray = np.append(tmpArray, flow[i][indexT])
    print(np.size(tmpArray))
    return tmpArray



for i, val in enumerate (np.unique(time)):
    print(val)
    tmpArray = Analysis(val)
    flowAtPoint = np.append(flowAtPoint, [tmpArray], axis=0)

print (flowAtPoint)
print(np.shape(flowAtPoint))



pCoeffT = np.empty([0, np.size(np.unique(time))])
print(pCoeffT)
print(np.shape(pCoeffT))
for i in range(0, np.size(np.unique(time))):
	pCoeffT = np.append(pCoeffT, np.corrcoef(flowAtPoint[160], flowAtPoint[i])[0][1])

print (pCoeffT)

plt.figure(1)
plt.plot(pCoeffT)
plt.xlabel("Time slot")
plt.ylabel("Correlation")
plt.show()
