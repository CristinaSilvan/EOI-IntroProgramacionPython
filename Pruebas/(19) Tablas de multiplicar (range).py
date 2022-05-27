# range es una función que crea una lista de números que
# empieza en a, termina en b (b no incluido) y c es el incremento/decremento range (a,b,c)

n = int(input("Ingrese un numero: "))
for i in range(1, 10+1, 1):
    print(i, " * ", n, " = ", i*n)
