import sys
import json
import urllib.request


n = sys.argv[1]

url = f'http://xkcd.com/info.{n}.json'

with urllib.request.urlopen(url) as input:
    data = json.loads(input.read())
    print(data)