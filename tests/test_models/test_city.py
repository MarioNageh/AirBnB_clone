#!/usr/bin/python3
"""Defines unittests for models/city.py."""
import os
import io
import sys
import models
import unittest
from datetime import datetime
from models.state import State
from models.city import City

class Test_State_instantiation(unittest.TestCase):
    """test instantiation of the city class."""

    def test_istance_not_none(self):
        self.assertIsNotNone(State())

    def test_istance_of_state(self):
        self.assertIsInstance(City(), City)

    def test_instace_with_kwargs(self):
        create_time = update_time = datetime.now().isoformat()
        kwargs = {
                'my_number': 91, 'name': 'My fourth Model',
                '__class__': 'City',
                'updated_at': update_time,
                'id': 'b6a6e40c-c67d-4312-9a75-9d084935e579',
                'created_at': create_time}
        ctt = City(**kwargs)
        self.assertIsInstance(ctt, City)
        self.assertEqual(ctt.my_number, 91)
        self.assertNotIn('__class__', ctt.__dict__)
        self.assertEqual(create_time, ctt.created_at.isoformat())
        self.assertEqual(update_time, ctt.updated_at.isoformat())

    def test_instance_with_args(self):
        args = (12, None)
        ctt = City(*args)
        self.assertIsNotNone(ctt)
        self.assertIsInstance(ctt, City)
        self.assertNotIn(12, ctt.__dict__.values())
        self.assertNotIn(None, ctt.__dict__.values())

    def test_instance_id_uuid(self):
        self.assertIsInstance(City().id, str)

    def test_instance_datetime_createdate(self):
        self.assertIsInstance(City().created_at, datetime)

    def test_instance_datetime_updatedate(self):
        self.assertIsInstance(City().updated_at, datetime)

    def test_instance_stateid(self):
        ctt = City()
        self.assertIsInstance(ctt.state_id, str)
        self.assertEqual(ctt.state_id, "")
        ctt.state_id = "123456789"
        self.assertEqual(ctt.state_id, "123456789")

    def test_instance_name(self):
        ctt = City()
        self.assertIsInstance(ctt.name, str)
        self.assertEqual(ctt.name, "")
        ctt.name = "doe"
        self.assertEqual(ctt.name, "doe")


if __name__ == "__main__":
    unittest.main()