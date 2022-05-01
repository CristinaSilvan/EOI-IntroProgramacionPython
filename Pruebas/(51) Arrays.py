# Arrays (Arreglos o Vectores)

'''
- Los arrays son conjuntos de datos (heterogéneos)

- Tienen un orden y pueden ser accedidos por su posición

- Se pueden recorrer mediante un for

- Todos los elementos del array, deben ser del mismo tipo

- El tamaño del array es fijo y debe ser especificado con su creación, al contrario que las listas que crecen de forma dinámica

- Normalmente son utilizados para albergar valores numéricos
'''

# Ejercicio que crea un arreglo de n múltilplos de un número m

n = int(input("Tamaño del arreglo: "))
m = int(input("Ingrese el numero de múltiplos: "))
arreglo = [] # Inicialización, ya que vamos a tomar los valores del usuario

for i in range(0,n):
    arreglo.append(i*m)

print(f"El arreglo que usted ha creado: {arreglo}")

