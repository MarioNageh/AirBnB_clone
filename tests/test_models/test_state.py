#!/usr/bin/python3
"""Defines unittests for models/state.py.
"""
import os
import io
import sys
import models
import unittest
from datetime import datetime
from models.state import State

class Test_State_instantiation(unittest.TestCase):
    """test instantiation of the State class."""

    def test_istance_not_none(self):
        self.assertIsNotNone(State())

    def test_istance_of_state(self):
        self.assertIsInstance(State(), State)

    def test_instace_with_kwargs(self):
        create_time = update_time = datetime.now().isoformat()
        kwargs = {
                'my_number': 90, 'name': 'My third Model',
                '__class__': 'State',
                'updated_at': update_time,
                'id': 'b6a6e30c-c67d-4312-9a75-9d084935e579',
                'created_at': create_time}
        stt = State(**kwargs)
        self.assertIsInstance(stt, State)
        self.assertEqual(stt.my_number, 90)
        self.assertNotIn('__class__', stt.__dict__)
        self.assertEqual(create_time, stt.created_at.isoformat())
        self.assertEqual(update_time, stt.updated_at.isoformat())

    def test_instance_with_args(self):
        args = (11, "hello")
        stt = State(*args)
        self.assertIsNotNone(stt)
        self.assertIsInstance(stt, State)
        self.assertNotIn(11, stt.__dict__.values())
        self.assertNotIn("hello", stt.__dict__.values())

    def test_instance_id_uuid(self):
        self.assertIsInstance(State().id, str)

    def test_instance_datetime_createdate(self):
        self.assertIsInstance(State().created_at, datetime)

    def test_instance_datetime_updatedate(self):
        self.assertIsInstance(State().updated_at, datetime)

    def test_instance_name(self):
        stt = State()
        self.assertIsInstance(stt.name, str)
        self.assertEqual(stt.name, "")
        stt.name = "john doe"
        self.assertEqual(stt.name, "john doe")


if __name__ == "__main__":
    unittest.main()