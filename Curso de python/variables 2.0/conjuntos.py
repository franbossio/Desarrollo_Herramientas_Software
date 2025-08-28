#los conjuntos no son modificables

#creando un conjunto con set()
#conjunto = set(['fran','bossio'])

#metiendo un conj dentro de otro conj 
#conjunto = frozenset(['datol','dato2'])
#conjunto2= {conjunto,'hola'}


#teoria de conjuntos
conjutnos1={1,3,5,7}
conjunto2 = {1,3,7}

#ver si un conj es un subconj de otro conj
#resultado = conjunto2.issubset(conjutnos1)
#resultado = conjunto2 <= conjutnos1

#verificar si es un superconjunto
#resultado = conjunto2.issuperset(conjutnos1)
resultado = conjunto2 > conjutnos1

#verificar si hay un numero en comun
resultado = conjunto2.isdisjoint(conjutnos1)
print(resultado)