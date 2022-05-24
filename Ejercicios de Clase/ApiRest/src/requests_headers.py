import requests
import json
url='http://httpbin.org/post' #endpoint de conexión
user = {'Username' : 'Cristi'}
header = {'content-type':'application/json'}
r = requests.post(url,data=user,headers=header)
