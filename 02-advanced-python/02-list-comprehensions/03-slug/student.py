# Write your code here
def slug(str):
    parts = str.split()
    voornaam = parts[0]
    achternaam = parts[1:]
    return '-'.join(s.lower() for s in achternaam + [voornaam])