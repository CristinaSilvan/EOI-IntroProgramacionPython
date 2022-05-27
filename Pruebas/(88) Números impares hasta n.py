'''
Escribir un programa que pida al usuario un número entero 
positivo y muestre por pantalla todos los números impares 
desde 1 hasta ese número separados por comas.
'''


n = int(input("Ingrese un entero positivo"))
print("Los números impares hasta {} son: ".format(n), end='')
for i in range(1,n):
    if i % 2 != 0:
        print(i, end=', ')

'''
# Alternativa (sin comprobación)

n = int(input("Introduce un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=", ")
'''