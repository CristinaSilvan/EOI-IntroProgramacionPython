import json

citricos = ["Limon", "Naranja", "Pomelo", "Lima"]

citricosJSON = json.dumps(citricos) # Serializar un objeto (Hidratar) o convertirlo a tipo JSON
# print(citricosJSON) # ["Limon", "Naranja", "Pomelo", "Lima"]

listacitricos = json.loads(citricosJSON) # Deserializar un objeto (Desidratar) o convertir a otro tipo de colección o variable
# print(listacitricos) # ['Limon', 'Naranja', 'Pomelo', 'Lima']

