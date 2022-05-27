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
        if fichero.closed == False:
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
    nombre_fichero = "C:\\1-PythonEOI\\Ejercicios de Clase\Bases de Datos\SQL\src\Ejercicio Colecciones\Datos_4 (A).txt"
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
    diccionario.clear()

    query = {'Id':id}
    resultado = coleccion.find_one(query)
    #datos = resultado['Data']
    #lista = eval(datos)
    #print(lista)

    # Procesando información y volcando resultados en fichero nuevo


    conexion.close()

# Para procesar los datos y obtener los resultados de las estadísticas
'''
    file = "C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Colecciones Ficheros II\\Datos_4 (B).txt"
    archivo = open(file, "wt", encoding='UTF-8')

    archivo.write("RESULTADOS DEL EJERCICIO 4:\n\n")

    archivo.write("="*100+'\n')

    DiccPromedioAnual = {}
    for clave, valor in dicc.items():
        archivo.write(f'{clave} -> {valor} \t')
        tuplatemperaturas = tuple(valor)
        MediaAnuales = round(sum(tuplatemperaturas)/12, 2)
        DiccPromedioAnual[clave] = MediaAnuales
    MaxProAnual = max(DiccPromedioAnual.values())
    MinProAnual = min(DiccPromedioAnual.values())

    archivo.write(
        f'La ciudad con el promedio anual mas ALTO 1 es {list(DiccPromedioAnual.keys())[list(DiccPromedioAnual.values()).index(MaxProAnual)]} con un promedio de: {MaxProAnual} ºC')
    archivo.write(
        f'\nLa ciudad con el promedio anual mas ALTO 2 es {max(DiccPromedioAnual,key=DiccPromedioAnual.get)} con un promedio de: {MaxProAnual} ºC')

    archivo.write(
        f'\n\nLa ciudad con el promedio anual mas BAJO 1 es {list(DiccPromedioAnual.keys())[list(DiccPromedioAnual.values()).index(MinProAnual)]} con un promedio de: {MinProAnual} ºC')
    archivo.write(
        f'\nLa ciudad con el promedio anual mas BAJO 2 es {min(DiccPromedioAnual,key=DiccPromedioAnual.get)} con un promedio de: {MinProAnual} ºC\n')
    ListaPromedioAnual = list(DiccPromedioAnual.items())
    ListaPromedioAnual.sort(key=lambda x: x[1], reverse=True)
    archivo.write("="*100+'\n')
    archivo.write(
        f'\n\nLa lista de las ciudades ordenadas es :\n{ListaPromedioAnual}\n\n')
    ListaPromedioAnual1 = sorted(
        DiccPromedioAnual, key=DiccPromedioAnual.get, reverse=True)

    archivo.write("="*100+'\n\n')

    for i in ListaPromedioAnual1:
        archivo.write(i + " = ")
        archivo.write(str(DiccPromedioAnual[i]) + "ºC\n")

    archivo.close()

'''
