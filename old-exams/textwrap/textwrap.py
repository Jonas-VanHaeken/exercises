# Write your solution in this file
import textwrap

with open("input.txt",'r') as input:
    with open("output.txt",'w') as output:
        output.write("\n".join(textwrap.wrap(input.read(),40)))