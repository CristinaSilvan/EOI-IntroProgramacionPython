from datetime import datetime

# Crea un objeto de la clase datetime parseando una cadena
fecha1 = '10-11-2022'
obj1 = datetime.strptime(fecha1, '%m-%d-%Y').date()
print(obj1)

fecha2 = '10 11 2022'
obj2 = datetime.strptime(fecha2, '%m %d %Y').date()
print(obj2)

fecha2 = '10/11/2022'
obj2 = datetime.strptime(fecha2, '%m/%d/%Y').date()
print(obj2)
print(f"{obj2.day}-{obj2.month}-{obj2.year}") # Para imprimirlo exactamente a mi gusto

# Da formato a la salida de una forma más estética y a nuestra elección
fecha = datetime.now()
print(fecha.strftime("%A %d %b %Y"))
