# Cuando multiplico una cadena por n, lo que hace es imprimirse n veces
# print('Python' * 3)   # PythonPythonPython

# Programa que emula el producto de cadenas
def producto_cadena(cadena, n):
    resultado = ""
    for i in range(n):
        resultado += cadena  # += sirve para concatenar cuando se usa con cadenas

    return resultado

print(producto_cadena('Python', 3))   # PythonPythonPython