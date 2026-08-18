"""
1. Realiza una peticion **‘GET’** al siguiente endpoint:
   **`https://jsonplaceholder.typicode.com/posts/1`**


Guarda la respuesta en **‘response’** y el JSON de la respuesta en una variable llamada **‘post’**.

Imprime **‘True’** solamente si:

- El status code es **‘200’**.
- El JSON contiene la llave **‘title’**
- El JSON contiene la llave **‘body’**.

De lo contrario imprime **‘False’**.
"""
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

post = response.json()

print(
    response.status_code == 200
    and "title" in post
    and "body" in post
)

"""Respuesta

response.status_code == 200 → verifica que la petición fue exitosa.
"title" in post → verifica que existe la llave title.
"body" in post → verifica que existe la llave body.
and → todas las condiciones deben cumplirse para obtener True.
"""