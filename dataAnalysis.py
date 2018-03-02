import numpy as np
import readData

days = readData.days
flow = np.array(readData.flow)
flowList = np.array(readData.flowList)
postMile = np.array(readData.postMile)

fPM = 61.06
timeSlot = 24*12
flowAtPoint = np.empty((0, timeSlot))
print (flowAtPoint)

indexT = np.where(postMile == fPM)

print (postMile)
print (indexT)
tmpArray = np.array([])
for i in range (0, days):
    for j, val in enumerate(indexT):
        tmpArray= np.append(tmpArray, flow[i][val])
    flowAtPoint = np.append(flowAtPoint, [tmpArray], axis=0)
    tmpArray = np.array([])

'''
for i in range (0, days):
    for j, val in enumerate(flowList[i]):
        if (float(flowList[i][j][1]) == fPM):
            tmpArray= np.append(tmpArray, int(flowList[i][j][5]))
    flowAtPoint = np.append(flowAtPoint, [tmpArray], axis=0)
    tmpArray = np.empty((0, 1))
'''
print (flowAtPoint)
