#!/usr/bin/python3
"""Unittests for Place class"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlaceClass(unittest.TestCase):
    """Test cases for Place class"""
    def test_is_instance(self):
        p1 = Place()
        self.assertTrue(isinstance(p1, BaseModel))

    def test_attributes_types(self):
        p2 = Place()
        self.assertTrue(type(p2.city_id) == str)
        self.assertTrue(type(p2.user_id) == str)
        self.assertTrue(type(p2.name) == str)
        self.assertTrue(type(p2.description) == str)
        self.assertTrue(type(p2.number_rooms) == int)
        self.assertTrue(type(p2.number_bathrooms) == int)
        self.assertTrue(type(p2.max_guest) == int)
        self.assertTrue(type(p2.price_by_night) == int)
        self.assertTrue(type(p2.latitude) == float)
        self.assertTrue(type(p2.longitude) == float)
        self.assertTrue(type(p2.amenity_ids) == list)


if __name__ == '__main__':
    unittest.main()
