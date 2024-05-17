#!/usr/bin/python3
"""
    User class
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    User class that inherits from Base Model
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
