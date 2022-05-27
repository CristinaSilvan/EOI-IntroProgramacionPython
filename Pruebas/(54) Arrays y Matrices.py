# Módulo específico para trabajar de una manera mejor con los vectores y matrices
import numpy as np  # as para poner un identificador que usar en el script

# VECTORES --------------------------------------

vector = np.array([6,7,1,2,3])
print(f"Mi vector en numpy {vector.astype(str)}") # .astype() para tratar el tipo de dato como otro
# ['6' '7' '1' '2' '3']

print(f"\nEl mayor valor de mi vector es {vector.max()}")
print(f"Y su posición dentro del vector es {vector.argmax()}") 
# Teniendo en cuenta que se posicionan del 0 al len(vector)
# Máximo valor y posición

print(f"\nEl manor valor de mi vector es {vector.min()}")
print(f"Y su posición dentro del vector es {vector.argmin()}")
# Mínimo valor y posición 

print(f"La multiplicación de mi vector es {vector.prod()}")
# Multiplicar todos los valores

a = np.array([6,7,1,2,3])
b = np.array([6,7,5,8,1])
print(f"\nSuma de vectores enteros {a+b}")
print(f"\nComparación de vectores enteros {a>b}")
# Operaciones con vectores

del vector
del a
del b


# MATRICES --------------------------------------

vector = np.array([6,7,1,2,3])
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]]) # Las matrices son vectores de tres dimensiones
print("\n\nEsto es un vector")
print(vector)
print("\nEsto es una matriz")
print(matriz)

matriz_1 = np.array([[1,1,1],[1,1,1],[1,1,1]])
matriz_2 = np.array([[2,2,2],[2,2,2],[2,2,2]])
print("\nSuma de matrices")
print(matriz_1 + matriz_2) # [[3,3,3],[3,3,3],[3,3,3]]
# Operaciones de matrices

print(f"El tamaño de mi vector es {vector.size}") # La cantidad de valores que contiene
print(f"El tamaño de mi matriz es {matriz.size}")
# Tamaño vector