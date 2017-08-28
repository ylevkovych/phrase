from flask import json
from entity import translation as translation_entity

def get_translation_from_data(data):
    translation = None
    
    if (data):
        translation_data = json.loads(data)
        if (translation_data and "username" in user_data and "password" in user_data and "email" in user_data):
            translation = translation_entity.Translation()
            translation.password = translation_data["password"]
            translation.username = translation_data["username"]
            translation.email = translation_data["email"]
    
    return translation
