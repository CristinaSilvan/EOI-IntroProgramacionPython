from datetime import datetime

# Para que reconozca español
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

fechacastellano = datetime.now()

print(fechacastellano.strftime("%A %d %b %Y"))