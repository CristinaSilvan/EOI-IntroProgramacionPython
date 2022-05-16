fichero = "C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Colecciones Ficheros I\\Ejercicio_3.txt"
archivo = open(fichero, "w", encoding='UTF-8')

from random import randint
from random import choice

archivo.write("Ejercicio 3\n\n")

def calculo_lista(lista, genero):
    lista.sort()
    promedio = 0
    if genero == 'M':
        for i in lista:
            if i >= 18:
                archivo.write(f"Hay {len(lista[lista.index(i):])} mujeres mayores de edad\n")
                break
        archivo.write(f"La mujer más joven tiene {min(lista)} años y la más mayor {max(lista)} años\n")
        for i in lista:
            promedio += i
        archivo.write("El promedio de edad de las mujeres es de {} años\n".format(promedio/100))
    else:
        for i in lista:
            if i < 18:
                archivo.write(f"Hay {len(lista[lista.index(i):])} hombres menores de edad\n")
                break
        archivo.write(f"El hombre más joven tiene {min(lista)} años y el más mayor {max(lista)} años\n")
        for i in lista:
            promedio += i
        archivo.write("El promedio de edad de los hombres es de {} años\n".format(promedio/100))


total = {}
total['M'] = []
total['H'] = []

for i in range(0,100):
    total[choice('MH')].append(randint(1,120))

archivo.write("\nTotal de personas: {}".format(len(total.get('M')) + len(total.get('H'))))
archivo.write("\nMujeres: {}".format(total.get('M')))
archivo.write("\nHombres: {}\n\n".format(total.get('H')))

calculo_lista(total.get('M'), 'M')
archivo.write('\n\n')
calculo_lista(total.get('H'), 'H')

archivo.write(f"\nHay un total de {len(total.get('M'))} mujeres")
archivo.write(f"\nHay un total de {len(total.get('H'))} hombres")
