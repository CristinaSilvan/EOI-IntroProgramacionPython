# Serie Fibonacci
# 1, 1, 2, 3, 5, 8, 13, 21, ...

'''
Ejemplo:
w1 + w2 = suma

1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8
5 + 8 = 13
8 + 13 = 21

'''

n = int(input("Ingrese un numero: "))
w1 = 1  # Interruptor 1
w2 = 1  # Interruptor 2
suma = 0  # Acumulador
c = 0  # Controlador

if n <= 0:
    print("El valor ingresado es erroneo")
elif n == 1:
    print(w1)
else:
    while c < n:
        print(w1)
        suma =  w1 + w2
        w1 = w2
        w2 = suma
        c += 1
