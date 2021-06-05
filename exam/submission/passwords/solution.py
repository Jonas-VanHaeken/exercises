# Write your solution in this file
import random
import string
import itertools
import re

with open("temp.txt",'w') as temp:
    chars = ['Q','W','E','R','T','Y','U','I','O','P']
    for item in itertools.product(chars, repeat=6):
        temp.write("".join(item) + "\n")

with open("temp.txt",'r') as input:
    with open("output.txt",'w') as output:
        data = input.readlines()
        for line in data:
            match = re.fullmatch(r'?(.*([AEIOU])\1.*([QWRTYP])\2.*)?(.*([QWRTYP])\3.*([AEIOU])\4.*)', line)
            if match:
                output.write(line)
