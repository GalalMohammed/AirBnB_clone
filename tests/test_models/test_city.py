#!/usr/bin/python3
"""Unittests for City class"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCityClass(unittest.TestCase):
    """Test cases for city class"""
    def test_is_instance(self):
        c1 = City()
        self.assertTrue(isinstance(c1, BaseModel))

    def test_attributes_types(self):
        c2 = City()
        self.assertTrue(type(c2.name) == str)
        self.assertTrue(type(c2.state_id) == str)


if __name__ == '__main__':
    unittest.main()
