import requests

if __name__=='__main__':
    url = 'https://www.google.com/'

    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        contenido = respuesta.content
        fichero = open(".\Ejercicios de Clase\ApiRest\src\Ejercicios Google\google.html", "wb")
        fichero.write(contenido)
        fichero.close()