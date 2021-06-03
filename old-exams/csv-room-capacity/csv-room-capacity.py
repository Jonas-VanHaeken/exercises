import sys
import csv
import collections

table = {}

with open("exam-schedule.csv",'r') as file:
    data = csv.DictReader(file)

    for row in data:
        lokaal = row['Lokaal']
        dagdeel = row['Dagdeel']
        datum = row['Datum']

        all = (lokaal,datum,dagdeel)

        table[all] = table.get(all, 0) + 1

output_dict = {}

for input in table:
    lokaal = input[0]
    aantal_lln = table[input]

    if output_dict.get(lokaal,0) < aantal_lln:
        output_dict[lokaal] = aantal_lln

od = collections.OrderedDict(sorted(output_dict.items()))

with open("output.txt",'w') as output:
    for lokalen in od:
        output.write(str(lokalen) + " " + str(od[lokalen]) + '\n')
