# Versión con H y M
from random import choice

fichero = "C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Ejericicio_1.txt"
archivo = open(fichero, "w", encoding='UTF-8')

archivo.write("Ejercicio 1\n\n")

lista = []
for i in range(0,100):
    lista.append(choice('HM'))

archivo.write("Lista generada: {}\n".format(lista))
archivo.write("Total de personas: {}\n".format(len(lista)))
archivo.write("Mujeres: {}\n".format(lista.count('M')))
archivo.write("Hombres: {}\n\n".format(lista.count('H')))

archivo.write(f"El porcentaje de mujeres es del: {lista.count('M')}%\n")
archivo.write(f"El porcentaje de hombres es del: {lista.count('H')}%\n")

if(lista.count('M') > lista.count('H')):
    archivo.write("Hay más mujeres que hombres")
elif(lista.count('M') == lista.count('H')):
    archivo.write("Hay igualdad")
else:
    archivo.write("Hay más hombres que mujeres")
