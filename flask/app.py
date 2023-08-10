from flask import Flask, jsonify
from src.config.config import FLASK_HOST, FLASK_PORT, FLASK_DEBUG
from src.firebase.firebase_connection import initialize_firebase
from src.routes.routes import register_blueprints
from flask_cors import CORS

initialize_firebase()

app = Flask(__name__)
CORS(app)
register_blueprints(app)
""""
# Para desarrollo
if __name__ == '__main__':
    # Iniciar Flask
    
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)
"""