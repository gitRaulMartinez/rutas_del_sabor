class CulinaryDestination:
    def __init__(self,_id,name,type_of_kitchen,ingredients,minimal_price,maximum_price,popularity,availability,location_id,image,logo):
        self._id = _id
        self.name = name
        self.type_of_kitchen = type_of_kitchen
        self.ingredients = ingredients
        self.minimal_price = minimal_price
        self.maximum_price = maximum_price
        self.popularity = popularity
        self.availability = availability
        self.location_id = location_id
        self.image = image
        self.logo = logo