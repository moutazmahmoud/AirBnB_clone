#!/usr/bin/python3
"""
    Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from Base Model
    """

    place_id = ""
    user_id = ""
    text = ""
