# Creando un módulo personalizado

# Trabaja temas referidos a la paridad

def es_par(n):  # Devuelve una cadena especificando si n es par o impar
    if(n % 2 == 0):
        return "par"
    else:
        return "impar"

def ciclo_pares(n):  # Devuelve una lista de los números pares de 0 a n
   return range(0,n+1,2)