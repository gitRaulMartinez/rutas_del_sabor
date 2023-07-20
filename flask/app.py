from flask import Flask, jsonify
from src.config.config import FLASK_HOST, FLASK_PORT, FLASK_DEBUG
from src.firebase.firebase_connection import initialize_firebase
from src.routes.routes import register_blueprints

initialize_firebase()

app = Flask(__name__)

if __name__ == '__main__':
    # Iniciar Flask
    register_blueprints(app)
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)