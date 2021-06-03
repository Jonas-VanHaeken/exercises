import re
from datetime import datetime, time

def isInvalid(timeStr):
    try:
        datetime.strptime(timeStr,"%H:%M:%S")
        return False
    except ValueError:
        return True



lineNumber = 0
with open("input.txt",'r') as input:
    with open("output.txt",'w') as output:
        data = input.readlines()

        for line in data:
            lineNumber += 1
            times = re.findall(r'\d\d\:\d\d\:\d\d', line)
            for onetime in times:
                if isInvalid(onetime):
                    output.write(str(lineNumber) + " " + str(onetime) + "\n")