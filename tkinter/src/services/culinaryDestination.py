from src.request.culinaryDestination import CulinaryDestinationData
from src.request.location import LocationData
from src.request.activity import ActivityData
from src.models.culinaryDestination import CulinaryDestination
from src.models.location import Location
from src.models.activity import Activity

class CulinaryDestinationService:
    def __init__(self):
        self.culinary_destinations_data = CulinaryDestinationData()
        self.location_data = LocationData()
        self.activity_data = ActivityData()

    def get_info(self):
        response_culinary_destinations = self.culinary_destinations_data.get_data()
        culinary_destinations = [CulinaryDestination(**culinary_destination) for culinary_destination in response_culinary_destinations] if response_culinary_destinations is not None else []

        response_locations = self.location_data.get_data()
        locations = [Location(**location) for location in response_locations] if response_locations is not None else []

        for culinary_destination in culinary_destinations:
            for location in locations:
                if location._id == culinary_destination.location_id:
                    culinary_destination.location_id = location
                    culinary_destination.location_id.short_country = location.country.split()[-1]
        
        return culinary_destinations
    
    def get_destination(self,culinary_destination_id):
        culinary_destinations = self.get_info()
        culinary_destination = None
        for culinary_destination_value in culinary_destinations:
            if culinary_destination_value._id == culinary_destination_id:
                culinary_destination = culinary_destination_value
                break
        
        response_activities = self.activity_data.get_data()
        activities = [Activity(**activity) for activity in response_activities] if response_activities is not None else []

        culinary_destination.activities = []
        for activity in activities:
            if activity.culinary_destination_id == culinary_destination._id:
                culinary_destination.activities.append(activity)

        return culinary_destination



        
                


