'''
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y 
muestre por pantalla el número de euros y el número de céntimos del precio introducido.
'''
while True:
    try:
        precio = input("Precio con decimales: ")
        if (precio.count('.') > 1) or (precio.count(',') > 1):
            print("Escriba un dato válido")
            continue
        if ',' in precio:
            precio = precio.replace(',', '.')
        precio = float(precio)
        precio = round(precio, 2)
        precio = str(precio)
        #print(precio)
        print(f"Ha escrito {precio[:precio.find('.')]} euros y {precio[precio.find('.') + 1:]} céntimos")
        break
    except:
        print("Escriba un dato válido")