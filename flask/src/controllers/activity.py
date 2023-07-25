from firebase_admin import db
from src.models.activity import Activity

def addActivity(activity):
    return db.reference('/activities').child(activity._id).set(activity.__dict__)

def getActivities():
    activities = db.reference('/activities').get()
    if activities is None:
        return []
    else:
        return [Activity(**activity) for activity in activities.values()]