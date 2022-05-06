
'''
# Para acceder a los subelementos de la forma básica
# (al ser cadena, acceder a cada caracter)
def devuelve_ciudades(*ciudades): 
    for  elemento in ciudades:  
        for subElemento in elemento:
            yield subElemento            
'''

# Para acceder a los subelementos con yield from para ahorrar bucles anidados
# (al ser cadena, acceder a cada caracter)
def devuelve_ciudades(*ciudades): 
    for elemento in ciudades:  
        yield from elemento        


ciudades_devueltas = devuelve_ciudades('Madrid', 'Barcelona', 'Bilbao', 'Valencia')

print(next(ciudades_devueltas)) # SALIDA: M

print(next(ciudades_devueltas)) # SALIDA: a

print(next(ciudades_devueltas)) # SALIDA: d

print(next(ciudades_devueltas)) # SALIDA: r

