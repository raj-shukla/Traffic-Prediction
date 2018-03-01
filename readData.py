#import numpy as np
import csv


days = 2
flowList = [[], []]
flow = [[], []]
postMile = []
lanes = []


print(flow)

for i in range (0, days):
    flowFile = "Data/testData/pems_output_"  + str(i) + ".csv"
    csvFile = open (flowFile, "r")
    #print (flow)
    csvReader = csv.reader(csvFile)
    next(csvReader)
    print (csvReader)
    for row in csvReader:
	print (i)
	print(flowList[i])
        flowList[i].append(row) 
        flow[i].append(int(row[4]))
	print (row) 
	print (flowList) 










for row in flowList[0]:
    postMile.append(float(row[1]))
    lanes.append(int(row[5]))
print(len(flowList[0]))
print(len(flowList[1]))
print(len(flow[0]))
print(len(flow[1]))
print(len(lanes))
print(len(postMile))

print (flowList)
print (flow)
        

