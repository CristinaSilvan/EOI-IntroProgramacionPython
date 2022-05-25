from pymongo import MongoClient

clientDB = MongoClient('mongodb://localhost:27017/')
db = clientDB.admin
resultado = db.command('serverStatus')
print('Host: ',resultado['host'])
print('Version: ',resultado['version'])
print('Proceso: ',resultado['process'])

# Guardado de resultado en .txt
Resultado_terminal = 'Host: '+ resultado['host'] + '\n' + 'Version: ' + resultado['version'] + '\n' + 'Proceso: ' + resultado['process']
fichero = open('..\\Resultado_Prueba_Conexión.txt', 'wt', encoding='UTF-8')
fichero.write(str(Resultado_terminal))
fichero.close()