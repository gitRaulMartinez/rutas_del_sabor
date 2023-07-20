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


