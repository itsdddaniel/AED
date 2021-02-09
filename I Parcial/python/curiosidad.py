import json


d={
	raw_input():raw_input()
}



for key in d:
	print "%s:%s" % (key,d[key])

file = open("ram.txt","w")
file.write(json.dumps(d))
file.close()

open("ram.txt","r")
											