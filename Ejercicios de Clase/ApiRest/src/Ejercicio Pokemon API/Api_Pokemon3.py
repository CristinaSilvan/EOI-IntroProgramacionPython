import requests

try:
    offset = int(input("¿A partir de qué id quieres ver la pokédex? "))
    url = 'https://pokeapi.co/api/v2/pokemon-form'
    params = {'offset': offset}
    r = requests.get(url, params)
except Exception as e:
    print(f"Introduzca un id válido: {e}")

fichero = './Ejercicios de Clase/ApiRest/src/Ejercicio Pokemon API/Pokemon_resultado3.json'
resultado = open(fichero, 'w') # Pokemon_resultado3.json (A partir del id 50)
resultado.write(r.text)