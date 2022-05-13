file = "C:\\00-Python\\Pruebas\\Práctica Ficheros\\FicheroI.txt"
archivo = open(file, "r", encoding='UTF-8')

print(archivo.read(11)) # Lee el archivo hasta la posición 11
print(archivo.read(20)) # Sigue leyendo el archivo 20 posiciones más

archivo.close()