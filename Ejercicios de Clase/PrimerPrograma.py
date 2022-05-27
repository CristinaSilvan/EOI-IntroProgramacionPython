# Este es un primer programa en Python
# Esto es un comentario
'''
Esto es un bloque 
de comentario
'''

text1 = "Este texto se asigna en una linea"

text2 = """Escribir valores alfanumericos
        en varias lineas"""

# Declaración de variables
numero = 10
Numero = 20
saludo = "Hola, mundo"
print(numero)
print(Numero)
print(numero+Numero) # 30
# Se suman las dos variables
print("Saludos "+saludo) # Saludos Hola, mundo
# Se concatenan las dos cadenas

'''
El operador '+'
funciona de una forma u otra según el tipo de dato
de la variable con la que se utiliza
Ej.
String o char -> concatena
Int, float -> suma
'''

# Mostrar el tipo de dato de las variables
print(type(numero))
print(type(saludo))

# Eliminamos una variable 
# (realmente borra el identificador y el puntero, 
# pero el valor sigue estando almacenado)

del numero
print(numero) # Da un error ya que esa variable ha sido eliminada

