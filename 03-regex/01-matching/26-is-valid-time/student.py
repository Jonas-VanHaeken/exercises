# Write your code here
import re

def is_valid_time(str):
    return re.fullmatch(r'[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]{3})?',str)