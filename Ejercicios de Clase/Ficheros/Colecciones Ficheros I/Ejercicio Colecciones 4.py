from random import randint

fichero = "C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Colecciones ficheros I\\Ejericicio_4.txt"
archivo = open(fichero, "wt", encoding='UTF-8')

ListaCiudades = ['Malaga','Alava','Albacete','Alicante','Almería','Asturias','Avila','Badajoz','Barcelona','Burgos','Cáceres','Cádiz','Cantabria','Castellón','Ceuta','Ciudad Real','Córdoba','Cuenca','Formentera','Girona']
dicc = {}

archivo.write("La lista de ciudades con sus temperaturas:\n")
for ciudad in ListaCiudades:
    listatemperaturas = []
    for i in range(0,12): 
        temperaturas = randint(0,50)
        listatemperaturas.append(temperaturas)
    dicc[ciudad] = listatemperaturas
DiccPromedioAnual={} 
for clave,valor in dicc.items():
    archivo.write(f'{clave} -> {valor} \t')
    tuplatemperaturas = tuple(valor)
    MediaAnuales = round(sum(tuplatemperaturas)/12 ,2)
    DiccPromedioAnual[clave] = MediaAnuales
MaxProAnual = max(DiccPromedioAnual.values())
MinProAnual = min(DiccPromedioAnual.values())
 
archivo.write(f'\n\nLa ciudad con el promedio anual mas ALTO 1 es {list(DiccPromedioAnual.keys())[list(DiccPromedioAnual.values()).index(MaxProAnual)]} con un promedio de: {MaxProAnual} ºC')
archivo.write(f'\nLa ciudad con el promedio anual mas ALTO 2 es {max(DiccPromedioAnual,key=DiccPromedioAnual.get)} con un promedio de: {MaxProAnual} ºC')
 
archivo.write(f'\n\nLa ciudad con el promedio anual mas BAJO 1 es {list(DiccPromedioAnual.keys())[list(DiccPromedioAnual.values()).index(MinProAnual)]} con un promedio de: {MinProAnual} ºC') 
archivo.write(f'\nLa ciudad con el promedio anual mas BAJO 2 es {min(DiccPromedioAnual,key=DiccPromedioAnual.get)} con un promedio de: {MinProAnual} ºC')
ListaPromedioAnual = list(DiccPromedioAnual.items())
ListaPromedioAnual.sort(key = lambda x: x[1], reverse=True)
archivo.write(f'\n\nLa lista de las ciudades ordenadas es (1) :\n{ListaPromedioAnual}\n\n')
ListaPromedioAnual1 = sorted(DiccPromedioAnual,key=DiccPromedioAnual.get,reverse=True)

for i in ListaPromedioAnual1:
    archivo.write(i + " = ")
    archivo.write(str(DiccPromedioAnual[i]) + "\n")