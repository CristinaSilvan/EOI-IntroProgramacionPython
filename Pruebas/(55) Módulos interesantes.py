# Un módulo (o biblioteca) es una colección de definiciones de 
# variables, funciones y tipos (entre otras cosas) que pueden ser
# importadas para ser usadas desde cualquier programa


# Ventajas
'''
- Las funciones y variables deben ser definidas sólo una vez,
y luego pueden ser reutilizadas en muchos programas sin necesidad
de reescribir el código

- permiten que un programa pueda ser organizado en varias secciones 
lógicas, puestas cada una en un archivo separado

- Hacen más fácil compartir componentes con otros programadores
'''

# Aplicaciones con constantes matemáticas y operaciones
import math

# Para importar únicamente una función del módulo
from math import sqrt   # Así utilizaría únicamente las operaciones con raíces sin importar el resto del módulo

# Para importar únicamente una constante
from math import pi   # Así utilizaría únicamente la constante pi

'''
---------------------------------------------------------------------------------
'''

# Aplicaciones con números aleatorios
import random

# Para importar únicamente una función
from random import choice   # Una función muy famosa que elige entre varios valores de forma aleatoria
a = choice(['cara', 'cruz'])
print(f"Salió {a}") # Juego de cara o cruz de una moneda

from random import randrange
b = randrange(5) # Valores desde 0 a 5
print(f"Salió el número {b}")

'''
---------------------------------------------------------------------------------
'''

# Aplicaciones con fechas
from datetime import date

dia = date(2022,5,2)
print(f"Fecha en que hice este programa {dia}")

año = date(2022,12,31) # Cuándo finaliza el año
fin_de_año = (año - dia).days # Le resto la "fecha actual"
print(f"Días restantes para acabar el año {fin_de_año}") # Días restantes para finalizar el año

'''
---------------------------------------------------------------------------------
'''

# Operaciones con fracciones
from fractions import Fraction
a = Fraction(2,4) # 2/4
b = Fraction(4,8) # 4/8

print(f"Suma de dos fracciones {Fraction(a+b)}")