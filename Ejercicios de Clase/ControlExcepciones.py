'''
num1=100
num2=0
print(num1/num2) 
# El IDE no encuentra error en esta sentencia
# ya que la sintaxis y acceso a variables es correcta,
# por lo tanto no es un error en tiempo de programación
'''

num1=100
num2=0

try: # Intenta la siguiente instrucción y si da error, trátala como excepción
    print(num1/num2) # Es decir, salta a la excepción correspondiente
except ZeroDivisionError:
    print("Error al dividir por cero")
    # ZeroDivisionError es una excepción previamente especificada únicamente para este caso
except:
    print("Error") # Si el error se produce por otro problema distinto, ejecutaría esta sentencia
else: # En caso de que no ocurra dichos errores
    print("La división se calculó correctamente")
finally:
    print("Se ejecuta el resto del script donde no existen posibles incidencias")


