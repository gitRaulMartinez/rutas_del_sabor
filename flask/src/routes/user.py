from flask import Blueprint, jsonify, request, g

import src.controllers.user as userController
from src.auth.auth import auth

# Creamos un Blueprint para las rutas de usuarios
users_bp = Blueprint('users', __name__, url_prefix='/users')

# Ruta GET para obtener todos los usuarios
@users_bp.route('/', methods=['GET'])
def get_users():
    try:
        users = userController.getUsers()
        return jsonify([user.__dict__ for user in users]), 200
    except Exception as e:
        return jsonify({'message': f'Error al obtener todos los usuarios {e}'}), 500
    
# Ruta GET para obtener un usuario por id
@users_bp.route('/myuser', methods=['GET'])
@auth
def get_my_user():
    try:
        user = userController.getUserByUsername(g.user.get('username'))  
        del user.password
        if user is not None:
            return jsonify(user.__dict__), 200
        else:
            return jsonify({'message': 'Usuario no existe.','status': 404}), 404
    except Exception as e:
        return jsonify({'message': f'Error al buscar usuario {e}'}), 500
    
# Ruta GET para obtener un usuario por id
@users_bp.route('/<string:id_usuario>', methods=['GET'])
@auth
def get_user(id_usuario):
    try:
        user = userController.getUser(id_usuario)
        if user is not None:
            return jsonify(user.__dict__), 200
        else:
            return jsonify({'message': 'Usuario no existe.','status': 404}), 404
    except Exception as e:
        return jsonify({'message': f'Error al buscar usuario {e}'}), 500