try:
    fichero = open("Ficherito.txt", "rt", encoding='UTF-8')
except NameError:
    print("No se encuentra el fichero")
except FileNotFoundError:
    print("No se encuentra el fichero")
finally:
    fichero.close()