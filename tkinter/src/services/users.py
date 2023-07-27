import json
from src.request.user import UserData
from src.models.user import User
from src.utils.session import get_token

class UserService:
    def __init__(self):
        self.user_data = UserData()

    def get_user(self):
        response_user = self.user_data.get_data(get_token())
        user = User(**response_user)
        return user
