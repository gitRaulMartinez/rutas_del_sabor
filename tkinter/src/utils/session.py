import os

import json

from src.localstorage.local import FILE

route = os.path.join(os.path.dirname(os.path.realpath(FILE)),"session.json")

def get_token():
    try:
        with open(route, 'r') as file:
            data = json.load(file)
            token = data.get('token')
            return token
    except Exception as e:
        print(f"Error al cargar el archivo JSON: {e}")
        return None
    

def set_token(token):
    data = {"token": token}
    try:
        with open(route, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        print(f"Error al cargar el archivo JSON: {e}")
        return None

    