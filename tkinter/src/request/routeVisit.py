import requests
from src.environments.environments import URL_SERVER

class RouteVisitData:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RouteVisitData, cls).__new__(cls)
            cls._instance._data = None
        return cls._instance

    def get_data(self,token):
        if self._data is None:
            header = {'Authorization': 'Bearer '+token}
            response = requests.get(f"{URL_SERVER}/routes_visit/my_routes",headers=header)
            if response.status_code != 500:
                self._data = response.json()
            else:
                print(response.json()['message'])
                self._data = None
        return self._data
    
    def create(self,token,data):
        header = {'Authorization': 'Bearer '+token}
        response = requests.post(f"{URL_SERVER}/routes_visit/create",headers=header,json=data)
        if response.status_code != 500:
            return response.json()
        else:
            print(response.json()['message'])
            return None
        
    def add(self,route_visit):
        if self._data is not None:
            self._data.append(route_visit)
        return self._data
    
    def logout(self):
        self._data = None
