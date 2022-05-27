'''
Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla.
'''

lista = []
palabra = ''
while True:
    palabra = input("Escriba asignaturas, fin para salir: ")
    if palabra == 'fin':
        break
    lista.append(palabra)
print(lista)
