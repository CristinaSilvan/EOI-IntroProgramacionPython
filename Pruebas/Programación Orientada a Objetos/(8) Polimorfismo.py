class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")



def desplazamientoVehiculo(vehiculo): # Este vehiculo cambia de clase según el objeto del parámetro
    vehiculo.desplazamiento()

miVehiculo = Camion()
desplazamientoVehiculo(miVehiculo)