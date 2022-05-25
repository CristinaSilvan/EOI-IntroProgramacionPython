from pymongo import MongoClient
from os.path import exists
from random import randint

# Lee el fichero, sino existe lo crea
def GestionFichero(fichero_nombre):
    try:
        if exists(fichero_nombre):
            fichero = open(fichero_nombre, "rt", encoding='UTF-8')
            #print(fichero.read())
        else:
            fichero = open(fichero_nombre, 'wt', encoding='UTF-8')
            fichero.write(str(RellenarFichero()))   

        datos = fichero.read()

    except Exception as e:
        print("ERROR: {e}".format(e))
    finally:
        fichero.close()

    return datos

# Función auxiliar que crea el fichero y lo rellena
def RellenarFichero ():
    ListaCiudades = ['Malaga','Alava','Albacete','Alicante','Almería','Asturias','Avila','Badajoz','Barcelona','Burgos','Cáceres','Cádiz','Cantabria','Castellón','Ceuta','Ciudad Real','Córdoba','Cuenca','Formentera','Girona']
    dicc = {}
    for ciudad in ListaCiudades:
        listatemperaturas = []
        for i in range(0,12):
            temperaturas = randint(0,50)
            listatemperaturas.append(temperaturas)
    dicc[ciudad] = listatemperaturas
    return dicc

# Trabajo con la Base de Datos
if __name__=='__main__':
    nombre_fichero = ".\Ejercicios de Clase\Ficheros\Colecciones Ficheros II\Datos_4 (A).txt"
    datos_fichero = eval(GestionFichero(nombre_fichero))

    url = "mongodb://localhost:27017/"
    conexion = MongoClient(url) # Establecer conexión
    cursor = conexion.admin # Crear cursor o puntero

    cursor = conexion["Estadisticas"] # Creando Base de Datos
    coleccion = cursor["ListaTemperaturas"] # Creando Colección

    # Insertando información del fichero
    for i in datos_fichero:
        diccionario = {
            "Ciudad":i,
            "Temperaturas":datos_fichero[i]
        }
        coleccion.insert_one(diccionario)


    # Leyendo información de la base de datos


    # Procesando información y volcando resultados en fichero nuevo


    conexion.close()