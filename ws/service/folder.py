from flask import json
from entity import folder as folder_entity

def get_folder_from_data(data):
    folder = None
    
    if (data):
        folder_data = json.loads(data)
        if (folder_data and "name" in folder_data):
            folder = folder_entity.Folder()
            folder.name = folder_data["name"]
    
    return folder
