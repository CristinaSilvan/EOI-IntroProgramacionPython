print("Ingrese Numero: ")
Num = int(input())
div = 1

while div <= Num:
    if Num % div == 0:
        print(div)

    div = div + 1