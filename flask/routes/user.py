from flask import Blueprint, jsonify, request
from models.user import User
from firebase_admin import db

# Creamos un Blueprint para las rutas de usuarios
users_bp = Blueprint('users', __name__)

# Ruta POST para crear un nuevo usuario
@users_bp.route('/register', methods=['POST'])
def create_user():
    # Datos del usuario (puedes obtenerlos desde el request)
    uid = '34234234'
    name = 'Raul Martinez'
    lastname = 'raul@ejemplo.com'

    # Crear una instancia del modelo Usuario
    nuevo_usuario = User(uid, name, lastname)

    # Agregar el usuario a la base de datos
    db.reference('/users').child(uid).set(nuevo_usuario.__dict__)

    return jsonify({'mensaje': 'Usuario creado exitosamente.'})

# Ruta GET para obtener todos los usuarios
@users_bp.route('/users', methods=['GET'])
def get_users():
    # Obtener todos los usuarios de la base de datos
    users = db.reference('/usuarios').get()

    # Si no hay usuarios en la base de datos, devolvemos una lista vacía
    if users is None:
        return jsonify([])

    # Convertir el diccionario de usuarios a una lista de objetos Usuario
    list_users = [User(**usuario) for usuario in users.values()]

    # Devolver la lista de usuarios como JSON
    return jsonify([usuario.__dict__ for usuario in list_users])