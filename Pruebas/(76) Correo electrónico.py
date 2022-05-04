'''
Escribir un programa que pregunte el correo electrónico del usuario en la consola y 
muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) 
pero con dominio ceu.es.
'''

correo = ''
while True:
    correo = input("Escriba su correo electrónico: ")
    if len(correo) < 1:
        print("El programa no puede funcionar si usted no introduce parámetros\n")
        continue
    if(' ' in  correo):
        print("El dato introducido no es un correo válido\n")
        continue
    if (not '@' in correo):
        print("El dato introducido no es un correo válido\n")
        continue
    nuevo = correo.split('@')
    if (not '.' in nuevo[1]):
        print("El dato introducido no es un correo válido\n")
        continue
    aux = nuevo[1].split('.')
    del nuevo[1]
    nuevo.append(aux[0])
    nuevo.append(aux[1])
    correo_nuevo = nuevo[0] + '@ceu.es'
    print("Su nuevo correo es: {}".format(correo_nuevo))
    break
    # print(nuevo)

'''
# Alternativa

email = input("Introduce tu correo electrónico: ")
print(email[:email.find('@')] + '@ceu.es')
'''