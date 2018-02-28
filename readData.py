import numpy as np
import csv


days = 2
flowList = [[]]*days
flow = [[]]*days
postMile = []
lanes = []

for i in range (0, days):
    flowFile = "Data/Oct2017_Flow/pems_output_"  + str(i) + ".csv"
    with open (flowFile) as csvFile :
        #print (flow)
        next(csvFile)
        csvReader = csv.reader(csvFile)
        for row in csvReader:
            flowList[i].append(row)    

print(flowList[1][5])

for i in range (0, days):
    for row in flowList[i] :
        #print(row[4])
        flow[i].append(int(row[4]))

for row in flowList[0]:
    postMile.append(float(row[1]))
    lanes.append(int(row[5]))
        
print (lanes)
