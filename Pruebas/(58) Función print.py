# Ejemplos útiles de utilización de la función print

print("Este es un ejemplo básico") # La cadena es el argumento que le pasamos a la función
# Automáticamente, por defecto, print realiza un salto de línea al terminar


print("\n") # Si solo pongo print() también se realizará un salto de línea


print("Este es un ejemplo más.", end=' ') # Para cambiar ese salto de línea por otra cosa a nuestra preferencia
print("Este es un ejemplo más.", end=' ') # Ejemplo, un espacio en blanco para que se escriban una a continuación de la otra


print() # Si solo pongo print() también se realizará un salto de línea
print()


print("Python", "es", "tremendo!") # Concatenar las cadenas con , o + (separador por defecto: el espacio)
print("Python", "es", "tremendo!", sep='-') # Concatenarlas mediante un separador elegido


print("\n")


# El format es más eficiente ya que solo concatena,
# mientras que las otras formas de imprimir, crean una cadena aparte con el valor concatenado resultante
print("{} es {}".format('Python', 'tremendo!'))
# Las llaves se conocen como "place holder"


print("\n")

# Forma de imprimir conjuntos de datos
lista = [2,3,4,5]
print(f"Esto es una lista {lista}")

tupla = (2,3,4,5)
print(f"Esto es una tupla {tupla}")

conjunto = {'España', 'Perú', 'México'}
print(f"Esto es un set {conjunto}")

diccionario = {'Cristina':25, 'Vicky':22, 'Jesús':21}
print(f"Esto es un diccionario {diccionario}")

array = [1,2,3]
print(f"Esto es un array {array}")

matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(f"Esto es una matriz {matriz}")
