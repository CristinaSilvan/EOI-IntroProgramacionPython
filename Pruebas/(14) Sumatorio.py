# Ejercicio sumatorio

n = int(input("Escribe un numero: "))
resul = 0
i = 1

if n < i:
    print("No se puede obtener el sumatorio de ese numero")

else:
    while i <= n:
        resul += i
        i = i + 1

    print("El sumatorio de ese numero es ", resul)
