import requests
r = requests.get('http://api.open-notify.org/iss-now.json')
print(type(r))
print(r.headers)
print(r.headers['content-type'])
print(f'{r.status_code}/{r.encoding}')
print(r.text)
print(r.json()['message']) # success

fichero = open(".\Ejercicios de Clase\ApiRest\src\Práctica Básica\\requests_get(ANSWER).json", "wt")
fichero.write(str(r.text))
fichero.close()