colores = ['Red', 'Yellow', 'Green']
colores_alternativos = ['Magenta', 'Blue', 'Pink']
# Añado a la primera lista, los elementos de la segunda
colores.extend(colores_alternativos) 

# Ordenar una lista de forma ascendente (por defecto)
numeros = ['3', '2', '4', '1']
numeros.sort()
# ['1', '2', '3', '4']

# Ordenar una lista de forma descencente (especificando)
numeros.sort(reverse=True)
# ['4', '3', '2', '1']

