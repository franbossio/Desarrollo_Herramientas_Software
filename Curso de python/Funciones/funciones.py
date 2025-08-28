#creando una funcion simple

def saludar():
    print('¿Hola como estas?')
saludar()

#creando una funcion que tenga parametros
def saludar2(nombre,sexo):
    sexo.lower()
    if sexo=='mujer':
        adjetivo = 'reina'
    elif sexo =='hombre':
        adjetivo = 'titan'
    else:
        adjetivo = 'amor'
    print(f'Hola {nombre} mi {adjetivo}')
    
saludar2('fran','hombre')

saludar2('fran','no binario')

#crear una funcion que retorne algo
def crear_contraseña_random(num):
    chars = 'adlfñjkladsfj'
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    #print(contraseña)
    return contraseña
    
    
print(crear_contraseña_random(254))

#utilizando el parametro  * como argumento (*args) 
def suma(*numeros):
    return sum(numeros)

resultado = suma(5,1,2,3,5)
print(resultado)

#cambiar de orden los parametros
def frase(nombre, apellido):
    print(f'hola {nombre} {apellido}')
    
frase(apellido='bossio',nombre='francisco')

def frase(nombre, apellido='bossio'): #esto siempre va a ser bossio, es un parametro opcional
    print(f'hola {nombre} {apellido}')