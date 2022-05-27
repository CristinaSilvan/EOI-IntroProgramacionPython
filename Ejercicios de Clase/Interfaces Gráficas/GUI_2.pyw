from tkinter import *

from numpy import place

root = Tk()
root.title("Ventana de Prueba")
root.config(bg="azure")
root.iconbitmap("C:\\1-Python\\Ejercicios de Clase\\Interfaces Gráficas\\assets\\icon.ico")
root.resizable(0,0)

my_frame = Frame(root, width=500, height=400)
my_frame.pack()
my_frame.config(bg="azure")

#my_label = Label(my_frame, text="Hola, lector")
#my_label.pack() este método hace que la raíz y el frame se ajusten al tamaño del label
#my_label.place(x=200, y=10)

''' Si no vamos a usar el label para nada más, podemos hacerlo sin declarar variable'''
Label(my_frame, text="Hola, lector", fg="blue", font=("Comic Sans MS",16)).place(x=200,y=10)

''' La librería tkinter solo admite png y gif, para usar otras extensiones habría que importar otras librerías'''
directorio = "C:\\1-Python\Ejercicios de Clase\Interfaces Gráficas\\assets\image.png"
imagen = PhotoImage(file=directorio)
Label(my_frame, image=imagen).place(x=10, y=30)

root.mainloop()