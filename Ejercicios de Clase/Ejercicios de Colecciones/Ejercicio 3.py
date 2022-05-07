'''
Hacer un programa que procese un total de 100 personas y establecer cuantas son mujeres 
mayores de edad y cuantos hombres menores de edad. Deberá sacar el hombre y la mujer con menor edad, 
el hombre y la mujer con mayor edad, promedio de edades de las mujeres y promedio de edades de los hombres.
'''
from random import randint
from random import choice

def calculo_lista(lista, genero):
    lista.sort()
    promedio = 0
    if genero == 'M':
        for i in lista:
            if i >= 18:
                print(f"Hay {len(lista[lista.index(i):])} mujeres mayores de edad")
                break
        print(f"La mujer más joven tiene {min(lista)} años y la más mayor {max(lista)} años\n")
        for i in lista:
            promedio += i
        print("El promedio de edad de las mujeres es de {} años".format(promedio/100))
    else:
        for i in lista:
            if i < 18:
                print(f"Hay {len(lista[lista.index(i):])} hombres menores de edad")
                break
        print(f"El hombre más joven tiene {min(lista)} años y el más mayor {max(lista)} años\n")
        for i in lista:
            promedio += i
        print("El promedio de edad de los hombres es de {} años".format(promedio/100))


total = {}
total['M'] = []
total['H'] = []

for i in range(0,100):
    total[choice('MH')].append(randint(1,120))

calculo_lista(total.get('M'), 'M')
print('\n')
calculo_lista(total.get('H'), 'H')

#print(total)
print(f"Hay un total de {len(total.get('M'))} mujeres")
print(f"Hay un total de {len(total.get('H'))} hombres")


'''
# Versión Antigua

from audioop import add
from random import randint
from random import choice

# Creando dos listas aleatorias de géneros y edades
generos = ['M', 'H']
lista1 = [] # Lista mujeres y hombres
lista2 = [] # Lista edades
for i in range (0,100):
    lista1.append(choice(generos))
    lista2.append(randint(1,115))

# Creando variables auxiliares
mujeres = 0
hombres = 0
muj_mayores = 0
hom_menores = 0
muj_prom = 0
hom_prom = 0
# Calculando mujeres mayores de edad, hombres menores de edad, cantidad de personas del género
for i in range(0,100):
    if lista1[i] == 'M':
        mujeres += 1
        if lista2[i] >= 18:
            muj_mayores += 1
        muj_prom += lista2[i]
    elif lista1[i] == 'H':
        hombres += 1
        if lista2[i] < 18:
            hom_menores += 1
        hom_prom += lista2[i]

# Calculando el promedio
muj_prom /= mujeres
hom_prom /= hombres

# Creando variables auxiliares
muj_peq = 120
hom_peq = 120
muj_may = 0
hom_may = 0
# Calculando la persona más joven y más mayor de cada género
for i in range(0,100):
    if lista1[i] == 'M':
        if lista2[i] < muj_peq:
            muj_peq = lista2[i]
        if lista2[i] > muj_may:
            muj_may = lista2[i]
    else:
        if lista2[i] < hom_peq:
            hom_peq = lista2[i]
        if lista2[i] > hom_may:
            hom_may = lista2[i]

print("Mujeres mayores de edad: {}".format(muj_mayores))
print("Hombres menores de edad: {}".format(hom_menores))

print("\nLa mujer más joven tiene {} años y la más mayor {}".format(muj_peq, muj_may))
print("El hombre más joven tiene {} años y el más mayor {}".format(hom_peq, hom_may))

print("\nEdad promedio de mujeres: {}".format(int(muj_prom)))
print("Edad promedio de hombres: {}".format(int(hom_prom)))

# Para ver la lista
respuesta = input("\n¿Quiere ver la lista completa?: ").lower()
if respuesta == 'si' or respuesta == 's' or respuesta == 'yes' or respuesta == 'sí' or respuesta == 'y':
    print("El total de personas: ")
    for i in range(0,100):
        if lista1[i] == 'M':
            print('Mujer de {} años'.format(lista2[i]))
        else:
            print('Hombre de {} años'.format(lista2[i]))
'''