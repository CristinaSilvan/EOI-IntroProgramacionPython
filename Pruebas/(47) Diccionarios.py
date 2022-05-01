# Diccionario: 
'''
Son estructuras de datos consistentes en listas de pares
de variables. Cada par tiene un elemento llamado clave (key)
que puede ser de cualquier tipo y otro elemento llamado
valor que también puede ser de cualquier tipo
'''

edades = {'Cristina':24, 'Verónica':49, 'Alejandra':26}
# Clave : Valor

print(f"Esta es la información de los compañeros: {edades}\n")
# Mostrar diccionario

print(f"Estas son solo las edades: {edades['Cristina']}, {edades['Verónica']}, {edades['Alejandra']}\n")
# Mostrar solo valores

edades['Cristina'] = 25
print(f"Esta es la nueva edad de Cristina: {edades['Cristina']}\n")
# Modificar valores

for i in edades:
    print(i, edades[i])
# Recorrer diccionario