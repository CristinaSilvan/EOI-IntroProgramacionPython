from datetime import datetime

# Para que reconozca español
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
# UTF-8 se refiere a la parte extendida de la tabla ASCII
# correspondiente a los caracteres del castellano

fechacastellano = datetime.now()

print(fechacastellano.strftime("%A %d %b %Y"))