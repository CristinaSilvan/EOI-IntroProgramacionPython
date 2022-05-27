# https://www.youtube.com/watch?v=kbTl3DaFJUk&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=47
from tkinter import *
from turtle import bgcolor

# CREACIÓN DE RAÍZ Y FRAME BÁSICOS

raiz = Tk()
raiz.title("Calculadora")
raiz.iconbitmap("C:\\1-Python\Ejercicios de Clase\Interfaces Gráficas\\assets\calculadora.ico")
raiz.resizable(0,0)

miFrame = Frame(raiz)
miFrame.pack()
miFrame.config(bg="black")

'''
==============================================================
'''
# VARIABLES GLOBALES

numeroPantalla = StringVar()
operacion = ""
resultado = 0


'''
==============================================================
'''
# PANTALLA

pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="dimgrey", fg="lime", justify="right")


'''
==============================================================
'''
# FUNCIONES

def numeroPulsado(num):
    global operacion
    if operacion != "":
        numeroPantalla.set(num)
        operacion = ""
    else:
        numeroPantalla.set(numeroPantalla.get() + num)

def suma(num):
    global resultado
    global operacion

    resultado += int(num)

    operacion = "suma"

    numeroPantalla.set(resultado)

def igual():
    global resultado
    numeroPantalla.set(resultado + int(numeroPantalla.get()))
    resultado = 0


'''
==============================================================
'''
# BOTONES FILA 1

boton7 = Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=1)
boton7.config(bg="dimgrey", fg="lime")

boton8 = Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2)
boton8.config(bg="dimgrey", fg="lime")

boton9 = Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2,column=3)
boton9.config(bg="dimgrey", fg="lime")

botonDIV = Button(miFrame, text="/", width=3)
botonDIV.grid(row=2,column=4)
botonDIV.config(bg="dimgrey", fg="lime")

'''
==============================================================
'''

# BOTONES FILA 2

boton4 = Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3,column=1)
boton4.config(bg="dimgrey", fg="lime")

boton5 = Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2)
boton5.config(bg="dimgrey", fg="lime")

boton6 = Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=3)
boton6.config(bg="dimgrey", fg="lime")

botonMUL = Button(miFrame, text="x", width=3)
botonMUL.grid(row=3,column=4)
botonMUL.config(bg="dimgrey", fg="lime")

'''
==============================================================
'''

# BOTONES FILA 3

boton1 = Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4,column=1)
boton1.config(bg="dimgrey", fg="lime")

boton2 = Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4,column=2)
boton2.config(bg="dimgrey", fg="lime")

boton3 = Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4,column=3)
boton3.config(bg="dimgrey", fg="lime")

botonSUM = Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSUM.grid(row=4,column=4)
botonSUM.config(bg="dimgrey", fg="lime")


'''
==============================================================
'''

# BOTONES FILA 4

botonIGUAL = Button(miFrame, text="=", width=8, command=lambda:igual)
botonIGUAL.grid(row=5,column=1, columnspan=2)
botonIGUAL.config(bg="dimgrey", fg="lime")

boton0 = Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5,column=3)
boton0.config(bg="dimgrey", fg="lime")


botonRESTA = Button(miFrame, text="-", width=3)
botonRESTA.grid(row=5,column=4)
botonRESTA.config(bg="dimgrey", fg="lime")


'''
==============================================================
'''
# FINAL DEL PROGRAMA

raiz.mainloop()