'''
Usando la comprensión de listas y un argumento condicional, 
cree un diccionario a partir del diccionario actual donde 
solo los pares clave:valor con un valor superior a 2000 se 
toman en el nuevo diccionario.
'''
dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
#dict2={x:dict1.get(x) for x in dict1 if dict1.get(x) > 2000}
dict2={x:dict1[x] for x in dict1 if dict1[x] > 2000}
print(dict2)