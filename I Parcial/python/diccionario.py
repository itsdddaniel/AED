diccionario = {"azul":"blue","rojo":"red","verde":"green"}
print diccionario["azul"]

diccionario["amarrillo"]="yellow"
print diccionario

del(diccionario["verde"])
print diccionario

diccionario = {"Daniel":[19,1.75]}
print diccionario

equipo = {10:"Paulo",11:"Douglas Costa",7:"Cristiano Ronaldo"}
print equipo.get(1,"no existe")
print equipo.keys()
print equipo.values()
print equipo.items()
print equipo.clear()