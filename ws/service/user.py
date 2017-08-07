from flask import json
from entity import user as user_entity

def get_user_from_data(data):
    user = None
    
    if (data):
        user_data = json.loads(data)
        if (user_data and "username" in user_data and "password" in user_data and "email" in user_data):
            user = user_entity.User()
            user.password = user_data["password"]
            user.username = user_data["username"]
            user.email = user_data["email"]
    
    return user
