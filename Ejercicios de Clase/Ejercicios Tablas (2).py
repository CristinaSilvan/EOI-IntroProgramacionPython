# Conversión de los algoritmos de tablas de Fundamentos de Programación a lenguaje Python
# (Ejercicios propuestos)

import math


Interruptor = True
while(Interruptor):
    ejercicio = input("Qué ejercicio quieres ver: ")
    if (ejercicio.isdigit() and (int(ejercicio) in range(1,13))):
        Interruptor = False
        ejercicio = int(ejercicio)
        
        if(ejercicio == 1):
        # I. Calcular y mostrar el cuadrado de los números del 1 a 30
            for numero in range(1,31):
                print(f"El cuadrado de {numero} es {numero*numero}")

        elif(ejercicio == 2):
        # II. Números primos
            nro = input("Ingrese un número: ")
            try:
                nro = int(nro)  # Parsear la entrada de input previamente string a integer
                div = 2
                band = True    # Boolean para comprobar si es primo o no
                if nro == 1:
                    print("Es primo")
                else:
                    while (band == True) and (nro > div):
                        if nro % div == 0:
                            band = False
                            break   # Al ser band == False, ya no necesitamos seguir iterando el bucle
                        div += 1
                    if band == True:
                        print("Es primo")
                    else:
                        print("No es primo")
            except ValueError:
                print("Por favor, escriba un valor numérico entero")
        
        elif(ejercicio == 3):
        # III. Construir un avión de papel
            print("Paso 1 - Conseguir Hoja de Papel")
            print("Paso 2 - Doblar el papel a la mitad")
            print("Paso 3 - Doblar la esquina al centro izquierda")
            print("Paso 4 - Doblar la esquina al centro derecha")
            print("Paso 5 - Con el papel doblado, volver a doblar la esquina al centro izquierda")
            print("Paso 6 - Doblar hacia abajo para formar alas en ambos lados")
            print("Paso 7 - Comprobar los pasos anteriores")
            print("Paso 8 - (Opcional) Probar que vuela")

        elif (ejercicio == 4):
        # IV. Realizar las cuatro Opes básicas (Suma, Resta, Multiplicación, División)
            Op = input("Ingrese operación: ")
            try:
                if('+' in Op):
                    Op = Op.split('+')
                    print(f"El resultado es {float(Op[0]) + float(Op[1])}")
                elif('-' in Op):
                    Op = Op.split('-')
                    print(f"El resultado es {float(Op[0]) - float(Op[1])}")
                elif('/' in Op):
                    Op = Op.split('/')
                    try:
                        print(f"El resultado es {float(Op[0]) / float(Op[1])}")
                    except ZeroDivisionError:
                        print("Error, división entre 0")
                elif('*' in Op):
                    Op = Op.split('*')
                    print(f"El resultado es {float(Op[0]) * float(Op[1])}")
            except ValueError:
                print("Por favor, escriba un valor numérico válido")
        
        elif(ejercicio == 5):
        # V. Volumen y Area de un Cilindro
            try:
                h = float(input("Altura"))
                r = float(input("Radio: "))

                V = math.pi * h * (r*r)
                print(f"Volumen del cilindro: {V}")
                    
                A = (2 * math.pi * r * h) + (2 * math.pi * (r*r)) # Se puede importar únicamente la constante mediante from math import pi
                print(f"Área del cilindro: {A}")                  # (De esta forma, podríamos usar pi directamente sin tener que escribir math.pi)
            except ValueError:
                print("Ingrese valores numéricos válidos")
    
        elif(ejercicio == 6):
        # VI. Pedir un libro en una biblioteca
            nombre = input("Usuario: ")
            id = input("ID: ")
            titulo = input("Título del libro: ")
            idlibro = input("Identificador libro: ")
            print("Permiso aceptado")
            print("Fecha de devolución")
            print("Introducir información en la base de datos")

        elif(ejercicio == 7):
        # VII. Encontrar el mayor de tres números
            Num1 = input("Ingrese primer numero:")
            Num2 = input("Ingrese segundo numero:")
            Num3 = input("Ingrese tercer numero:")

            print("El mayor valor es: ", end='')
            if Num1 > Num2:
                if Num1 > Num3:
                    print(Num1)
                else:
                    print(Num2)
            else:
                if Num2 > Num3:
                    print(Num2)
                else:
                    print(Num3)

        elif(ejercicio == 8):
        # VIII. Factorial de cualquier numero
            try:
                nro = int(input("Ingrese un número: "))
                m = 2
                resul = 0

                print("El factorial es: ", end='')
                if nro == 1:
                    print(nro)
                else:
                    while m <= nro:
                        resul *= m
                        m += 1
                    print(resul)
            except:
                print("Introduzca un número entero válido")
            # Los errores personalizados deben ir primero y los no personalizados después debido a la prioridad de las excepciones
            # (Consultar lista de excepciones para saber la prioridad)
    
        elif(ejercicio == 9):
        # IX. Encontrar si un numero es mayor o menor a uno dado
                try:    
                    Num1 = float(input("Ingrese primer numero: "))
                    Num1 = float(input("Ingrese segundo numero: "))

                    if Num1 > Num2:
                        print(f"{Num1} es mayor")
                    else:
                        print(f"{Num2} es mayor")
                except:
                    print("Ingrese un valor numérico válido")

        elif(ejercicio == 10):
        # X. Adivinar una palabra
            palabra1 = "suerte"

            print("Adivine la palabra: ", end='')
            while True:
                palabra2 = input()
                palabra2 = palabra2.lower()
                if palabra2 == palabra1:
                    break
                print("Vuelve a intentarlo: ", end='')
            print("Felicidades, has adivinado la palabra")
    
    else:
        print("Ingresa un número del 1 al 10")