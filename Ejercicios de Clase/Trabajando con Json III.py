'''
{
"departamento": 8,
"nombredepto": "Ventas",
"director": "Juan Rodríguez",
"empleados": [
        {
            "nombre": "Pedro",
            "apellido:": "Fernandez"
        },
        {
            "nombre": "Jacinto",
            "apellido": "Benavente"
        }
    ]
}
'''
import json

jsonventas = '{"departamento": 8,"nombredepto": "Ventas","director": "Juan Rodríguez","empleados": [{"nombre": "Pedro","apellido:": "Fernandez"},{"nombre": "Jacinto","apellido": "Benavente"}]}'
# Pasamos la información como una cadena a una variable (debe hacerse con las comillas EXACTAMENTE de esta forma, sino habrá problemas de tipo a la hora de deserializar)

datosDepartamento = json.dumps(jsonventas) # Serializamos información dentro de la cadena
print("Json de departamentos: {}".format(datosDepartamento))

#print(type(datosDepartamento)) # Los JSON aparecen como tipo String

ejemplo = json.loads(datosDepartamento)
# print(type(ejemplo)) # Los objetos deserializados se convierten a un tipo de colección que decidirá según el contenido o formato (diccionario, lista, ...)
# print(ejemplo)

for val in ejemplo:
    print(val, datosDepartamento[val])    

'''
ERROR
'''