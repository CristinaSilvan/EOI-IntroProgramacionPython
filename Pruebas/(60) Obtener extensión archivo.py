# Obtiene la extensión de un archivo especificado por el ususario
# (FORMA BÁSICA) No trata errores como dos puntos, extensiones erróneas o sin extensión


nombre_archivo = input("Ingrese el nombre del archivo: ")
# Ej.: main.py

partes = nombre_archivo.split('.') # Partes es una lista que almacenará la cadena antes del '.' y después de él
# print(partes) # ['Main', 'py']

print(f"La extensión del archivo es: {partes[-1]}") 
# Escribiendo el índice -1, nos aseguramos de que siempre sea la última posición independientemente de la cantidad de caracteres en la lista
