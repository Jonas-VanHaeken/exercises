import re
from datetime import datetime

def isValidDate(string):
    datum = string.split('-')
    dag = int(datum[0])
    maand = int(datum[1])
    jaar = int(datum[2])

    try:
        newDate = datetime(jaar,maand,dag)
        return True
    except ValueError:
        return False


with open("input.txt",'r') as input:
    with open("output.txt",'w') as output:
        for line in input:
            if re.fullmatch(r'\d{1,2}-\d{1,2}-\d{4}',line.strip()):
                if isValidDate(line):
                    output.write(line)

