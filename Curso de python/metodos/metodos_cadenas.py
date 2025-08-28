cadena1 = 'Hola soy German'
cadena2 = 'hola,que,haces'

resultado = dir(cadena1) #muestra todo lo que podes hacer con este objeto

#convertir en mayuscula
print(cadena1.upper()) #dato.metodo(), asi funcionan los metodos

#convertir en minuscula
print(cadena1.lower())

#convertir primera letra en mayusculas
print(cadena1.capitalize())

#buscamos una cadena en otra cadena
print(cadena1.find('o')) #si retorna -1 significa que no encontro nada

print(cadena1.index('l')) #si no encuentra nada nos lanza una excepcion

#si es numerico, devuelve true
print(cadena2.isnumeric())
print(cadena2.isalpha())

#buscamos una cadena en otra cadena, devuelve las veces que coincide
print(cadena1.count('a'))

#contamos cuantos caracteres tiene una cadena
print(len(cadena1))

#verificamos si una cadena empieza con otra cadena, si es asi devuele true
print(cadena1.startswith('Hola'))

#verificamos si una cadena termina con otra cadena, si es asi devuele true
print(cadena1.endswith('man'))

"reemplaza un pedazo de la cadena"
print(cadena1.replace('German','Fran'))

#separar cadenas con la cadena que le pasamos
print(cadena2.split(',')[1])