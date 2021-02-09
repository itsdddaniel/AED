class Alumno:
	def __init__(self,nombre,edad):
		self.nombre = nombre
		self.edad = edad

	def getNombre(self):
		return self.nombre

	def getEdad(self):
		return self.edad	
		current = self.getValor()

		while current is not None:
			current = self.getNext()
			last = current

			if not last:
				last = self.valor

class Node:
	def __init__(self,valor,next=None):
		self.valor = valor
		self.next = next

	def getValor(self):
		return self.valor

	def getNext(self):
		return self.next

	def getLast(self):
		last = None

	def recorrerNode(self,node):
		node = self

		while node is not None:
			self.imprimir(node)
			node = node.getNext()

	def imprimir(self,node):
		print(
			(
				"El nombre del estudiante es: " + "%s y su edad es:  %s")
			) % (
			    
			    a.getNombre(),
			    a.getEdad()
			    )


a = Alumno(Node,Alumno)

		