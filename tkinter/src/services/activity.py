from datetime import datetime, date

from src.request.activity import ActivityData
from src.request.culinaryDestination import CulinaryDestinationData
from src.models.activity import Activity
from src.models.culinaryDestination import CulinaryDestination

class ActivitiesServices:
    def __init__(self):
        self.culinary_destinations_data = CulinaryDestinationData()
        self.activities_data = ActivityData()
    
    def get(self):
        response_activities = self.activities_data.get_data()
        activities = [Activity(**activity) for activity in response_activities] if response_activities is not None else []
        activities = sorted(activities, key=lambda activity: activity.start_time)

        response_culinary_destinations = self.culinary_destinations_data.get_data()
        culinary_destinations = [CulinaryDestination(**culinary_destination) for culinary_destination in response_culinary_destinations] if response_culinary_destinations is not None else []

        for activity in activities:
            for culinary_destination in culinary_destinations:
                if activity.culinary_destination_id == culinary_destination._id:
                    activity.culinary_destination = culinary_destination
        
        return activities
    
    def filter(self,name=None,date_option=None):
        activities = self.get()
        if name is not None:
            activities = list(filter(lambda value: name.lower() in value.name.lower(),activities))
        if date_option is not None:
            today = date.today()
            if date_option == 'Hoy':
                activities = list(filter(lambda value: datetime.fromisoformat(value.start_time).date() == today, activities))
            elif date_option == 'Proximos':
                activities = list(filter(lambda value: datetime.fromisoformat(value.start_time).date() > today, activities))
            elif date_option == 'Pasados':
                activities = list(filter(lambda value: datetime.fromisoformat(value.start_time).date() < today, activities))
        return activities