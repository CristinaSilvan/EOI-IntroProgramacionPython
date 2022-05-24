import requests
# import json
params= {'offset':40, 'limit':20} # No funciona si serializamos
url = 'https://pokeapi.co/api/v2/pokemon-form'
r = requests.get(url, params=params)
# https://pokeapi.co/api/v2/pokemon-form?offset=40&limit=20

print(r.text) # Pokemon_resultado2.json (Respuesta con parámetros)