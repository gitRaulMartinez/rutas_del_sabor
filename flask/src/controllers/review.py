from firebase_admin import db
from src.models.review import Review

def addReview(review):
    return db.reference('/reviews').child(review._id).set(review.__dict__)

def getReviews():
    reviews = db.reference('/reviews').get()
    if reviews is None:
        return []
    else:
        return [Review(**review) for review in reviews.values()]
    
def getMyReview(list_my_reviews):
    reviews = db.reference('/reviews').get()

    if reviews is None:
        return []
    else:
        return [Review(**review) for review in reviews.values() if Review(**review)._id in list_my_reviews]