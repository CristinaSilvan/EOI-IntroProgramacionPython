'''
Escribir un programa que pida al usuario una palabra y 
la muestre por pantalla 10 veces.
'''

palabra = input("¿Qué palabra quieres repetir? ")
for i in range(0,10):
    print(palabra)

'''
# Alternativa (sin bucle)
palabra = input("¿Qué palabra quieres repetir? ")
print((palabra + '\n')*10)

'''