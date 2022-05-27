'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
'''

try:
    edad = int(input("Dime tu edad: "))
    if edad < 1 or edad > 120:
        print("ESO ES IMPOSIBLE!!! Voy a llamar al área 51")
    elif edad > 18:
        print("Eres mayor de edad")
    else:
        print("No eres mayor de edad")
except:
    print("El dato no es válido")