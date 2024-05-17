#!/usr/bin/python3

"""
    File Storage
"""
import json
import os
from models import BaseModel

class FileStorage:
    """
    File Storage Class
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for obj_data in obj_dict.values():
                    cls_name = obj_data['__class__']
                    if cls_name == "BaseModel":
                        self.new(BaseModel(**obj_data))
