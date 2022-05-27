'''
Para tributar un determinado impuesto se debe ser mayor de 16 años
y tener unos ingresos iguales o superiores a 1000 € mensuales. 
Escribir un programa que pregunte al usuario su edad y sus ingresos 
mensuales y muestre por pantalla si el usuario tiene que tributar o no.
'''

while True:
    try:
        edad = int(input("¿Cuántos años tienes? "))
        ingresos = float(input("¿Cuáles son tus ingresos mensuales? "))
        if edad > 16 and ingresos >= 1000:
            print("Tienes que tributar")
        else:
            print("No tienes que tributar")
        break
    except:
        print("Introduzca datos válidos\n")