'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje 
En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las 
correspondientes notas introducidas por el usuario.
'''

lista = []
palabra = ''
while True:
    palabra = input("Escriba la asignatura, fin para salir: ")
    if palabra == 'fin':
        break
    lista.append(palabra)
    for i in lista:
        nota = input(f"Escriba la nota de {i}: ")
print(lista)
