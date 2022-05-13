'''
Cree nuevas instancias hasta el sexto elemento siguiendo este orden: F14, SU33, AJS37, Mirage2000, Mig29, A10.

Puede tener en cuenta que los orígenes son:

F14: USA SU33: Russia AJS37: Sweden Mirage2000: France Mig29: USSR A10: USA
'''

class Jets:
    model = None
    country = 0
    def __init__(self, name, country):
        self.name = name
        self.origin = country
      

first_item= Jets("F14","USA")
second_item= Jets("SU33", "Russia")
third_item= Jets("AJS37", "Sweden")
fourth_item= Jets("Mirage2000", "France")
fifth_item= Jets("Mig29", "USSR")
sixth_item= Jets("A10", "USA")
first_army=[first_item.name,second_item.name,third_item.name,fourth_item.name,fifth_item.name,sixth_item.name]
print(first_army)