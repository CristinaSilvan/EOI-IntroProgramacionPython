import math

nro = int(input("Ingrese un nro: "))
resul = 0

while nro > 0:
    resul = resul + nro % 10
    nro = math.trunc(nro / 10)
print("El resultado es ", resul)