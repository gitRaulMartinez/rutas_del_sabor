class User:
    def __init__(self,id,username,password,name,lastname,route_history=None):
        self.id = id
        self.username = username
        self.password = password
        self.name = name
        self.lastname = lastname
        if route_history is None:
            self.route_history = []
        else:
            self.route_history = route_history
        
    
    