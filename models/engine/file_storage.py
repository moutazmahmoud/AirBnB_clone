#!/usr/bin/python3

"""
    File Storage
"""
import json

from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Class to handle serialization and
    deserialization of instances to/from
    a JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all saved objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the storage dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {key: obj.to_dict() for key, obj in odict.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objs_dict = json.load(f)
                for key, option in objs_dict.items():
                    class_name = option["__class__"]
                    del option["__class__"]
                    obj = eval(class_name)(**option)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            return
