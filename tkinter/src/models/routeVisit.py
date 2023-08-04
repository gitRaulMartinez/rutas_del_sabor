class RouteVisit:
    def __init__(self,_id,name,destinations=None):
        self._id = _id
        self.name = name
        self.destinations = destinations if destinations is not None else []