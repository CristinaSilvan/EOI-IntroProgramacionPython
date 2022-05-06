class Coche():

    # Constructor de la clase
    def __init__(self, largo, ancho, ruedas, estado): # Va a dar valores iniciales customizados a los atributos
        self.largoChasis = largo
        self.anchoChasis = ancho
        self.ruedas = ruedas
        self.enmarcha = estado

    def arrancar(self, arrancamos):
        self.enmarcha = arrancamos
        if self.enmarcha:
            print("El coche está en marcha")
            return
        print("El coche está parado")
        return

    def imprimir_info(self):
        print(f"El coche tiene {self.largoChasis}x{self.anchoChasis}cm de Chasis y {self.ruedas} ruedas")

    def quitar_rueda(self):
        if self.ruedas > 0:
            self.ruedas -= 1

# miCoche = Coche()
# miCoche.arrancar(False) # El coche está parado
# miCoche.arrancar(True) # El coche está en marcha

miCoche = Coche(250,120,3,True)
miCoche.imprimir_info()

