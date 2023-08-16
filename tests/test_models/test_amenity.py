#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""
import os
import io
import sys
import models
import unittest
from datetime import datetime
from models.amenity import Amenity

class Test_State_instantiation(unittest.TestCase):
    """test instantiation of the Amenity class."""

    def test_istance_not_none(self):
        self.assertIsNotNone(Amenity())

    def test_istance_of_state(self):
        self.assertIsInstance(Amenity(), Amenity)

    def test_instace_with_kwargs(self):
        create_time = update_time = datetime.now().isoformat()
        kwargs = {
                'my_number': 92, 'name': 'My Amentiy',
                '__class__': 'Amenity',
                'updated_at': update_time,
                'id': 'b6a6e50c-c67d-4312-9a75-9d084935e579',
                'created_at': create_time}
        att = Amenity(**kwargs)
        self.assertIsInstance(att, Amenity)
        self.assertEqual(att.my_number, 92)
        self.assertNotIn('__class__', att.__dict__)
        self.assertEqual(create_time, att.created_at.isoformat())
        self.assertEqual(update_time, att.updated_at.isoformat())

    def test_instance_with_args(self):
        att = Amenity(15)
        self.assertIsNotNone(att)
        self.assertIsInstance(att, Amenity)
        self.assertNotIn(15, att.__dict__.values())

    def test_instance_id_uuid(self):
        self.assertIsInstance(Amenity().id, str)

    def test_instance_datetime_createdate(self):
        self.assertIsInstance(Amenity().created_at, datetime)

    def test_instance_datetime_updatedate(self):
        self.assertIsInstance(Amenity().updated_at, datetime)

    def test_instance_name(self):
        att = Amenity()
        self.assertIsInstance(att.name, str)
        self.assertEqual(att.name, "")
        att.name = "john"
        self.assertEqual(att.name, "john")


if __name__ == "__main__":
    unittest.main()