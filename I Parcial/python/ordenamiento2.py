def Ordenamiento(self):	
	for i in range (len(A)-1,0,-1):
		for j in range (i):
			if A[j] < A[j+1]:
				T = A[j]
				A[j] = A[j+1]
				A[j+1] = T


A=[7,4,3,5,10,11]
Ordenamiento(A)
print A		

def OrdenamientoPorSeleccion(self):
	for i in range(len(A)-1,0,-1):
		Mayor=0
		for j in range(0,i+1):
			if A[j]<A[Mayor]:
				Mayor = j

		T = A[j]
		A[j] = A[Mayor]
		A[Mayor] = T

A=[7,4,3,5,10,11]
OrdenamientoPorSeleccion(A)
print A			

def OrdenamientoPorInsercion(self):
	for i in range(1,len(A)):
		Actual = A[i]
		posicion = i

		while posicion>0 and A[posicion-1]>Actual:
			A[posicion]=A[posicion-1]
			posicion=posicion-1

		A[posicion]=Actual	

A=[7,4,3,5,10,11]
OrdenamientoPorInsercion(A)
print A	