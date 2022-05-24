import requests
r = requests.get('https://pokeapi.co/api/v2/pokemon-form')
print(r.text) # Pokemon_resultado1.json (Respuesta sin parámetros)