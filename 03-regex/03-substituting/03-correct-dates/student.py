# Write your code here
import re

def correct_dates(str):
    return re.sub(r'(\d+)/(\d+)/(\d+)',r'\2/\1/\3',str)