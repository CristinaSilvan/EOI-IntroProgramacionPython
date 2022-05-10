#Versión que imprime la lista hasta la posición
# No imprime el 0 ARREGLAR
def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)

while True:
    try:
        n = int(input("Ingrese la posición de Fibonacci que quiera ver: "))
        serie_fibonacci=[]
        for i in range(1,n+1):
            r=Fibonacci(i)
            serie_fibonacci.append(r)
        print(f"La serie Fibonacci es", *serie_fibonacci)
        break
    except ValueError: 
        print("(ERROR: Ingrese un número natural)\n")
    except:
        print("(ERROR: No se permiten valores negativos)\n")

'''
# Versión que imprime únicamente la posición

def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)

while True:
    try:
        n = int(input("Ingrese la posición de Fibonacci que quiera ver: "))
        print(f"La serie Fibonacci en la posición {n} es {Fibonacci(n)}")
        break
    except ValueError: 
        print("(ERROR: Ingrese un número natural)\n")
    except:
        print("(ERROR: No se permiten valores negativos)\n")

'''