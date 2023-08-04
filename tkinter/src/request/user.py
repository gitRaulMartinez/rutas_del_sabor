import requests
from src.environments.environments import URL_SERVER

class UserData:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserData, cls).__new__(cls)
            cls._instance._data = None
        return cls._instance

    def get_data(self,token):
        header = {'Authorization': 'Bearer '+token}
        if self._data is None:
            response = requests.get(f"{URL_SERVER}/users/myuser",headers=header)
            if response.status_code != 500:
                self._data = response.json()
            else:
                print(response.json()['message'])
                self._data = None
        return self._data
    
    def logout(self):
        self._data = None