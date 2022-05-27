#Índices y trabajos con ellos
curso = 'python'
print(f"Cadena original: {curso}",end='\n')

# Índices positivos
print("\nAccediento a la cadena mediante Índices positivos:")
print(curso[0],end='')
print(curso[1],end='')
print(curso[2],end='')
print(curso[3],end='')
print(curso[4],end='')
print(curso[5],end='\n')

# Índices negativos
print("\nAccediento a la cadena mediante Índices negativos:")
print(curso[-6],end='')
print(curso[-5],end='')
print(curso[-4],end='')
print(curso[-3],end='')
print(curso[-2],end='')
print(curso[-1],end='\n')

# Índices con rangos
cadena = 'constitucionalmente'
print(f"\nAccediendo con rangos: {cadena[0:len(cadena)]}")
del(cadena)

# Transformar cadena como lista o tupla
cadena = 'aeiou'
vocales = list(cadena) # tuple() para convertir a tupla
print(f"\nCadena '{cadena}' convertida a lista: {vocales}")

print(f"\nLa vocal 'i' se encuentra en la posición {vocales.index('i')}")