import fileinput
import json

data = []
for line in fileinput.input():
    line = line.replace('\n', '')
    a, b, _, _, link = line.split(';')
    data.append({'a': a, 'b': b, 'link': float(link)})

print "data =", json.dumps(data, indent=2)
