#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines Review Class.

Example:
    my_model = Review()
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class to inherit from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
