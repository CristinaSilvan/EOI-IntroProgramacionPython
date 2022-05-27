from tkinter import *  # Documentación: https://docs.python.org/3/library/tk.html

'''
 Extensión .pyw para ejecutar sin consola en vez de .py
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
# (El tamaño de la raíz se ajusta automáticamente al de su contenido)
raiz.geometry("650x550")

# Cambiar color de fondo
raiz.config(bg="azure")

'''
=======================================================
'''

# Crear objeto frame
miframe = Frame()

# Introducir frame en raíz
#miframe.pack()
miframe.pack(side="left", anchor="n")

# Rellenar la raíz
#miframe.pack(fill="x") -> Horizontalmente
#miframe.pack(fill="y", expand="True") -> Verticalmente
#miframe.pack(fill="both") -> Rellenar siempre la raíz

# Darle tamaño para que sea visible
# (Por defecto su tamaño es fijo, por lo que no se adapta a la manipulación de la raíz)
miframe.config(width="550", height="450")

# Cambiar color de fondo
miframe.config(bg="white")

# Cambiar el borde
miframe.config(bd=10)
miframe.config(relief="groove")

# Cambiar el cursor cuando pasa por el frame
miframe.config(cursor="hand2")

'''
=======================================================
'''

# Mantener el programa en loop a la espera de eventos 
# (esta sentencia siempre al final del programa)
raiz.mainloop()