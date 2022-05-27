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

mujeres = []
hombres = []

genero = [randint(0,1) for n in range(1,101)]
mujeres = [randint(0,101) for g in genero if g==1]
hombres = [randint(0,101) for g in genero if g==0]

file1 = '.\\Ejercicios de Clase\\Ficheros\\Colecciones Ficheros II\\Datos_3 (Mujeres).txt'
file2 = '.\\Ejercicios de Clase\\Ficheros\\Colecciones Ficheros II\\Datos_3 (Hombres).txt'

lee_o_crea_fichero(file1, mujeres)
lee_o_crea_fichero(file2, hombres)