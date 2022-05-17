from genericpath import exists


try:
    fichero = "C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Colecciones Ficheros II\\Datos_2 (A).txt"
    archivo = open(fichero, "rt", encoding='UTF-8')
    cadena = archivo.read()
    cadena = cadena.strip()
    cadena = cadena.strip('[')
    cadena = cadena.strip(']')
    lista = [int(x) for x in cadena.split(',')]
except Exception as e:
    print(f"Error: {e}")
finally:
    if archivo != None: #En caso de no abrirse, se rompería al tratar de cerrarlo por lo que hay que controlar ese bug
    # (Esta es una opción, la otra es comprobando que existe con fichero.exists)    
        archivo.close()


fichero = "C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Colecciones Ficheros II\\Datos_2 (B).txt"
archivo = open(fichero, "wt", encoding='UTF-8')

archivo.write("RESULTADOS DEL EJERCICIO 2:\n\nLista generada: {}".format(str(lista)))

lista.sort()
for i in lista:
    if i >= 18:
        archivo.write(f"Hay {len(lista[lista.index(i):])} personas mayores de edad\n")
        break
archivo.write(f"La persona más joven tiene {min(lista)} años y la más mayor {max(lista)} años\n\n")

for i in lista:
    archivo.write(f"El porcentaje de personas con {i} años es de {round(((lista.count(i))),2)}%\n")
    for j in range(lista.index(i),len(lista)-1):
        if j == i:
            lista.pop(j)

archivo.close()