'''
Agregue otro atributo llamado "cantidad" al método de inicialización (generalmente denominado constructor o init).

Luego defina "asignar" este atributo al atributo self.quantity dentro del constructor.

Luego cree 2 instancias para: F14 y Mirage2000 con cantidades 87 y 35.
'''

class Jets:
    model = None
    country = 0
    quantity = 0
    def __init__(self, name, country, quantity):
        self.name = name
        self.origin = country
        self.quantity = quantity

    def __str__(self):
        return "{} {} {}".format(self.name,self.country,self.quantity)

#Escriba su respuesta aquí.        
first_item= Jets("F14", "USA", "87")
second_item= Jets("Mirage2000", "France", "35")
total= [str(first_item), str(second_item)] # Si no especificamos que queremos que se muestre como un str, se imprimirá el objeto como tal
print("Lista: ", total) # Otra opción para imprimir sin tener que hacer str(), ya que el print lo resuelve como cadena concatenándolo
print(total)