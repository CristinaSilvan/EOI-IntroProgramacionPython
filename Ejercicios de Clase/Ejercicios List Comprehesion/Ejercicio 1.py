'''
Cree una lista idéntica a partir de la primera lista 
utilizando la comprensión de listas.
'''

lista1 = [1,2,3,4,5]
lista2 = []
# for i in lista1:
#    lista2.append(i)
lista2 = [i for i in lista1] # List Comprehesion
print(f"Lista 1: {lista1}\nLista 2: {lista2}")