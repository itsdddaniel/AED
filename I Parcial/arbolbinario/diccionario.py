d={}
d.update(nombre="algoritmos")
print d

dynamic = "hola"
d[dynamic] = "???"
print d

for key in d:
	print "%s:%s" % (key,d[key])

for item in d.items():
	key,value = item
	print "%s:%s" % (key,value)

for key in d.iterkeys():
	print "%s:%s" % (key,d[key])		

import json
file = open("rom.txt","w")
file.write(json.dumps(d))
file.close()

file = open("rom.txt","r")
print file.read()	