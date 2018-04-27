import numpy as np
import readData
import matplotlib.pyplot as plt
import csv



days = readData.days
flow = np.array(readData.flow)
flowList = np.array(readData.flowList)
time = np.array(readData.time)
postMile = np.array(readData.postMile)

fPM = 35.78
fTime = '12:00'
timeSlot = 24*12
points = 136

def TemporalCorrelation(fPM):
    indexT = np.where(postMile == fPM)
    tmpArray = np.array([])
    flowAtPoint = np.empty((0, timeSlot))
    for i in range (0, days):
        for j, val in np.ndenumerate(indexT):
            tmpArray= np.append(tmpArray, flow[i][val])
        flowAtPoint = np.append(flowAtPoint, [tmpArray], axis=0)
        tmpArray = np.array([])

    pCoeffT = np.empty([0, days-1])
    for i in range(0, days -1):
	    pCoeffT = np.append(pCoeffT, np.corrcoef(flowAtPoint[30], flowAtPoint[i])[0][1])
    
    return pCoeffT

def SpatialCorrelation(fDay):
    tmpArray = np.array([])
    flowAtTime = np.empty((0, timeSlot ))
    for i in range (0, points):
        if (postMile[i] == 57.75 or postMile[i] == 57.6 or postMile[i] == 57.45 or postMile[i] == 57.3 or postMile[i] == 56.59):
	        continue	
        indexD = np.where(postMile == postMile[i])
        for j, val in np.ndenumerate(indexD):
            tmpArray= np.append(tmpArray, flow[fDay][val])
        flowAtTime = np.append(flowAtTime, [tmpArray], axis=0)
        tmpArray = np.array([])


    pCoeffD = np.empty([0, points-1])
    #print (np.size(flowAtTime, 0))
    for i in range(0, np.size(flowAtTime, 0) -1):
	    pCoeffD = np.append(pCoeffD, np.corrcoef(flowAtTime[60], flowAtTime[i])[0][1])
    
    return pCoeffD

def Analysis(fTime, fPM):
    indexTmp = np.where(postMile == fPM)
    for i in range(0, np.size(indexTmp)):
        if(time[indexTmp[0][i]] == fTime):
	    indexT =  indexTmp[0][i]
    tmpArray = np.array([])
    for i in range (0, days):
        tmpArray = np.append(tmpArray, flow[i][indexT])
    return tmpArray

def TimeCorrelation(fPM):
    flowAtPoint = np.empty((0, days))
    for i, val in enumerate (np.unique(time)):
        tmpArray = Analysis(val, fPM)
        flowAtPoint = np.append(flowAtPoint, [tmpArray], axis=0)

    pCoeffT = np.empty([0, np.size(np.unique(time))])
    for i in range(0, np.size(np.unique(time))):
	    pCoeffT = np.append(pCoeffT, np.corrcoef(flowAtPoint[140], flowAtPoint[i])[0][1])
    
    return pCoeffT

listPostMile = [51.72, 42.18, 31.83, 6.62]
fixedDay = [0, 1, 2, 5, 6]

outList = []
for i in range(0, 4):
    pCoeffT = TemporalCorrelation(listPostMile[i])
    outList.append(pCoeffT)

for i in range(0, 4):
    pCoeffD = SpatialCorrelation(fixedDay[i])
    outList.append(pCoeffD)

for i in range(0, 4):
    pCoeffT =TimeCorrelation(listPostMile[i])
    outList.append(pCoeffT)

print (outList)

'''
for i in range(0, 4):
    
    pCoeffT = TemporalCorrelation(listPostMile[i])
    plt.figure(1)
    plt.plot(pCoeffT)
    plt.xlabel("Days")
    plt.ylabel("Correlation between traffic between different \n days at a single point in different times")
    plt.show()
    

    pCoeffD = SpatialCorrelation(fixedDay[i])
    plt.figure(2)
    plt.plot(pCoeffD)
    plt.xlabel("Points")
    plt.ylabel("Correlation between traffic between different \n points in  a singleday at different times")
    plt.show()
    
    pCoeffT =TimeCorrelation(listPostMile[i])
    plt.figure(1)
    plt.plot(pCoeffT)
    plt.xlabel("Days")
    plt.ylabel("Correlation between traffic between different \n days at a single point in different times")
    plt.show()
'''

with open("correlation_analysis.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(outList)

#for i in range(0, len(outList)):
    #plt.plot(outList[i])
    #plt.show()

    



