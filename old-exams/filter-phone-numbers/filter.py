import re

with open("input.txt",'r') as input:
    with open("output.txt",'w') as output:
        for line in input:
            if re.fullmatch(r'(\+32-|0)4[56789]\d(-(\d){2}){3}',line.strip()):
                output.write(line)

