import FunciónSaludar

FunciónSaludar.saludo('Pedro') # SALIDA: Hola, Pedro



# Alternativa 1

from FunciónSaludar import saludo

saludo('Pedro') # SALIDA: Hola, Pedro


# Alternativa 2

from FunciónSaludar import saludo as hola

hola('Pedro') # SALIDA: Hola, Pedro

