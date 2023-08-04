from firebase_admin import db
from src.models.routeVisit import RouteVisit

def addRouteVisit(route_visit):
    return db.reference('/routes_visit').child(route_visit._id).set(route_visit.__dict__)

def getRoutesVisit():
    routes_visit = db.reference('/routes_visit').get()
    if routes_visit is None:
        return []
    else:
        return [RouteVisit(**route_visit) for route_visit in routes_visit.values()]
    
def getMyRoutesVisit(list_my_routes):
    routes_visit = db.reference('/routes_visit').get()

    if routes_visit is None:
        return []
    else:
        return [RouteVisit(**route_visit) for route_visit in routes_visit.values() if RouteVisit(**route_visit)._id in list_my_routes]