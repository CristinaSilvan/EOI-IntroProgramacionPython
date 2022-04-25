# Serie alfabética
#   A, B, A, B, A, B, ...


n = int(input("Ingrese un numero: "))
interruptor = 0
for i in range(1, n+1):
    if interruptor == 0:
        print("A", end=', ')
        interruptor = 1
    else:
        print("B", end=', ')
        interruptor = 0
    
