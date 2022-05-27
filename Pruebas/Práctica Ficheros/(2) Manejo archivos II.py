file = file = "C:\\00-Python\\Pruebas\\Práctica Ficheros\\FicheroI.txt"
archivo = open(file, "r", encoding='UTF-8')
contenido_exterior = archivo.read()
archivo.close()
print("Esto es lo que hay en el interior del archivo:\n{}".format(contenido_exterior))