import json
import sys

with open('test.json') as f:
    data=json.load(f)

ind = sys.argv
print(data['data'][int(ind[1])])
