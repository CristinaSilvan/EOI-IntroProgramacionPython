#  Ordena de forma ascenciente o descenciente

n = int(input("Escriba un numero: "))
orden = (input("Escriba ascendiente o descendiente: "))
orden = orden.lower() # .lower() .upper()

if orden == "ascendiente":
    i = 1
    while i <= n:
        print(i)
        i = i + 1
elif orden == "descendiente":
    i = n
    while i >= 1 :
        print(i)
        i = i - 1
else:
    print("Lo que ha escrito no es valido")