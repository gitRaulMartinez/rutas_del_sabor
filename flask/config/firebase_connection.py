import os
import firebase_admin
from firebase_admin import credentials

def initialize_firebase():
    # Ruta de la clave de servicio de Firebase (descargada desde la Consola de Firebase)
    RUTA_CLAVE_SERVICIO = os.path.join(os.path.dirname(__file__), 'rutas-del-sabor.json')

    # Inicializar la aplicación Firebase
    cred = credentials.Certificate(RUTA_CLAVE_SERVICIO)
    firebase_admin.initialize_app(cred)