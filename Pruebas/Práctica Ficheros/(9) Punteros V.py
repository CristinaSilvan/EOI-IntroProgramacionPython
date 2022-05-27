file = "C:\\00-Python\\Pruebas\\Práctica Ficheros\\FicheroII.txt"
archivo = open(file, "r+", encoding='UTF-8')

#archivo.write("Primera línea del fichero\nSegunda línea del fichero\nTercera línea del fichero")

lista = archivo.readlines()

lista[1] = "Segunda línea modificada mediante Script\n"
archivo.seek(0)
archivo.writelines(lista) # writelines pide una lista por parámetros

archivo.close()