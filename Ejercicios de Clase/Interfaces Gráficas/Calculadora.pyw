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
num1=0
contador_resta=0
contador_multi=0
contador_divi=0
reset_pantalla=False


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
#-------------------pulsaciones teclado--------------------------

def numeroPulsado(num):

	global operacion

	global reset_pantalla

	if reset_pantalla!=False:

		numeroPantalla.set(num)

		reset_pantalla=False

	else:
	
		numeroPantalla.set(numeroPantalla.get() + num)


#----------------funcion suma----------------------------------

def suma(num):

	global operacion

	global resultado

	global reset_pantalla

	resultado+=int(num) #resultado=resultado+int(num)

	operacion="suma"

	reset_pantalla=True

	numeroPantalla.set(resultado)



#---------------funcion resta------------------------------

def resta(num):

	global operacion

	global resultado

	global num1

	global contador_resta

	global reset_pantalla

	if contador_resta==0:

		num1=int(num)

		resultado=num1

	else:

		if contador_resta==1:

			resultado=num1-int(num)

		else:

			resultado=int(resultado)-int(num)	

		numeroPantalla.set(resultado)

		resultado=numeroPantalla.get()


	contador_resta=contador_resta+1

	operacion="resta"

	reset_pantalla=True


#-------------funcion multiplicacion---------------------

def multiplica(num):

	global operacion

	global resultado

	global num1

	global contador_multi

	global reset_pantalla
	
	if contador_multi==0:

		num1=int(num)
		
		resultado=num1

	else:

		if contador_multi==1:

			resultado=num1*int(num)

		else:

			resultado=int(resultado)*int(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_multi=contador_multi+1

	operacion="multiplicacion"

	reset_pantalla=True

#-----------------funcion division---------------------


def divide(num):

	global operacion

	global resultado

	global num1

	global contador_divi

	global reset_pantalla
	
	if contador_divi==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_divi==1:

			resultado=num1/float(num)

		else:

			resultado=float(resultado)/float(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_divi=contador_divi+1

	operacion="division"

	reset_pantalla=True



#----------------funcion el_resultado----------------

def el_resultado():

	global resultado

	global operacion

	global contador_resta

	global contador_multi

	global contador_divi
	

	if operacion=="suma":

		numeroPantalla.set(resultado+int(numeroPantalla.get()))

		resultado=0

	elif operacion=="resta":

		numeroPantalla.set(int(resultado)-int(numeroPantalla.get()))

		resultado=0

		contador_resta=0

	elif operacion=="multiplicacion":

		numeroPantalla.set(int(resultado)*int(numeroPantalla.get()))

		resultado=0

		contador_multi=0

	elif operacion=="division":

		numeroPantalla.set(int(resultado)/int(numeroPantalla.get()))

		resultado=0

		contador_divi=0


def borrar():
        global resultado
        global operacion
        global contador_resta
        global contador_multi
        global contador_divi

        resultado = 0
        operacion = 0
        contador_resta = 0
        contador_multi = 0
        contador_divi = 0
        numeroPantalla.set("")
	
'''
==============================================================
'''
# BOTONES FILA 1

botonBORRAR = Button(miFrame, text="BORRAR", width=10, command=lambda:borrar())
botonBORRAR.grid(row=2,column=1, padx=10, pady=10, columnspan=4)
botonBORRAR.config(bg="dimgrey", fg="lime")

'''
==============================================================
'''
# BOTONES FILA 2

boton7 = Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=3,column=1)
boton7.config(bg="dimgrey", fg="lime")

boton8 = Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=3,column=2)
boton8.config(bg="dimgrey", fg="lime")

boton9 = Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=3,column=3)
boton9.config(bg="dimgrey", fg="lime")

botonDIV = Button(miFrame, text="/", width=3, command=lambda:divide(numeroPantalla.get()))
botonDIV.grid(row=3,column=4)
botonDIV.config(bg="dimgrey", fg="lime")

'''
==============================================================
'''

# BOTONES FILA 3

boton4 = Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=4,column=1)
boton4.config(bg="dimgrey", fg="lime")

boton5 = Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=4,column=2)
boton5.config(bg="dimgrey", fg="lime")

boton6 = Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=4,column=3)
boton6.config(bg="dimgrey", fg="lime")

botonMUL = Button(miFrame, text="x", width=3)
botonMUL.grid(row=4,column=4)
botonMUL.config(bg="dimgrey", fg="lime", command=lambda:multiplica(numeroPantalla.get()))

'''
==============================================================
'''

# BOTONES FILA 4

boton1 = Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=5,column=1)
boton1.config(bg="dimgrey", fg="lime")

boton2 = Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=5,column=2)
boton2.config(bg="dimgrey", fg="lime")

boton3 = Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=5,column=3)
boton3.config(bg="dimgrey", fg="lime")

botonSUM = Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSUM.grid(row=5,column=4)
botonSUM.config(bg="dimgrey", fg="lime")


'''
==============================================================
'''

# BOTONES FILA 5

botonIGUAL = Button(miFrame, text="=", width=8, command=lambda:el_resultado())
botonIGUAL.grid(row=6,column=1, columnspan=2)
botonIGUAL.config(bg="dimgrey", fg="lime")

boton0 = Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=6,column=3)
boton0.config(bg="dimgrey", fg="lime")


botonRESTA = Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRESTA.grid(row=6,column=4)
botonRESTA.config(bg="dimgrey", fg="lime")


'''
==============================================================
'''
# FINAL DEL PROGRAMA

raiz.mainloop()