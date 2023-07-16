#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines Amenity Class.

Example:
    my_model = Amenity()
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """class to inherit from BaseModel"""

    name = ""
