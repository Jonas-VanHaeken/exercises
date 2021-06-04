# Write your solution in this file
import csv




with open("solutions.csv",'r') as solution_file:
    data = solution_file.read()
    solution = data.strip().split(',')
    aantalVragen = len(solution)

with open("answers.csv",'r') as answers_file:
    with open("output.txt",'w') as output:
        data = answers_file.readlines()

        for line in data:
            punten = 0
            answer_student = line.strip().split(',')
            student = answer_student.pop(0)

            for i in range(0,aantalVragen):
                if answer_student[i]==solution[i]:
                    punten += 1

            output.write(student + " " + str(punten) + "\n")
