from firebase_admin import db

def getAll():
    return db.reference('/').get()