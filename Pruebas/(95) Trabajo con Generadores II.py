def devuelve_ciudades(*ciudades): # En Python, cuando le ponemos un asterisco al parámetro
    for  elemento in ciudades:    # de las funciones que creamos, le estamos indicando que 
        yield elemento            # le vamos a pasar un número indeterminado de elementos
                                  # y lo tomará como si se tratara de una tupla

ciudades_devueltas = devuelve_ciudades('Madrid', 'Barcelona', 'Bilbao', 'Valencia')

# Para acceder de uno en uno a los elementos
print(next(ciudades_devueltas)) # SALIDA: Madrid

print(next(ciudades_devueltas)) # SALIDA: Barcelona

