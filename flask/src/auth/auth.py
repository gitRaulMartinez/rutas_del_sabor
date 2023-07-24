from functools import wraps
from flask import jsonify, request, g
from src.config.config import JWT_SECRET_KEY
import jwt

# Función para verificar el token JWT
def auth(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        header = request.headers.get('Authorization')
        token = header.split()[1] if header is not None else None
        if token is None:
            return jsonify({'mensaje': 'Token no proporcionado'}), 401
        try:
            # Verificar y decodificar el token JWT con la clave secreta
            g.user = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'mensaje': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'mensaje': 'Token inválido'}), 401

        return f(*args, **kwargs)

    return decorador