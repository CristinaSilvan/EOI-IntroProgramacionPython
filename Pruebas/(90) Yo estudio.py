'''
Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>,
donde <asignatura> es cada una de las asignaturas de la lista.
'''

lista = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']

for i in lista:
    if i == lista[0]:
        print(f"Yo estudio {i},", end=' ')
    elif i == lista[len(lista) - 2]:
        print(f'yo estudio {i} ', end='')
    elif i == lista[len(lista) - 1]:
        print(f'y yo estudio {i}.', end='')
    else:
        print(f"yo estudio {i},", end=' ')