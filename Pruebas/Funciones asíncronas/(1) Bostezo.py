import asyncio

async def saludo():
    print("Hola!!")
    await asyncio.sleep(2)
    print("Perdón, estaba bostezando")

asyncio.run(saludo())