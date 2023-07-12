#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines Base class.

Example:
    my_model = BaseModel()
"""

import uuid
from datetime import datetime


class BaseModel(object):
    """class for all other classes to inherit from."""

    def __init__(self):
        """method to instantiate instance of BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Returns a string representation of the object
        Returns:
            BaseModel string representation.
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        Returns:
            a dict.
        """
        returned_dict = self.__dict__.copy()
        returned_dict['__class__'] = type(self).__name__
        returned_dict['created_at'] = self.created_at.isoformat()
        returned_dict['updated_at'] = self.updated_at.isoformat()
        return returned_dict
