from tkinter import *

'''
 Extensión .pyw para ejecutar sin consola
'''

# Crear objeto tkinter
raiz = Tk()

# Agregar un título
raiz.title("Ventana de Prueba")

# Hacer que el tamaño de la ventana no se pueda ajustar
#raiz.resizable(0,0)

# Agregar icono
raiz.iconbitmap("C:\\1-PythonEOI\\Ejercicios de Clase\\Interfaces Gráficas\\assets\\icon.ico")

# Ajustar tamaño por defecto
raiz.geometry("550x450")

# Cambiar color de fondo
raiz.config(bg="azure")

'''
=======================================================
'''

# Crear objeto frame
miframe = Frame()

# Introducir frame en raíz
miframe.pack()

'''
=======================================================
'''

# Mantener el programa en loop a la espera de eventos 
# (esta sentencia siempre al final del programa)
raiz.mainloop()