#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines City Class.

Example:
    my_model = City()
"""

from models.base_model import BaseModel


class City(BaseModel):
    """class to inherit from BaseModel"""

    state_id = ""
    name = ""
