with open("input.txt",'r') as input:
    with open("output.txt",'w') as output:
        data = input.readlines()

        for line in data:
            students = line.strip().split(',')
            for student in students:
                output.write(str(student) + "\n")