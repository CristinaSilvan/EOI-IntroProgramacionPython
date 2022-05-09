'''
El diccionario dado consta de vehículos y sus pesos en 
kilogramos. Construya una lista de nombres de vehículos con 
peso inferior a 1300 kilogramos. En la misma lista de 
comprensión, haga que los nombres de las claves estén 
en mayúsculas.
'''

dict={"Susuke Ignis": 985, "Chevrolet park Activ": 1100, "Volkswagen CrossUP": 1245, "Masda CX-3": 1254, "Susuki Vitara": 1245, "Nissan Kicks": 1310, "Mazda CX-5": 1672, "Ford Escape": 1625}
lst=[x.upper() for x in dict if dict.get(x) < 1300]
#lst=[x.upper() for x in dict if dict[n] < 13000]
print(lst)