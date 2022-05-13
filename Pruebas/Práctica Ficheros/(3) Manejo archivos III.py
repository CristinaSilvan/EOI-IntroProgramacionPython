file = "C:\\00-Python\\Pruebas\\Práctica Ficheros\\FicheroI.txt"
archivo = open(file, "r", encoding='UTF-8')
lista = archivo.readlines()
archivo.close()

print(lista)