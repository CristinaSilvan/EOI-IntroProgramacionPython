nombre="Cristina"
print("Longitud de mi nombre: ", len(nombre))

print("Caracter almacenado en cada posicion: ")
print("0 -> ",nombre[0]) # C
print("1 -> ",nombre[1]) # r
print("2 -> ",nombre[2]) # i
print("3 -> ",nombre[3]) # s
print("4 -> ",nombre[4]) # t
print("5 -> ",nombre[5]) # i

print("Hay algun digito en mi nombre: ", nombre.isdigit())

print("Mayusculas: ", nombre.upper())
print("Minuculas: ", nombre.lower())
print("Capitalizado: ", nombre.capitalize())
print("Reverso: ", nombre.swapcase())

print("Muestra los caracteres dentro del rango: ", nombre[0:6]) # La posición 6 no la introduce

print("Imprime el caracter en la posición -2: ", nombre[-2])

nombre = "Cristina"
edad = 24
print("Mi nombre es {} y tengo {}".format(nombre, edad))
