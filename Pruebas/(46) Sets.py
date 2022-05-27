# Los SET (conjuntos)
SET = {2,3,4}
print(f"Esto es un conjunto {SET}")

SET.add(1)
SET.add(5)
SET.add(7)
SET.add(10)
SET.add(6)
SET.add(8)
SET.add(9)
print(f"Se le añadió valores {SET}")
# En los SETs, los valores se añaden de forma ordenada

del(SET)

SET = {'a','c'}
print(f"\nEsto es otro conjunto {SET}")

SET.add('b')
SET.add('d')
print(f"Se le añadió valores {SET}")

del(SET)

a = 'python'
print(f"\nEsto es una cadena: {a}")
print(f"Tratando una cadena como un conjunto{set(a)}")
# Es este contexto, 'set' es una función para tratar un valor como un conjunto (parsear)

a = set(a) # Ordena los valores alfanuméricos como en la ASCII
print(f"Esta es la cadena parseada a set {a}")

b = [3,6,8,3,5]
print(f"\nEsto es una lista {b}")
print(f"Lista convertida a set {set(b)}")
# Los sets además eliminan la información repetida (ya sea parseo de listas o tuplas)

c = (1,1,1,2,2,2,3,3,3)
print(f"\nEsto es una tupla {c}")
print(f"Tupla convertida a ser {set(c)}")

del(a,b,c)

SET = {'python', 'javascript', 'html'}
print(f"\n¿Se ecuentra python dentro del set? {'python' in SET}")
print(f"¿Se ecuentra php dentro del set? {'php' in SET}")
# Buscar datos dentro de conjutnos
