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
        self.assertTrue(isinstance(b1, BaseModel))
        self.assertNotEqual(b1.id, b2.id)
        self.assertTrue(type(b1.id) == str)
        self.assertTrue(type(b1.created_at) == datetime)
        self.assertTrue(isinstance(b1.updated_at, datetime))
        self.assertEqual(b1.__str__(), "[" + b1.__class__.__name__ + "]"
                         " (" + b1.id + ") " + str(b1.__dict__))
        dt = datetime.now()
        dt_iso = dt.isoformat()
        b3 = BaseModel(id="10", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(b3.id, "10")
        self.assertEqual(b3.created_at, dt)
        self.assertEqual(b3.updated_at, dt)

    def test_save(self):
        b4 = BaseModel()
        first_update = b4.updated_at
        b4.save()
        after_save = b4.updated_at
        self.assertTrue(after_save > first_update)

    def test_to_dict(self):
        b5 = BaseModel()
        b5.name = "John"
        b5.age = 40
        b5_dict = b5.to_dict()
        self.assertTrue(type(b5_dict["created_at"] == str))
        self.assertTrue(type(b5_dict["updated_at"] == str))
        self.assertTrue(type(b5.created_at) == datetime)
        self.assertTrue(type(b5.updated_at) == datetime)
        self.assertEqual(b5_dict["created_at"], b5.created_at.isoformat())
        self.assertEqual(b5_dict["updated_at"], b5.updated_at.isoformat())
        self.assertIn("name", b5_dict)
        self.assertIn("age", b5_dict)


if __name__ == "__main__":
    unittest.main()
