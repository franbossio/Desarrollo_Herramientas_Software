#import modulo_saludar as m_saludar

#desde ese modulo, importamos las funciones, y pones , se puede importar mas funciones, 
#  y si pones import * , importar todas las funciones
from modulo_saludar import saludar

#para importar un archivo dentro de otro es 
#import funciones.saludar
saludo = saludar('lucas')
print(saludo) 