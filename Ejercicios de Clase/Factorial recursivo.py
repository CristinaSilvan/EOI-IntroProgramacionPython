def Factorial(N):
    if N < 0:
        # Pendiente de implementar ...
        # raise # Para generar una excepción personalizada
        pass
    
    if N == 1 or N == 0:
        return 1
    return N * Factorial(N-1)

while True:
    try:
        n = int(input("Ingrese el número cuyo factorial quiere calcular: "))
        r = Factorial(n)
        print(f"El factorial de {n} es {r}")
        break
    except ValueError: # El TypeError no captura la excepción cuando introducimos un valor no numérico
        print("(ERROR: Ingrese un número natural)\n")
    except:
        print("(ERROR: No se permiten valores negativos)\n")