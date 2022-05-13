file = "C:\\00-Python\\Pruebas\\Práctica Ficheros\\FicheroI.txt"
archivo = open(file, "a", encoding='UTF-8')
archivo.write("\nEsta es una nueva línea agreagada desde script")
archivo.close()