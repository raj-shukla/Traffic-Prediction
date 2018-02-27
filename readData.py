import numpy as np
import csv


days = 2
flow = [[]]*days
flowData = [[]]*days
for i in range (0, days):
    fileFlow = "Data/Oct2017_Flow/pems_output_"  + str(i) + ".csv"
    with open (fileFlow) as csvfile :
        flowData.append(csv.reader(csvfile))
        print (flowData)
        for row in csvfile:
            flow[i].append(row)

print (flow[0])  
print (flow[1]) 
flow[0] = list(map(list, zip(*flow[0]))) 

for i in range (0, days):
    for row in flow[i] :
        flowData[i].append(int(row[4]))
        
