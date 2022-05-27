'''
Escribir un programa que pida al usuario que introduzca una frase en la consola y 
muestre por pantalla la frase invertida.
'''

from audioop import reverse
from msilib import CAB


cadena = input("Ingrese una frase a su gusto: ")
print("Su cadena del revés es: {}".format(''.join(reversed(cadena))))

'''
# Alternativa

frase = input("Ingrese una frase a su gusto: ")
print(frase[::-1])
'''