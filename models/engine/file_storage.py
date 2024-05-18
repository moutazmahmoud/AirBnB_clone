#!/usr/bin/python3

"""
    File Storage
"""
import json
import models


class FileStorage:
    """Class to handle serialization and
    deserialization of instances to/from
    a JSON file."""

    __file_path = "the_file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all saved objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize objects to the JSON file."""
        with open(self.__file_path, "w") as f:
            json.dump({key: obj.to_dict() for key,
                       obj in self.__objects.items()}, f)

    def reload(self):
        """Deserialize the JSON file to objects
        , if it exists."""
        try:
            with open(self.__file_path, "r") as f:
                obj_json = json.load(f)
                for key, value in obj_json.items():
                    class_name = value["__class__"]
                    the_class = getattr(models, class_name)
                    self.__objects[key] = the_class(**value)
        except FileNotFoundError:  # todo: revise this maybe cause error
            pass
