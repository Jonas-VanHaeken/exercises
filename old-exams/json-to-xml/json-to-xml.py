import json

with open("input.json",'r') as input:
    with open("output.txt",'w') as output:
        data = json.loads(input.read())
        output.write("<students>\n")

        for line in data:
            student_id = line['id']
            grades = line['grades']
            output.write('<student id="' + student_id + '"><grades>')
            for grade in grades:
                output.write("<grade>"+ str(grade) + "</grade>")
            output.write("</grades></student>\n")
        output.write("</students>")