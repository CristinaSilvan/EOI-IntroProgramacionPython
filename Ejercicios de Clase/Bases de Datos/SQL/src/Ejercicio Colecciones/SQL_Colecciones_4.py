import pyodbc 
from os.path import exists
from random import randint

"""
CREATE TABLE Temperaturas 
(   
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    CIUDAD varchar(50) NOT NULL, 
    TEMPERATURAS varchar(300)
)
"""

# Lee el fichero, sino existe lo crea
def GestionFichero(fichero_nombre):
    if exists(fichero_nombre):
        fichero = open(fichero_nombre, "rt", encoding='UTF-8')
        
    else:
        fichero = open(fichero_nombre, 'wt', encoding='UTF-8')
        fichero.write(str(RellenarFichero()))   
    
    datos = fichero.read()

    if fichero.closed == False:
        fichero.close()

    return datos

# Función auxiliar que rellena el fichero
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
    nombre_fichero = "C:\\1-PythonEOI\\\Ejercicios de Clase\\Bases de Datos\\SQL\\src\\Ejercicio Colecciones\\Datos_4 (A).txt"
    
    datos_fichero = eval(GestionFichero(nombre_fichero))

    server = 'PC-CRIS'
    database = 'Estadistica' 
    username = 'Developer' 
    password = 'P4$$w0rd' 
    driver='DRIVER={ODBC Driver 17 for SQL Server};'
    others=f"SERVER={server};DATABASE={database};UID={username};PWD={password}"
    connection_string='{}{}'.format(driver,others)
    conexion = pyodbc.connect(connection_string)
    cursor = conexion.cursor()