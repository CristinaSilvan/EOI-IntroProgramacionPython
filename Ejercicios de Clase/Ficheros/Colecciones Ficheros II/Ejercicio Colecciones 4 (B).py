file = "C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Colecciones Ficheros II\\Datos_4 (A).txt"
archivo = open(file, "rt", encoding='UTF-8')

contenido = archivo.read()
dicc = eval(contenido)
archivo.close()

file = "C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Colecciones Ficheros II\\Datos_4 (B).txt"
archivo = open(file, "wt", encoding='UTF-8')

archivo.write("RESULTADOS DEL EJERCICIO 4:\n\n")

archivo.write("="*100+'\n')

DiccPromedioAnual={} 
for clave,valor in dicc.items():
    archivo.write(f'{clave} -> {valor} \t')
    tuplatemperaturas = tuple(valor)
    MediaAnuales = round(sum(tuplatemperaturas)/12 ,2)
    DiccPromedioAnual[clave] = MediaAnuales
MaxProAnual = max(DiccPromedioAnual.values())
MinProAnual = min(DiccPromedioAnual.values())
 
archivo.write(f'La ciudad con el promedio anual mas ALTO 1 es {list(DiccPromedioAnual.keys())[list(DiccPromedioAnual.values()).index(MaxProAnual)]} con un promedio de: {MaxProAnual} ºC')
archivo.write(f'\nLa ciudad con el promedio anual mas ALTO 2 es {max(DiccPromedioAnual,key=DiccPromedioAnual.get)} con un promedio de: {MaxProAnual} ºC')
 
archivo.write(f'\n\nLa ciudad con el promedio anual mas BAJO 1 es {list(DiccPromedioAnual.keys())[list(DiccPromedioAnual.values()).index(MinProAnual)]} con un promedio de: {MinProAnual} ºC') 
archivo.write(f'\nLa ciudad con el promedio anual mas BAJO 2 es {min(DiccPromedioAnual,key=DiccPromedioAnual.get)} con un promedio de: {MinProAnual} ºC\n')
ListaPromedioAnual = list(DiccPromedioAnual.items())
ListaPromedioAnual.sort(key = lambda x: x[1], reverse=True)
archivo.write("="*100+'\n')
archivo.write(f'\n\nLa lista de las ciudades ordenadas es :\n{ListaPromedioAnual}\n\n')
ListaPromedioAnual1 = sorted(DiccPromedioAnual,key=DiccPromedioAnual.get,reverse=True)

archivo.write("="*100+'\n\n')

for i in ListaPromedioAnual1:
    archivo.write(i + " = ")
    archivo.write(str(DiccPromedioAnual[i]) + "ºC\n")

archivo.close()