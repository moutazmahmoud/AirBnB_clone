#!/usr/bin/python3
"""Unit tests for the amenity module."""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests for Amenity class"""

    def test_attributes(self):
        """Test place attributesss"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()
