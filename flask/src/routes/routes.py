#Importar rutas
from src.routes.user import users_bp
from src.routes.auth import auth_bp 

all_bp = []

all_bp.append(users_bp)
all_bp.append(auth_bp)

def register_blueprints(app):
    for bp in all_bp:
        app.register_blueprint(bp)

