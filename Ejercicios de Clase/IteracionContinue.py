# range(1,21,2) -> 1 3 5 7 9 11 13 15 17 19

# Este programa sirve para NO IMPRIMIR los números menores o igual que 5
contador = 0
for numero in range(1,21,2):
    contador+=1
    if(contador<5):
        continue # Salta directamente a la siguiente iteración sin leer las instrucciones bajo este
    print(numero) # 9 11 13 15 17 19

# Este programa sirve para NO IMPRIMIR los 5 primeros dígitos de la lista
contador = 0
for numero in range(1,21,2):
    contador+=1
    if(contador<=5):
        continue  
    print(numero) # 11 13 15 17 19