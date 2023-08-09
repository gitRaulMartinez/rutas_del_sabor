#Importar rutas
from src.routes.user import users_bp
from src.routes.auth import auth_bp 
from src.routes.culinaryDestination import culinary_destination_bp
from src.routes.location import location_bp
from src.routes.activity import activity_bp
from src.routes.routesVisit import route_visit_bp
from src.routes.review import review_bp
from src.routes.general import general_bp

all_bp = []

all_bp.append(users_bp)
all_bp.append(auth_bp)
all_bp.append(culinary_destination_bp)
all_bp.append(location_bp)
all_bp.append(activity_bp)
all_bp.append(route_visit_bp)
all_bp.append(review_bp)
all_bp.append(general_bp)

def register_blueprints(app):
    for bp in all_bp:
        app.register_blueprint(bp)

