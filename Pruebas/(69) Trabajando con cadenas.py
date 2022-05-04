ubicacion = 'Madrid capital de España'
print(ubicacion.upper()) # SALIDA: MADRID CAPITAL DE ESPAÑA (no lo asigna a la variable)
print(ubicacion.lower()) # SALIDA: madrid capital de españa (el contenido original no se modifica)
print(ubicacion) # SALIDA: Madrid capital de España

aes = 'aaaaaaa'
nueva = aes.replace('a', 'b', 3)
print(f"Cadena original: {aes}, Nueva cadena: {nueva}") # SALIDA: Cadena original: aaaaaaa, Nueva cadena: bbbaaaa

print(ubicacion.split(' ')) # SALIDA: ['Madrid', 'capital', 'de', 'España'] 
# (Lo imprime como una lista en la cual cada elemento son las palabra que se separan por el espacio en blanco)

ubicacion = '\t\tHola qué tal\t\t'# '       Hola qué tal        '
print(ubicacion.strip()) # strip() corta la cadena según le indiquemos
# (Si no le pasamos parámetros, elimina los espacios en blanco del principio y del dinal de la cadena)
# SALIDA: Hola qué tal

ubicacion = 'Madrid capital de España'
print(ubicacion.endswith('paña')) # SALIDA: True (responde a la pregunta 'termina de la forma')
print(ubicacion.endswith('Madrid')) # SALIDA: False

print(ubicacion.startswith('Madrid')) # SALIDA: True (responde a la pregunta 'empieza de la forma')
print(ubicacion.startswith('paña')) # SALIDA: False

print(aes.count('a')) # SALIDA: 7 (cuenta las apariciones del caracter o cadena que le especifiquemos)

datos = 'País: {}, Comunidad: {}'
print(datos.format('España', 'Andalucía')) # SALIDA: País: España, Comunidad: Andalucía
# format encuentra las {} y las sustituye por lo que le especifiquemos EN EL MISMO ORDEN

# Forma alternativa de usar el format con variables
datos_pais = 'España'
datos_comunidad = 'Andalucía'
print(datos.format(datos_pais, datos_comunidad)) # SALIDA: País: España, Comunidad: Andalucía

