#_*_coding: utf8 _*_
print "reverse"
lista = [5,4,-7,9,0,1,3]  #le da vuelta a la lista.
lista.reverse()
print lista

print "extend"
lista = [5,4,-7,9,0,1,3]
lista.extend([100,111])  #extend añade varios valores al vez al final de lista.
print lista

print "index"
lista = [5,4,-7,9,0,1,3]
print(lista.index(5))    #imprime la indexacion en donde se encuentra lo puesto en el argumento.

print "count"
lista = [1,1,1,1,4]
lista.count(1)           #cuenta cuentas veces esta repetido lo puesto en el argumento.
print lista

print "pop"
lista = [5,4,-7,9,0,1,3]  #elimina el ultimo valor en la lista.
lista.pop()
print lista               

print "remove"
lista = [5,4,-7,9,0,1,3]  #elimina el valor ingresado en el argumento.
lista.remove(5)
print lista

print "append"
lista = [5,4,-7,9,0,1,3]  #append agrega valores al final de la lista.
lista.append(10)
print lista

print "insert"
lista = [5,4,-7,9,0,1,3] #insert agrega valores donde sea y toma dos argumentos el primero siendo la indexacion
                         #se quiere poner el valor y el segundo el valor como tal.
lista.insert(0,3)
print lista

print "sort"
lista = [5,4,-7,9,0,1,3]
lista.sort(reverse=True) #sort es para arreglar de menor a mayor pero usando reverse=true es de mayor a menor.
print lista

print "lista a tupla"
lista = [4,"Hola",6.78,[1,2,3],4] #convertir una lista a tupla
tupla = tuple(lista)
print tupla

print "tupla a lista"
tupla = (4,3,2) #convertir una tupla a una lista. Las tuplas no se pueden modificar.
lista = list(tupla)
print lista

