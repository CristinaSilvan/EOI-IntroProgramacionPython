from datetime import datetime

# Parseando una fecha
# Recibe un texto y lo convierte en una variable de tipo Datetime

fecha1 = "26-04-2022"
obj = datetime.strptime(fecha1, '%d-%m-%Y').date()

# %d-%m-%Y es el formato en el que queremos que se guarde
# Al estar en formato americano, los años aparacen primero independientemente de lo que pongamos
# (Lo modificaremos más adelante)
# %d día | %m mes | %Y año (Consultar tabla formato en apuntes)

print(obj) 
# Si en la asignación de obj, hubiese puesto now().date()
# saldría también la hora, minutos y segundos al imprimir
# Aunque no lo especifiquemos en el formato

# Una forma de escribir el formato occidental:
print(f"{obj.day}/{obj.month}/{obj.year}")

# Otra forma de escribir el formato occidental:
fecha2 = datetime.now()
print(fecha2.strftime("%A %d %b %Y")) # Tuesday 26 Apr 2022
