cadena = "Curso de Python"
print(cadena)

# lower convierte todos los caracteres a minúsculas
print(cadena.lower())   # SALIDA: "curso de python"

# upper convierte todos los caracteres a mayúsculas
print(cadena.upper())   # SALIDA: "CURSO DE PYTHON"

# swapcase convierte los caracteres de mayúsculas a minúsculas y viceversa
cadena = "CuRsO dE pYtHoN"
print(cadena)
print(cadena.swapcase())    # SALIDA: "cUrSo De PyThOn"

# count cuenta la cantidad de elementos en la cadena
cadena = "Curso de Python"
print(cadena.count('P'))    # SALIDA: "1"

# replace reemplaza un elemento por otro
print(cadena.replace("Python", "Programacion"))     # SALIDA: "Curso de programación"

# capitalize convierte el primer caracter en mayúsculas y el resto en minúsculas
cadena = "cuRso De pythOn"
print(cadena.capitalize())      # SALIDA: "Curso de python"

# find enumera los caracteres antes de la selección encontrada
cadena = "Curso de Python"
print(cadena.find("de"))        # SALIDA: "6"
