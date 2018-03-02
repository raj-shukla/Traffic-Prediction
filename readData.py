import numpy as np
import csv


days = 2
flowList = [[], []]
flow = [[], []]
postMile = []
lanes = []


print(flow)

for i in range (0, days):
    flowFile = "Data/Oct2017_Flow/pems_output_"  + str(i) + ".csv"
    csvFile = open (flowFile, "r")
    #print (flow)
    csvReader = csv.reader(csvFile)
    next(csvReader)
    for row in csvReader:
        flowList[i].append(row) 
        flow[i].append(int(row[4]))
	


for row in flowList[0]:
    postMile.append(float(row[1]))
    lanes.append(int(row[5]))
print(len(flowList[0]))
print(len(flowList[1]))
print(len(flow[0]))
print(len(flow[1]))
print(len(lanes))
print(len(postMile))


        
np.asarray(flow)
np.asarray(lanes)
np.asarray(postMile)


print (flow)
