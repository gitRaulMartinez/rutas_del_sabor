from flask import Blueprint, jsonify, request
from src.models.culinaryDestination import CulinaryDestination
import src.controllers.culinaryDestination as culinaryDestinationController

import uuid

culinary_destination_bp = Blueprint('culinary_destination', __name__, url_prefix='/culinary_destinations')

# Registramos usuario
@culinary_destination_bp.route('/create', methods=['POST'])
def create_culinary_destination():
    new_culinary_destination = request.json
    # Datos del usuario (puedes obtenerlos desde el request)
    uid = str(uuid.uuid4())
    name = new_culinary_destination.get('name')
    type_of_kitchen = new_culinary_destination.get('type_of_kitchen')
    ingredients = new_culinary_destination.get('ingredients')
    minimal_price = new_culinary_destination.get('minimal_price')
    maximum_price = new_culinary_destination.get('maximum_price')
    popularity = new_culinary_destination.get('popularity')
    availability = new_culinary_destination.get('availability')
    location_id = new_culinary_destination.get('location_id')
    image = new_culinary_destination.get('image')
    logo = new_culinary_destination.get('logo')

    # Crear una instancia del modelo Usuario
    new_culinary_destination = CulinaryDestination(uid, name, type_of_kitchen, ingredients, minimal_price, maximum_price, popularity, availability, location_id, image, logo)
    try:
        culinaryDestinationController.addCulinaryDestination(new_culinary_destination)
        return jsonify({'message': 'Destino culinario creado exitosamente.','status': 200}), 200
    except Exception as e:
        return jsonify({'message': f'Error al destino culinario {e}','status': 500}), 500
    
@culinary_destination_bp.route('/', methods=['GET'])
def get_users():
    try:
        culinary_destinations = culinaryDestinationController.getCulinaryDestinations()
        return jsonify([culinary_destination.__dict__ for culinary_destination in culinary_destinations]), 200
    except Exception as e:
        return jsonify({'message': f'Error al obtener destinos culinarios {e}'}), 500