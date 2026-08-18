"""
Realiza una peticion ‘POST’ al siguiente endpoint:
https://jsonplaceholder.typicode.com/posts

Debes enviar el siguiente diccionario:

data = { "title": "Python", "body": "API exercise", "userId": 1 }

La respuesta debe almacenarse en una variable llamada ‘response’.

Convierte la respuesta a JSON y almacenala en una variable llamada ‘result’.

Imprime ‘True’ si:

El status code es ‘201’.
La respuesta contiene la llave ‘d’.

En cualquier otro caso imprime ‘False’.

"""
import requests

data = {
    "title": "Python",
    "body": "API exercise",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

result = response.json()

print(
    response.status_code == 201
    and "d" in result
)

"""Respuesta
Este endpoint, la respuesta normalmente contiene title, body, userId e id, no contiene la llave d.
Es False, ya que la condición de que la respuesta contenga la llave d no se cumple.
"""