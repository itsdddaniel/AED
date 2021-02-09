from alumno import *
from nodee import *

node = Node(
	Alumno("Alice",20), Node(
		Alumno("Carlos",21), Node(
			Alumno("Orlando",19)
			)
		)
	)

node.recorrerNode(node)