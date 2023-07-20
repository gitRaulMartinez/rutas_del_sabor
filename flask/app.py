from flask import Flask, jsonify
from config.config import FLASK_HOST, FLASK_PORT, FLASK_DEBUG
from config.firebase_connection import initialize_firebase
from routes.routes import all_bp

app = Flask(__name__)

#Iniciar firebase
initialize_firebase()

# Registrar todos los Blueprints en la aplicación
for bp in all_bp:
    app.register_blueprint(bp)

if __name__ == '__main__':
    # Inicializar Firebase
    initialize_firebase()
    # Iniciar Flask
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)