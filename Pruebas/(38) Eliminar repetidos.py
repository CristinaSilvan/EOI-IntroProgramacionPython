lista = [1,2,3,3,4,5,6,6,6,6,7,8,9,9,9]
print(lista)
for i in lista:
    if lista.count(i) > 1:  # Cuenta la cantidad de veces que existe el elemento en la lista
        lista.pop(i)    # Elimina el elemento de la lista
print(lista)
