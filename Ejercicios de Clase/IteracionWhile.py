# Realizando pruebas con el bucle while
print("Antes del while")
valor = 0
while(valor < 5):
    print(f"Valor actual: {valor}")
    valor+=1
print("Después del while")

'''
Antes del while
Valor actual: 0
Valor actual: 1
Valor actual: 2
Valor actual: 3
Valor actual: 4
Después del while
'''

print("Antes del while")
valor = 0
while(valor < 5):
    valor+=1
    print(f"Valor actual: {valor}")
print("Después del while")

'''
Antes del while
Valor actual: 1
Valor actual: 2
Valor actual: 3
Valor actual: 4
Valor actual: 5
Después del while
'''


# Probando continue
print("Antes del while")
valor = 0
while(valor < 5):
    valor+=1
    if(valor==3):
        continue # Salta a la siguiente iteración, por lo tanto no imprime 3
    print(f"Valor actual: {valor}")
print("Después del while")

'''
Antes del while
Valor actual: 1
Valor actual: 2
Valor actual: 4
Valor actual: 5
Después del while
'''

# Alternativa del mismo programa sin usar cotinut
print("Antes del while")
valor = 0
while(valor < 5):
    valor+=1
    if(valor != 3): # Otra forma de que salte el valor 3
        print(f"Valor actual: {valor}")
print("Después del while")


# Probando break
print("Antes del while")
valor = 0
while(valor < 5):
    valor+=1
    if(valor>3):
        break # Termina inmediatamente el bucle, por lo tanto no imprime los valores mayor a 3
    print(f"Valor actual: {valor}")
print("Después del while")

'''
Antes del while
Valor actual: 1
Valor actual: 2
Valor actual: 3
Después del while
'''