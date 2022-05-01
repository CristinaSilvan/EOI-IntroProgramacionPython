# Palabras reservadas del & in

curso = 'pythonm'
lista = list(curso)
del lista[len(curso)-1] # del para borrar un elemento de una lista

print(f"La palabra Python perfectamente escrita:\n {lista}\n")

print(f"¿Se encuentra la 'y' dentro de la lista? \n {'y' in curso}\n")
# in para consultar si un elemento se encuentra en un conjunto (Devuelve True o False)


# Ejemplo de uso del in
if 'y' in lista:
    print("\nEl elemento 'y' es parte de la lista")
else:
    print("\nEl elemento 'y' no es parte de la lista")

if 'a' in lista:
    print("\nEl elemento 'a' es parte de la lista")
else:
    print("\nEl elemento 'a' no es parte de la lista")

print("\n")