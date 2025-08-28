# posicion de la lista: 0 1 2 3 4
lista = ['Francisco','Bossio','corro 37',True, 1.90]
print(lista[1]) #mostrar posicion 1 (bossio)
tupla = ('Francisco','Bossio','corro 37',True, 1.90)
print(tupla[1])
#la diferencia entre lista y dupla es que la dupla no se puede modificar la lista si

#creando un conjunto (set), no tiene un orden fijo, son datos que se pueden intercambiar y 
#no se pueden modificar los datos como la tupla
conjunto = {'Francisco','Bossio','corro 37',True, 1.90}
conjunto = {'nuevo  conjunto'}
print(conjunto)#se va a imprimir el ultimo conjutno (no se puede acceder por indice)

#creando dicceonarios (dict)
diccionarios = {
    'nombre' : 'Francisco Bossio',
    'altura' : 1.90,
    'esta emocionado' : True    
}
print(diccionarios['nombre'])
print(diccionarios['esta emocionado'])
print(diccionarios['altura'])