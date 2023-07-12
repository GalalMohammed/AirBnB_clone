#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines FileStorage class.

Example:
    all_objs = storage.all()
"""

import json
from os import path


class FileStorage(object):
    """class for serializing instances to a JSON file and vice-versa"""

    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """method to instantiate instance of FileStorage"""
        pass

    def all(self):
        """gets objects
        Returns:
            dict.
        """
        return self.__objects

    def new(self, obj):
        """sets obj in __objects
        Args:
            obj (object): an object to be used.
        """
        self.__objects[f'{type(obj).__name__}.{obj.id}'] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        """deserializes the JSON file to __objects """
        if path.exists(self.__file_path):
            with open(self.__file_path) as file:
                self.__objects = json.loads(file.read())
