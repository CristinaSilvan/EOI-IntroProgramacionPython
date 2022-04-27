# Zonas horarias
from datetime import datetime
from pytz import timezone
import pytz

# print(pytz.all_timezones) me aparece la lista con todas las zonas horarias existentes
print(datetime.now(pytz.timezone('Asia/Tokyo'))) # La hora de Tokyo en este momento
print(datetime.now(pytz.timezone('Europe/Madrid')))

