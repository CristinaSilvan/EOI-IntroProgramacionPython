#  Calcula la cantidad de vocales en una frase

frase = str(input("Escriba una frase: "))
vocales =  "aeiouAEIOU"
contador = 0

for i in frase:
    if i in vocales:  #Si i es igual a alguno de los caracteres dentro de la variable vocales
        contador = contador + 1
print("El numero de vocales es ", contador)
