class Coche():
    def __init__(self, largo, ancho, ruedas, estado):
        self.__largoChasis = largo  # Atributos encapsulados o privados
        self.__anchoChasis = ancho
        self.__ruedas = ruedas
        self.__enmarcha = estado

    def imprimir_info(self):
        print(f"El coche tiene {self.__largoChasis}x{self.__anchoChasis}cm de Chasis y {self.__ruedas} ruedas")
        
# miCoche.ruedas = 5 # NO FUNCIONARÍA PORQUE ES UN ATRIBUTO PRIVADO, solo se podría acceder a un atributo privado
# si existe un método público (no encapsulado) que lo permita
miCoche = Coche(250,120,3,True)
miCoche.imprimir_info() # SALIDA: El coche tiene 250x120cm de Chasis y 3 ruedas