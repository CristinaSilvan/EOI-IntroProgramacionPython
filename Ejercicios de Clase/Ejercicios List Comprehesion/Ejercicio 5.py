'''
Utilizando la comprensión de listas, 
construya una lista a partir de los cuadrados de cada 
elemento de la lista, si el cuadrado es mayor que 50.
'''

lst1=[2, 4, 6, 8, 10, 12, 14]
lst2 = [(x*x) for x in lst1 if (x*x > 50)]

print(f"Lista 1: {lst1}\nLista 2: {lst2}")