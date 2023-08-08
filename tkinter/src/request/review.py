import requests
from src.environments.environments import URL_SERVER

class ReviewData:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ReviewData, cls).__new__(cls)
            cls._instance._data = None
        return cls._instance

    def get_data(self):
        if self._data is None:
            response = requests.get(f"{URL_SERVER}/reviews/")
            if response.status_code != 500:
                self._data = response.json()
            else:
                print(response.json()['message'])
                self._data = None
        return self._data
    
    def create(self,token,data):
        header = {'Authorization': 'Bearer '+token}
        response = requests.post(f"{URL_SERVER}/reviews/create",headers=header,json=data)
        if response.status_code != 500:
            return response.json()
        else:
            print(response.json()['message'])
            return None
        
    def reload(self):
        response = requests.get(f"{URL_SERVER}/reviews/")
        if response.status_code != 500:
            self._data = response.json()
        else:
            print(response.json()['message'])
            self._data = None
    
    def logout(self):
        self._data = None