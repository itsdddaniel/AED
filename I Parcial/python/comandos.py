import os
class RootComandos():

	def comandos(self):
		comando = ''
		self.comando = comando
		while comando != 'exit()':
			print '>'
			comando = raw_input() 
			if comando == 'ls':
				os.system('ls')	

			elif comando == 'pwd':
				print 'Directorio actual: %s' % os.getcwd()	

			elif comando == 'cd':
				cd = raw_input()
				os.chdir(cd)
				print 'El nuevo directorio es: %s' % os.getcwd(cd) 

				

			elif comando == 'exit()':
				pass	

			else:
				print "IS310 - Comando Invalido"

c = RootComandos()
c.comandos()

