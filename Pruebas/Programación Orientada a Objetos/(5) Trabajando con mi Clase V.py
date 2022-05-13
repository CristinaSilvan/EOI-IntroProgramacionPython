class Coche():
    def __init__(self):
        self.largoChasis = 250
        self.anchoChasis = 120
        self.ruedas = 4
        self.enmarcha = False
        self.gasolina=0
        self.aceite=0
        self.puertas=0

    def arrancar(self,estado):
        self.enmarcha = estado
        if self.enmarcha:
            if self.__chequeoInterno():
                return "El coche está en marcha"
            return "El coche no puede arrancar"
        return "El coche está parardo"    

    def estado(self):
        print(f"\nEl coche tiene {self.largoChasis}x{self.anchoChasis}cm de Chasis, tiene {self.ruedas} ruedas, la gasolina está al {self.gasolina}%, el aceite está al {self.aceite}% y tiene {self.puertas} puertas cerradas\n")
        
    def prepararCoche(self, gasolina, aceite):
        self.gasolina = gasolina
        self.aceite = aceite
        self.puertas = 4
        print("\nLa gasolina y el aceite están ya llenos y las puertas todas cerradas\n")

    def __chequeoInterno(self):
        print("Realizando chequeo interno...")
        if self.gasolina > 25 and self.aceite > 25 and self.puertas == 4:
            return True
        return False

miCoche = Coche()
miCoche.estado()
miCoche.prepararCoche(50,75)
print(miCoche.arrancar(True))
# miCoche.__chequeoInterno() # No es accesible desde fuera de la clase