'''
Escribir un programa que pregunte al usuario su edad y 
muestre por pantalla todos los años que ha cumplido 
(desde 1 hasta su edad).
'''

while True:
    try:
        edad = int(input("¿Cuántos años tienes? "))
        print("Has cumplido:", end=' ')
        for i in range (1, edad + 1):
            if i == edad:
                print(i, end=' años\n')
            elif i == (edad - 1):
                print(i, end=' y ')
            else:
                print(i, end=', ')
        break
    except:
        print("Introduzca un número entero\n")