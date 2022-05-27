# Creamos una lista a partir de una entrada del usuario separada por comas

entrada = input("Ingrese números separados por comas: ")

# print(entrada)          # Para comprobar lo que se ha guardado en la variable
# print(type(entrada))     # Para comprobar el tipo de dato con el que ha guardado la información


entrada = entrada.split(',') # Convierte la cadena a una lista eliminando los elementos ','
print(entrada) # Imprime la lista sin comas ['1', '2', '3']
# En este paso, el tipo de dato sigue siendo string y podría incluir espacios si el usuario los ingresa

entrada = [int(item) for item in entrada] # Convertidos los datos a numéricos y eliminados posibles caracteres como espacios
print(entrada) # [1, 2, 3]


# De lo contrario consideraría las comas como elementos de la lista
'''
entrada = list(entrada)
print(entrada)  # ['1', ',', '2', ',', '3']
'''