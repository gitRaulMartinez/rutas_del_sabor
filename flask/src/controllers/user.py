from firebase_admin import db
from src.models.user import User

def addUser(user):
    # Agregar el usuario a la base de datos
    return db.reference('/users').child(user.id).set(user.__dict__)

def getUsers():
    # Obtener todos los usuarios
    users = db.reference('/users').get()
    if users is None:
        return []
    else:
        return [User(**usuario) for usuario in users.values()]
    
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



