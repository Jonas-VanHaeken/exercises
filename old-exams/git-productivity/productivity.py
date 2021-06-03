import re
import collections
from typing import OrderedDict

names = {}


with open("input.txt",'r') as input:
        data = input.readlines()

        for line in data:
            line = line.strip()
            if re.fullmatch(r'^Author: .*$',line):
                parts = line.split(' ')
                name = ' '.join(parts[1:-1])
                names[name] = names.get(name, 0) + 1

with open("output.txt",'w') as output:
    sorted_dict = (sorted(names, key=names.get,reverse=True))
    for name in sorted_dict:
        output.write(name + ": " + str(names[name]) + "\n")