from datetime import datetime

datenow1 = datetime.now().date()
print(f"La fecha actual: {datenow1}")

datenow2 = datetime.now()
print(f"La fecha y hora actuales: {datenow2}") # Incluye los microsegundos

print(f"Año: {datenow1.year}")
print(f"Mes: {datenow1.month}")
print(f"Día: {datenow1.day}")
# print(f"Hora: {datenow1.hour}") No está disponible porque la variable solo es de fecha
print(f"Hora: {datenow2.hour}:{datenow2.minute}") # Si está disponible porque la variable también es de hora
print(f"Segundos: {datenow2.second}")
print(f"Microsegundos: {datenow2.microsecond}")
