# Write your code here
import re

def scrape_email_addresses(str):
    return re.findall(r'[a-zA-Z0-9\.]+@[a-zA-Z0-9\.]+',str)