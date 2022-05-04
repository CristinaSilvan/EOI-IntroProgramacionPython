'''
Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre 
por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con 
todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
'''

nombre = input('Nombre y apellidos: ')
print(f"Su nombre en minúculas: {nombre.lower()}")
print(f"Su nombre en mayúsculas: {nombre.upper()}")
#nombre1, apellido1, apellido2 = nombre.split(' ')
#print(f"Su nombre en capitalizado: {str(nombre1.capitalize())} {str(apellido1.capitalize())} {str(apellido2.capitalize())}")
print(nombre.title())