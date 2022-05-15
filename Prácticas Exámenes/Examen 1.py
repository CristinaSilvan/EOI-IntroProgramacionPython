from dis import dis


print("VELOCIDAD")
uni_dis = input("Unidad de distancia (m o km): ").lower()
if uni_dis == 'm' or uni_dis == 'km':
    try:
        distancia = float(input("Distancia recorrida: "))
        uni_tiempo = input("Unidad de tiempo (s o h): ").lower()
        if uni_tiempo == 's' or uni_tiempo == 'h':
            tiempo = float(input("Tiempo empleado: "))
            if(uni_dis == 'm' and uni_tiempo == 's'):
                print(f"Si ha recorrido {distancia}{uni_dis} en {tiempo}{uni_tiempo} su velocidad ha sido {(distancia/tiempo) :.1f}{uni_dis}/{uni_tiempo} ({(distancia/tiempo) * 3.6 :.1f} km/h)")
            elif(uni_dis == 'km' and uni_tiempo == 'h'):
                print(f"Si ha recorrido {distancia}{uni_dis} en {tiempo}{uni_tiempo} su velocidad ha sido {(distancia/tiempo) :.1f}{uni_dis}/{uni_tiempo} ({(distancia/tiempo) / 3.6 :.1f} m/s)")
            else:
                print("La unidad de velocidad debe ser m/s o km/h")
        else:
            print("La unidad de tiempo indicada no es s o h.")
    except ValueError or TypeError:
        print("El dato introducido no es numérico.")
else:
    print("La unidad de distancia que ha indicado no es m o km.")