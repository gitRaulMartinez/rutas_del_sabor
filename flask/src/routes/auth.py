from flask import Blueprint, jsonify, request

import uuid

from src.models.user import User
import src.controllers.user as userController

from src.utils.password import hash_password,check_password
from src.utils.auth import generate_token

# Creamos un Blueprint para las rutas de usuarios
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Registramos usuario
@auth_bp.route('/register', methods=['POST'])
def register():
    new_user = request.json
    # Datos del usuario (puedes obtenerlos desde el request)
    uid = str(uuid.uuid4())
    username = new_user.get('username')
    password = hash_password(new_user.get('password'))
    name = new_user.get('name')
    lastname = new_user.get('lastname')

    # Crear una instancia del modelo Usuario
    new_user = User(uid, username, password, name, lastname)
    try:
        user = userController.getUserByUsername(username)
        if user is None:
            userController.addUser(new_user)
            return jsonify({'message': 'Usuario creado exitosamente.','status': 200}), 200
        else:
            return jsonify({'message': 'Usuario ya existente.','status': 409}), 409
    except Exception as e:
        return jsonify({'message': f'Error al agregar el usuario {e}','status': 500}), 500
    
# Realizamos inicio de session
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    try:
        user = userController.getUserByUsername(data.get('username'))
        if user is None:
            return  jsonify({'message': 'Este usuario no existe','status': 401}), 401
        else:
            if check_password(data.get('password'),user.password):
                token = generate_token(user)
                return jsonify({'token': token})
            else:
                return  jsonify({'message': 'La contraseña no es valida','status': 401}), 401

    except Exception as e:
        return jsonify({'message': f'Error al querer loguear el usuario {e}','status': 500}), 500