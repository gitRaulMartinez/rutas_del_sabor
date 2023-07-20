from flask import Blueprint, jsonify, request

import uuid

from models.user import User
import controllers.user as userController


# Creamos un Blueprint para las rutas de usuarios
users_bp = Blueprint('users', __name__, url_prefix='/flask/user')

# Ruta POST para crear un nuevo usuario
@users_bp.route('/register', methods=['POST'])
def create_user():
    new_user = request.json
    # Datos del usuario (puedes obtenerlos desde el request)
    uid = str(uuid.uuid4())
    name = new_user.get('name')
    lastname = new_user.get('lastname')

    # Crear una instancia del modelo Usuario
    new_user = User(uid, name, lastname)

    try:
        userController.addUser(new_user)
        return jsonify({'mensaje': 'Usuario creado exitosamente.'}), 200
    except Exception as e:
        return jsonify({'mensaje': f'Error al agregar el usuario {e}'}), 500

# Ruta GET para obtener todos los usuarios
@users_bp.route('/users', methods=['GET'])
def get_users():
    try:
        users = userController.getUsers()
        return jsonify([user.__dict__ for user in users]), 200
    except Exception as e:
        return jsonify({'mensaje': f'Error al agregar el usuario {e}'}), 500