# Write your code here
import re


def contains_a(string):
    return re.fullmatch('.*a.*', string)
