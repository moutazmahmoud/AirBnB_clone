#!/usr/bin/python3

"""
    File Storage
"""
import json

class FileStorage:
    """Class to handle serialization and deserialization of instances to/from a JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize objects to the JSON file."""
        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        """Deserialize the JSON file to objects, if it exists."""
        try:
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
                for key, value in objs.items():
                    cls_name = key.split('.')[0]
                    cls = globals()[cls_name]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
