def thedecimal(i):
    if i - int(i) == 0:
        print(f"El número {int(i)} es entero")
    else:
        print(f"La parte entera es {int(i)} y la parte decimal {i - int(i)}")

try:
    numero = float(input("Ingrese un número decimal o entero: "))
    thedecimal(numero)
except ValueError:
    print("ERROR: el programa no acepta caracteres o números negativos")
# Falla con números negativos