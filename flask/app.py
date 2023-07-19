from flask import Flask, jsonify
from config.config import FLASK_HOST, FLASK_PORT, FLASK_DEBUG
from config.firebase_connection import initialize_firebase
app = Flask(__name__)

# Ruta GET para obtener el JSON de prueba
@app.route('/ejemplo', methods=['GET'])
def obtener_ejemplo():
    # Datos de prueba en formato JSON
    data = {
        'nombre': 'Ejemplo',
        'edad': 30,
        'profesion': 'Desarrollador',
    }
    # Devolvemos el JSON como respuesta
    return jsonify(data)

if __name__ == '__main__':
    # Inicializar Firebase
    initialize_firebase()
    # Iniciar Flask
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)