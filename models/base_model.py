#!/usr/bin/python3
"""
    Base Model
"""

import uuid
from datetime import datetime

import models


class BaseModel:
    """
    Base class to take care of the initialization
    , serialization and deserialization.
    """

    def __init__(self, *args, **kwargs):
        """
        init method that initializes new instances and integrates
        with the FileStorage system.

        Using kwargs for deserialization of
        (key, value) pairs
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.the_file_storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        "Save changes"
        self.updated_at = datetime.now()
        models.the_file_storage.save()

    def to_dict(self):
        "Convert to dict"
        dict_copy = self.__dict__.copy()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["__class__"] = self.__class__.__name__
        return dict_copy
