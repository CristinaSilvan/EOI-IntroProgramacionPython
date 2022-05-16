try:
    fichero = open(".\\Ejercicios de Clase\\Ficheros\\Fichero_1.txt", "rt", encoding='UTF-8')
    fichero.write("Esta línea no se escribirá por los permisos")
except Exception as e:
    print("Error en el fichero '{}'".format(e))
finally:
    fichero.close()