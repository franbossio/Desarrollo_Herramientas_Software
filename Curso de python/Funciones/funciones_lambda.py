#funcino anonimas, lo podemos usar para usar algo sencillo y rapido, y retorna rapidamente
multiplicar_por_dos = lambda x : x*2

print(multiplicar_por_dos(5))
#filter devuelve solo lo true
numeros = [1,5,6,3,8,52,5]
numeros_pares = filter(lambda numero:numero%2==0,numeros)
print(list(numeros_pares))