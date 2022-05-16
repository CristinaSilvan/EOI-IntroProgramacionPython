fichero = "C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Colecciones Ficheros II\\Datos_1 (A).txt"
archivo = open(fichero, "rt", encoding='UTF-8')

cadena = archivo.read()
lista = []
for i in cadena:
    if i == 'M':
        lista.append('M')
    if i == 'H':
        lista.append('H')

archivo.close()

fichero = "C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Colecciones Ficheros II\\Datos_1 (B).txt"
archivo = open(fichero, "wt", encoding='UTF-8')

archivo.write("RESULTADOS DEL EJERCICIO 1:\n\nLista generada: {}\n\n".format(lista))
archivo.write("Total de personas: {}\n".format(len(lista)))
archivo.write("Mujeres: {}\n".format(lista.count('M')))
archivo.write("Hombres: {}\n\n".format(lista.count('H')))

archivo.write(f"El porcentaje de mujeres es del: {lista.count('M')}%\n")
archivo.write(f"El porcentaje de hombres es del: {lista.count('H')}%\n")

if(lista.count('M') > lista.count('H')):
    archivo.write("\tConclusión: Hay más mujeres que hombres")
elif(lista.count('M') == lista.count('H')):
    archivo.write("\tConclusión: Hay igualdad")
else:
    archivo.write("\tConclusión: Hay más hombres que mujeres")

archivo.close()