import requests
import asyncio
import aiohttp
import time

URL = 'https://jsonplaceholder.typicode.com/comments/1'
TOTAL_REQUESTS = 50

#METODOS: GET (leer), POST (crear), PUT (actualizar), DELETE (borrar).
#URL/Endpoint: La dirección del recurso.
#Headers: Metadatos (ej. Content-Type: application\json).
#Body: (Cuerpo): Los datos que enviamos (usualmente en JSON).

# -- MODO SÍNCRONO --
def test_synchronous():
    print(f'Iniciando {TOTAL_REQUESTS} peticiones síncronas...')
    start = time.perf_counter()
    for _ in range(TOTAL_REQUESTS):
        requests.get(URL)
    end = time.perf_counter()
    return end - start

# -- MODO ASÍNCRONO --
async def fetch(session):
    async with session.get(URL) as response:
        return await response.text()

async def test_asynchronous():
    print(f'Iniciando {TOTAL_REQUESTS} peticiones asíncronas.')
    start = time.perf_counter()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session) for _ in range(TOTAL_REQUESTS)]
        # print(f'Lista de comprehension: {tasks}')
        await asyncio.gather(*tasks)
    end = time.perf_counter()
    return end - start

# -- EJECUCIÓN --
if __name__ == '__main__':
    #Síncrono
    time_sync = test_synchronous()
    print(f'Tiempo síncrono: {time_sync:.2f} segundos\n')

    #Asíncrono
    time_async = asyncio.run(test_asynchronous())
    print(f'Tiempo asíncrono: {time_async:.2f} segundos\n')

    #Mejora
    print(f'--- !La versión asíncrona fue {time_sync/time_async:.1f} veces más rápida ---')