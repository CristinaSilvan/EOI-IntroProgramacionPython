'''
Escribir un programa que pida al usuario un número entero y
muestre por pantalla si es par o impar.
'''

while True:
    try:
        n = int(input("Su número: "))
        if n % 2 == 0:
            print(f"{n} es par")
        else:
            print(f"{n} es impar")
        break
    except:
        print("Introduzca un número entero\n")