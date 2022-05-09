'''
Cree un diccionario de la lista con los mismos pares 
clave:valor, como: {"clave": "clave"}.
'''

lst=["NY", "FL", "CA", "VT"]
dic={x:x for x in lst}

print(dic)