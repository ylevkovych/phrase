from flask import json
from entity import language as language_entity

def get_language_from_data(data):
    language = None
    
    if (data):
        language_data = json.loads(data)
        if (language_data and "name" in language_data):
            language = language_entity.Language()
            language.name = language_data["name"]
    
    return language
