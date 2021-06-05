# Write your solution in this file
import csv
import collections

sample = {}



with open("input.csv",'r') as input:
    data = input.readlines()
    
    header = data[0].strip().split(',')
    header.pop(0)
    
    for row in data[1:]:
        parts = row.strip().split(',',1)
        name = parts[0]
        possible_dates = parts[1].split(',')
        
        lengte = len(possible_dates)
        
        for i in range(0,lengte):
            if possible_dates[i] == 'yes':
                sample[header[i]] = sample.get(header[i],0) + 1
            else:
                sample[header[i]] = sample.get(header[i],0)

sorted_sample = sorted(sample.items(), key=lambda kv: kv[1],reverse=True)
sorted_dict = collections.OrderedDict(sorted_sample)


with open("output.txt",'w') as output:
    for entry in sorted_dict:
        output.write(str(entry) + " " + str(sorted_dict[entry]) + "\n")
        
        
            