import firebase_admin
from firebase_admin import credentials
from src.config.config import ROUTE_CREDENTIALS, DATABASE_URL

def initialize_firebase():
    # Inicializar la aplicación Firebase
    try:
        cred = credentials.Certificate(ROUTE_CREDENTIALS)
        firebase_admin.initialize_app(cred, {'databaseURL': DATABASE_URL})
        print("Firebase inicializado correctamente 🚀.")
    except Exception as e:
        print("Error al inicializar Firebase:", e)