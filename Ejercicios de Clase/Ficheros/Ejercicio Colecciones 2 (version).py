from random import randint
from os.path import exists

def lee_o_crea_fichero(file, personas):
    try:
        if exists(file):
            fichero = open(file, 'rt', encoding='UTF-8')
            print("Contenido de fichero:\n{}".format(fichero.read()))
        else:
            fichero = open(file, 'wt', encoding='UTF-8')
            fichero.write(str(personas))
            print(f"Fichero: Generado con éxito!")
    except Exception as e:
        print("ERROR: {e}".format(e))
    finally:
        fichero.close()

personas1 = []
for n in range(1,101):
    personas1.append(randint(0,125))

personas2 = [randint(1,125) for i in range(1,101)]

file1 = '.\\Ejercicios de Clase\\Ficheros\\Datos_Colecciones2 (1).txt'
file2 = '.\\Ejercicios de Clase\\Ficheros\\Datos_Colecciones2 (2).txt'

lee_o_crea_fichero(file1,personas1)
lee_o_crea_fichero(file2,personas2)