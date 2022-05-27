lenguajes=['Python', 'C', 'C++', 'Java'] 
# Declaración de una colección o array

print("Los lenguajes son: ", lenguajes) # ['Python', 'C', 'C++', 'Java']

'''
print(lenguajes[0]) # Python
print(lenguajes[1]) # C
print(lenguajes[2]) # C++
print(lenguajes[3]) # Java
print(lenguajes[4]) # Error: ya que no existe esta posición
'''

# Para recorrer la colección o array (FORMA 1)
for i in range(0,len(lenguajes)): # len(lenguajes) cantidad de valores
    print(lenguajes[i])

# Para recorrer la colección o array (FORMA 2)
for len in lenguajes:
    print(len)


