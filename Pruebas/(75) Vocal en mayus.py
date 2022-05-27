'''
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, 
y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
'''

frase = ''
vocal = ''
vocales = 'aeiouAEIOU'
while True:
    frase = input("Escriba una frase: ")
    vocal = input("Escriba una vocal: ")
    if (len(vocal) < 1) or (len(frase) < 1):
        print("El programa no puede funcionar si usted no escribe los parámetros\n")
        continue
    if not vocal in vocales:
        print("La letra introducida no es una vocal\n")
        continue
    if not vocal in frase:
        print("La vocal no se encuentra en la frase\n")
        continue
    print(frase.replace(vocal, vocal.upper()))
    break