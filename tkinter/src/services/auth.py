import requests

from src.environments.environments import URL_SERVER

def login(username,password):
    data = {
        'username': username,
        'password': password
    }
    response = requests.post(f"{URL_SERVER}/auth/login", json=data)

    if response.status_code != 500:
        return response.json()
    else:
        print(response.json()['message'])
        return None
    
def register(username,password,name,lastname):
    data = {
        'username': username,
        'password': password,
        'name': name,
        'lastname': lastname
    }
    response = requests.post(f"{URL_SERVER}/auth/register", json=data)

    if response.status_code != 500:
        return response.json()
    else:
        print(response.json()['message'])
        return None