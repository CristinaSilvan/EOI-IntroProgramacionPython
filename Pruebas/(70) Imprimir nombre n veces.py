'''
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
'''

while(True):
    nombre = input("INICIO: Ingrese su nombre: ")
    try:
        n = int(input("Ingrese el número de veces que quiere que se repita: "))
        if n <= 0:
            print('Ingrese un número válido')
            continue
        print((nombre + '\n')*n)
        break
    except:
        print('Ingrese un número válido')