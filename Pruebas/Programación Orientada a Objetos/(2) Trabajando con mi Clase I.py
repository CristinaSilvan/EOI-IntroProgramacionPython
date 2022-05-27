class Coche():

    longitud_Chasis = 250
    ancho_Chasis = 220
    ruedas = 4
    enmarcha = False
    
    def arrancar(self):
        self.enmarcha = True

    def estado(self):
        if self.enmarcha:
            return "El coche está en marcha"
        return "El coche está parado"

    def imprimir_info(self):
        print(f"El coche tiene {self.longitud_Chasis}x{self.ancho_Chasis}cm de Chasis y {self.ruedas} ruedas")

    def quitar_rueda(self):
        if self.ruedas > 0:
            self.ruedas -= 1

miCoche = Coche()

# print(miCoche.longitud_Chasis) # SALIDA: 250
# print(miCoche.ancho_Chasis)    # SALIDA: 220
# print(miCoche.ruedas)          # SALIDA: 4
# print(miCoche.enmarcha)        # SALIDA: False

miCoche.arrancar()
print(miCoche.enmarcha) # SALIDA: True
# El equivalente a hacer miCoche.enmarcha = True

print(miCoche.estado()) # SALIDA: El coche está en marcha

miCoche.imprimir_info() # SALIDA: El coche tiene 250x220cm de Chasis y 4 ruedas