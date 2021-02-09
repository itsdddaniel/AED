arreglocomando = raw_input()	
arreglocomando = []
for i in arreglocomando:
	comando = arreglocomando[i].split('ls')[0]
	directorio = arreglocomando[i].split(raw_input)[1]
	if directorio = '':
		
elif comando == 'ls -l':
		print "Los archivos en el directorio: {}\n".format(arbol.root.value.root)
		print arbol.root.leftChild.value.root 
		print arbol.root.rightChild.value.root
	elif comando == 'pwd':
		print "Estoy en {}\n".format(arbol.root.value.root)
	elif comando == 'touch':		
		file = raw_input()
		File('file')
		arbol.root.leftChild.tree.add(file)
		print 'Archivo creado existosamente'
	elif comando == 'mkdir':
		folder = raw_input()
		Folder('folder')
		arbol.add(folder)
		print 'Directorio creado existosamente'
	elif comando == 'mv':
		pass
	elif comando == 'rm':
		pass
	elif comando == 'rm -r':
		pass
	elif comando == 'cd':
		pass
	elif comando == 'exit':
		pass #este ya esta creado pero solo es para evitar problemas con el while.								
	else:
		print 'Comando Invalido'