dias=('Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom')

# Imprime los días de la semana
for dia in dias:
    print(dia)

# Imprime los días de la semana enumerados
for dia_numero in enumerate(dias,1):
    print(dia_numero)

# letras=('a', 'b', 'c', 'd', 'e', 'fghijklmnñopqrstuvwxyz')
letras='abcdefghijklmnñopqrstuvwxyz'

# Crea una tupla a raíz de la cadena letras con cada caracter
# como un elemento de la tupla
letrasDelAlfabeto = tuple(x for x in letras)

# Imprime las letras del abecedario (cadena)
for letra in letras:
    print(letra)

# Imprime las letras del abecedario enumeradas (tupla)
for letra in enumerate(letrasDelAlfabeto, 1):
    print(letra)

# Empaquetando los valores de variables en una tupla
gato1 = 'Naranja'
gato2 = 'Persa'
gato3 = 'Calvo'
gatos_tupla = (gato1, gato2, gato3)
# packing

# Desempaquetando los valores de la tupla
# (metiendo cada elemento de la tupla en una variable)
postres_tupla = ('tiramisú', 'flan', 'pudin')
postre1, postre2, postre3 = postres_tupla
# unpaking
