'''
Construir una clase simple desde cero. 
Es la misma que el ejercicio anterior, 
ahora usará la función __ str __ para devolver una representación de cadena para la clase cuando sea necesario.
'''

class Nobel:
    category = ""
    year = 0
    winner = ""

    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner

    def __str__(self):
        return "Category: {} Year: {} Winner: {}".format(self.category, self.year, self.winner)

nq2019=Nobel("Chemistry", 2019, "John B. Goodenough")
print(str(nq2019))