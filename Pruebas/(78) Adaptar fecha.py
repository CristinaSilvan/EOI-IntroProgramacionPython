'''
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y 
muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione 
cuando el día o el mes se introduzcan con un solo carácter.
'''

import locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

fecha = input("Introduzca su fecha de nacimiento en el formato dd/mm/aaaa: ")
fecha = datetime.strptime(fecha, '%d/%m/%Y').date()
#print(fecha)
cadena = str(fecha.strftime("%A %d %b %Y")).capitalize()
print(cadena)

'''
# Alternativa (sin datetime)
fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)
fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)
'''