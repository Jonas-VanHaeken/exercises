# Write your code here
import  re

def ababa(str):
    return re.fullmatch(r'(.+)(.+)\1\2\1',str)