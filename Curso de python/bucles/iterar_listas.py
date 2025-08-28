animales = ['gato','perro','loro']
numeros = [1,5,3]
for animal in animales:
    print(animal)
    
#iteramos dos listas al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(animal)
    print(numero)
    
for num in range(5,10):
    print(num)
    

for num in range(10):
    print(num)    

#forma correcta de recorrer una lista con su indece
for num in enumerate(numeros):
    print(num[1])
    
#usando el else
for num in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {num}')
else:
    print('el bucle termino')
    
