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
# Pasamos la información como una cadena a una variable

datosDepartamento = json.dumps(jsonventas) # Serializamos información dentro de la cadena
print("Json de departamentos: {}".format(datosDepartamento))

#print(type(datosDepartamento)) # Los JSON aparecen como tipo String

# ejemplo = json.loads(datosDepartamento)
# print(type(ejemplo)) # Los objetos deserializados se convierten a un tipo de colección que decidirá según el contenido o formato (diccionario, lista, ...)
# print(ejemplo)