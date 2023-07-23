import requests
import json

def login(username,password):
    data = {
        'username': username,
        'password': password
    }
    response = requests.post('http://localhost:5000/user/login', json=data)

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
    response = requests.post('http://localhost:5000/user/register', json=data)

    if response.status_code != 500:
        return response.json()
    else:
        print(response.json()['message'])
        return None