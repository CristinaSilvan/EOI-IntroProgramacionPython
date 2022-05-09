'''
Cree un rango de 100 a 160 con paso 10. 
Utilizando la comprensión de listas, cree un diccionario en
el que cada número del rango sea la clave y cada elemento 
dividido por 100 sea el valor.
'''

rng=range(100,160+1,10)
dict={x:(x/100) for x in rng}

print(dict)