import csv

with open ('Data/Oct2017_Flow/pems_output_0.csv') as csvfile :
    data = csv.reader(csvfile)
    #for row in data:
        #print(row)
    print (data)
