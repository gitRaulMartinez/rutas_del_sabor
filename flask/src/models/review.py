class Review:
    def __init__(self,_id,culinary_destination_id,user_id,score,comment):
        self._id = _id
        self.culinary_destination_id = culinary_destination_id
        self.user_id = user_id
        self.score = score
        self.comment = comment