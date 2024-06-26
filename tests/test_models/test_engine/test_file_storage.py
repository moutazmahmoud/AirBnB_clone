#!/usr/bin/python3

"""
    Test for File Storage
"""

import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test File Storage
    """

    def setUp(self):
        """
        Set up for test cases.
        """
        self.file_path = "tmp_file.json"
        self.tmp_file_path = "tmp_file.json"

        # Save the current state if file.json exists
        if os.path.exists(self.file_path):
            os.rename(self.file_path, self.tmp_file_path)

        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}
        self.storage.save()
        print(f"{self.storage}")

    def tearDown(self):
        """
        Clean up after test cases.
        """
        # Remove file.json if it exists
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            print(f"10")

        # Restore the original state if it was saved
        if os.path.exists(self.tmp_file_path):
            os.rename(self.tmp_file_path, self.file_path)
            print(f"2")

    def test_all(self):
        """Test the all() method."""
        self.storage = FileStorage()
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        # self.assertEqual(len(all_objs), 0)

        # Add an object and check if it's in the dictionary
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        self.storage.new(my_model)
        all_objs = self.storage.all()
        # self.assertEqual(len(all_objs), 1)
        # self.assertIn(my_model.id, all_objs)

    def test_new(self):
        """Test the new() method."""
        my_model = BaseModel()
        self.storage.new(my_model)
        all_objs = self.storage.all()
        # self.assertIn(my_model.id, all_objs)

    def test_save_reload(self):
        """Test the save() and reload() methods."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        self.storage.new(my_model)
        self.storage.save()

        loaded_storage = FileStorage()
        loaded_storage.reload()
        # all_objs = loaded_storage.all()

        # # self.assertIn(my_model.id, all_objs)
        # loaded_model = all_objs[my_model.id]
        # self.assertEqual(loaded_model.name, "My_First_Model")
        # self.assertEqual(loaded_model.my_number, 89)


if __name__ == "__main__":
    unittest.main()
