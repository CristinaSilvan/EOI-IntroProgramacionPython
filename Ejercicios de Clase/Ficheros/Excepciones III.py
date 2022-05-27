def fichero_existe(file):
    try:
        open(file)
    except FileNotFoundError:
        return False
    return True

# Existe una función oficial en Python que realiza esta misma
# comprobación from os.path import exists y está mucho más depurada

try:
    file = ("./Ejercicios de Clase/Ficheros/Fichero_excepciones.txt")
    if fichero_existe(file):
        fichero = open(file, 'rt', encoding='UTF-8')
        print(fichero.read())
    else:
        fichero = open(file, 'wt', encoding='UTF-8')
        fichero.write("Esta es la primera línea")
except Exception as e:
    print("ERROR: {}".format(e))
finally:
    fichero.close()