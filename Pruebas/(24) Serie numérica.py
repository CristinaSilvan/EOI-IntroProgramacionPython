# Serie numérica
# 4, 3, 2, 1, 4, 3, 2, 1, ....


n = int(input("Ingrese un numero: "))
controlador = 0
interruptor = 4
while controlador < n:
    print(interruptor, end=', ')
    if interruptor > 1:
        interruptor = interruptor - 1
    else:
        interruptor = 4
    controlador = controlador + 1
