'''
Ahora hagamos algunos cambios en la clase que creamos en el ejercicio anterior de Python.

Primero haga su función para que tome los parámetros: x e y. x será el número que se eleva, e será la potencia. ¡Entonces, los usuarios pueden elevar los números a cualquier potencia! También cambiemos el nombre de la función a "ElevarAlaPotencia".

También agreguemos una representación de cadena rápidamente, de modo que cuando un usuario imprima la clase obtenga una descripción significativa.

Puede ser algo como: Esta clase consistirá en operaciones matemáticas. Solo tenemos una función llamada ElevarAlaPotencia.
'''

class myfunc:
    def ElevarAlaPotencia(x,e):
        return x**e

    def __str__(self):
        return "La función ElevarAlaPotencia toma el primer parámetro y eleva la potencia a un segundo parámetro"

ans1=myfunc.ElevarAlaPotencia(5,6)
ans2= myfunc()
print(ans1)
print(ans2)