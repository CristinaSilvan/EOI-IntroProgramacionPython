'''
def generarPares (limite): 
    num = 1                
    lista = []
    while num < limite:
        lista.append(num*2)
        num += 1
    return lista
'''

def generarPares (limite): 
    num = 1
    while num < limite:
        yield num*2
        num += 1


pares = generarPares(10)
for i in pares:
    print(i)

mis_pares = generarPares(100)

print(next(mis_pares))

print("Aquí podría haber más código...")

print(next(mis_pares))

print("Aquí podría haber más código...")

print(next(mis_pares))