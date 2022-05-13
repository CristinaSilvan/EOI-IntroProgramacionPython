# Clase
class Persona:
    Nombres="" # Python no es fuertemente tipado, por lo que podríamos introducir cualquier tipo de valor al margen del string
    Apellidos=""

    # Métodos de la clase (funciones que solo los objetos de esta clase puede usar)

    # Podemos prescindir de crear los atributos de arriba si en el constructor las estamos creando
    def __init__(self, nombres, apellidos):
        self.Nombres = nombres
        self.Apellidos = apellidos

    def caminar(self):
        print("caminando...")

# Python no es un lenguaje riguroso, por lo que no es necesario el uso de get y set
# Ejemplo de implementación de get y set (en otros lenguajes como Java o C, es necesario el uso de estos)
    # Métodos get
    def get_nombres(self):
        return self.Nombres

    def get_apellidos(self):
        return self.Apellidos

    # Métodos set
    def set_nombres(self, nuevo_nombre):
        self.Nombres = nuevo_nombre

    def set_apellidos(self, nuevo_apellidos):
        self.Apellidos = nuevo_apellidos

    # Redefiniendo funciones predefinidas
    def __str__(self):
        return "{} {}".format(self.Nombres, self.Apellidos)


# Código aparte de la clase (Cógido principal)
profesor = Persona("Billy", "Vanegas") # Equivalente a set
alumno = Persona("Pedro", "Sanchez")
administrativo = Persona("Oscar", "León")


print("El profesor: {} {}".format(profesor.Nombres, profesor.Apellidos)) # Equivalente a get
print("El alumno: {} {}".format(alumno.Nombres, alumno.Apellidos))
print("El administrativo: {} {}".format(administrativo.Nombres, administrativo.Apellidos))

print("\nProfesor con __str__:", profesor) # Llama al método __str__