from random import choice

fichero = "C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Colecciones Ficheros II\\Datos_1 (A).txt"
archivo = open(fichero, "wt", encoding='UTF-8')

lista = []
for i in range(0,100):
    lista.append(choice('HM'))

archivo.write(str(lista))
archivo.close()
