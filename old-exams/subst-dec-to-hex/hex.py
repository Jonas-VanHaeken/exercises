import re

with open("input.txt",'r') as input:
    with open("output.txt",'w') as output:
        data = input.readlines()

        for line in data:
            line = re.sub(r'\$HEX\((\d+)\)', lambda m: "0x" + hex(int(m.group(1)))[2:].upper(),line)
            output.write(line)