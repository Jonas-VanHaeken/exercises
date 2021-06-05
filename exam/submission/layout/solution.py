# Write your solution in this file
import re

names = []
ips = []
all_parts = []

with open("input.txt",'r') as input:
    data = input.readlines()
    
    for line in data:
        parts = re.split(r'(\d+\.\d+\.\d+\.\d+)', line.strip())
        name = parts[0]
        ip = parts[1]
        country = parts[2]
        names.append(name)
        ips.append(ip)
        all_parts.append(parts)

longestName = len(max(names,key=len))
longestIP = len(max(ips,key=len))

with open("output.txt",'w') as output:
    for entry in all_parts:
        output.write(str(entry[0]).rjust(longestName," ") + str(entry[1]).ljust(longestIP) + str(entry[2]) +"\n")

