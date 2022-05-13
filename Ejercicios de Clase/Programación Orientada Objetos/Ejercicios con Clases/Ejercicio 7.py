'''
Cree una clase llamada myfunc y dentro de ella coloque una función muy simple llamada "quinta" que toma x y devuelve la quinta potencia de x. No se necesitan init o atributos de clase.

Finalmente llame a su función con el número 5 y asígnela a la variable ans.
'''

class myfunc:
    def quinta(x):
        return x**5

ans=myfunc.quinta(5)
print(ans)