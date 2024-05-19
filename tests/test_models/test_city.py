#!/usr/bin/python3
"""Unit tests for the city module."""


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for City class"""

    def test_attributes(self):
        """Test city attributes"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == "__main__":
    unittest.main()
#comment