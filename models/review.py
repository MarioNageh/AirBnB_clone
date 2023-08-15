#!/usr/bin/env python3
"""This module contains the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ The State class inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
