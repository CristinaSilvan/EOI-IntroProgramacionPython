import requests

if __name__ == '__main__':
    url = 'http://httpbin.org/cookies'
    cookies = {
        'my-cookie':'true' # Para mandar cookies a traves de una peticion 
    }

    respuesta = requests.get(url,cookies=cookies)

    if respuesta.status_code==200:
        cookies = respuesta.cookies
        print(cookies)

        print(f"El contenido es: \n{respuesta.content}")
    
    fichero = open(".\Ejercicios de Clase\ApiRest\src\Ejercicio Cookies\Respuesta_Cookies.txt", "wt")
    fichero.write(str(cookies) + "\n" + str(respuesta.content))
    fichero.close()