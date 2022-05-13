file = "C:\\00-Python\\Pruebas\\Práctica Ficheros\\FicheroI.txt"
archivo = open(file, "r", encoding='UTF-8')

print(archivo.read())
print(archivo.read()) # No puede volver a leerlo porque el cursor se encuentra al final por lo tanto no imprime nada
archivo.seek(0) # Para desplazar el cursor de lectura al principio (puedo colocarlo donde yo quiera)
print(archivo.read())
archivo.close()