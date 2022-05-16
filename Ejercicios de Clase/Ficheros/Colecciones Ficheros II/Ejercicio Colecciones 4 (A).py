from random import randint
from os.path import exists

file = "C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Colecciones Ficheros II\\Datos_4 (A).txt"

def lee_o_crea_fichero(file, diccionario):
    try:
        if exists(file):
            fichero = open(file, 'rt', encoding='UTF-8')
            print("Contenido de fichero:\n{}".format(fichero.read()))
        else:
            fichero = open(file, 'wt', encoding='UTF-8')
            fichero.write(str(diccionario))
            print(f"Fichero: Generado con éxito!")
    except Exception as e:
        print("ERROR: {e}".format(e))
    finally:
        fichero.close()

ListaCiudades = ['Malaga','Alava','Albacete','Alicante','Almería','Asturias','Avila','Badajoz','Barcelona','Burgos','Cáceres','Cádiz','Cantabria','Castellón','Ceuta','Ciudad Real','Córdoba','Cuenca','Formentera','Girona']
dicc = {}
for ciudad in ListaCiudades:
    listatemperaturas = []
    for i in range(0,12):
        temperaturas = randint(0,50)
        listatemperaturas.append(temperaturas)
    dicc[ciudad] = listatemperaturas

lee_o_crea_fichero(file,dicc)