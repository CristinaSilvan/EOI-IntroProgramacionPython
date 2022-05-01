# Convertir una tupla a una lista
tupla1 = (4,6,9,3,6,19) # Al ser las tuplas inmutables, necesito pasarlas a lista a veces
print(f"Esto es una tupla: {tupla1}")
lista1 = list(tupla1) # Forma de parsearla
print(f"Esto es una lista: {lista1}")

print("\n") # Salto de línea

# Convertir una lista a una tupla
lista2 = [1,2,3,5,7]
print(f"Esto es una lista: {lista2}")
tupla2 = tuple(lista2)
print(f"Esto es una tupla: {tupla2}")

print("\n")

# Longitud
print(f"La longitud de {tupla1} es {len(tupla1)}")
print(f"La longitud de {lista2} es {len(lista2)}")

print("\n")

# Máximo y mínimo
print(f"El mayor valor en {tupla2} es {max(tupla2)}")
print(f"El menor valor en {lista1} es {min(lista1)}")
