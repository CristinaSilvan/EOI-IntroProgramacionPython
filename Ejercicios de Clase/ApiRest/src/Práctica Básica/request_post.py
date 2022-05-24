import requests
u = {'Nombre':'Cristina', 'Apellidos':'Silvan'}
r = requests.post('http://postman-echo.com/post', data=u)
print(r.text)