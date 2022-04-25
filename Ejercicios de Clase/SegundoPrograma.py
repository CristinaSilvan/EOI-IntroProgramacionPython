a = 5
b = 10
print("Paso 1. Valores iniciales")
print(a)
print(b)

# Variable auxiliar para poder intercambiar valores
c = b

b = a
a = c
del c
print("Paso 2. Valores intercambiadas")
print(a)
print(b)