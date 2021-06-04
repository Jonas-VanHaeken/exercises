# Write your solution in this file

klassement = {}


with open("input.txt",'r') as input:
    data = input.readlines()
    
    score = 100
    for line in data:
        speler = line.strip()
        klassement[speler] = klassement.get(speler,0) + score
        score -= 1
        if score == 0:
            score = 100

klassement = (sorted(klassement.items(), key=lambda x:x[1], reverse=True))

with open("output.txt",'w') as output:
    for speler in (klassement[:10]):
        output.write(str(speler[0]) + "\n")
        