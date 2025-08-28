diccionario = {
    "nombre" : 'francisco',
    "apellido" : 'bossio',
    "edad" : 21
}
print(diccionario['edad'])
print(diccionario.keys())#mostrar las claves
print(diccionario.get('nombre'))

#eliminar todos los elementos del dicceonario

#diccionario.clear()

#elemina un elemento
diccionario.pop('edad')
print(diccionario)

#devolver exactamente el dicc
print(diccionario.items())

