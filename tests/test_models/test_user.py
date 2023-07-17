#!/usr/bin/python3
"""Unittests for User class"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUserClass(unittest.TestCase):
    """Test cases for User class"""
    def test_is_instance(self):
        u1 = User()
        self.assertTrue(isinstance(u1, BaseModel))

    def test_attributes_types(self):
        u2 = User()
        self.assertTrue(type(u2.email) == str)
        self.assertTrue(type(u2.password) == str)
        self.assertTrue(type(u2.first_name) == str)
        self.assertTrue(type(u2.last_name) == str)


if __name__ == '__main__':
    unittest.main()
