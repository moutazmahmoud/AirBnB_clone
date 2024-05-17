#!/usr/bin/python3
"""
    __init__
"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User



temp_storage = FileStorage()
temp_storage.reload()
