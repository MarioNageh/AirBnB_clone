#!/usr/bin/env python3
"""This module contains the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """ The User class inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs)
