# Clase
class Persona:
    # Declaración/Iniciación de atributos (variables/colecciones que solo los objetos de esta clase tienen)
    # Pueden ser declaradas con valores por defecto en caso de que sea necesario
    Nombres=""
    Apellidos=""

    # Métodos de la clase (funciones que solo los objetos de esta clase puede usar)

    #def __init__(self, nombres, apellidos):  # Contructor de la clase
    #   self.Nombres = nombre
    #   self.Apellidos = apellidos

    def caminar(self): # Si hago print de una función que ya hace print, me saldrá None
        print("caminando...")
        

# Código aparte de la clase (Cógido principal)
profesor = Persona() # Objeto instanciado o creado
profesor.Nombres = "Billy"
profesor.Apellidos = "Vanegas"


alumno = Persona()
alumno.Nombres = "Pedro"
alumno.Apellidos = "Sanchez"

administrativo = Persona()
administrativo.Nombres = "Oscar"
administrativo.Apellidos = "León"

print("El profesor: {} {}".format(profesor.Nombres, profesor.Apellidos))
print("El alumno: {} {}".format(alumno.Nombres, alumno.Apellidos))
print("El administrativo: {} {}".format(administrativo.Nombres, administrativo.Apellidos))

print("{} está ".format(profesor.Nombres), end='')
profesor.caminar()