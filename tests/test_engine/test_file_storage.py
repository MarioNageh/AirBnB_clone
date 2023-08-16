#!/usr/bin/python3
"""
Test cases for FileStorage class
"""
import json
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import os
import models
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review

class TestFileStorage(unittest.TestCase):
    """
    test class
    """
    fs = FileStorage()

    def test_default_values(self):
        """test default value"""

        initial_count = len(self.fs.all())
        new_base_model = BaseModel()
        self.fs.new(new_base_model)

        self.fs.save()
        self.fs.reload()

        updated_count = len(self.fs.all())
        self.assertEqual(updated_count, initial_count + 1)
        obj_key = f"BaseModel.{new_base_model.id}"
        self.assertIn(obj_key, self.fs.all())
        reloaded_obj = self.fs.all()[obj_key]
        self.assertEqual(reloaded_obj.updated_at, new_base_model.updated_at)

        os.remove("file.json")
        new_base_model = BaseModel()
        new_base_model.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_method_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_reload_method(self):
        b_m_c = BaseModel()
        u_s_c = User()
        s_t_c = State()
        p_l_c = Place()
        c_y_c = City()
        a_m_c = Amenity()
        r_v_c = Review()
        models.storage.new(b_m_c)
        models.storage.new(u_s_c)
        models.storage.new(s_t_c)
        models.storage.new(p_l_c)
        models.storage.new(c_y_c)
        models.storage.new(a_m_c)
        models.storage.new(r_v_c)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + b_m_c.id, objs)
        self.assertIn("User." + u_s_c.id, objs)
        self.assertIn("State." + s_t_c.id, objs)
        self.assertIn("Place." + p_l_c.id, objs)
        self.assertIn("City." + c_y_c.id, objs)
        self.assertIn("Amenity." + a_m_c.id, objs)
        self.assertIn("Review." + r_v_c.id, objs)

    def test_all(self):
        fs = FileStorage()
        self.assertIsInstance(fs.all(), dict)
        for v in fs.all().values():
            self.assertIsInstance(v, BaseModel)

    def test_new(self):
        fs = FileStorage()
        bs = BaseModel()
        self.assertIn(bs, fs.all().values())

    def test_save_method(self):
        bs = BaseModel()
        key = ".".join([bs.__class__.__name__, bs.id])
        models.storage.save()
        with open("file.json", "r") as f:
            rd = json.load(f)
            self.assertIn(key, rd)