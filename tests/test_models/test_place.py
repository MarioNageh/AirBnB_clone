#!/usr/bin/python3
"""Defines unittests for models/place.py.
"""
import os
import io
import sys
import models
import unittest
from datetime import datetime
from models.place import Place

class Test_State_instantiation(unittest.TestCase):
    """test instantiation of the place class."""

    def test_istance_not_none(self):
        self.assertIsNotNone(Place())

    def test_istance_of_state(self):
        self.assertIsInstance(Place(), Place)

    def test_instace_with_kwargs(self):
        create_time = update_time = datetime.now().isoformat()
        kwargs = {
                'my_number': 93, 'name': 'My Place',
                '__class__': 'Place',
                'updated_at': update_time,
                'id': 'b6a6e60c-c67d-4312-9a75-5555555',
                'created_at': create_time}
        ptt = Place(**kwargs)
        self.assertIsInstance(ptt, Place)
        self.assertEqual(ptt.my_number, 93)
        self.assertNotIn('__class__', ptt.__dict__)
        self.assertEqual(create_time, ptt.created_at.isoformat())
        self.assertEqual(update_time, ptt.updated_at.isoformat())

    def test_instance_with_args(self):
        args = (12, None)
        ptt = Place(*args)
        self.assertIsNotNone(ptt)
        self.assertIsInstance(ptt, Place)
        self.assertNotIn(12, ptt.__dict__.values())
        self.assertNotIn(None, ptt.__dict__.values())

    def test_instance_id_uuid(self):
        self.assertIsInstance(Place().id, str)

    def test_instance_datetime_createdate(self):
        self.assertIsInstance(Place().created_at, datetime)

    def test_instance_datetime_updatedate(self):
        self.assertIsInstance(Place().updated_at, datetime)

    def test_instance_cityid(self):
        ptt = Place()
        self.assertIsInstance(ptt.city_id, str)
        self.assertEqual(ptt.city_id, "")
        ptt.city_id = "0123456789"
        self.assertEqual(ptt.city_id, "0123456789")

    def test_instance_userid(self):
        ptt = Place()
        self.assertIsInstance(ptt.user_id, str)
        self.assertEqual(ptt.user_id, "")
        ptt.user_id = "100"
        self.assertEqual(ptt.user_id, "100")

    def test_instance_name(self):
        ptt = Place()
        self.assertIsInstance(ptt.name, str)
        self.assertEqual(ptt.name, "")
        ptt.name = "doe"
        self.assertEqual(ptt.name, "doe")

    def test_instance_description(self):
        ptt = Place()
        self.assertIsInstance(ptt.description, str)
        self.assertEqual(ptt.description, "")
        ptt.description = "great place"
        self.assertEqual(ptt.description, "great place")

    def test_instance_number_rooms(self):
        ptt = Place()
        self.assertIsInstance(ptt.number_rooms, int)
        self.assertEqual(ptt.number_rooms, 0)
        ptt.number_rooms = 12
        self.assertEqual(ptt.number_rooms, 12)

    def test_instance_number_bathrooms(self):
        ptt = Place()
        self.assertIsInstance(ptt.number_bathrooms, int)
        self.assertEqual(ptt.number_bathrooms, 0)
        ptt.number_bathrooms = 5
        self.assertEqual(ptt.number_bathrooms, 5)

    def test_instance_max_guest(self):
        ptt = Place()
        self.assertIsInstance(ptt.max_guest, int)
        self.assertEqual(ptt.max_guest, 0)
        ptt.max_guest = 99
        self.assertEqual(ptt.max_guest, 99)

    def test_instance_price_by_night(self):
        ptt = Place()
        self.assertIsInstance(ptt.price_by_night, int)
        self.assertEqual(ptt.price_by_night, 0)
        ptt.price_by_night = 1500
        self.assertEqual(ptt.price_by_night, 1500)

    def test_instance_latitude(self):
        ptt = Place()
        self.assertIsInstance(ptt.latitude, float)
        self.assertAlmostEqual(ptt.latitude, 0.0)
        ptt.latitude = 124.4
        self.assertAlmostEqual(ptt.latitude, 124.4)

    def test_instance_longitude(self):
        ptt = Place()
        self.assertIsInstance(ptt.longitude, float)
        self.assertAlmostEqual(ptt.longitude, 0.0)
        ptt.longitude = 124.8
        self.assertAlmostEqual(ptt.longitude, 124.8)

    def test_instance_amenity_ids(self):
        ptt = Place()
        self.assertIsInstance(ptt.amenity_ids, list)
        self.assertEqual(ptt.amenity_ids, [])
        ptt.amenity_ids = [1, 2]
        self.assertAlmostEqual(ptt.amenity_ids, [1, 2])


if __name__ == "__main__":
    unittest.main()