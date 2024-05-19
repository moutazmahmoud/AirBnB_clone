#!/usr/bin/python3
"""Unit tests for the state module."""


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests for State class"""

    def test_attributes(self):
        """Test state Attrs"""
        state = State()
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
