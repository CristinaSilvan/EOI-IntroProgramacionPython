def SaludarATodos(*nombres):    # El asterisco indica que puede recibir varios parámetros
    for i in nombres: # Trata el parámetro como una lista a recorrer
        print(f"Hola: {i}")
# Muy útil cuando no sabemos cuántos argumentos vamos a pasarle a la función

def SaludarATodosDiccionario(**nombres):  # El asterisco indica que los trata como a un diccionario
    for i in nombres:
                                # Clave Valor
        print(f"Saludar a todos: {i} {nombres[i]}")

SaludarATodos('Cristina', 'Alba', 'Sara', 'Julia') # Hola: Cristina Hola: Alba Hola: Sara Hola: Julia

SaludarATodosDiccionario(nombre='Cristina', apellido='Silván')
# Saludar a todos: nombre Cristina
# Saludar a todos: apellido Silván

