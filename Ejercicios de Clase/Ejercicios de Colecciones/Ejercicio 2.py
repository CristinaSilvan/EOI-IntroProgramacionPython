'''
Hacer un programa que procese las edades de 100 personas. 
Deberá decir cuantas tienen más de (≥18) y cuál es la persona con menor edad 
y cuál es la persona con mayor edad. También deberá mostrar el porcentaje de edades de las 100 personas.
'''

from random import randint

lista = []
for i in range(0,100):
    lista.append(randint(1, 120))

lista.sort()
for i in lista:
    if i >= 18:
        print(f"Hay {len(lista[lista.index(i):])} personas mayores de edad")
        break
print(f"La persona más joven tiene {min(lista)} años y la más mayor {max(lista)} años\n")

for i in lista:
    print(f"El porcentaje de personas con {i} años es de {round(((lista.count(i))),2)}%")
    for j in range(lista.index(i),len(lista)-1):
        if j == i:
            lista.pop(j)

'''
# Versión antigua

from random import randint

lista = []
for i in range(0,100):
    lista.append(randint(1,115))

#print(lista)
mayores_edad = 0
for i in lista:
    if i >= 18:
        mayores_edad += 1
por1 = 0.00
por2 = 0.00
por3 = 0.00
por4 = 0.00
por5 = 0.00
por6 = 0.00
for i in lista:
    if i < 18:
        por1+=1
    elif i < 35:
        por2+=1
    elif i < 50:
        por3+=1
    elif i < 75:
        por4+=1
    elif i < 90:
        por5+=1
    else:
        por6+=1
print("Total de edades: {}\n".format(lista))
print("Hay {} personas mayores de edad".format(mayores_edad))
print("La persona más joven tiene {} años".format(min(lista)))
print("La persona más mayor tiene {} años".format(max(lista)))
print("""Porcentajes de edad: \n\tDe 1 a 18 años: {}%\n\tDe 18 a 35 años: {}%\n\tDe 35 a 50 años: {}%\n\tDe 50 a 75 años: {}%\n\tDe 75 a 90 años: {}%\n\tDe 90 a 115 años: {}%"""
.format((round((por1*100)/115)),(round((por2*100)/115)),(round((por3*100)/115)),(round((por4*100)/115)),(round((por5*100)/115)),(round((por6*100)/115))))
'''