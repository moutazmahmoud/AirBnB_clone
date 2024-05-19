#!/usr/bin/python3
"""Unit tests for the review module."""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests for Review class"""

    def test_attributes(self):
        """Test review attributes"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()
