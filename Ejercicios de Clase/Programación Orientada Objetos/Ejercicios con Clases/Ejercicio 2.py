'''
Ahora imprima el origen del primer_elemento.
'''
class Jets:
    model = None
    country = 0

    def __init__(self, name, country):
        self.name = name
        self.origin = country
        
first_item = Jets("F16", "USA")
b=first_item.origin
print(b)