#!/usr/bin/python3
"""Unittests for FileStorage class"""
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageClass(unittest.TestCase):
    """Test cases for FileStorage class"""
    def test_is_instance(self):
        self.assertTrue(isinstance(models.storage, FileStorage))

    def test_all(self):
        s2 = FileStorage()
        all_dict = s2.all()
        self.assertTrue(type(all_dict) == dict)

    def test_new(self):
        s3 = FileStorage()
        b1 = BaseModel()
        s3.new(b1)
        new_dict = s3.all()
        key = f'{type(b1).__name__}.{b1.id}'
        self.assertTrue(key in new_dict)
        self.assertTrue(b1 in s3.all().values())

    def test_reload(self):
        s4 = FileStorage()
        b2 = BaseModel()
        s4.new(b2)
        s4.save()
        s4.reload()
        objs_dict = FileStorage._FileStorage__objects
        key = f'{type(b2).__name__}.{b2.id}'
        self.assertTrue(key in objs_dict)

    def test_save(self):
        s5 = FileStorage()
        b3 = BaseModel()
        s5.new(b3)
        s5.save()
        key = f'{type(b3).__name__}.{b3.id}'
        text = ""
        with open("file.json") as f:
            text = f.read()
            self.assertTrue(key in text)


if __name__ == '__main__':
    unittest.main()
