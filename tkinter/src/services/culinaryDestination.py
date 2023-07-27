from src.request.culinaryDestination import CulinaryDestinationData
from src.request.location import LocationData
from src.models.culinaryDestination import CulinaryDestination
from src.models.location import Location

class CulinaryDestinationService:
    def __init__(self):
        self.culinary_destinations_data = CulinaryDestinationData()
        self.location_data = LocationData()

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

