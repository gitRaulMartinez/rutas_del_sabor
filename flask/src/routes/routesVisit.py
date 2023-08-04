from flask import Blueprint, jsonify, request, g
from src.auth.auth import auth
from src.models.routeVisit import RouteVisit
import src.controllers.routeVisit as routeVisitController
import src.controllers.user as userController

import uuid

route_visit_bp = Blueprint('routeVisit', __name__, url_prefix='/routes_visit')

# Registramos usuario
@route_visit_bp.route('/create', methods=['POST'])
@auth
def create_route_visit():
    new_route = request.json
    uid = str(uuid.uuid4())
    name = new_route.get('name')
    destinations = new_route.get('destinations')

    new_route = RouteVisit(uid, name, destinations)
    try:
        routeVisitController.addRouteVisit(new_route)
        userController.addRoute(g.user.get('_id'),route=uid)  
        return jsonify(new_route.__dict__), 200
    except Exception as e:
        return jsonify({'message': f'Error al agregar rutas de visita {e}'}), 500

@route_visit_bp.route('/my_routes', methods=['GET'])
@auth
def get_route_visit():
    try:
        user = userController.getUser(g.user.get('_id'))
        activities = routeVisitController.getMyRoutesVisit(user.route_history)
        return jsonify([activity.__dict__ for activity in activities]), 200
    except Exception as e:
        return jsonify({'message': f'Error al obtener rutas de visita {e}'}), 500


@route_visit_bp.route('/', methods=['GET'])
def get_routes_visit():
    try:
        activities = routeVisitController.getRoutesVisit()
        return jsonify([activity.__dict__ for activity in activities]), 200
    except Exception as e:
        return jsonify({'message': f'Error al obtener rutas de visita {e}'}), 500