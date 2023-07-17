#!/usr/bin/python3
"""Unittests for State class"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestStateClass(unittest.TestCase):
    """Test cases for State class"""
    def test_is_instance(self):
        s1 = State()
        self.assertTrue(isinstance(s1, BaseModel))

    def test_attributes_types(self):
        s2 = State()
        self.assertTrue(type(s2.name) == str)


if __name__ == '__main__':
    unittest.main()
