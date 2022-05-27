from os.path import exists

try:
    file = ("./Ejercicios de Clase/Ficheros/Fichero_excepciones.txt")
    if exists(file):
        fichero = open(file, 'rt', encoding='UTF-8')
        print(fichero.read())
    else:
        fichero = open(file, 'wt', encoding='UTF-8')
        fichero.write("Esta es la primera línea")
except Exception as e:
    print("ERROR: {}".format(e))
finally:
    fichero.close()