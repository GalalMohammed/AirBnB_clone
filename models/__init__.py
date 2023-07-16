#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module to init the package
"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
