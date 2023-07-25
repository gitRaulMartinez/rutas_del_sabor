class RouteVisit:
    def __init__(self,_id,name,culinary_destinations=None):
        self._id = _id
        self.name = name
        if culinary_destinations is None:
            self.culinary_destinations = []
        else:
            self.culinary_destinations = culinary_destinations