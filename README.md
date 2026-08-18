# 🧪 Ejercicios

## Crear un Entorno Virtual y activar dependencias

```bash
python -m venv venv

.\venv\Scripts\activate
```

## Instalar Dependecias de requests

```bash
pip install requests

```
## Ejercicio 1 — Petición GET

Realizar una petición `GET` y comprobar si el servidor devuelve el código de estado `200`.

```python
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)

print(response.status_code == 200)
```

### Resultado esperado

```text
True
```

---

## Ejercicio 2 — Obtener datos JSON

Realizar una petición `GET`, convertir la respuesta JSON en un diccionario y obtener el valor de `name`.

```python
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1"
)

user = response.json()

print(user)
print(user["name"])
```

### Resultado esperado

```text
Leanne Graham
```

La variable `user` contiene un **diccionario de Python** con la información del usuario.

---

## Ejercicio 3 — Validar una respuesta JSON

Comprobar que:

* El código de estado sea `200`.
* La respuesta contenga la clave `title`.
* La respuesta contenga la clave `body`.

```python
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)

post = response.json()

print(
    response.status_code == 200
    and "title" in post
    and "body" in post
)
```

### Resultado esperado

```text
True
```

---

## Ejercicio 4 — Petición POST

Enviar información mediante una petición `POST`.

```python
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
```

> **Nota:** En este ejercicio se comprueba intencionalmente la existencia de la clave `"d"`, tal como solicita el ejercicio. Sin embargo, la respuesta de JSONPlaceholder normalmente contiene las claves `id`, `title`, `body` y `userId`, por lo que esta condición devuelve `False`.

---

# Guardar las dependencias

Para guardar las dependencias instaladas en un archivo:

```bash
python -m pip freeze > requirements.txt
```

Esto generará un archivo:

```text
requirements.txt
```

Por ejemplo:

```text
requests==2.x.x
```

Posteriormente, las dependencias pueden instalarse con:

```bash
python -m pip install -r requirements.txt
```

## API utilizada

Los ejercicios utilizan **JSONPlaceholder**, una API REST gratuita para realizar pruebas y ejercicios.

Endpoint utilizado:

```text
https://jsonplaceholder.typicode.com
```
