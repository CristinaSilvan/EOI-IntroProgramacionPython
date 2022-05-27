# La función determina si un número dado es cercacno a 1000 o a 2000

def cercanía(n):
    return (abs(1000 - n) < 100) or (abs(2000 - n) < 100) 
    # Lo consideramos cercano si está como mucho a 100 cifras de mil o dosmil


n = int(input("Ingrese un número: "))
if(cercanía(n)):
    print(f"{n} es cercano a 1000 o 2000")
else: 
    print(f"{n} no es cercano a 1000 o 2000")