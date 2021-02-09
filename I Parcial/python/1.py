import json
d={}

while d != 'stop':
	t = raw_input()
	dynamic = t 
	dynamic = 'hola'
	d[dynamic] = '???'
	d = t 

file = open('rom.txt','w')
file.write(json.dumps(dynamic))

	


