# Forma estandar de crear una función y de utilizarla
def saludar (nombre):
    print(f"Hola, {nombre}!")

saludar('Pedro') # SALIDA: Hola, Pedro!


# Forma alternativa de crear una función, siendo esta
# de pocas líneas y sin necesidad de identificador 'saludar'
# al contrario que la anterior

saludarLambda = lambda nombre:print(f"Hola, {nombre}!")
saludarLambda('Pedro') # SALIDA: Hola, Pedro!