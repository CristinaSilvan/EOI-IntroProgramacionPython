# Imprime solo los impares

arreglo_origen = [1,2,3,4,5,6,7,8,9]
arreglo_fin = []
for i in arreglo_origen: # for i in range(0, len(arreglo_origen)):
    if i % 2 != 0:
        arreglo_fin.append(i) # append en arrays, añade en el último lugar sin tener en cuenta un orden

print(f"Array original: {arreglo_origen}\n")
print(f"Array de impares: {arreglo_fin}\n")