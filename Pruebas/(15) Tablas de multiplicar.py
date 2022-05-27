#  Muestra la tabla de multiplicar del número que queramos del 1 al 9

n = int(input("Que tabla de multiplicar quiere ver: "))
i = 1

if n < 1 or n > 9:
    print("No existe una tabla para ese numero")
else:
        while(i <= 10):
            print(n, "*", i, " = ", (n*i))
            i = i + 1
