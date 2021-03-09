# Write your code here
import re

def remove_repeated_words(str):
     return re.sub(r'([a-zA-Z]+)( \1)+', r'\1', str)