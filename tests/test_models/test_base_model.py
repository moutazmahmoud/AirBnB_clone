#!/usr/bin/python3

"""
    Test base model
"""

from time import sleep
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class"""

    def setUp(self):
        """Set up test methods."""
        self.model = BaseModel()

    def tearDown(self):
        """Tear down test methods."""
        del self.model

    def test_init(self):
        """Test the initialization of BaseModel"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_init_with_kwargs(self):
        """Test initialization with kwargs"""
        data = {
            "id": "1234",
            "created_at": "2024-01-01T00:00:00",
            "updated_at": "2024-01-01T00:00:00",
        }
        model = BaseModel(**data)
        self.assertEqual(model.id, "1234")
        self.assertEqual(
            model.created_at, datetime.fromisoformat("2024-01-01T00:00:00")
        )
        self.assertEqual(
            model.updated_at, datetime.fromisoformat("2024-01-01T00:00:00")
        )

    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(
            str(self.model), f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        )

    def test__save(self):
        """
        Test that the 'updated_at' attribute updates after calling the 'save()' method.
        """
        # Create a new instanceument instance
        instance = BaseModel()

        # Store the initial value of 'updated_at'
        initial_saved_time = instance.updated_at

        # small time delay
        sleep(0.03)

        # Call the 'save()' method
        instance.save()

        # Assert that 'updated_at' has changed after calling 'save()'
        self.assertNotEqual(initial_saved_time, instance.updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], self.model.updated_at.isoformat())
        self.assertIsInstance(model_dict, dict)


if __name__ == "__main__":
    unittest.main()
