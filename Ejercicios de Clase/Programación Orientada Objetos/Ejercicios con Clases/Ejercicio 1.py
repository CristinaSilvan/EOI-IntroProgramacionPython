'''
Se ha definido una clase que representa un inventario de aviones. También se crea una instancia de esta clase Jet y se asigna a la variable first_item.

Imprimir el nombre del primer_elemento.
'''

class Jets:
    def __init__(self, name, country):
        self.name = name
        self.origin = country
    
first_item = Jets("F16", "USA")
a = first_item.name
print(a)