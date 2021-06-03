import re

with open("input.txt",'r') as input:
    with open("output.txt",'w') as output:
        data = input.readlines()

        for line in data:
            line = line.strip().lower()
            if re.fullmatch(r'^(s|r).{7}$',line):
                output.write(str(line)+"@student.ucll.be" + "\n")
            if re.fullmatch(r'^u.{7}$',line):
                output.write(str(line)+"@ucll.be" + "\n")