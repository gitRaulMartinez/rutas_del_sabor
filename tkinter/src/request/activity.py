import requests
from src.environments.environments import URL_SERVER

class ActivityData:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ActivityData, cls).__new__(cls)
            cls._instance._data = None
        return cls._instance

    def get_data(self):
        if self._data is None:
            response = requests.get(f"{URL_SERVER}/activities/")
            if response.status_code != 500:
                self._data = response.json()
            else:
                print(response.json()['message'])
                self._data = None
        return self._data