from tkinter import *

root = Tk()
root.title("Prueba")
root.config(bg="azure")
root.iconbitmap("C:\\1-Python\\Ejercicios de Clase\\Interfaces Gráficas\\assets\\icon.ico")
root.resizable(0,0)

my_frame = Frame(root, width=500, height=400)
my_frame.pack()



cuadroNombre = Entry(my_frame)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="blue", justify="right")

cuadroApellido = Entry(my_frame)
cuadroApellido.grid(row=1, column=1, padx=10, pady=10)
cuadroApellido.config(fg="red", justify="right")

cuadroEdad = Entry(my_frame)
cuadroEdad.grid(row=2, column=1, padx=10, pady=10)
cuadroEdad.config(fg="green", justify="right")

cuadroPass = Entry(my_frame)
cuadroPass.grid(row=3, column=1, padx=10, pady=10)
cuadroPass.config(justify="center", show="*")



nombreLabel = Label(my_frame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

apellidoLabel = Label(my_frame, text="Apellido:")
apellidoLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

edadLabel = Label(my_frame, text="Edad:")
edadLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

passLabel = Label(my_frame, text="Password:")
passLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)



root.mainloop()