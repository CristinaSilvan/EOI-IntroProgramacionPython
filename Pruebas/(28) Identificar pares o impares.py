# Identificar pares e impares según rango

n = int(input("Escriba el primero numero: "))
m = int(input("Escriba el segundo numero: "))

if n > m:
        print("Error, el primero debe ser menor")
else:
    for i in range(n,m+1):
        if i % 2 == 0:
            print(f"El numero {i} es par")
        else:
            print(f"El numero {i} es impar")
