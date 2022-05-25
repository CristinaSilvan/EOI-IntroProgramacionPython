import requests
import json
url='http://httpbin.org/post'
user = {'Username' : 'Cristi'}
headers = {'content-type':'application/json'}
r = requests.post(url,data=user,headers=headers)
print(r.text)

fichero = open(".\Ejercicios de Clase\ApiRest\src\Práctica Básica\\requests_headears(ANSWER).json", "wt")
fichero.write(str(r.text))
fichero.close()