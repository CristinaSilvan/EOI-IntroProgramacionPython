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

#print(f"Ejercicio: {__name__}")
if __name__ == '__main__': # Esto es para diferenciar la función del código principal, para poder usar la función fuera del módulo sin problemas
    personas = [randint(1,125) for i in range(1,101)]

    file = '.\\Ejercicios de Clase\\Ficheros\\Colecciones Ficheros II\\Datos_2 (A).txt'

    lee_o_crea_fichero(file,personas)