from tkinter import *

#CREACIÓN DE RAÍZ Y FRAME BÁSICOS
root = Tk()
root.title("Prueba")
root.iconbitmap("C:\\1-Python\\Ejercicios de Clase\\Interfaces Gráficas\\assets\\icon.ico")
root.resizable(0,0)

my_frame = Frame(root, width=500, height=400)
my_frame.pack()

nombre = StringVar()
apellido = StringVar()
edad = StringVar()

'''
==============================================================
'''
# CUADROS

cuadroNombre = Entry(my_frame, textvariable=nombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="blue", justify="right")

cuadroApellido = Entry(my_frame, textvariable=apellido)
cuadroApellido.grid(row=1, column=1, padx=10, pady=10)
cuadroApellido.config(fg="red", justify="right")

cuadroEdad = Entry(my_frame, textvariable=edad)
cuadroEdad.grid(row=2, column=1, padx=10, pady=10)
cuadroEdad.config(fg="green", justify="right")

cuadroPass = Entry(my_frame)
cuadroPass.grid(row=3, column=1, padx=10, pady=10)
cuadroPass.config(justify="center", show="*")


'''
==============================================================
'''
# LABELS

nombreLabel = Label(my_frame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

apellidoLabel = Label(my_frame, text="Apellido:")
apellidoLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

edadLabel = Label(my_frame, text="Edad:")
edadLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

passLabel = Label(my_frame, text="Password:")
passLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)


'''
==============================================================
'''

# TEXTO

# Por defecto los text son enormes y pueden agrandarse según el texto que se introduzca
texto_comentario = Text(my_frame, width=16, height=5) 
texto_comentario.grid(row=4, column=1, padx=10, pady=10)

comentarios = Label(my_frame, text="Comentarios: ")
passLabel.grid(row=4, column=0, sticky="w", padx=10, pady=10)


'''
==============================================================
'''
# BARRA DE SCROLL

barraVertical = Scrollbar(my_frame, command=texto_comentario.yview)
barraVertical.grid(row=4, column=2, sticky="nsew")
texto_comentario.config(yscrollcommand=barraVertical.set)


'''
==============================================================
'''
# BOTONES 

def codigoBoton():
    nombre.set("Cristina")
    apellido.set("Silvan")
    edad.set("25")


botonRellenar = Button(root, text="Autorellenar", command=codigoBoton)
botonRellenar.pack()


'''
==============================================================
'''

root.mainloop()