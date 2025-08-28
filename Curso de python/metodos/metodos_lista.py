lista = list(['hola','fran',34]) #crear una lista con list

print(len(lista)) #devuelve la cantidad de elementos de la lista

#agregar elementos a la lista
lista.append('putooo')
print(lista)

#agregar elementos a un indice espesifico
lista.insert(0,'presente')
print(lista)

#agregar varios elementos a la lista
lista.extend([False,2025])
print(lista)

#eliminar un elemento por su indice
lista.pop(0)#para eliminar el ultimo es -1, basicamente lo que hace es con el menos recorre la lista al reves
print(lista)

#eleminiar un elemento por su valor
lista.remove('hola')
print(lista)

#elimina todos los elementos de la lista
lista.clear()

lista = [1,5,0,2586,56]

#ordenando la lista en forma ascendete 
lista.sort()
print(lista)

#ordenando la lista en reversa en forma descendente
lista.sort(reverse=True)
print(lista)

#invirtiendo los elementos de una lsita
lista.reverse()
print(lista)

