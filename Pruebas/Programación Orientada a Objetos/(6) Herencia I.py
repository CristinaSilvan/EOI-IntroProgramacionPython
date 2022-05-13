# Superclase de las que heredarán otras clases
# ----------------------------------------------------------------------------------------------------  
class Vehiculos:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(f"\nMarca: {self.marca}\nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nFrenando: {self.frena}")

# Superclase de las que heredarán otras clases
# ----------------------------------------------------------------------------------------------------  
class Electricos():
    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

# Clase heredada
# ----------------------------------------------------------------------------------------------------  
class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="¡¡Voy haciendo el caballito!!"

    # Sobreescribiendo el método de la clase padre
    def estado(self):
        print(f"\nMarca: {self.marca}\nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nFrenando: {self.frena}\n{self.hcaballito}")

# Clase heredada
# ----------------------------------------------------------------------------------------------------  
class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado=cargar
        if self.cargado:
            return "La furgoneta está cargada"
        return "La furgoneta no está cargada"

# Clase heredada
# ----------------------------------------------------------------------------------------------------  
class Quad(Moto):
    pass # Hereda el método 'estado' de la clase 'Moto' así que puede hacer el caballito


# Clase heredada
# ----------------------------------------------------------------------------------------------------  
class BiciElectrica(Vehiculos, Electricos): # Hereda de dos clases con prioridad (Herencia múltiple)
    pass

# Código de mi programa
# ----------------------------------------------------------------------------------------------------  
miMoto=Moto("Hona", "CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")
miFurgoneta.estado()
print(miFurgoneta.carga(True))

miBici=BiciElectrica("Orbea", "HC1030") # Hereda el constructor de Vehículos que es la primera clase de la que hereda
miBici.estado()