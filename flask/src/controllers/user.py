from firebase_admin import db
from src.models.user import User

def addUser(user):
    return db.reference('/users').child(user._id).set(user.__dict__)

def getUsers():
    users = db.reference('/users').get()
    if users is None:
        return []
    else:
        return [User(**user) for user in users.values()]
    
def getUser(user_id):
    # Obtener un usuario específico por su ID
    user = db.reference('/users').child(user_id).get()
    if user is None:
        return None
    else:
        return User(**user)
    
def getUserByUsername(username):
    # Obtener un usuario específico por su nombre de usuario
    users = db.reference('/users').get()
    if users is not None:
        for user_id, user_data in users.items():
            if user_data.get('username') == username:
                return User(**user_data)
    return None

def addRoute(user_id,route):
    user_ref = db.reference('/users').child(user_id)
    user = user_ref.get()
    if user is not None:
        route_history = user.get('route_history', [])
        route_history.append(route)

        user['route_history'] = route_history
        user_ref.set(user)
            




