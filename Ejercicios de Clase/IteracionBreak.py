contador = 0
for numero in range(1,21,2):
    contador+=1
    if(contador>5):
        break # Finaliza el bucle 
              # (Salta a la línea después del bucle for si la hubiera)
              # (De lo contrario acabaría la ejecución del programa)
    print(numero)