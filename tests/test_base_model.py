#!/usr/bin/python3
"""Unittests for BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""
    def test_initalization(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)
        self.assertTrue(type(b1.id) == str)
        self.assertTrue(type(b1.created_at) == datetime)
        self.assertTrue(isinstance(b1.updated_at, datetime))
        b3 = BaseModel(**{"id": "ed6648e7-a709-4cf0-8a3e-083db06da8f0",
                          "created_at": "2023-07-16T23:02:47.978408",
                          "updated_at": "2023-07-16T23:02:47.978408",
                          "__class__": "City", "name": "John", "age": 40})
        self.assertEqual(40, b3.age)
        self.assertEqual("John", b3.name)
