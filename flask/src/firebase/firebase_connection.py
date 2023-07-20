import firebase_admin
from firebase_admin import credentials

def initialize_firebase():
    # Ruta de la clave de servicio de Firebase (descargada desde la Consola de Firebase)
    RUTA_CLAVE_SERVICIO = 'src/firebase/credentials/rutas-del-sabor.json'
    # URL de la base de datos de Firebase
    DATABASE_URL = 'https://rutas-del-sabor-default-rtdb.firebaseio.com'
    # Inicializar la aplicación Firebase
    try:
        cred = credentials.Certificate(RUTA_CLAVE_SERVICIO)
        firebase_admin.initialize_app(cred, {'databaseURL': DATABASE_URL})
        print("Firebase inicializado correctamente 🚀.")
    except Exception as e:
        print("Error al inicializar Firebase:", e)