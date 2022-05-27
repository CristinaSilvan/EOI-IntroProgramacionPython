'''
Utilizando la comprensión de listas, 
construya una lista a partir de los cuadrados de 
cada elemento de la lista.
'''

lst1=[2, 4, 6, 8, 10, 12, 14]
lst2=[(n*n) for n in lst1]

print(f"Lista 1: {lst1}\nLista 2: {lst2}")