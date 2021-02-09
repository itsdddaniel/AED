class Persona:
	def __init__(self,nombre,edad):
		self.nombre = nombre
		self.edad = edad
	def getEdad(self):
		return self.edad
	def getNombre(self):
		return self.nombre
class Node:
	def __init__(self,persona,next=None):
		self.persona = persona
		self.next = next 
	def getPersona(self):
		return self.persona
	def getNext(self):
		return next
Renata = Persona("Renata Dubon",20)
David = Persona("David Lopez",21)
Gabriela = Persona("Gabriela Maldonado",24)
node = Node(Renata,
	Node(Gabriela,
		Node(David)
		)
	)								
print "Persona: %s y su Edad es: %s " % (node.getPersona().getNombre(),node.getPersona().getEdad())
while node == node.getNext():
	print "Persona: %s y su Edad es: %s " % (node.getPersona().getNombre(),node.getPersona().getEdad())