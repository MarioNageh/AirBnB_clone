#!/usr/bin/env python3
"""This module contains the State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """ The State class inherits from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes State"""
        super().__init__(*args, **kwargs)
