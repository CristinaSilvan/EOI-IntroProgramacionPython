# Para utilizar la asíncronidad, necesitamos importar:
import asyncio

async def saludo():
    print("Hola...")
    await asyncio.sleep(4) # Duerme el programa durante 4 segundos
    print("...mundo")      # para luego seguir con su ejecución en orden

asyncio.run(saludo())
print("Fin del programa")