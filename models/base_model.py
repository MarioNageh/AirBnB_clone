#!/usr/bin/env python3
""" Base model module """

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """__init__ method"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """__str__ method"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """save method"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        to_dict method

        :returns dictionary representation
        """
        data = self.__dict__.copy()
        data["__class__"] = self.__class__.__name__
        data["created_at"] = self.created_at.isoformat()
        data["updated_at"] = self.updated_at.isoformat()
        return data
