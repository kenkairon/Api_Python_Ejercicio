"""Utilizando la librería ‘requests’ realiza una petición GET a la siguiente API:
https://jsonplaceholder.typicode.com/posts/1

Guarda la respuesta en una variable llamada ‘response’.

Imprime en consola ‘True’ si el status code de la respuesta es ‘200’. En caso contrario imprime ‘False’."""

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code == 200)