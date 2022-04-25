# Separa una lista en dos (pares e impares)

lista = [1,2,3,4,5,6,7,8,9]

def separar_lista(lista):
    lista.sort()
    pares = []  # Declaración lista vacía
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares

pares, impares = separar_lista(lista)  # Para devolver los resultados a una variable
                                                                 # externa a la función definida

print(pares)
print(impares)
