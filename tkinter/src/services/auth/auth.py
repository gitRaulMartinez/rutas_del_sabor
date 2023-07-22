import requests
import json

def login(username,password):
    data = {
        'username': username,
        'password': password
    }
    response = requests.post('http://localhost:5000/user/login', json=data)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        return response.json()
    else:
        return 'Error en el servidor'