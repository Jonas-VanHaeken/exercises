
with open("input.txt",'r') as input:
    with open("output.txt",'w') as output:
        data = input.readlines()

        for line in data:
            binairy = bin(int(line.strip()))
            output.write(str(binairy[2:]) + "\n")