'''
Hacer un programa que procese 100 mujeres y hombres (M/H).
Mostrar el porcentaje de hombres y mujeres y si hay más mujeres que hombres, si hay igualdad o si hay más hombres que mujeres.
'''

# Versión con H y M
from random import choice

lista = []
for i in range(0,100):
    lista.append(choice('HM'))

print(f"El porcentaje de mujeres es del: {lista.count('M')}%")
print(f"El porcentaje de hombres es del: {lista.count('H')}%")
if(lista.count('M') > lista.count('H')):
    print("Hay más mujeres que hombres")
elif(lista.count('M') == lista.count('H')):
    print("Hay igualdad")
else:
    print("Hay más hombres que mujeres")

respuesta = input("¿Quieres ver el total de los datos? ").lower()
if respuesta == 'si' or respuesta == 'sí' or respuesta == 's' or respuesta == 'yes' or respuesta == 'y':
    print("\nMujeres: {}".format(lista.count('M')))
    print("Hombres: {}".format(lista.count('H')))
    print("Lista: {}".format(lista))
    print("Total de personas: {}".format(len(lista)))


'''
# Versión con 0 y 1
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

respuesta = input("¿Quieres ver el total de los datos? ").lower()
if respuesta == 'si' or respuesta == 'sí' or respuesta == 's' or respuesta == 'yes' or respuesta == 'y':
    print("\nMujeres: {}".format(lista.count(0)))
    print("Hombres: {}".format(lista.count(1)))
    print("Lista: {}".format(lista))
    print("Total de personas: {}".format(len(lista)))

'''