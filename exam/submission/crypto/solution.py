# Write your solution in this file
import json

with open("input.json",'r') as input:
    with open("output.txt",'w') as output:
        data = json.loads(input.read())
        
        for line in data:
            currency = line['currency']
            history = line["history"]
            current = history[-1]
            minimum = min(history)
            maximum = max(history)
            output.write(currency + " " + str(minimum) + " " + str(maximum) + " " + str(current) +"\n")