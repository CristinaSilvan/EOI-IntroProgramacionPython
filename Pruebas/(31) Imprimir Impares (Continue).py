# Continue hace (en las estructuras de condicional)  que salte a la siguiente condición
# Continue hace (en las estructuras iterativas) que salte a la siguiente iteración
# sin leer el resto de instrucciones tras de él

n = int(input("Ingrese un numero: "))
for i in range(1, n+1):
    if i % 2 == 0:
        continue
        print(i)
    else: 
        print(i)
