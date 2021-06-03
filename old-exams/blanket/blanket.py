import json
import statistics
from datetime import datetime
from collections import OrderedDict


with open("input.txt",'r') as input:
    unformatted_data = input.read()

parsed_json = (json.loads(unformatted_data))

key_list = list(parsed_json.keys())
val_list = list(parsed_json.values())
avg_list = []
date_list = []

for i in val_list:
    avg_list.append(round(statistics.mean(i)))
    

for date_str in key_list:
    date_list.append(datetime.strptime(date_str, '%d/%m/%Y'))
    
zip_iterator = zip(date_list,avg_list)
mydict = dict(zip_iterator)
ordered = OrderedDict(sorted(mydict.items(), key=lambda t: t[0]))


with open("output.txt",'w') as output:
    for dates in ordered:
        output.write(str(ordered[dates])+'\n')






