# Write your code here
import re

def remove_trailing_whitespace(str):
    return re.sub('\s*$','',str, flags=re.MULTILINE)