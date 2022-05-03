# Conversión de los algoritmos de tablas de Fundamentos de Programación a lenguaje Python
# (Este script tiene mejoras de los algoritmos, por lo que no son exactamente iguales)

import math

Interruptor = True
while(Interruptor):
    ejercicio = input("Qué ejercicio quieres ver: ")
    if (ejercicio.isdigit() and (int(ejercicio) in range(1,13))):
        Interruptor = False
        ejercicio = int(ejercicio)
        if(ejercicio == 1):
            # 1. Hola Mundo
            print("Hola Mundo")


        elif(ejercicio == 2):
            # 2. A partir de un número ingresado diga si es mayor, menor o igual a 9
            '''
            N = 0
            N = int(input("Escribir el numero ")) # Si el usuario introduce por error un caracter, fallaría el programa
            if N == 9:
                print("El numero es igual a 9")
            else:
                if N > 9:
                    print("El numero es mayor a 9")
                else:
                    print("El numero es menor a 9")
            '''
            
            # 2. Versión más eficiente
            print("Escribe el número: ")
            N = input() # De esta forma no daría error si se introduce un valor alfanumérico
            if(N.isdigit()): # Pregunta si el valor es numérico
                N = int(N) # Convierte N a entero (ya que input asigna el valor como string)
                if N == 9:
                    print("El numero es igual a 9")
                else:
                    if N > 9:
                        print("El numero es mayor a 9")
                    else:
                        print("El numero es menor a 9")
            else:
                print("Por favor, introduzca un valor numérico")


        elif (ejercicio == 3):
            # 3. A partir de un número ingresado diga si el mismo es par o impar
            nro = input("Ingrese un número: ")
            if (nro.isdigit()):
                nro = int(nro)
                if (nro % 2 == 0):
                    print("Es par")
                else:
                    print("No es par")
            else:
                print("Por favor, introduzca un valor numérico")


        elif (ejercicio == 4):
            Num1=input("Escribir el numero 1:")
            Num2=input("Escribir el numero 2:")
            if(Num1.isdigit() and Num2.isdigit()): # De lo contrario, al utilizar + concatenaría
                print(f"El resultado es {int(Num1)+int(Num2)}")
            else:
                print("Por favor, introduzca un valores numéricos")
        
        
        elif (ejercicio == 5):
            # 5. Sumar todos los números pares entre 2 y 100
            '''
            suma = 0
            nro = 2
            while(nro <= 100):
                if(n % 2 == 0):
                    suma += nro
                nro += 1
            print(f"La suma de todos los pares entre 2 y 100 es {suma}")
            '''
            
            # 5. Versión más eficiente (1)
            '''
            suma = 0
            nro = 2
            while(nro <= 100):
                suma += nro
                nro += 2
            print(f"La suma de todos los pares entre 2 y 100 es {suma}")
            '''
            
            # 5. Versión más eficiente (2)
            suma = 0
            for i in range(2, 102, 2):
                suma += i
            print(f"La suma de todos los pares entre 2 y 100 es {suma}")
        
        
        elif(ejercicio == 6):
            # 6. Ingrese un número y muestre todos los divisores del mismo
            print("Ingrese un número entero:")
            Num = input()
            if(Num.isdigit()):
                Num = int(Num)
                div = 1
                while(div<=Num):
                    if(Num % div == 0):
                        print(div, end='')
                    div += 1
            else:
                print("Por favor, introduzca un valor numérico")


        elif(ejercicio == 7):
            #7. Determinar si un alumno aprueba o suspende un curso, sabiendo que aprobará si su promedio de tres calificaciones es mayor o igual a 4.0; supsende en caso contrario. Deberá permitir ingresar las tres calificaciones y luego calcular su promedio
            # SOLO FUNCIONA CON ENTEROS
            Cal1 = input("Ingrese calificación 1:")
            Cal2 = input("Ingrese calificación 2:")
            Cal3 = input("Ingrese calificación 3:")

            if(Cal1.isdigit() and Cal2.isdigit() and Cal3.isdigit()):
                # Validación
                Cal1 = int(Cal1)
                Cal2 = int(Cal2)
                Cal3 = int(Cal3)
                # if((Ca1 >= 0 and Cal1 <= 10) and (Ca2 >= 0 and Cal2 <= 10) and (Ca3 >= 0 and Cal3 <= 10))
                if((Cal1 in range(0,11)) and (Cal2 in range(0,11)) and (Cal3 in range(0,11))):
                    Prom = ((Cal1+Cal2+Cal3)//3) # La // es una división entera
                    if(Prom >= 5):
                        print("Aprueba")
                    else:
                        print("Suspende")
                    print(f"Nota media: {Prom}")
                else:
                    print("Por favor, introduzca un valores enteros del 0 al 10")
            else:
                print("Por favor, introduzca un valores numéricos enteros")

            # Versión que funciona con decimales
            '''
            cal1=input("Ingrese calificacion 1: ")
            cal2=input("Ingrese calificacion 2: ")
            cal3=input("Ingrese calificacion 3: ")
            try: #Con el try nos evitamos comprobar .isdigit()
                cal1=float(cal1)
                cal2=float(cal2)
                cal3=float(cal3)
                if((Ca1 >= 0 and Cal1 <= 10) and (Ca2 >= 0 and Cal2 <= 10) and (Ca3 >= 0 and Cal3 <= 10))
                    prom=(cal1+cal2+cal3)/3
                    if (prom>=4):
                        print(f"El alumno aprueba el curso. Su media es de {prom}")
                    else:
                        print(f"El alumno suspende el curso. Su media es de {prom}")
                else:
                    print("Por favor, introduzca un valores del 0 al 10")
            except ValueError:
                print("Ingrese unas calificaciones numericas")    
            '''
        
        
        elif (ejercicio == 8):
            # 8. Crear un algoritmo que permita ingresar un nombre y una cantidad numérica para escribir este nombre tantas veces como su cantidad ingresada
            nombre = input("Ingresar nombre: ")
            if(not nombre.isdigit()): # Si el usuario introduce números en vez de un nombre
                num = input("Ingresar cantidad: ")
                try:
                    num = int(num)
                    '''
                    while(num > 0):
                        print(nombre)
                        num -= 1            # Num = Num -1
                    '''
                    for i in range(0, num):
                        print(nombre)
                except ValueError:
                    print("Por favor, escriba un valor numérico en la segunda entrada")
            else: 
                print("Escriba un valor alfabético en la primera entrada") 
            
            # 8. Versión alternativa más corta
            '''
            nombre = input("Ingresar nombre: ")
            num = input("Ingresar cantidad: ")
            try:
                print((nombre+"\n")*int(Num))
            except ValueError:
                print("Por favor, escriba un valor numérico en la segunda entrada")
            '''
        
        
        elif (ejercicio == 9):
            # 9. Sumar todos los números naturales comprendidos entre 1 y 50
            Num = 1
            Resul = 0
            for Num in range(1, 50):
                Resul += Num
                Num += 1
            print(Resul)

        elif (ejercicio == 10):
            #10. Leer tres números; si el primero es negativo, debe imprimir la multiplicación de los tres y si no lo es, imprimirá la suma
            Num1 = int(input("Ingrese numero 1"))
            Num2 = int(input("Ingrese numero 2"))
            Num3 = int(input("Ingrese numero 3"))

            if Num1 < 0:
                Resul = Num1 * Num2 * Num3
            else:
                Resul = Num1 + Num2 + Num3

            print(Resul)

        elif (ejercicio == 11):
            # 11. Determina si un número ingresado es primo o no. (Un número es primo si es divisible únicamente por 1 y por sí mismo)
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
        
            '''
            # Alternativa programa que imprime los 'numerodePrimos' primeros números primos

            numerodePrimos = input("Número de primos a mostrar: ")
            if(numerodePrimos.isdigit()):
                nro = 1
                while numerodePrimos > 0:
                    div = 2
                    band = True
                    if nro == 1:
                        print(f"{nro} es primo")
                        numerodePrimos -= 1
                    else:
                        while band and (nro > div):
                            if nro % div == 0:
                                band = False
                                break
                            div += 1
                        if band:
                            print(f"{nro} es primo")
                            numerodePrimos -= 1
                    nro += 1
            else:
                print("Por favor, ingrese un número válido")
            '''
        
        elif (ejercicio == 12):
            # 12. Sumar los dígitos de un número ingresado. Ejemplo: Si se ingresa 123, debería devolver 6
            nro = input("Ingrese un número: ")
            try:
                nro = int(nro)
                resul = 0
                while nro != 0:
                    resul = resul + nro % 10
                    nro = math.trunc(nro / 10) # nro = nro//10
                print("El resultado es ", resul)
            except:
                print("Ingrese un número válido")
    else:
        print("Ingresa un número del 1 al 12")