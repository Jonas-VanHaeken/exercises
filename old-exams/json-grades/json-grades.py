import json
import statistics
import collections

table = {}

with open("input.json",'r') as input:
    data = json.loads(input.read())
    for line in data:
        student_id = line['id']
        grades = line['grades']
        avg = round(statistics.mean(grades))
        table[student_id] = avg

od = collections.OrderedDict(sorted(table.items()))


with open ("output.txt", 'w') as output:
    for student in od:
        output.write(student + " " + str(od[student]) + "\n")
