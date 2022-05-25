import requests

if __name__ == '__main__':
    url = 'http://www.python.org/images/success/nasa.jpg'

    respuesta = requests.get(url, stream=True) # Realiza la petición sin descargar el contenido 

    with open('.\Ejercicios de Clase\ApiRest\src\Ejercicio NASA\image.jpg', 'wb') as fichero:
        for chuck in respuesta.iter_content(): # Descarga el contenido poco a poco
            
            fichero.write(chuck)

            '''
            (method) iter_content: (chunk_size: int | None = ..., decode_unicode: bool = ...) -> Iterator
            Iterates over the response data. When stream=True is set on the request, this avoids reading 
            the content at once into memory for large responses. The chunk size is the number of bytes it 
            should read into memory. This is not necessarily the length of each item returned as decoding can take place.

            chunk_size must be of type int or None. A value of None will function differently depending 
            on the value of stream. stream=True will read data as it arrives in whatever size the chunks are received. 
            If stream=False, data is returned as a single chunk.
            '''
    respuesta.close()