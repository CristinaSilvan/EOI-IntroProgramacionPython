# Factorial de un número dado
# Ejemplo:
# 2! = 1 * 2 = 2
# 3! = 1 * 2 * 3 = 6

n = int(input("Ingrese un numero: "))
if n <= 0:
    print("Ingrese un numero positivo")
else:
    if n == 1:
        print("El factorial de 1 es 1")
    else:
        factorial = 1 # No puede iniciarse en cero porque es una multiplicación
        for i in range (1, n+1):
            factorial = factorial * i
        print(f"El facorial de {n} es {factorial}")
#Otra forma de imprimir por pantalla
