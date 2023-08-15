#!/usr/bin/env python3
"""This module contains the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ The Amenity class inherits from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
