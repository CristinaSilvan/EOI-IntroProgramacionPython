class Coche():
# La primera letra del identificador en mayúsculas
    
    # Atributos (variables, objetos y colecciones)
    # Propiedades que tendrán los objetos de esta clase (coches)
    longitud_Chasis = 250
    ancho_Chasis = 220
    ruedas = 4
    enmarcha = False # Los coches creados por defecto están parados
    
    # Métodos (funciones que únicamente se puede usar en los objetos de esta clase)
    # Comportamientos que tendrán los objetos de esta clase (coches)
    def arrancar(self):  # Self hace referencia al propio objeto
                         # (Conocido como 'this' en los lenguajes C en los que se puede obviar)
        pass             # 'pass' sirve para que no dé error al estar vacío el método 
                         # (se puede usar cuando vamos a desarrollar algo en el futuro)   


# Objeto
miCoche = Coche() # Instanciar una clase (crear un objeto de esa clase)
# (No es necesario la palabra reservada 'new' como en los lenguajes C)