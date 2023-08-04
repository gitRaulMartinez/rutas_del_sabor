from src.request.user import UserData
from src.request.culinaryDestination import CulinaryDestinationData
from src.request.activity import ActivityData
from src.request.location import LocationData
from src.request.routeVisit import RouteVisitData
from src.models.user import User
from src.utils.session import get_token, set_token

class UserService:
    def __init__(self):
        self.user_data = UserData()
        self.culinary_destination_data = CulinaryDestinationData()
        self.activity_data = ActivityData()
        self.location_data = LocationData()
        self.route_visit_data = RouteVisitData()

    def get_user(self):
        response_user = self.user_data.get_data(get_token())
        user = User(**response_user)
        return user
    
    def logout(self):
        self.user_data.logout()
        self.culinary_destination_data.logout()
        self.activity_data.logout()
        self.location_data.logout()
        self.route_visit_data.logout()
        set_token("")