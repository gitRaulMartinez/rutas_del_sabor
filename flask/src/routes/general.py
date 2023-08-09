from flask import Blueprint, jsonify, request, g

import src.controllers.general as generalController

# Creamos un Blueprint para las rutas de usuarios
general_bp = Blueprint('general', __name__, url_prefix='/all')

# Ruta GET para obtener todos los usuarios
@general_bp.route('/', methods=['GET'])
def get_all():
    try:
        all = generalController.getAll()
        return jsonify(all), 200
    except Exception as e:
        return jsonify({'message': f'Error al obtener todos los datos {e}'}), 500
    