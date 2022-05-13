file = "C:\\00-Python\\Pruebas\\Práctica Ficheros\\FicheroI.txt"
archivo = open(file, "r", encoding='UTF-8') # "r+" significa lectura y escritura

archivo.seek(len(archivo.readline())) # Sitúa el puntero al final de la primera línea
print(archivo.read()) # Incluye el primer salto de línea
archivo.close()