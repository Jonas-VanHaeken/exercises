import sys
import csv
import collections


table = {}

with open("exam-schedule.csv") as file:
    data = csv.DictReader(file)

    for row in data:
        soort = row['Ex. Soortx']
        if soort == "S":
            lectors = row['Lector']
            lectors = lectors.split("/")
            for lector in lectors:
                table[lector] = table.get(lector, 0) + 1

od = collections.OrderedDict(sorted(table.items()))


with open("output.txt",'w') as output:
    for lector in od:
        output.write(lector + " " + str(od[lector]) + "\n")
            