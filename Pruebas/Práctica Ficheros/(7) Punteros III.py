file = "C:\\00-Python\\Pruebas\\Práctica Ficheros\\FicheroI.txt"
archivo = open(file, "r", encoding='UTF-8')

archivo.seek(len(archivo.read())/2) # Sitúa el puntero en la mitad del fichero
print(archivo.read()) # Lee la segunda mitad del fichero
archivo.close()