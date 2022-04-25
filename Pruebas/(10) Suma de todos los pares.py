# Suma todos los pares entre 2 y 100

n = 2
suma = 0

while (n <= 100):
    if n % 2 == 0:
        suma = suma + n
    n = n + 1

print("La suma de los pares entre 2 y 100 es ",suma)