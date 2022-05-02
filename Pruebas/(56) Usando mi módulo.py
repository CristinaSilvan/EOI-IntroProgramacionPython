from Mi_Módulo import es_par

a = (es_par(2))
print(f"Mi variable a es {a}")

# Dentro de Mi_Módulo, la función es_par
'''
def es_par(n):
    if(n % 2 == 0):
        return "par"
    else:
        return "impar"
'''

# -----------------------------------------------

from Mi_Módulo import ciclo_pares

n = 10
print("Lista de pares del 0 al 10")
for i in ciclo_pares(n):
    print(i, end=' ')

# Dentro de Mi_Módulo, la función ciclo_pares
'''
def ciclo_pares(n):
   return range(0,n+1,2)
'''