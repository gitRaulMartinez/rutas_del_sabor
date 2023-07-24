import requests

from src.environments.environments import URL_SERVER

def get_my_user(token):
    headers = { 'Authorization': 'Bearer '+token }
    response = requests.get(f"{URL_SERVER}/users/myuser",headers=headers)

    if response.status_code != 500:
        return response.json()
    else:
        print(response.json()['message'])
        return None