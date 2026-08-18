"""
Realiza una peticion ‘GET’ al siguiente endpoint:
https://jsonplaceholder.typicode.com/users/1

Guarda la respuesta en una variable llamada ‘response’.

Convierte el contenido de la respuesta a un diccionario y almacenalo en una variable llamada ‘user’.

Imprime en consola el valor de la propiedad ‘name’.

"""
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

user = response.json()
print(user) # Aqui puedes ver que es un diccionario y que contiene la llave name
print(user["name"])

""" Respuesta
La variable user contiene el JSON convertido a un diccionario de Python.
"""