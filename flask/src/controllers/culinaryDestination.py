from firebase_admin import db
from src.models.culinaryDestination import CulinaryDestination

def addCulinaryDestination(culinary_destination):
    # Agregar el usuario a la base de datos
    return db.reference('/culinary_destinations').child(culinary_destination._id).set(culinary_destination.__dict__)

def getCulinaryDestinations():
    # Obtener todos los usuarios
    culinary_destinations = db.reference('/culinary_destinations').get()
    if culinary_destinations is None:
        return []
    else:
        return [CulinaryDestination(**culinary_destination) for culinary_destination in culinary_destinations.values()]