#!/usr/bin/python3
"""Defines unittests for models/review.py."""
import os
import io
import sys
import models
import unittest
from datetime import datetime
from models.review import Review

class Test_State_instantiation(unittest.TestCase):
    """test instantiation of the review class."""

    def test_istance_not_none(self):
        self.assertIsNotNone(Review())

    def test_istance_of_state(self):
        self.assertIsInstance(Review(), Review)

    def test_instace_with_kwargs(self):
        create_time = update_time = datetime.now().isoformat()
        kwargs = {
                'my_number': 96, 'name': 'My Review',
                '__class__': 'Review',
                'updated_at': update_time,
                'id': 'b6a6e70c-c67d-4312-9a75-9d084935e579',
                'created_at': create_time}
        ctt = Review(**kwargs)
        self.assertIsInstance(ctt, Review)
        self.assertEqual(ctt.my_number, 96)
        self.assertNotIn('__class__', ctt.__dict__)
        self.assertEqual(create_time, ctt.created_at.isoformat())
        self.assertEqual(update_time, ctt.updated_at.isoformat())

    def test_instance_with_args(self):
        args = (12, None)
        ctt = Review(*args)
        self.assertIsNotNone(ctt)
        self.assertIsInstance(ctt, Review)
        self.assertNotIn(12, ctt.__dict__.values())
        self.assertNotIn(None, ctt.__dict__.values())

    def test_instance_id_uuid(self):
        self.assertIsInstance(Review().id, str)

    def test_instance_datetime_createdate(self):
        self.assertIsInstance(Review().created_at, datetime)

    def test_instance_datetime_updatedate(self):
        self.assertIsInstance(Review().updated_at, datetime)

    def test_instance_placeid(self):
        ctt = Review()
        self.assertIsInstance(ctt.place_id, str)
        self.assertEqual(ctt.place_id, "")
        ctt.place_id = "6789"
        self.assertEqual(ctt.place_id, "6789")

    def test_instance_userid(self):
        ctt = Review()
        self.assertIsInstance(ctt.user_id, str)
        self.assertEqual(ctt.user_id, "")
        ctt.user_id = "66"
        self.assertEqual(ctt.user_id, "66")

    def test_instance_text(self):
        ctt = Review()
        self.assertIsInstance(ctt.text, str)
        self.assertEqual(ctt.text, "")
        ctt.text = "bla bla"
        self.assertEqual(ctt.text, "bla bla")


if __name__ == "__main__":
    unittest.main()