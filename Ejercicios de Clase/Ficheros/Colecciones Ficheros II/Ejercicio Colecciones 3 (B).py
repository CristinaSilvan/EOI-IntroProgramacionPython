fichero1 = "C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Colecciones Ficheros II\\Datos_3 (Mujeres).txt"
fichero2 = "C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Colecciones Ficheros II\\Datos_3 (Hombres).txt"
archivo1 = open(fichero1, "rt", encoding='UTF-8')
archivo2 = open(fichero2, "rt", encoding='UTF-8')

def devolver_lista(cadena):
    cadena = cadena.strip()
    cadena = cadena.strip('[')
    cadena = cadena.strip(']')
    return [int(x) for x in cadena.split(',')]

mujeres = devolver_lista(archivo1.read())
hombres = devolver_lista(archivo2.read())
archivo1.close()
archivo2.close()

mujeres.sort()
hombres.sort()

fichero = "C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Colecciones Ficheros II\\Datos_3 (B).txt"
archivo = open(fichero, "wt", encoding='UTF-8')

def calculo_lista(lista, genero):
    promedio = 0
    if genero == 'M':
        for i in lista:
            if i >= 18:
                archivo.write(f"Hay {len(lista[i:])} mujeres mayores de edad\n")
                break
        archivo.write(f"La mujer más joven tiene {min(lista)} años y la más mayor {max(lista)} años\n")
        for i in lista:
            promedio += i
        archivo.write("El promedio de edad de las mujeres es de {} años\n".format(promedio/100))
    else:
        for i in lista:
            if i < 18:
                archivo.write(f"Hay {len(lista[i:])} hombres menores de edad\n")
                break
        archivo.write(f"El hombre más joven tiene {min(lista)} años y el más mayor {max(lista)} años\n")
        for i in lista:
            promedio += i
        archivo.write("El promedio de edad de los hombres es de {} años\n".format(promedio/100))


archivo.write("RESULTADOS DEL EJERCICIO 3:\n\n")
archivo.write("="*100+'\n')
archivo.write("Total de personas: {}\n".format(len(mujeres) + len(hombres)))
archivo.write("="*100+'\n')
archivo.write("\nMujeres: {}".format(mujeres))
archivo.write("\nHombres: {}\n\n".format(hombres))
archivo.write("="*100+'\n')

calculo_lista(mujeres, 'M')
archivo.write("="*100+'\n')
calculo_lista(hombres, 'H')
archivo.write("="*100+'\n')
archivo.write(f"\nHay un total de {len(mujeres)} mujeres")
archivo.write(f"\nHay un total de {len(hombres)} hombres")
