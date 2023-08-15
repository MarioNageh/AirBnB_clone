#!/usr/bin/env python3
"""This module contains the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """ The City class inherits from BaseModel"""

    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """initializes City"""
        super().__init__(*args, **kwargs)
