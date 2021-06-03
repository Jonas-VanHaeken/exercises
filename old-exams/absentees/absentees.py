with open("attending.txt",'r') as f:
    attending = set( line.strip().lower() for line in f )

with open("all.txt", 'r') as all:
    with open ("absentees.txt", 'w') as out:
        for line in all:
            line = line.strip().lower()
            if line not in attending:
                out.write(f'{line}\n')
