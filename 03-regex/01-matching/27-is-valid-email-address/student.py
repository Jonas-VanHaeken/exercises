# Write your code here
import re

def is_valid_email_address(str):
    return re.fullmatch(r'[a-z0-9\.]+@(ucll\.be|student\.ucll\.be)',str)