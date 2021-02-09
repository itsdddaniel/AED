class Cola:
	def __init__(self):
		self.cola=[]

	def pop(self):
		return self.cola[0]

	def push(self, elemento):
		self.cola.append(elemento)

	def getCola(self):
		return self.cola		

C=Cola()
C.push("1")
C.push("2")
print C.pop()
print C.getCola()
		