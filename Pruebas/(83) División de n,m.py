'''
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error.
'''

while True:
    try:
        n = int(input("Introduzca dividendo: "))
        m = int(input("Introduzca divisor: "))
        print(f"\nEl resultado de la división es: {(n/m):.2f}")
        break
    except ZeroDivisionError:
        print("No se puede realizar la división entre cero\n")
    except:
        print("Introduzca datos válidos\n")