from random import randint
print("JUEGO DE DADOS")
try:
    veces = int(input("¿Cuántas veces se va a tirar el dado? "))
    if veces < 1:
        print("¡No se puede tirar menos de una vez el dado!")
    else:
        total = 0
        cubitus = 0
        humerus = 0
        resul = 0
        for i in range(0, veces+1):
            resul = randint(1,6)
            if resul % 2 == 0:
                cubitus += 1
            else:
                humerus += 1
            resul = 0
        
except ValueError or TypeError:
    print("Un valor numérico debe ser introducido")