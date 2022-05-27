# Por defecto, si no le especifico al range(n)
# recorrerá desde 0 hasta n (n no incluido) incrementando 1

for numero in range(3):
    print(numero, end=' ') # 0 1 2

for numero in range(1,4):
    print(numero, end=' ') # 1 2 3

for numero in range(1,10,3):
    print(numero, end=' ') # 1 4 7
