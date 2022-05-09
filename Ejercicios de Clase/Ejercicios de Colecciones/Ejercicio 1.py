'''
Hacer un programa que procese 100 mujeres y hombres (M/H).
Mostrar el porcentaje de hombres y mujeres y si hay más mujeres que hombres, si hay igualdad o si hay más hombres que mujeres.
'''

from random import randint

# En este programa, procesa las mujeres como 0 y los hombres como 1
lista = []
for i in range(0,100):
    lista.append(randint(0,1))

print(f"El porcentaje de mujeres es del: {lista.count(0)}%")
print(f"El porcentaje de hombres es del: {lista.count(1)}%")
if(lista.count(0) > lista.count(1)):
    print("Hay más mujeres que hombres")
elif(lista.count(0) == lista.count(1)):
    print("Hay igualdad")
else:
    print("Hay más hombres que mujeres")