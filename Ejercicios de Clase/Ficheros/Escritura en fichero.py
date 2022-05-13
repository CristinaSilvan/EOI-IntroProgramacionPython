file = "C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Fichero_2.txt"
fichero = open(file, "w", encoding='UTF-8')
contenido = "Este contenido está generado desde el script 'Escritura en fichero.py'"
fichero.write(contenido)
# eval() sirve para pasar una cadena de caracteres a lista o diccionarios