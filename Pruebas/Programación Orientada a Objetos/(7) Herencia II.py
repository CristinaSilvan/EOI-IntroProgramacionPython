# Superclase de las que heredarán otras clases
# ----------------------------------------------------------------------------------------------------  
class Persona():
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):
        print(f"\nNombre: {self.nombre}\nEdad: {self.edad}\nResidencia: {self.residencia}")

# Clase heredada
# ----------------------------------------------------------------------------------------------------  
class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre, edad, residencia):
        super().__init__(nombre, edad, residencia) # Para añadir el constructor de Persona
        self.salario = salario
        self.antiguedad = antiguedad
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):
        super().descripcion()
        print(f"Salario: {self.salario}\nAntiguedad: {self.antiguedad}")

# Código de mi programa
# ----------------------------------------------------------------------------------------------------  

print("Esto es una persona:")
Antonio=Persona("Antonio", 55, "España")
Antonio.descripcion()

print("\n--------------\n")

print("Esto es un empleado:")
Manuel=Empleado(1500, 15, "Manuel", 55, "Colombia")
Manuel.descripcion()

print("\n--------------\n")

print(f"¿Es Manuel una instancia de Persona? {isinstance(Manuel, Persona)}") # isinstance nos devuelve True o False
print(f"¿Es Manuel una instancia de Empleado? {isinstance(Manuel, Empleado)}") # Tiene en cuenta la herencia

print("\n")