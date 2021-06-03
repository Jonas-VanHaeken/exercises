import re

with open("input.txt", 'r') as input:
    data = input.readlines()

with open("output.txt",'w') as output:
    for students in data:
        aantal_plus = (students.count("+"))
        aantal_min = students.count("-")
        score = re.findall('(\d+)',students)
        aantal_tegoed = int(score[1]) + aantal_plus
        aantal_gebruikt = int(score[0]) + aantal_min
        score_string = str(aantal_gebruikt) + "/" + str(aantal_tegoed)
        string = re.sub('(\d+)\/(\d+)', score_string , students)
        string = re.sub('\+','',string)
        string = re.sub('\-','',string)
        output.write(string)

