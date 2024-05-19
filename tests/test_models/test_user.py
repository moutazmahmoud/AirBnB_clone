#!/usr/bin/python3
"""Unit tests for the user module."""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Tests for User class"""

    def test_attributes(self):
        """Test review attributes"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == "__main__":
    unittest.main()
