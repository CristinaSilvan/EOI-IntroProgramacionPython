'''
Hacer un programa que procese las temperaturas mensuales de 20 ciudades. 
Deberá sacar cuál de las ciudades tiene en promedio anual la temperatura más alta y 
cual la más baja. También deberá sacar la lista de las 20 ciudades con el promedio de 
temperaturas anuales desde la más alta hasta la más baja.
'''

from random import randint

total = {}
promedio = 0
for i in range(1,20 + 1):
    total[i] = []
    for j in range(0,365):
        total[i].append(randint(-20,50))
        promedio += total.get(i)[j]
    total[i] = round(promedio/365)

print(total)
