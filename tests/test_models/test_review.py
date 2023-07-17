#!/usr/bin/python3
"""Unittests for Review class"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReviewClass(unittest.TestCase):
    """Test cases for Review class"""
    def test_is_instance(self):
        r1 = Review()
        self.assertTrue(isinstance(r1, BaseModel))

    def test_attributes_types(self):
        r2 = Review()
        self.assertTrue(type(r2.place_id) == str)
        self.assertTrue(type(r2.user_id) == str)
        self.assertTrue(type(r2.text) == str)


if __name__ == '__main__':
    unittest.main()
