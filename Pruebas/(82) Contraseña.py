'''
Escribir un programa que almacene la cadena de caracteres contraseña
en una variable, pregunte al usuario por la contraseña e imprima por pantalla
si la contraseña introducida por el usuario coincide con la guardada en la variable 
sin tener en cuenta mayúsculas y minúsculas.
'''

contraseña = 'pepito69'
intentos = 5
while intentos > 0:
    dato = input("Escribe la contraseña: ").lower()
    if dato == contraseña:
        print("\nCorrecto!")
        exit()
    intentos -= 1
print("\nFallaste los 5 intentos. Bloqueando usuario...")