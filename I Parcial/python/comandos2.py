import os
comando = ''
class RootComandos():

	def comandols(self):
		comando = ''
		while comando != 'exit()':
			print '>'
			comando = raw_input() 
			if comando == 'ls':
				os.system('ls')	
			else:
				print "IS310 - Comando Invalido"

	def comandopwd(self):
		comando = ''
		while comando != 'exit()':
			print '>'
			comando = raw_input() 
			if comando == 'pwd':
				print 'Directorio actual: %s' % os.getcwd()	
			else:
				print "IS310 - Comando Invalido"	

	def comandocd(self):
		comando = ''
		while comando != 'exit()':
			print '>'
			comando = raw_input() 
			if comando == 'cd':
				cd = raw_input()
				os.chdir(cd)
				print 'El nuevo directorio es: %s' % os.getcwd()
			else:
				print "IS310 - Comando Invalido"

	def comandoexit(self):
		if comandoexit == 'exit()':
			pass

c = RootComandos()
if comando == 'ls':
	c.comandols()	
elif comando == 'pwd':
	c.comandopwd()
elif comando == 'cd':
	c.comandocd()
elif comando == 'exit()':			
	c.comandoexit()