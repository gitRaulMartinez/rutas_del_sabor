from flask import Blueprint, jsonify, request
from src.models.activity import Activity
import src.controllers.activity as activityController

import uuid

activity_bp = Blueprint('activity', __name__, url_prefix='/activities')

# Registramos usuario
@activity_bp.route('/create', methods=['POST'])
def create_activity():
    new_activity = request.json
    uid = str(uuid.uuid4())
    name = new_activity.get('name')
    culinary_destination_id = new_activity.get('culinary_destination_id')
    start_time = new_activity.get('start_time')

    new_activity = Activity(uid, name, culinary_destination_id, start_time)
    try:
        activityController.addActivity(new_activity)
        return jsonify({'message': 'Actividad creada exitosamente','status': 200}), 200
    except Exception as e:
        return jsonify({'message': f'Error al agregar actividad {e}','status': 500}), 500
    
@activity_bp.route('/', methods=['GET'])
def get_activities():
    try:
        activities = activityController.getActivities()
        return jsonify([activity.__dict__ for activity in activities]), 200
    except Exception as e:
        return jsonify({'message': f'Error al obtener actividad {e}'}), 500