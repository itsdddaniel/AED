class Node:
	def __init__(self,value):
		self.value = value
		self.rightchild = None
		self.leftchild = None

class BST:
	def __init__(self):
		self.root = None #la raiz del nodo la creamos sin nada.

	def setRoot(self,value):    
		self.root = Node(value) #la raiz lo igualamos al valor que se ingresara en el nodo.

	def add(self,value):
		if self.root is None:    #como el nodo esta vacio entonces se le asigna el valor que fue ingresado en "value"
			self.setRoot(value)
		else:
			self.addNode(self.root,value) #si no esta vacio entonces pone otro nodo

	def addNode(self,currentNode,value):   
		if currentNode.value > value:         #si el valor ingresado es menor al valor del nodo actual
			if currentNode.leftchild:   #si el nodo a la derecha existe
				self.addNode(currentNode.leftchild,value) #usa recursividad para verificar si aun siguen existiendo
			else:                                         #nodos siguientes
				currentNode.leftchild = Node(value)   #si ya no hay nodos, entonces se crea uno con el valor

				#lo mismo aqui pero por la izquierda
		elif value > currentNode.value: 
			if currentNode.rightchild:
				self.addNode(currentNode.rightchild,value)
			else: 
				currentNode.rightchild = Node(value)		
	def search(self,value):
		return self.searchinner(self.root,value)

	def searchinner(self,currentNode,value):
		if currentNode is None:
			return False
		elif currentNode.value == value:
			return True
		elif currentNode.value > value:
			return self.searchinner(currentNode.leftchild,value)
		elif value < currentNode.value:
			return self.searchinner(currentNode.rightchild,value)					
				