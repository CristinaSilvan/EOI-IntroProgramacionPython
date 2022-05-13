file = "C:\\00-Python\\Pruebas\\Práctica Ficheros\\FicheroI.txt"
archivo = open(file, "w", encoding='UTF-8')
contenido = "Esto es un ejemplo de contenido que se encontrará en el cuerpo del fichero\nHoy es 13 de Mayo de 2022"
archivo.write(contenido)
archivo.close() # Cerrarlo en la memoria del programa