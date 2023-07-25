from firebase_admin import db
from src.models.location import Location

def addLocation(location):
    # Agregar el usuario a la base de datos
    return db.reference('/locations').child(location._id).set(location.__dict__)

def getLocations():
    # Obtener todos los usuarios
    locations = db.reference('/locations').get()
    if locations is None:
        return []
    else:
        return [Location(**location) for location in locations.values()]