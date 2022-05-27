from pymongo import MongoClient
from pymongo import errors

url = "mongodb://localhost:27017/" # Endpoint

try:
    conexion = MongoClient(url,serverSelectionTimeoutMS=1000) # Conectar con servidor
    cursor = conexion.admin # Crear un cursor

    cursor = conexion["Escuela"] # Crear base de datos
    
    coleccion = cursor["Alumnos"] # Crear colección

    # Diccionario
    documento = {  # Crear documento
        "Nombre":"Cristina",
        "Apellido":"Silvan",
        "Edad":25
    }     
    coleccion.insert_one(documento)  # Insertar documento en colección


    # Lista de diccionarios
    documentos = [   # Crear muchos documentos
        {
            "Nombre":"Álvaro",
            "Apellido":"Rodriguez",
            "Edad":23
        },

        {
            "Nombre":"Alba",
            "Apellido":"Martín",
            "Edad":24
        },

        {
            "Nombre":"Jorge",
            "Apellido":"Triana",
            "Edad":27
        }
    ]
    coleccion.insert_many(documentos) # Insertar muchos documentos en colección


    conexion.close() # Cerrar conexión

# Errores habituales que vienen predefinidos con el módulo
except errors.ServerSelectionTimeoutError as e:
    print(f"Tiempo de conexión excedido: {e}")
except errors.ConnectionFailure as e:
    print(f"Error al conectarse a mongoDB: {e}")