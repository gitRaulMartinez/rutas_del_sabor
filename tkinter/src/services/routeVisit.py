from src.request.routeVisit import RouteVisitData
from src.request.culinaryDestination import CulinaryDestinationData
from src.request.location import LocationData
from src.models.routeVisit import RouteVisit
from src.models.culinaryDestination import CulinaryDestination
from src.models.location import Location
from src.utils.session import get_token

class RouteVisitServices:
    def __init__(self):
        self.route_visit_data = RouteVisitData()
        self.culinary_destination_data = CulinaryDestinationData()
        self.location_data = LocationData()

    def get_data(self):
        response_routes_visit = self.route_visit_data.get_data(token=get_token())
        routes_visit = [RouteVisit(**route_visit) for route_visit in response_routes_visit] if response_routes_visit is not None else []

        return routes_visit
    
    def create(self,name,list_destinations):
        data = {
            'name': name,
            'destinations': list_destinations
        }

        response_route_visit = self.route_visit_data.create(token=get_token(),data=data)
        new_route_visit = RouteVisit(**response_route_visit) if response_route_visit is not None else None
        self.route_visit_data.add(new_route_visit.__dict__)

        return new_route_visit
    
    def destinations_visited(self):
        response_routes_visit = self.route_visit_data.get_data(token=get_token())
        routes_visit = [RouteVisit(**route_visit) for route_visit in response_routes_visit] if response_routes_visit is not None else []

        destinations_visited = set()
        for route_visit in routes_visit:
            for destination in route_visit.destinations:
                destinations_visited.add(destination)

        response_destinations = self.culinary_destination_data.get_data()
        destinations = [CulinaryDestination(**destination) for destination in response_destinations if CulinaryDestination(**destination)._id in destinations_visited] if response_destinations is not None else []

        response_location = self.location_data.get_data()
        locations = [Location(**location) for location in response_location] if response_location is not None else []

        for destination in destinations:
            for location in locations:
                if destination.location_id == location._id:
                    destination.location_id = location
                    break

        return destinations
