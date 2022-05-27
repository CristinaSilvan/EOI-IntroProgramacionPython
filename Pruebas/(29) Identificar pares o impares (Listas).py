# Identificar pares e impares según lista

A = [0,0,0,0,0]
for i in range(0, 5):
    A[i] = int(input("Inserte un numero: "))

for i in range(0,5):
    if A[i] % 2 == 0:
        print(f"El numero {A[i]} es par")
    else:
        print(f"El numero {A[i]} es impar")
