import re

names = []


with open("input.txt",'r') as input:
        data = input.readlines()

        for line in data:
            line = line.strip()
            if re.fullmatch(r'^Author: .*$',line):
                parts = line.split(' ')
                name = ' '.join(parts[1:-1])
                names.append(name)

with open("output.txt",'w') as output:
    names = list(dict.fromkeys(names))
    names.sort()
    for name in names:
        output.write(str(name) + "\n")