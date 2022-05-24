import requests
import json

def get_pokemon(url,offset=0):
    param = {'offset':offset}
    r = requests(url, params=param)
    if r.status_code == 200:
        resultado = r.json()
        lista_pokemon = resultado.get('results',[])

        if lista_pokemon:
            for pokemon in lista_pokemon:
                name = pokemon['name']
                print(name)
        continuar = input