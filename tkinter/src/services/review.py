from src.request.review import ReviewData
from src.request.user import UserData
from src.request.culinaryDestination import CulinaryDestinationData
from src.models.review import Review
from src.models.user import User
from src.models.culinaryDestination import CulinaryDestination
from src.utils.session import get_token

class ReviewServices:
    def __init__(self):
        self.review_data = ReviewData()
        self.user_data = UserData()
        self.destinations_data = CulinaryDestinationData()

    def get_data(self):
        response_reviews = self.review_data.get_data()
        reviews = [Review(**review) for review in response_reviews] if response_reviews is not None else []

        return reviews
    
    def create(self,data):
        review = self.review_data.create(token=get_token(),data=data)
        new_review = Review(**review) if review is not None else None
        self.review_data.reload()

        response_user = self.user_data.get_my_user(token=get_token())
        user = User(**response_user)
        new_review.user = user

        response_destinations = self.destinations_data.get_data()
        destinations = [CulinaryDestination(**destination) for destination in response_destinations] if response_destinations is not None else []
        
        for destination in destinations:
            if new_review.culinary_destination_id == destination._id:
                new_review.destination = destination
                break

        return new_review
    
    def get_my_reviews(self):
        response_reviews = self.review_data.get_data()
        reviews = [Review(**review) for review in response_reviews] if response_reviews is not None else []

        response_user = self.user_data.get_my_user(token=get_token())
        user = User(**response_user)

        response_destinations = self.destinations_data.get_data()
        destinations = [CulinaryDestination(**destination) for destination in response_destinations] if response_destinations is not None else []

        my_reviews = []
        for review in reviews:
            if review.user_id == user._id:
                review.user = user
                for destination in destinations:
                    if review.culinary_destination_id == destination._id:
                        review.destination = destination
                        break
                my_reviews.append(review)

        return my_reviews

