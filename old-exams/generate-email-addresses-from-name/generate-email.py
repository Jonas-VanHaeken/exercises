
from os import waitpid


with open("input.txt",'r') as input:
    with open("output.txt",'w') as output:
        data = input.readlines()

        for line in data:
            line = line.strip().lower()
            name = line.split(' ',1)
            output.write(str(name[0])+"."+str(name[1].replace(" ",""))+"@student.ucll.be\n")
