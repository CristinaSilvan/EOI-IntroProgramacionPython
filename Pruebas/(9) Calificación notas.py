# Diferencia las diferentes notas y las cataloga

n = float(input("Ingrese la nota: "))

if n < 5:
    print("Suspenso")
elif n < 8:
    print("Aprobado")
elif n < 10:
    print("Sobresaliente")
else:
    print("Excelente")