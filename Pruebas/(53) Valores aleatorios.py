# Para usar la función random, la cual devuelve valores aleatorios
import random

# Calcula 10 números aleatorios
def vector_aleatorio(n): # Forma de declarar funciones
    vector = [0]*n # Este array no puede inicializarse como vacío
    for i in range(n):
        vector[i] = random.randint(0,10) # Genera valores aleatorios enteros entre 0 y 10
    return vector

print("Ingrese cuántos números aleatorios desea obtener: ")
n = int(input())

aleatorio = vector_aleatorio(n)
print(aleatorio)