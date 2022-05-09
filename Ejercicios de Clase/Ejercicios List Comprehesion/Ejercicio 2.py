'''
Crear una lista a partir de los elementos de un rango de 
1200 a 2000 con pasos de 130, utilizando la comprensión de listas.
'''

rng = []
for i in range(1200,2001,130):
    rng.append(i)
'''
# Alernativa
rng = range(1200,2001,130)
print(list(rng)) # Sino parseamos a list, aparecerá como objeto range
'''
lista = [i for i in rng]
print(f"Lista 1: {rng}\nLista 2: {lista}")