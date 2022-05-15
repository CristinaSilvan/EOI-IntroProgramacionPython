from random import randint

fichero = "C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Ejericicio_2.txt"
archivo = open(fichero, "w", encoding='UTF-8')

lista = []
for i in range(0,100):
    lista.append(randint(1, 120))

archivo.write("Ejercicio 2\n\n")
archivo.write("Lista generada de edades: {}\n".format(lista))
lista.sort()
archivo.write("Lista ordenada: {}\n".format(lista))
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
