# Suma los primeros n números (Sumatorio)

n = int(input("Ingrese un numero: "))
suma = 0
# También podría ser range (1, n+1)  ya que si no se especifica c, por defecto incrementa 1
for i in range (n, 0, -1):
    suma = suma + i
print("La suma de los primeros ", n, " numeros es ", suma)
