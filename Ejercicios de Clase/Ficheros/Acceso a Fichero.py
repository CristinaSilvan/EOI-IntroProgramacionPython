try:
    #fichero = open("C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Fichero.txt", "rt") # Hay que escapar las barras para que las detecte dentro de la cadena
        #,encoding='UTF-8' es un tercer parámetro opcional que se usa para interpretar los caracteres
    fichero = open("C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Fichero_1.txt", "rt",encoding='UTF-8')
    # Hay que especificar la ruta porque la terminal de Studio Code no se encuentra dónde el fichero (en la consola de Windows no hace falta)
    print("Este es el type del fichero ", type(fichero))
    contenido = fichero.read()
    print("He leído el fichero y este es su contenido: \n\t", contenido)
    # Si no se pone el enconding, no aparecerían correctamente los caracteres de otros idiomas
except FileNotFoundError as e:
    print(f"{e}")
except Exception as e:
    print(f"{e}")
finally:
    fichero.close() # Esta línea da error si no se accede al fichero 
    # porque no se puede cerrar algo que no ha abierto
    print("Cerrando el programa...")

    # Importante cerrar el fichero con close() al terminar