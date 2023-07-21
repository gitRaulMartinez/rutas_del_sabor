import jwt
import datetime

from src.config.config import JWT_SECRET_KEY

def generate_token(user):
    # Crear el payload del token
    payload = {
        'username': user.username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # El token expira en 30 minutos
    }

    # Generar el token JWT con la clave secreta configurada en la aplicación
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')

    return token