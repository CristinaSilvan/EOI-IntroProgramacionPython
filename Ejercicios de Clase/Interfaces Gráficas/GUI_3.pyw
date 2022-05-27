from tkinter import *

root = Tk()
root.title("Ventana de Prueba")
root.config(bg="azure")
root.iconbitmap("C:\\1-Python\\Ejercicios de Clase\\Interfaces Gráficas\\assets\\icon.ico")
root.resizable(0,0)

my_frame = Frame(root, width=500, height=400)
my_frame.pack()

cuadroTexto = Entry(my_frame) # Para introducir texto
cuadroTexto.place(x=150,y=10)

nombreLabel = Label(my_frame, text="Nombre:")
nombreLabel.place(x=150,y=10) # Si se utiliza las mismas cordenadas, el primer widget empuja al segundo
''' No es recomendable porque pueden superponerse y demás'''

root.mainloop()