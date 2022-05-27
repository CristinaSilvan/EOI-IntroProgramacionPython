# Diccionarios y funciones

notas = {'David': 8, 'Carlos': 6, 'Victor': 9, 'Hector': 7}
print(f"Este es mi diccionario: {notas}")

print(f"\nEste es mi diccionario convertido a cadenas: {notas}")
# str() Convierte el diccionario una cadena
# Visualmente no se aprecia un cambio

print(f"\nMi diccionario es de tipo: {type(notas)}")
# type() Consultar el tipo de elemento

notas2 = notas.copy()
# diccionario.copy() para copiar información entre diccionarios

notas.clear() # No hace falta asignación, ya que esto es una función, no un parseo
print(f"\nMi diccionario tras el clear: {notas}")
# diccionario.clear() para eliminar todos los elementos del diccionario

notas = dict.fromkeys(['David', 'Carlos', 'Victor', 'Hector'], 100) # Si pongo solo un valor, todas las claves tendrán dicho valor
# diccionario.fromkeys(lista,valor) crea un nuevo diccionario, las claves son de lista con valor

print(f"\nEl valor asociado a Victor es: {notas.get('Victor')}")
# diccionario.get(clave)

print(f"\nItems dentro de mi diccionario: {notas.items()}")
# diccionario.items() lista cada uno de los elementos como una lista de tuplas pares

print(f"\nEstas son las keys de mi diccionario: {notas.keys()}")
# diccionario.keys() devuelve una lista con las claves

print(f"\nEstas son los valores de mi diccionario: {notas.values()}")
# diccionario.value() devuelve una lista con los valores

edad_1 = {'Cris':25}
edad_2 = {'Alex':26, 'Laura':21}
edad_1.update(edad_2) # Si existen clave/valor repetidos, elimina una de las tuplas pares
print(f"\nEdades totales {edad_1}")
# diccionario1.update(diccionario2) añade los pares clave/valor del diccionario 2 al 1

print(f"\nLa edad de Cris es: {edad_1.pop('Cris')}")
print(f"Diccionario tras el pop: {edad_1}") # Cris ya no está en el diccionario
# diccionario.pop(clave) para mostrar el valor asignado Y BORRAR LA TUPLA DEL DICCIONARIO
