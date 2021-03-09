# Write your code here
import re

def collect_links(str):
    return re.findall(r'<a href="(.*)">', str)