# Genera los n primeros múltiplos de 3

n = int(input("Ingrese un numero: "))
m = 3
for i in range (1, n + 1):
    print(m, end=' ') # De esta forma no se imprime en vertical
    m = m + 3
