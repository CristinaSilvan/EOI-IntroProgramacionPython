'''
Use la comprensión de listas para construir una nueva lista,
pero agregue 6 a cada elemento.
'''

'''
lst1=[44,54,64,74,104]
lst2 = []
for n in lst1:
    lst2.append(n+6)
'''

lst1=[44,54,64,74,104]
lst2 = [n+6 for n in lst1]

print(f"Lista 1: {lst1}\nLista 2: {lst2}")