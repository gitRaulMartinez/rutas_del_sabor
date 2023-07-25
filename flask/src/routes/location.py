from flask import Blueprint, jsonify, request
from src.models.location import Location
import src.controllers.location as locationController

import uuid

location_bp = Blueprint('location', __name__, url_prefix='/locations')

# Registramos usuario
@location_bp.route('/create', methods=['POST'])
def create_culinary_destination():
    new_location = request.json
    uid = str(uuid.uuid4())
    country = new_location.get('country')
    address = new_location.get('address')
    coordinates = new_location.get('coordinates')

    new_location = Location(uid, address, coordinates,country)
    try:
        locationController.addLocation(new_location)
        return jsonify({'message': 'Ubicación creada exitosamente','status': 200}), 200
    except Exception as e:
        return jsonify({'message': f'Error al agregar ubicación {e}','status': 500}), 500
    
@location_bp.route('/', methods=['GET'])
def get_locations():
    try:
        locations = locationController.getLocations()
        return jsonify([location.__dict__ for location in locations]), 200
    except Exception as e:
        return jsonify({'message': f'Error al obtener ubicación {e}'}), 500