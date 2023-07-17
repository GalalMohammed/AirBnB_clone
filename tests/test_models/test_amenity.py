#!/usr/bin/python3
"""Unittests for Amenity class"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenityClass(unittest.TestCase):
    """Test cases for Amenity class"""
    def test_is_instance(self):
        a1 = Amenity()
        self.assertTrue(isinstance(a1, BaseModel))

    def test_attributes_types(self):
        a2 = Amenity()
        self.assertTrue(type(a2.name) == str)


if __name__ == '__main__':
    unittest.main()
